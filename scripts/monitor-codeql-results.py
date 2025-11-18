#!/usr/bin/env python3
"""
CodeQL Results Monitor and Analyzer

This script analyzes CodeQL scan results and generates reports.
It can be run locally or as part of a GitHub Actions workflow.
"""

import json
import os
import sys
import csv
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Any
import yaml

# Organization-specific configurations
ORGANIZATION_CONFIG = {
    "critical_rules": {
        "go/insecure-tls": "Insecure TLS configuration detected",
        "go/command-line-injection": "Potential command injection vulnerability",
        "bpf/memory-corruption": "Potential BPF memory corruption issue",
        "bpf/privilege-escalation": "Potential privilege escalation in BPF program"
    },
    "custom_checks": [
        {
            "id": "custom/bpf-helper-usage",
            "description": "Check for unsafe BPF helper function usage",
            "severity": "error",
            "pattern": r"bpf_probe_read_kernel|bpf_probe_read_user"
        },
        {
            "id": "custom/ebpf-map-access",
            "description": "Verify proper eBPF map access patterns",
            "severity": "warning",
            "pattern": r"bpf_map_lookup_elem\([^,]+,\s*&?([^,)]+)"
        }
    ]
}

class CodeQLResultsAnalyzer:
    def __init__(self, results_dir: str = "results"):
        self.results_dir = Path(results_dir)
        self.findings = {
            "critical": [],
            "high": [],
            "medium": [],
            "low": []
        }
        self.metrics = {
            "total_findings": 0,
            "by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0},
            "by_language": {},
            "by_rule": {}
        }
        self.organization_checks = ORGANIZATION_CONFIG["custom_checks"]
        self.critical_rules = ORGANIZATION_CONFIG["critical_rules"]

    def load_sarif_results(self, file_path: Path) -> Dict:
        """Load SARIF results from file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading SARIF file {file_path}: {e}")
            return {}

    def analyze_sarif_results(self, sarif_data: Dict) -> None:
        """Analyze SARIF results and update metrics."""
        if not sarif_data.get("runs"):
            return

        for run in sarif_data["runs"]:
            tool = run.get("tool", {}).get("driver", {}).get("name", "unknown")
            language = run.get("properties", {}).get("metrics", {}).get("language", "unknown")
            
            if language not in self.metrics["by_language"]:
                self.metrics["by_language"][language] = 0

            for result in run.get("results", []):
                self._process_result(result, tool, language)

    def _process_result(self, result: Dict, tool: str, language: str) -> None:
        """Process a single SARIF result."""
        rule_id = result.get("ruleId", "unknown")
        severity = result.get("properties", {}).get("problem.severity", "warning").lower()
        message = result.get("message", {}).get("text", "No message")
        
        # Update metrics
        self.metrics["total_findings"] += 1
        self.metrics["by_language"][language] = self.metrics["by_language"].get(language, 0) + 1
        
        # Categorize by rule
        if rule_id not in self.metrics["by_rule"]:
            self.metrics["by_rule"][rule_id] = 0
        self.metrics["by_rule"][rule_id] += 1
        
        # Categorize by severity
        if severity in ["error", "critical"]:
            self.findings["critical"].append({"rule_id": rule_id, "message": message})
            self.metrics["by_severity"]["critical"] += 1
        elif severity == "warning":
            self.findings["high"].append({"rule_id": rule_id, "message": message})
            self.metrics["by_severity"]["high"] += 1
        elif severity == "note":
            self.findings["medium"].append({"rule_id": rule_id, "message": message})
            self.metrics["by_severity"]["medium"] += 1
        else:
            self.findings["low"].append({"rule_id": rule_id, "message": message})
            self.metrics["by_severity"]["low"] += 1
        
        # Run organization-specific checks
        self._run_organization_checks(result, language)

    def _run_organization_checks(self, result: Dict, language: str) -> None:
        """Run organization-specific security checks."""
        # Check for critical rules
        rule_id = result.get("ruleId", "")
        if rule_id in self.critical_rules:
            print(f"⚠️  Critical finding: {self.critical_rules[rule_id]}")
        
        # Run custom checks based on file content
        locations = result.get("locations", [])
        for location in locations:
            file_path = location.get("physicalLocation", {}).get("artifactLocation", {}).get("uri", "")
            if file_path and os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self._check_custom_patterns(content, file_path, language)

    def _check_custom_patterns(self, content: str, file_path: str, language: str) -> None:
        """Check for custom patterns in file content."""
        import re
        
        for check in self.organization_checks:
            if re.search(check["pattern"], content):
                print(f"🔍 {check['severity'].upper()}: {check['description']} in {file_path}")

    def generate_report(self) -> Dict:
        """Generate a report of the analysis."""
        return {
            "summary": {
                "total_findings": self.metrics["total_findings"],
                "by_severity": self.metrics["by_severity"],
                "by_language": self.metrics["by_language"],
                "critical_rules_found": [
                    rule_id for rule_id in self.metrics["by_rule"] 
                    if rule_id in self.critical_rules
                ]
            },
            "findings": self.findings,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "organization_checks_run": len(self.organization_checks)
        }

def main():
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description="Analyze CodeQL scan results")
    parser.add_argument("--results-dir", default="results", help="Directory containing CodeQL results")
    parser.add_argument("--output", default="codeql-analysis-report.json", help="Output file for the report")
    args = parser.parse_args()

    # Initialize analyzer
    analyzer = CodeQLResultsAnalyzer(args.results_dir)
    
    # Process all SARIF files in the results directory
    sarif_files = list(Path(args.results_dir).glob("*.sarif"))
    if not sarif_files:
        print(f"No SARIF files found in {args.results_dir}")
        return 1
    
    print(f"Found {len(sarif_files)} SARIF file(s) to analyze")
    
    for sarif_file in sarif_files:
        print(f"Analyzing {sarif_file}...")
        sarif_data = analyzer.load_sarif_results(sarif_file)
        analyzer.analyze_sarif_results(sarif_data)
    
    # Generate and save report
    report = analyzer.generate_report()
    with open(args.output, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\nAnalysis complete. Report saved to {args.output}")
    print(f"Total findings: {report['summary']['total_findings']}")
    print(f"By severity: {json.dumps(report['summary']['by_severity'], indent=2)}")
    
    if report['summary']['critical_rules_found']:
        print("\n🚨 Critical security issues found!")
        for rule_id in report['summary']['critical_rules_found']:
            print(f"- {rule_id}: {ORGANIZATION_CONFIG['critical_rules'].get(rule_id, 'No description')}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

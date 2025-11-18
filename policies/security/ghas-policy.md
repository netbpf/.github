# GitHub Advanced Security (GHAS) Policy for NETBPF

## 1. Overview
This document outlines the GitHub Advanced Security (GHAS) configuration and enforcement policies for all repositories under the NETBPF organization. This policy ensures consistent security practices across all projects.

## 2. Code Scanning

### 2.1 Requirements
- All repositories must have CodeQL analysis enabled
- Code scanning must be run on:
  - Every push to `main` and `develop` branches
  - Every pull request targeting protected branches
  - Weekly scheduled scans

### 2.2 Configuration
- Use the [advanced-security-scanning.yml](/.github/workflows/advanced-security-scanning.yml) workflow as the base configuration
- Customize the `SECURITY_LEVEL` based on repository sensitivity:
  - `high`: For repositories handling sensitive data or critical infrastructure
  - `medium`: For standard application repositories
  - `low`: For documentation or non-production repositories

### 2.3 Severity Thresholds
- `high` and `critical` severity findings must be addressed before merging
- `medium` and `low` severity findings should be reviewed and addressed in a timely manner

## 3. Secret Scanning

### 3.1 Protection
- Secret scanning must be enabled for all repositories
- Push protection must be enabled for all repositories
- Custom patterns for organization-specific secrets must be defined

### 3.2 Response
- Detected secrets must be rotated immediately
- Incident response team must be notified of any secret leaks
- Root cause analysis required for any secret leaks

## 4. Dependabot Security Updates

### 4.1 Configuration
- Dependabot security updates must be enabled for all repositories
- Security updates should be configured to:
  - Target the default branch and all active release branches
  - Use the highest compatible version by default
  - Create pull requests with appropriate labels and reviewers

### 4.2 Review Process
- Security updates must be reviewed within 3 business days
- Critical and high severity updates must be prioritized for immediate review
- All updates must pass CI/CD pipelines before merging

## 5. Dependency Review

### 5.1 Requirements
- Dependency review must be enabled for all repositories
- All pull requests that change dependencies must pass dependency review

### 5.2 Policies
- No known vulnerabilities of `high` or `critical` severity are allowed
- New dependencies must be reviewed for:
  - License compatibility
  - Maintenance status
  - Security history
  - Community support

## 6. SBOM Generation

### 6.1 Requirements
- Software Bill of Materials (SBOM) must be generated for all releases
- SBOMs must be signed and verified
- SBOMs must be stored as release artifacts

### 6.2 Format
- Use SPDX format as the primary format
- Include all direct and transitive dependencies
- Include build and development dependencies

## 7. Compliance and Enforcement

### 7.1 Branch Protection
- `main` and `develop` branches must be protected
- Required status checks must include:
  - CodeQL analysis
  - Dependency review
  - Test suite
  - Build verification

### 7.2 Monitoring and Reporting
- Weekly security reports must be generated
- Security metrics must be tracked and reviewed monthly
- Regular security audits must be conducted

### 7.3 Incident Response
- Security incidents must be reported within 1 hour of detection
- Critical vulnerabilities must be patched within 24 hours
- Post-mortem analysis required for all security incidents

## 8. Repository Requirements

### 8.1 New Repositories
- Must enable GHAS during creation
- Must include base security workflows
- Must configure branch protection rules

### 8.2 Existing Repositories
- Must enable all GHAS features within 30 days
- Must remediate critical and high severity findings within 14 days
- Must complete initial security assessment within 60 days

## 9. Exceptions
- Exceptions to this policy must be documented and approved by the security team
- Temporary exceptions must include an expiration date
- All exceptions must be reviewed quarterly

## 10. Review and Updates
- This policy must be reviewed every 6 months
- Updates must be approved by the security team
- Changes must be communicated to all maintainers

## 11. References
- [GitHub Advanced Security Documentation](https://docs.github.com/en/code-security)
- [CodeQL Documentation](https://codeql.github.com/docs/)
- [Dependabot Documentation](https://docs.github.com/en/code-security/dependabot)
- [SPDX Specification](https://spdx.dev/)

---
*Last Updated: 2025-03-19*

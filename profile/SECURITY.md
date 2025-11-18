# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 2.x     | :white_check_mark: |
| 1.x     | :x: (Security fixes only) |
| < 1.0   | :x:                |

## Reporting a Vulnerability

### Security Vulnerability Disclosure

We take all security vulnerabilities seriously. Thank you for improving the security of our open source software. We appreciate your efforts and responsible disclosure and will make every effort to acknowledge your contributions.

### How to Report a Vulnerability

**DO NOT** report security vulnerabilities through public GitHub issues, discussions, or pull requests.

Instead, please report security vulnerabilities by emailing our security team at [security@netbpf.org](mailto:security@netbpf.org). You should receive a response within 48 hours. If for some reason you do not, please follow up via email to ensure we received your original message.

Please include the following details in your report:
- Type of issue (e.g., buffer overflow, SQL injection, cross-site scripting)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit the issue

### Our Security Process

1. Our security team will acknowledge receipt of your report within 48 hours
2. We will confirm the problem and determine the affected versions
3. We will audit code to find any potential similar problems
4. We will apply fixes to all supported versions and releases
5. We will document the vulnerability in the release notes
6. We will credit the reporter (unless they prefer to remain anonymous)

### Vulnerability Management

We categorize vulnerabilities based on their severity:

| Level | Response Time | Public Disclosure |
|-------|---------------|--------------------|
| Critical | 24 hours | 7 days after patch |
| High | 72 hours | 14 days after patch |
| Medium | 7 days | 30 days after patch |
| Low | Next release | Next release |

### Security Updates and Alerts

Security updates are released as patches for the current version. We recommend always running the latest stable release.

To receive security alerts, please [watch](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications#configuring-your-watch-settings-for-an-individual-repository) our repositories on GitHub.

### Security Best Practices

To enhance the security of your implementation, we recommend:

1. **Keep software up to date**: Always run the latest stable version
2. **Minimal privileges**: Run services with the least privileges necessary
3. **Network security**: Use firewalls and limit network exposure
4. **Input validation**: Always validate and sanitize input
5. **Dependencies**: Keep all dependencies up to date

### Security Advisories

For a list of all security advisories, please visit our [Security Advisories](https://github.com/netbpf/.github/security/advisories) page.

### Responsible Disclosure

We follow responsible disclosure principles. Please provide us with reasonable time to address vulnerabilities before public disclosure.

### Bug Bounty

We currently do not have a formal bug bounty program, but we may offer rewards for critical security issues at our discretion.

### Security Contacts

- **Security Team**: [security@netbpf.org](mailto:security@netbpf.org)
- **PGP Key**: [Link to PGP key](https://netbpf.org/security.asc)
  - Fingerprint: `[PGP Fingerprint]`

---
*Last Updated: 2025-03-19*

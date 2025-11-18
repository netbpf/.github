---
name: Security Review Request
about: Request a security review for new dependencies, significant changes, or security-related updates
labels: 'security, needs-triage'
assignees: ''
---

## Security Review Request

### Basic Information
- **Repository:** [Repository Name]
- **Related PR(s):** [PR Links]
- **Requested By:** @[username]
- **Target Branch:** [branch name]
- **Security Impact:** [High/Medium/Low]

### Change Summary
[Provide a brief description of the changes that require security review]

### Security Considerations
- [ ] Added/updated dependencies
- [ ] Authentication/authorization changes
- [ ] Data handling (storage/transmission)
- [ ] API changes
- [ ] Infrastructure changes
- [ ] Other (please specify): 

### Dependencies Added/Updated
| Package | Current Version | Previous Version | Purpose |
|---------|-----------------|------------------|----------|
|         |                 |                  |          |

### Security Controls
- [ ] Input validation implemented
- [ ] Output encoding applied
- [ ] Authentication checks in place
- [ ] Authorization checks in place
- [ ] Data encryption implemented
- [ ] Error handling and logging configured
- [ ] Security headers set
- [ ] Rate limiting implemented
- [ ] Security tests added/updated

### Testing Performed
- [ ] Unit tests
- [ ] Integration tests
- [ ] Security scans
- [ ] Manual testing
- [ ] Performance testing

### Additional Context
[Add any additional information that might be helpful for the security review]

### Attachments
- [ ] Architecture diagrams
- [ ] Threat model
- [ ] Test results
- [ ] Other (please specify):

### Reviewers
@[security-team-member-1] @[security-team-member-2]

---
*This template is part of the NETBPF Security Policy*

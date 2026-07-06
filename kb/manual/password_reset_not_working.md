# Password Reset Not Working

## Issue Pattern
Users cannot reset their password through self-service portals or receive password reset emails, preventing them from regaining access to accounts.

## Common Symptoms
- Self-service password reset (SSPR) button appears disabled
- "Password reset is not available for your account" error
- Password reset email never arrives
- Reset link in email is expired or invalid
- User receives reset email but link doesn't work
- "Your current password is incorrect" when trying to verify identity
- Security questions cannot be answered (user doesn't remember setup)
- Cannot register for password reset options

## Possible Causes
- User not registered for self-service password reset (SSPR)
- Security questions/email not set up during SSPR registration
- User phone number in directory is incorrect or unverified
- Account does not meet SSPR policy requirements
- Password reset policy disabled for user's organization unit
- Email server not delivering reset emails (spam folder)
- Reset link expired (usually valid for 15 minutes)
- Incorrect identity verification method selected
- User in excluded security group that cannot use SSPR

## Troubleshooting Steps
1. Verify user meets SSPR registration requirements and is registered
2. Check if user can log into https://myprofile.microsoft.com to register for SSPR
3. Confirm user's phone number and email in Azure AD are correct
4. Ask if reset email went to spam/junk folder
5. Check reset link validity (links expire after 15 minutes)
6. Verify user can answer security questions correctly
7. Test password reset on a different device/browser
8. Check if account is in excluded security group
9. Verify SSPR policy allows the user's role/department
10. Check if user is using personal phone that changed numbers
11. Test alternate password reset method (if multiple options available)
12. Contact admin for manual password reset if SSPR fails

## Expected Outcomes
- User successfully resets password through SSPR portal
- Password reset email arrives within 2-3 minutes
- User can immediately log in with new password
- Account unlocks and becomes active again

## Escalation Criteria
- User account critical (executive, shared account)
- Multiple users affected (SSPR service issue)
- User completely locked out with no recovery options
- Email server not delivering any password reset messages

## Related Issues
- Microsoft 365 login issues
- Account locked problems
- MFA setup problems

## Escalation Team
Identity and Access Management (IAM) team

## Priority Guidance
- **High:** User completely locked out, executive user, time-sensitive
- **Medium:** User can temporarily use different account
- **Low:** User can try again later, testing SSPR functionality

## Source
Manual knowledge base article for password reset issues.

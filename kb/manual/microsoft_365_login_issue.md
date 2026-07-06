# Microsoft 365 Login Issues

## Issue Pattern
Users cannot log in to Microsoft 365 after password changes, MFA setup, or account lockouts. This is a critical issue that prevents access to email, Teams, OneDrive, and other M365 services.

## Common Symptoms
- User cannot access Microsoft 365 portal at login.microsoft.com
- "Invalid username or password" error despite correct credentials
- MFA prompt does not appear or code does not work
- Account locked after multiple failed login attempts
- Browser shows "We couldn't sign you in" or "Your account has been temporarily locked"
- Access works on mobile but not desktop
- Recently changed password but still cannot log in

## Possible Causes
- Incorrect username format (should be user@company.com, not just username)
- Password not synced properly after recent reset
- MFA device lost, phone changed, or app deleted
- Account locked due to too many failed login attempts
- Conditional Access policy blocking the login
- Browser cache or cookies causing authentication issues
- IP-restricted access policy preventing login from current location
- Account disabled or deprovisioned in Azure AD
- Legacy authentication blocked on account

## Troubleshooting Steps
1. Ask user to verify they are using the correct username (should be their email address)
2. Confirm password was successfully reset by checking if user can reset password again at account.activedirectory.windowsazure.com
3. Ask user to clear browser cache and try a private/incognito browser window
4. Check if MFA is required by visiting https://account.microsoft.com/account/manage-my-microsoft-account
5. If MFA is locked, verify user has access to registered phone or authenticator app
6. Check Azure AD for account status and any sign-in risks
7. Verify no Conditional Access policies are blocking the user's IP or location
8. Check if the user's IP address is in an unexpected location (travel, VPN issue)
9. Test login on a different device to rule out local machine issues
10. Request account unlock from Azure AD admin if account is locked
11. If recently changed device/MFA, confirm MFA setup completed successfully
12. Check for any recent security incidents affecting the user account

## Expected Outcomes
- User can successfully log in to Microsoft 365 portal
- MFA prompt appears and accepts valid code
- User can access email, Teams, OneDrive, and other M365 services
- No "account locked" or "access denied" messages

## Escalation Criteria
- Account appears locked in Azure AD
- Multiple users affected (possible service outage)
- User is in restricted security group and needs emergency access
- MFA device completely lost and user cannot authenticate any way
- Sign-in risk detected (possible compromise)

## Related Issues
- MFA setup problems
- Password reset not working
- Teams access issues
- OneDrive not syncing

## Escalation Team
Identity and Access Management (IAM) team

## Priority Guidance
- **High:** Multiple users affected, executive user, security incident detected
- **Medium:** Single user locked out, can work around with mobile access
- **Low:** User prefers desktop but can use web or mobile temporarily

## Source
Manual knowledge base article for common M365 authentication issues.

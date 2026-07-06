# VPN Connection Issues

## Issue Pattern
Users cannot connect to corporate VPN, experience frequent disconnections, or have very slow VPN speeds. VPN is critical for remote workers to access internal resources.

## Common Symptoms
- VPN client shows "connection failed" or "unable to connect"
- VPN drops every few minutes or hours
- VPN connects but traffic is extremely slow
- Split tunneling not working as expected
- Client shows "reconnecting" loop
- "Connection rejected" error from VPN gateway
- No internet access when connected to VPN
- Can connect to VPN but cannot access internal resources

## Possible Causes
- VPN client outdated or corrupted
- Network connectivity issues (firewall, ISP blocking)
- VPN server is down or overloaded
- Firewall rules blocking VPN ports (UDP 500, 4500, TCP 443)
- ISP blocking VPN protocols
- Multiple VPN sessions from same account (not allowed)
- User credentials expired or revoked
- Router configuration issues
- DNS not resolving internal hostnames
- Split tunneling misconfiguration

## Troubleshooting Steps
1. Check if VPN service status page shows any ongoing incidents
2. Ask user to verify internet connectivity (can reach external websites)
3. Ask user to check which VPN client version is installed (should be latest)
4. Restart VPN client application completely
5. Test with different network (mobile hotspot) to rule out ISP issues
6. Check Windows Event Viewer or VPN client logs for specific error codes
7. Verify user credentials are correct and have not expired
8. Disconnect any other VPN or remote access software
9. Disable firewall temporarily to test (reenable after testing)
10. Clear VPN client cache and connection history
11. Reinstall VPN client if persistent issues
12. Check if user has multiple active VPN sessions (disconnect other sessions)
13. Verify DNS settings when connected to VPN
14. Test on a different device to rule out machine-specific issues

## Expected Outcomes
- VPN client connects successfully and shows "Connected" status
- User can access internal resources and intranet
- VPN connection remains stable without frequent drops
- Data transfer speeds are acceptable (>5 Mbps)
- Split tunneling works as configured (if enabled)

## Escalation Criteria
- Multiple users affected (possible VPN gateway outage)
- User cannot access critical business systems
- Persistent connection after multiple troubleshooting attempts
- Suspected VPN server failure

## Related Issues
- Firewall blocking VPN traffic
- DNS resolution issues
- Network authentication problems
- Split tunneling configuration

## Escalation Team
Network and Infrastructure team

## Priority Guidance
- **High:** Multiple users affected, VPN gateway down, user cannot work
- **Medium:** Single user with workaround (can use office/hotspot)
- **Low:** Intermittent issues, user can retry later

## Source
Manual knowledge base article for common VPN troubleshooting.

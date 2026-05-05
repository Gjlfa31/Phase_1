# CLOUDNANO REMEDIATION PLAN
**Operator:** ## TOP 5 CRITICAL FIXES
*(From the 20 raw findings, select the 5 that pose the greatest ACTUAL risk. Explain your reasoning.)*

1. **Unauthenticated AWS S3 Bucket (Contains Customer PII)**
   * **Justification:** The likelihood of an attack is higher because it is publicly exposed, and the impact is still significant.

2. **SQL Injection in Login Page (Customer Database Portal)**
   * **Justification:** The likelihood is high because it is internet facing, and the impact would compromise the whole database.

3. **Remote Code Execution in Apache Struts (Internet Facing Web Server)**
   * **Justification:** Internet facing web server, if an attack occurred there would be a full server takeover.

4. **SMBv1 Enabled (Internal HR File Server)**
   * **Justification:** This is internal but it is still exploitable through the right means, and it would allow the attacker to move laterally throughout the server.

5. **Cross-Site Scripting (XSS) on Support Forum**
   * **Justification:** This is on a public support forum which means that it won't take a lot to exploit, and the consequences could include full account takeovers.

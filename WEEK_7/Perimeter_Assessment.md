# TITANCORP: PERIMETER ASSESSMENT REPORT
**Operator:** **Target Subnet:** 172.88.0.0/24

## PHASE 1: ACTIVE ENUMERATION (NMAP)
*(List the live IPs discovered and their running services/versions)*
* **Host 1 (172.88.0.10):** http (nginx 1.14.2)
* **Host 2 (172.88.0.15):** redis (Redis key-value store 8.6.2)
* **Host 3 (172.88.0.20):** http (Apache httpd 2.4.67 (Unix))

## PHASE 2: VULNERABILITY AUDIT (NIKTO)
*(Run Nikto against the TWO web servers discovered above. List one major finding for each.)*
* **Web Server 1 Finding:** Server is missing the X-Frame-Options header which means that the application is exposed to clickjacking attacks.
* **Web Server 2 Finding:** HTTP TRACE method is enabled which means that the server is exposed to cross-site tracing (XST) attacks.

## PHASE 3: RISK TRIAGE
*(Review your findings. Identify the SINGLE highest-risk vulnerability across the entire DMZ. Justify why it is the top priority using the Likelihood x Impact formula.)*

* **Top Priority Remediation:** HTTP TRACE method being active on Apache/2.4.67 (172.88.0.20) which exposes the server to XST attacks.
* **Justification:** This vulnerability is the highest priority because the TRACE method is active on a publicly facing web server suggesting a high likelihood of being exploited, and XST attacks are very dangerous since they can expose authentication cookies and the data that is in the session, which in turn gives the possibility for complete account compromise which is considered to be very high impact.

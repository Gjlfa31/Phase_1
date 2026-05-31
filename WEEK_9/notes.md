# Week 9 — The Application Layer
**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned
This week shifted the focus from infrastructure exploitation to the vulnerabilities that live inside web applications. I learned how SQL Injection can bypass authentication and extract sensitive data, how Reflected and Stored XSS can hijack user sessions, and how CSRF can weaponize a victim’s browser to perform unauthorized actions. I also explored API exploitation through Broken Object Level Authorization (BOLA), using Burp Suite to intercept and manipulate REST traffic. Together, these skills formed the foundation for executing a full-stack compromise against a unified target.

## Artifacts
**sqli_report.txt**  
Created during Session 25, this report documents the SQL Injection attack chain used to bypass a login portal, enumerate hidden database tables, and extract sensitive employee salary data. It includes the tautology payload and the UNION-based schema mapping process.

**xss_payloads.txt**  
This artifact captures the Reflected and Stored XSS payloads used in Session 26. It includes the JavaScript used to steal the admin’s `auth_token` cookie and the crafted CSRF attack link that silently triggers an unauthorized fund transfer.

**api_audit.log**  
Generated during Session 27, this log contains intercepted API traffic from Burp Suite. It documents the BOLA exploitation process, including enumeration of unauthorized order IDs and the discovery of a confidential “Server Lease” order that was never meant for the authenticated user.

**OmniPortal_Assessment.md**  
The TLAB 9 artifact for Operation Omni‑Portal. This full-stack assessment chains SQLi, Stored XSS, and API BOLA into a single compromise path. It includes the SQLi bypass payload, the stolen session cookie value, the exfiltrated confidential order details, and remediation recommendations for all three vulnerabilities.

## Challenges & How I Solved Them
One challenge was chaining SQL Injection into meaningful post-authentication access. After bypassing the login, I had to identify the correct API entry point (`View My Orders`) and understand how the `auth_token` cookie controlled session state.  
Stored XSS introduced another challenge: crafting a payload that reliably executed on every page load. By testing multiple DOM‑based payloads, I identified one that consistently revealed the session cookie and confirmed persistent execution.  
The API BOLA phase required careful enumeration. Burp Suite intercepted the `/api/v2/orders/502` request, but determining the correct unauthorized order required testing nearby IDs and analyzing the JSON responses.  
Finally, writing the remediation section required translating offensive findings into actionable defensive guidance. I focused on parameterized queries for SQLi, output encoding for XSS, and object‑level authorization checks for BOLA.

## Reflection
Week 9 reinforced that the most devastating breaches often occur at the application layer. Learning to exploit SQLi, XSS, CSRF, and API flaws gave me a deeper understanding of how attackers chain vulnerabilities to reach sensitive data. This week strengthened my ability to think like both an attacker and a defender, and it prepared me to evaluate real-world web applications with a more critical and structured approach.

## References
OWASP Foundation. (2025). *OWASP Top 10 Web Application Security Risks.* https://owasp.org  
PortSwigger. (2025). *Burp Suite documentation.* https://portswigger.net  
Mozilla Developer Network. (2025). *Web security and browser behavior.* https://developer.mozilla.org

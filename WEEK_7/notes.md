# Week 7 — The Perimeter
**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned
This week shifted my perspective from builder to scout, focusing on reconnaissance, scanning, and vulnerability analysis. I learned how to perform passive OSINT to map an organization’s digital footprint without touching its infrastructure, and how to “go loud” with active scanning using Nmap on an isolated subnet. I also practiced interpreting vulnerability data beyond raw CVSS scores by applying a risk-based lens — using Likelihood × Impact to prioritize what truly matters to a defender.

## Artifacts
**ThreatProfile_CloudNano.md**  
A passive reconnaissance profile built from OSINT sources. I used tools like Sublist3r, Wappalyzer/BuiltWith, HaveIBeenPwned, and Shodan to enumerate subdomains, identify tech stacks, and check for credential leaks without sending direct traffic to the target’s servers.

**nmap_scan_results.txt**  
An active enumeration log of the 172.99.0.0/24 (and TLAB 7’s 172.88.0.0/24) sandbox networks. This artifact documents host discovery, open ports, and service version data gathered with Nmap ping sweeps and `-sV` scans, forming the basis of a professional network enumeration map.

**remediation_plan.md**  
A written vulnerability triage plan based on automated web scans (e.g., Nikto) and a 20‑item corporate report. I applied the Risk = Likelihood × Impact framework to reduce the noise down to the top five findings, justifying each remediation priority in clear, defensive language.

**Perimeter_Assessment.md**  
The TLAB 7 artifact for Operation Shadow Map. This perimeter assessment report consolidates Nmap ping sweep results on 172.88.0.0/24, Nikto findings against two web servers, and a final risk prioritization for TitanCorp’s suspected CloudNano assets. It concludes with a clearly justified “top risk” finding for the CISO based on exposure, exploitability, and business impact.

## Challenges & How I Solved Them
One challenge was keeping passive recon truly “passive.” It was tempting to probe targets directly, but I stayed within OSINT boundaries by relying on third‑party data sources and search engines instead of sending packets to production infrastructure.  

Active scanning introduced another challenge: interpreting Nmap output across multiple hosts and ports without getting overwhelmed. I solved this by organizing results by IP, then by service, and focusing on version data that mapped to known vulnerabilities or misconfigurations.  

During Operation Shadow Map, the hardest part was triaging findings from Nikto and Nmap into a single, defensible priority. I resolved this by explicitly scoring each issue on Likelihood and Impact, then selecting the one with both high exposure (internet-facing) and high potential damage as my top risk.

## Reflection
Week 7 helped me understand that strong defense starts with clear visibility. Learning how to map assets, enumerate services, and prioritize vulnerabilities made me think more like an attacker and a defender at the same time. Going forward, I want to deepen my OSINT techniques and become faster at turning raw scan data into concise, executive-ready risk narratives.

## References
SANS Institute. (2024). *Reconnaissance and footprinting techniques.* https://www.sans.org  
Nmap Project. (2025). *Nmap reference guide.* https://nmap.org/book  
OWASP Foundation. (2025). *Risk rating methodology.* https://owasp.org

# Week 8 — The Breach
**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned
This week marked the transition from reconnaissance to full offensive operations. I learned how to validate vulnerabilities through controlled exploitation, escalate privileges on both Linux and Windows systems, and maintain persistent access through scheduled backdoors. I also practiced deep network pivoting, using a compromised host as a launch point to reach an otherwise unreachable internal database. Finally, I shifted back to the defensive mindset by building a Python brute‑force detector to analyze authentication logs.

## Artifacts
**escalation_path.txt**  
This file records my privilege escalation chain from Session 23. It includes the GTFOBins‑based sudo bypass on Linux and the Windows Unquoted Service Path hijack, demonstrating how misconfigurations can be chained to reach full SYSTEM‑level control.

**Deep_Pivot_Report.md**  
The full mission report for Operation Deep Pivot. It documents all three phases: privilege escalation on the bastion host, persistence via cron, and network pivoting to scan the air‑gapped vault server. The report includes real commands, outputs, and findings from each phase.

## Challenges & How I Solved Them
One challenge was stabilizing the initial foothold during exploitation. The reverse shell would occasionally drop, so I validated connectivity with Netcat before launching Metasploit to ensure the exploit chain was reliable.  
Privilege escalation also required careful analysis. The sudo misconfiguration was subtle, but by checking allowed binaries and cross‑referencing GTFOBins, I identified the correct bypass. The Windows escalation required understanding how unquoted service paths allow payload injection.  
The pivoting phase was the most complex. Routing traffic through the bastion required correctly adding the route in Metasploit, starting the SOCKS proxy, and configuring proxychains. After troubleshooting DNS and routing errors, I successfully scanned the hidden database and documented the open port.  
Finally, building the brute‑force detector required handling malformed log lines and ensuring the script didn’t break on unexpected input. Adding conditional checks and structured parsing solved this.

## Reflection
Week 8 pushed me to operate like a real penetration tester — exploiting, escalating, persisting, and pivoting through a live environment. It also reinforced the importance of defensive tooling, since offensive activity always leaves traces that must be detected. This week strengthened my confidence in both red‑team and blue‑team workflows, and showed me how deep network access can be achieved through chained misconfigurations.

## References
Rapid7. (2025). *Metasploit Framework documentation.* https://docs.rapid7.com  
GTFOBins. (2025). *Privilege escalation techniques.* https://gtfobins.github.io  
The Linux Foundation. (2025). *Cron, scheduling, and persistence.* https://linuxfoundation.org  
OWASP Foundation. (2025). *Authentication and brute‑force attack patterns.* https://owasp.org

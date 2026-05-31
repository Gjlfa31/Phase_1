# Week 1 — Terminal Supremacy
**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned
This week focused on mastering the Linux command line as a secure and efficient navigation tool. I learned how command anatomy, the Filesystem Hierarchy Standard (FHS), and headless navigation work together to support system administration and security analysis. I also developed a deeper understanding of Linux permissions, the RWX matrix, and how misconfigurations—especially in sensitive files like `/etc/shadow`—can create serious security risks. Finally, I strengthened my ability to treat text as data by using tools like `grep`, `sed`, and `awk` to transform and analyze large datasets.

## Artifacts
**discovery.txt**  
Captured the results of navigating the Linux filesystem and mapping multi‑directory structures. This artifact reflects my ability to apply the FHS to locate configuration files and understand how web applications organize their components.

**harden.sh**  
A shell script implementing basic permission and configuration hardening. Building this required applying octal and symbolic notation, identifying insecure permission states, and automating fixes to reduce attack surface.

**threats_ips.txt**  
A filtered list of high‑priority IP addresses extracted from large log files. I produced this by using stream‑editing tools to isolate patterns, remove noise, and convert raw logs into actionable intelligence.

**final_threat_report.txt**  
A summary of findings from Week 1, including permission issues, suspicious activity, and recommended mitigations. This report demonstrates my ability to synthesize command‑line output into a structured security assessment.

## Challenges & How I Solved Them
One major challenge was diagnosing permission errors during the Permissions Gauntlet, especially when working with files like `/etc/shadow`. I initially struggled to understand why certain commands failed, but by breaking down the RWX matrix and checking ownership with `ls -l`, I was able to pinpoint the exact misconfigurations.  
Another challenge came during the log‑analysis deep dive, where parsing a 10,000‑line Apache log felt overwhelming. I solved this by chaining commands with pipes, using `grep` to filter, `awk` to extract fields, and `sort | uniq -c` to identify the top IP addresses efficiently.

## Reflection
Week 1 reinforced that the command line is not just a tool but a core security skill. Understanding permissions, filesystem structure, and text processing gives me the foundation to analyze systems confidently and respond to incidents quickly. Moving forward, I want to improve my speed and precision with stream‑editing tools so I can handle even larger datasets with ease.

## References
The Linux Documentation Project. (2024). *The Linux system administrator’s guide.* https://tldp.org  
GNU Project. (2025). *GNU Coreutils manual.* https://www.gnu.org/software/coreutils  
Apache Software Foundation. (2025). *Log formats and analysis.* https://httpd.apache.org/docs/

# Week 3 — Scripting the Defense
**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned
This week marked the shift from operator to builder, where I learned how to transform manual command‑line workflows into automated Python tools. I explored Python as a security instrument rather than a general programming language, focusing on data types, logic, loops, and functional automation to process real security data at scale. I also learned how to isolate scripts in virtual environments to prevent dependency conflicts and safely interact with the operating system through file parsing and port checking.

## Artifacts
**port_check.py**  
A Python script built during Session 07 to validate open ports using the `socket` library. This required setting up and activating a Python virtual environment to isolate dependencies and prevent system‑level conflicts while testing defensive tools.

**brute_detector.py**  
Created in Session 08, this script uses lists, loops, and conditional logic to categorize network events by risk level. It automates the process of cross‑referencing incoming traffic against known malicious IPs, enabling scalable threat filtering.

**system_auditor.py**  
Developed in Session 09, this script reads system logs, identifies failed login attempts, and writes flagged entries to a new block‑list file. It incorporates functions and error‑handling to ensure stability even when logs are missing or corrupted.

**incident_response.py**  
This was the Week 3 Take‑Home Lab (TLAB): *Operation Automated Hunt*. The mission required building a Python‑based incident response tool that detects brute‑force attacks by parsing simulated authentication logs. The script uses `subprocess.run()` to grep for “Failed password” attempts , extracts attacker IPs through line‑by‑line parsing and string splitting , and exports a structured JSON alert containing the threat data .  
The final deliverables were `incident_response.py` and the generated `threat_report.json`, both pushed to GitHub as required .

## Challenges & How I Solved Them
One challenge was preventing scripts from crashing due to unexpected input or missing files. I solved this by implementing `try/except` blocks and validating user input early, which made my tools more resilient.  
Another challenge came from structuring loops and logic cleanly when processing large datasets. Breaking the problem into smaller functions helped me maintain readability and reuse code across multiple scripts.  
Finally, setting up the virtual environment initially caused path issues, but reviewing the activation steps and verifying my environment variables allowed me to isolate dependencies correctly.

## Reflection
Week 3 pushed me to think like an automation engineer, not just a command‑line operator. Building tools that can parse logs, detect threats, and write actionable intelligence helped me understand how real SOC teams scale their workflows. Adding the TLAB reinforced how automation accelerates incident response and reduces analyst workload. Moving forward, I want to refine my function design and improve my ability to structure larger automation projects.

## References
Python Software Foundation. (2025). *Python 3 documentation.* https://docs.python.org  
The Linux Foundation. (2025). *System log architecture and analysis.* https://linuxfoundation.org  
IETF. (2024). *Socket programming standards.* https://ietf.org

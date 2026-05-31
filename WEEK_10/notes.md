# Week 10 — The Defender
**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned
This week marked the transition from offensive operations to full Digital Forensics and Incident Response (DFIR). I learned how to execute the PICERL lifecycle, perform live triage without destroying volatile evidence, and use cryptographic hashing to maintain a defensible Chain of Custody. I also practiced disk forensics using The Sleuth Kit to recover deleted files and used a SIEM (Kibana/ELK) to correlate logs and reconstruct an attacker’s timeline. This week emphasized evidence‑driven investigation and professional reporting.

## Artifacts
**collection_log.txt**  
Created during Session 28, this artifact documents my live response actions on a compromised system. It includes initial triage steps, cryptographic hashing, and chain‑of‑custody validation using MD5 and SHA256.

**forensic_findings.md**  
Generated during Session 29, this file captures my memory forensics and disk imaging workflow. It includes MFT enumeration, deleted file identification, and raw data extraction using `fls` and `icat`.

**attack_timeline.csv**  
Produced during Session 30, this report contains my SIEM log correlation work. I used Kibana to search for critical alerts, pivot through related logs, and reconstruct the attacker’s movement across the environment.

**Incident_Response_Report.md**  
The TLAB 10 artifact for Operation Phantom Pursuit. This full investigation report documents all three phases: SIEM correlation (source IP discovery) , live triage and chain‑of‑custody hashing (PID + SHA256) , and disk forensics to recover the deleted `beacon.exe` payload using inode extraction and Sleuth Kit tooling . It represents the complete breach lifecycle from alert to evidence recovery.

## Challenges & How I Solved Them
One challenge was configuring the SIEM index correctly. Without the proper index pattern (`enterprise_logs*`), no alerts appeared. After reviewing the Stack Management workflow, I recreated the index and successfully located the “Critical Alert” entry containing the attacker’s source IP .

Live triage also presented difficulties. Identifying the malicious process required carefully parsing `netstat -antp` output inside the quarantined host. Once I located the process listening on port 4444, I documented the PID and exited cleanly to avoid contaminating evidence .

Disk forensics was the most technically demanding phase. Navigating the MFT with `fls -r` required patience, and locating the deleted `beacon.exe` file meant scanning for entries marked with an asterisk. After identifying the correct inode, I used `icat` to extract the payload and verified the recovered data before adding it to my report .

## Reflection
Week 10 solidified my understanding of what it means to be a defender. Instead of exploiting systems, I had to reconstruct an attacker’s actions using evidence alone. This week strengthened my investigative mindset, attention to detail, and ability to produce professional forensic documentation. Moving forward, I want to deepen my skills in SIEM query design and automate parts of the triage workflow.

## References
The Sleuth Kit. (2025). *File system forensics tools.* https://sleuthkit.org  
Elastic. (2025). *Kibana and SIEM log analysis documentation.* https://elastic.co  
NIST. (2024). *Incident Response Lifecycle (PICERL) guidelines.* https://csrc.nist.gov

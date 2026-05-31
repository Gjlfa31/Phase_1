# Week 6 — The Forge: Sprint Finale
**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned
Week 6 was a culmination of everything learned in the first half of the fellowship. Instead of introducing new tools, this week required me to diagnose, repair, and deploy systems using the full stack of skills from Weeks 1–5. I learned how to map failures to OSI layers, troubleshoot under pressure, and architect a complete enterprise environment from scratch. This week emphasized synthesis, resilience, and the ability to operate without guidance — the core traits of a real security engineer.

## Artifacts
**readiness_check.log**  
Created during Session 16, this artifact documents my diagnosis and repair of a deliberately sabotaged environment. I identified a Layer 7 file‑permission lockout, resolved a Layer 4 Docker port conflict, and validated system recovery using the Outside‑In troubleshooting methodology.

**practical_exam_report.txt**  
This report captures my work during the Session 17 practical exam. I located hidden root‑owned `.log` files, moved them to a secure directory, and applied strict permissions. This artifact demonstrates my ability to perform Linux, networking, and file‑system tasks under timed, no‑assistance conditions.

**HardenedOutpost_SAD.pdf**  
The capstone Security Architecture Document for Session 18. It outlines the full deployment of a cross‑platform enterprise environment: promoting a Windows Server to a Domain Controller, joining a Linux host to the domain, writing a Python auditing script, and architecting an air‑gapped Docker Compose stack. This document reflects my ability to design, justify, and communicate a complete security architecture.

## Challenges & How I Solved Them
One major challenge was diagnosing the sabotaged environment in Session 16. The permission lockout initially appeared to be a user‑level issue, but by checking ownership and applying OSI mapping, I traced it to a Layer 7 application‑level failure. The Docker port conflict required identifying the container binding to port 8080 and removing it before redeploying services.

During the practical exam, the biggest challenge was locating hidden `.log` files owned by root. I solved this by using targeted `find` commands and verifying permissions with `ls -la` before applying secure access controls.

The capstone deployment was the most demanding task. Managing Windows AD promotion, Linux domain joining, and Docker Compose orchestration simultaneously required careful sequencing. I overcame this by breaking the deployment into phases, validating each component before moving on, and documenting every configuration step in the SAD.

## Reflection
Week 6 transformed my understanding of what it means to be a security operator. Instead of following instructions, I had to diagnose, design, and deploy independently — just like a real engineer responding to a 2 AM outage. This week strengthened my confidence in troubleshooting, system architecture, and cross‑platform integration. Moving forward, I want to continue improving my speed in diagnosing OSI‑layer failures and refine my ability to write clear, professional architecture documentation.

## References
Microsoft. (2025). *Active Directory Domain Services overview.* https://learn.microsoft.com  
Docker Inc. (2025). *Docker networking and Compose documentation.* https://docs.docker.com  
The Linux Foundation. (2025). *Linux troubleshooting and system diagnostics.* https://linuxfoundation.org

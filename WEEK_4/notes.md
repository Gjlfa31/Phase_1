# Week 4 — Fortifying the Node
**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned
This week focused on infrastructure hardening across virtual machines, containers, and multi‑service orchestration. I learned how hypervisors isolate workloads, how containerization differs from hardware virtualization, and how network segmentation prevents lateral movement. I also gained hands‑on experience designing secure environments by configuring Host‑Only networks, deploying isolated containers, and orchestrating multi‑tier stacks with Docker Compose.

## Artifacts
**sandbox_report.txt**  
This report documents the process of converting a VirtualBox VM from Bridged mode to Host‑Only mode and validating that the VM was fully isolated. It includes the malware detonation test performed in the Quarantine Zone and the forensic observations gathered during the deep dive.

**deploy_web.sh**  
A deployment script that automates pulling an Alpine/Nginx image, running it interactively, modifying content, auditing logs, and destroying the container cleanly. This artifact demonstrates mastery of the Docker workflow and the difference between VM‑level and container‑level isolation.

**docker-compose.yml**  
A declarative multi‑container configuration defining a segmented WordPress + MariaDB stack. It includes two networks (`public_net` and `private_net`), a named volume (`db_data`), and an air‑gapped database service. This file reflects the orchestration principles learned in Session 12.

**hyperstack_audit.json**  
The final artifact for TLAB 4: Operation Fortified Node. This machine‑readable audit includes my real host IP, VM sandbox IP, container ID, isolation test result, and volume persistence verification. It documents the full mission: evicting the squatter container, deploying the hardened three‑tier stack, validating network segmentation, and confirming that the database remained isolated.

## Challenges & How I Solved Them
One challenge was ensuring the VM was correctly isolated in Host‑Only mode. I initially misread the interface list, but by re‑running `ip addr` and confirming the 192.168.56.x range, I aligned the VM with the required network configuration.  
Another challenge occurred during the eviction phase when the decoy_web container continued responding on port 80. I resolved this by fully removing the container and re‑auditing the port with `curl` to confirm the environment was clean.  
The most difficult step was the isolation test inside the WordPress container. The requirement was that the container must not be able to ping the VM’s Host‑Only IP. After verifying the failure, I documented the result in the JSON artifact and confirmed that the private network was functioning as intended.

## Reflection
Week 4 pushed me to think like a systems architect rather than just an operator. Designing hardened environments, enforcing segmentation, and validating isolation gave me a deeper understanding of secure infrastructure design. Moving forward, I want to continue improving my ability to architect multi‑layered defensive environments and automate more of the deployment process.

## References
Oracle. (2025). *VirtualBox networking guide.* https://www.virtualbox.org  
Docker Inc. (2025). *Docker and containerization fundamentals.* https://docs.docker.com  
Docker Inc. (2025). *Docker Compose specification.* https://docs.docker.com/compose

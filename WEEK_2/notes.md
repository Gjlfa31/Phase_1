# Week 2 — Networking, Subnetting & Protocol Interrogation
**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned
This week focused on understanding how devices communicate across a network and how misconfigurations at Layers 1–3 can isolate or expose systems. I learned how to identify network interfaces, restore broken routes, and rebuild connectivity using tools like `ip link`, `ip addr`, and `ip route`. I also strengthened my understanding of CIDR notation and subnet boundaries, and how mathematical errors in masks can completely sever communication. Finally, I explored DNS, ports, and service discovery to uncover hidden services and remediate deception at the application layer.

## Artifacts
**network_audit.txt**  
Documented the state of all network interfaces, MAC addresses, and IP assignments. This artifact demonstrates my ability to diagnose downed links and restore a default gateway to bring a system back online.

**subnet_blueprint.txt**  
A breakdown of subnet calculations performed during the Subnetting Crucible. I used binary conversion and CIDR math to map secure boundaries and correct a mismatched subnet mask during Operation Grid Lock.

**protocol_audit.txt**  
Captured DNS queries, open ports, and service discovery results using tools like `ss` and `dig`. This artifact includes the remediation steps taken to fix a poisoned `/etc/hosts` file and locate a service running on a non‑standard port.

## Challenges & How I Solved Them
The biggest challenge this week was restoring connectivity during Operation Broken Link. The system appeared functional, but the default gateway was missing, causing all outbound traffic to fail. By checking interface states with `ip link` and verifying routes with `ip route`, I identified the missing gateway and manually rebuilt the path.

Subnetting also presented difficulties, especially when converting between decimal and binary to understand mask boundaries. I solved this by writing a small Python helper to visualize octets as 8‑bit strings, which made it easier to see where the network and host portions were misaligned.

During Operation Hidden Door, I initially misdiagnosed the issue as a DNS outage. After inspecting `/etc/hosts`, I discovered a malicious override redirecting traffic. Removing the poisoned entry and scanning ports with `ss -tulpn` revealed the hidden service and allowed me to complete the audit.

## Reflection
Week 2 pushed me to think like a network troubleshooter and a security analyst at the same time. Understanding how connectivity breaks — and how to rebuild it — gave me confidence in diagnosing real-world outages. I also gained a deeper appreciation for how small configuration errors can create major security gaps. Moving forward, I want to continue improving my speed with CIDR calculations and deepen my understanding of service enumeration.

## References
Cisco Systems. (2024). *IP addressing and subnetting guide.* https://www.cisco.com  
The Linux Foundation. (2025). *Linux networking tools reference.* https://linuxfoundation.org  
IETF. (2024). *Domain Name System (DNS) specifications.* https://ietf.org

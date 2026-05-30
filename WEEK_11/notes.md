# Week 11 — The Fortress
**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned
This week shifted my focus fully into defensive engineering. I learned how to design a multi‑layered perimeter that stops attackers at the firewall, detects them on the wire, and catches them on the endpoint. I practiced building a DMZ architecture with Docker subnets, writing raw iptables egress filtering rules, deploying Suricata as a live IDS sensor, and crafting SysmonForLinux XML policies to detect ransomware precursor behavior. Week 11 emphasized Defense in Depth — not as a theory, but as a system I engineered myself.

## Artifacts
**firewall_config.sh**  
Created during Session 31, this script contains the iptables egress filtering rule I engineered to block all outbound traffic to the attacker’s C2 subnet (198.51.100.0/24). This artifact demonstrates my ability to enforce outbound restrictions and prevent compromised servers from calling home.

**custom_ids.rules**  
Built during Session 32, this file includes my custom Suricata IDS signature designed to detect the exact malicious payload `cmd=whoami` sent over TCP port 80. The rule uses a SID above 1,000,000 and triggers alerts in `fast.log` when the exploit crosses the perimeter.

**edr_policy.xml**  
Developed during Session 33, this XML policy defines a `<ProcessCreate>` detection rule that flags any command containing `curl http://198.51.100.5`. This artifact demonstrates endpoint‑level detection engineering using SysmonForLinux.

**Operation_Fortress_Report.md**  
The TLAB 11 artifact for Operation Fortress. This report documents all three defensive layers working together: the egress firewall rule, the Suricata signature, and the Sysmon detection policy. It represents a complete Defense in Depth architecture designed to stop, detect, and contain an active adversary.

## Challenges & How I Solved Them
One challenge was writing the iptables rule correctly. Small syntax errors caused the rule to silently fail. By testing with `iptables -L -v -n` and sending controlled outbound traffic, I confirmed the DROP rule was active and blocking the C2 subnet.

Another challenge came from Suricata signature engineering. My first rule triggered no alerts because the content match was not placed in the correct direction of traffic. After reviewing Suricata’s rule structure, I corrected the flow and verified alerts in `fast.log`.

The Sysmon XML policy was the most sensitive to formatting. Incorrect indentation or tag placement caused Sysmon to reject the configuration. I validated the XML structure carefully, reloaded Sysmon, and confirmed the detection fired when executing the malicious curl command.

## Reflection
Week 11 solidified my understanding of how real enterprise defenses are built. Offensive knowledge from earlier weeks directly informed my defensive engineering — I knew exactly what attackers would try, and I built controls to stop them. This week strengthened my confidence in designing layered security architectures and writing custom detection logic. Moving forward, I want to deepen my skills in IDS tuning and endpoint telemetry analysis.

## References
Suricata IDS Project. (2025). *Rule writing and detection engine documentation.* https://suricata.io  
Microsoft. (2025). *Sysmon for Linux configuration guide.* https://learn.microsoft.com  
Netfilter Project. (2025). *iptables administration reference.* https://netfilter.org

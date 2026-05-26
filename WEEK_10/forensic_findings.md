# FORENSIC FINDINGS REPORT (THE MALWARE AUTOPSY)

### WHO:
* The Threat Actor is Ghost_Bear. A hidden process was revealed: rootkit_beacon.exe with a PID of 4444

### WHAT:
* The deleted malicious executable is Resume.exe found with a inode of 582.

### WHEN:
* The recovered malware payload contained an embedded timestamp of 04/30/2026 02:00:00 UTC.

### HOW:
* The infection began when the user executed Resume.exe, which deployed a hidden process (rootkit_beacon.exe) that did not appear in normal system process listings.

The malware established persistence by adding itself to: HKLM\Software\Microsoft\Windows\CurrentVersion\Run

It also modified a critical system file: C:\Windows\System32\drivers\tcpip.sys, indicating a deeper system compromise.

After execution, the attacker attempted anti‑forensic cleanup by deleting the executable from disk. Despite this, memory artifacts and the recovered payload provided enough evidence to reconstruct the infection chain.

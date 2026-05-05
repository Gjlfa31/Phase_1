# TARGET THREAT PROFILE: CloudNano 
**Classification:** Passive Security Audit
**Operator:** ## 1. Subdomain Discovery 
* **Tool Used:** Sublist3r
* **Subdomains Found:** * [Subdomain 1: news.yahoo.com] 
  * [Subdomain 2: finance.yahoo.com] 

## 2. Tech Stack Mapping 
* **Tool Used:** BuiltWith / Wappalyzer
* **Identified Technologies (CMS/CDN/Backend):** * [Tech 1: Analytics & Tracking (Google Analytics, Datadog RUM)] 
  * [Tech 2: Backend Technologies: Java EE, Perl, nginx]
  * [Tech 3: CDN: CloudFront, Amazon S3, Yahoo Image CDN] 

## 3. Major Exposure Points & Dangers 
*(List three major exposure points discovered during your OSINT audit and explain why they are dangerous)*
1. **[Exposure Point 1: A lot of third-party tracking & analytics]:** [Why it is a danger: because each additional third-party involved increases the attack surface and creates new ways for attackers to gain unauthorized access to the internal server.] 
2. **[Exposure Point 2: Complex Tech Stack with legacy components]:** [Why it is a danger: because legacy factors often contain unpatched vulnerabilities and increased weaknesses in regard to modern attacking methods.] 
3. **[Exposure Point 3: Reliant on CDN and CLoud Infrastructure]:** [Why it is a danger: because misconfigurations in cloud/CDN infrastucture, or even attacks to the cloud/CDN environements themselves can result in the exposure of highly sensitive data accompanied by other risks.] 

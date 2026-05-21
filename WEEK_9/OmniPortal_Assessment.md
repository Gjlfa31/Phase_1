# OMNI-PORTAL ASSESSMENT REPORT
**Operator:** **Deadline:** April 5 @ 11:59 PM 

## PHASE 1: AUTH BYPASS (SQLi)
* **Payload Used:** ' OR 1=1 --
* **Result:** Successfully bypassed login and obtained 'auth_token' cookie with the value: SUPPORT_TIER_1_SECRET_TOKEN.

## PHASE 2: CLIENT-SIDE HIJACK (XSS)
* **Stored XSS Payload:** <script>alert(document.cookie)</script>
* **Secret Cookie Captured:** SUPPORT_TIER_1_SECRET_TOKEN

## PHASE 3: API ENUMERATION (BOLA)
* **Insecure Order ID:** 501
* **Confidential Data Leaked:** {"amount":"$15,000.00","details":"Confidential Server Lease","order_id":501}

## PHASE 4: THE REMEDIATION
* **Fix for SQLi:** Since the root cause of this is the user input being concatenated directly into SQL queries, a fix for SQLi would be to use parameterized queries which are basically prepared statements so that user input is never executed as SQL queries in the first place. 
* **Fix for XSS:** XSS occur because of comments that are supplied by the user which are rendered into HTML without escaping, which means that the ideal fix for this would be to apply context aware output encoding before rendering user input into HTML.
* **Fix for API BOLA:** An easy fix for this sort of vulnerability would be to add an ownership check before returning the requested order. This would make it so that the confidentiality of the CIA triad is being respected.

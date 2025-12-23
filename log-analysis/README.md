#  Log Analysis Lab — Detecting Brute-Force Attempts Using Python

This project is part of my **Cybersecurity Blue Team practice** series.  
It focuses on detecting **SSH brute-force attempts** from real-world Linux log data using Python.

---

##  Project Overview

Linux systems record authentication activity under `/var/log/`, commonly in `messages` or `secure` logs.  
Using sample data from the **[LogHub Public Security Log Sharing Project](https://github.com/logpai/loghub)**, this lab simulates how a SOC analyst can parse, structure, and detect malicious login behavior.

---

##  How It Works

The workflow uses three Python scripts that run in sequence:

### **1️ `read_failures.py` — Log Reader**
- Reads the raw log file (`Linux_2k.log`).
- Filters lines containing authentication failures (e.g., from `sshd` or `pam_unix`).

 *Purpose:* Extract only relevant failed login entries from thousands of log lines.

---

### **2️⃣ `extract_fields.py` — Data Extractor**
- Reads `Linux_2k.log` and uses **regular expressions** to extract:
  - Date & Time  
  - Hostname  
  - Service (e.g., `ssshd`)  
  - Username  
  - Source IP address  
- Outputs the structured data

 *Purpose:* Transform raw text into structured, machine-readable data.

---

### **3️⃣ `count_attempts.py` — Attack Detector**
- Counts how many failed login attempts come from each IP address.
- Flags IPs with unusually high failure counts as **suspicious** (possible brute-force sources).
- Saves these to `alerts.csv`.

 *Purpose:* Identify and report suspicious IPs that may be performing brute-force attacks.

---

##  File Outputs

| File | Description |
|------|--------------|
| `alerts.csv` | List of suspicious IPs and attempt counts |

---

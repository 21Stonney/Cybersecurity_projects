
#  Cybersecurity Projects

A collection of hands-on cybersecurity labs, tools, and automation scripts I’m building to strengthen my skills in threat detection, network defense and SOC operations.

---

##  Projects

### 1. [Wazuh Docker SOC](./wazuh-docker)
A containerized Wazuh setup for real-time monitoring, alerting, and log analysis.  
Focus areas:
- SIEM configuration  
- Security event indexing  
- Dashboard analytics

```
#  Wazuh Docker SOC

This project sets up a **home SOC (Security Operations Center)** using **Wazuh**, deployed with **Docker Compose**.  
It provides **real-time monitoring, alerting, and visualization** of host security events.

##  Components

| Service | Description |
|----------|-------------|
| **Wazuh Manager** | Collects and analyzes logs from agents |
| **Wazuh Indexer** | Stores indexed security events |
| **Wazuh Dashboard** | Web interface for alerting and visualization |

##  Setup



## Start the Stack:
sudo docker-compose up -d

## Access the Dashboard:
Open: https://127.0.0.1

Default credentials:
Username: admin
Password: admin


###  Clone the Project
If you don’t have it yet:

git clone https://github.com/21Stonney/Cybersecurity_projects.git
cd Cybersecurity_projects/wazuh-docker

```
---

### 2. Log Analysis Lab - Detecting Brute-Force Attempts 
A Python-based log analysis lab for detecting SSH brute-force attacks using real Linux logs.
Focus areas:

Log parsing and regex extraction

Suspicious IP detection

SOC-style log triage workflow
```
#  Log Analysis Lab — Detecting Brute-Force Attempts Using Python

This project analyzes Linux authentication logs to detect **SSH brute-force attempts** using Python.  
It demonstrates how to process, extract, and identify suspicious login activity from real-world data.

##  Project Flow

1️⃣ **read_failures.py** — Reads raw logs and filters failed authentication attempts  
2️⃣ **extract_fields.py** — Extracts key fields (date, user, IP, etc.) into CSV format  
3️⃣ **count_attempts.py** — Counts failed attempts per IP and flags suspicious ones


### Clone the Project

git clone https://github.com/21Stonney/Cybersecurity_projects.git
cd Cybersecurity_projects/log-analysis/src


```


##  Dataset
Dataset source: [LogHub Public Security Log Sharing Project](https://github.com/logpai/loghub)


---

##  Learning Goals
- Practice real-world SOC monitoring and detection  
- Automate repetitive security analysis tasks  
- Explore blue team tools and network visibility
- Strengthen incident response and threat-hunting skills
- Build hands-on experience with security tooling in a lab environment

---

### Star this repo if you find it useful or want to follow my cybersecurity journey!

### 1. [Wazuh Docker SOC](./wazuh-docker)
A containerized Wazuh setup for real-time monitoring, alerting, and log analysis.  
Focus areas:
- SIEM configuration  
- Security event indexing  
- Dashboard analytics

```markdown
# 🧩 Wazuh Docker SOC

This project sets up a **home SOC (Security Operations Center)** using **Wazuh**, deployed with **Docker Compose**.  
It provides **real-time monitoring, alerting, and visualization** of host security events.

## 🧰 Components

| Service | Description |
|----------|-------------|
| **Wazuh Manager** | Collects and analyzes logs from agents |
| **Wazuh Indexer** | Stores indexed security events |
| **Wazuh Dashboard** | Web interface for alerting and visualization |

## ⚙️ Setup

###  Clone the Project
If you don’t have it yet:

git clone https://github.com/21Stonney/Cybersecurity_projects.git
cd Cybersecurity_projects/wazuh-docker

## Start the Stack:
sudo docker-compose up -d

## Access the Dashboard:
Open: https://127.0.0.1

Default credentials:
Username: admin
Password: admin

```

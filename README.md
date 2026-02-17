# Cloud Security Honeypot Analyzer

A Python-based SSH honeypot log analyzer used to detect brute-force login attempts by analyzing real-world attack data.

This project processes honeypot logs, extracts attacker IP addresses, counts failed login attempts, and generates a report highlighting suspicious sources.

---

## 📌 Project Overview

Modern cloud systems face constant automated attacks. One common method is brute-force SSH login attempts.

This project demonstrates how Python can be used to:

- Parse honeypot SSH logs
- Extract attacker IP addresses
- Count failed login attempts per IP
- Identify suspicious activity
- Generate a summarized security report

The dataset comes from a public SSH honeypot capturing real attack traffic.

---

## 📂 Files Included

- `main.py` – Python script for analyzing honeypot logs  
- `honeypot.txt` – SSH honeypot dataset  
- `report.txt` – Generated attack summary report  

---

## ⚙️ How It Works

1. Reads SSH honeypot logs
2. Extracts IP addresses from failed login attempts
3. Counts failures per IP
4. Flags IPs exceeding a threshold
5. Outputs results to `report.txt`






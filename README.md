📊 SOC Ticket Processor
This Streamlit app streamlines the analysis of ServiceNow SOC incident reports and Tenable vulnerability data. It extracts hosts and solutions from incident descriptions, matches them against Autodesk vulnerability data, and highlights matches with color-coded Excel output for easy review.

🚀 Features
Upload and process:

✅ ServiceNow SOC Incident Report (.xlsx)

✅ Tenable Vulnerability Report (.csv)

Extract hosts and solutions from incident descriptions using regex

Match incidents against Tenable solutions

Color-coded Excel output:

🔴 Red: Host with matching solution found

🟢 Green: Host without matching solution

Identify duplicate hosts with shared solutions

Download:

📥 Processed incident file

📥 Cleaned Tenable report

View troubleshooting-required incidents and duplicates in-app

📂 File Inputs
1. Incident Report
Format: Excel (.xlsx)

Required Column: Description

Content: Free-text descriptions containing hostnames and solution references

2. Tenable Report
Format: CSV (.csv)

Required Columns:

asset.name — Hostname

definition.solution — Suggested remediation

🧠 Logic Highlights
🔍 Regex-based extraction of hostnames and solution keywords

🧹 Cleaning and normalization of Tenable data for reliable matching

🔗 Host-solution matching with validation

♻️ Duplicate host detection with shared solution logic

🎨 Excel styling via openpyxl for visual clarity and quick triage

📦 Installation
bash
pip install -r requirements.txt
▶️ Run the App
bash
streamlit run app.py
💡 Make sure you're in the project directory before running the app.

🛠️ Troubleshooting
Ensure both input files are correctly formatted and contain required columns

If regex extraction fails, check for inconsistent formatting in the Description field

For Excel styling issues, confirm openpyxl is installed and compatible

📌 Notes
Designed for SOC analysts and vulnerability managers

Optimized for Autodesk-style Tenable exports

Easily extendable for other formats or matching logic

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to modify.

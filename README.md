# 📊 SOC Ticket Processor

This Streamlit app streamlines the analysis of ServiceNow SOC incident reports and Tenable vulnerability data. It extracts hosts and solutions from incident descriptions, matches them against Autodesk vulnerability data, and highlights matches with color-coded Excel output.

## 🚀 Features

- Upload and process:
  - ServiceNow SOC Incident Report (`.xlsx`)
  - Tenable Vulnerability Report (`.csv`)
- Extract hosts and solutions from incident descriptions
- Match incidents against Tenable solutions
- Color-coded Excel output:
  - 🔴 Red: Host with matching solution found
  - 🟢 Green: Host without matching solution
- Identify duplicate hosts with shared solutions
- Download processed incident file and cleaned Tenable report
- View troubleshooting-required incidents and duplicates in-app

## 📂 File Inputs

- **Incident Report**: Excel file with a `Description` column containing host and solution info
- **Tenable Report**: CSV file with vulnerability data including `asset.name` and `definition.solution`

## 🧠 Logic Highlights

- Regex-based extraction of hosts and solutions
- Host-solution matching using cleaned Tenable data
- Duplicate host detection with shared solution validation
- Excel styling via `openpyxl` for visual clarity

## 📦 Installation

```bash
pip install -r requirements.txt

▶️ Run the App
bash
streamlit run app.py

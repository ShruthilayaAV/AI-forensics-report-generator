# AI-Driven Digital Forensics Investigation Bot

An AI-powered Digital Forensics and Incident Response (DFIR) assistant that automates forensic evidence collection, log analysis, and professional forensic report generation using Retrieval-Augmented Generation (RAG), ChromaDB, and Google's Gemini AI.

---

## Project Overview

Digital forensic investigations often require analysts to manually examine system processes, correlate logs, identify indicators of compromise, and document findings. This process can be repetitive, time-consuming, and prone to human error.

This project automates major stages of forensic analysis by collecting telemetry from Linux systems, retrieving relevant cybersecurity knowledge through Retrieval-Augmented Generation (RAG), and using Large Language Models (LLMs) to generate structured forensic investigation reports.

The generated reports follow a Digital Forensics and Incident Response (DFIR) format, helping investigators quickly analyze suspicious processes and document incidents.

---

## Features

- AI-assisted forensic investigation
- Linux process inspection
- Time-window based log collection
- Automatic telemetry source detection
- Retrieval-Augmented Generation (RAG)
- ChromaDB knowledge retrieval
- Gemini AI powered forensic analysis
- SHA-256 evidence hashing
- Automated HTML forensic report generation
- Chronological incident reconstruction
- Professional DFIR report formatting
- Investigation recommendations

---

## Technologies Used

- Python
- Google Gemini API
- ChromaDB
- Retrieval-Augmented Generation (RAG)
- HTML
- Linux
- Digital Forensics
- Incident Response (DFIR)

---

## Project Structure

```text
AI-forensics-report-generator/
│
├── knowledge_base/
│   ├── cmd_injection.txt
│   ├── file_inclusion.txt
│   ├── rce_patterns.txt
│   └── reverse_shells.txt
│
├── Sample_reports/
│   ├── Official_Forensic_Report_PID_20295.html
│   └── Official_Forensic_Report_PID_21296.html
│
├── agent.py
├── aut_agent.py
├── ingest.py
├── tools.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## System Workflow

```
                Linux System
                     │
                     ▼
        Process ID & Timestamp Input
                     │
                     ▼
          Telemetry Collection Agent
                     │
                     ▼
       Process & Log Data Extraction
                     │
                     ▼
       ChromaDB Knowledge Retrieval
                     │
                     ▼
      Gemini AI Forensic Analysis
                     │
                     ▼
    Structured DFIR Investigation Report
                     │
                     ▼
         HTML Report Generation
```

---

## Knowledge Base

The project uses Retrieval-Augmented Generation (RAG) to improve forensic reasoning.

Current knowledge sources include:

- Command Injection
- File Inclusion
- Remote Code Execution (RCE)
- Reverse Shell Detection

New knowledge can easily be added by placing `.txt` files inside the `knowledge_base` folder.

To index the knowledge base:

```bash
python ingest.py
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AI-forensics-report-generator.git
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GEMINI_API_KEY=your_api_key_here
```

---

## Initialize the Knowledge Base

Before running the application, ingest the knowledge base into ChromaDB.

```bash
python ingest.py
```

---

## Run the Application

Start the forensic investigation agent:

```bash
python agent.py
```

---

## Investigation Workflow

During execution, the investigator is prompted to enter:

- Process ID (PID)
- Starting Timestamp (HH:MM)

Example:

```text
Identify Subject PID: 20295
Start Investigation From (HH:MM): 19:07
```

The application then performs the following steps:

1. Verifies the process status.
2. Collects telemetry from available log sources.
3. Retrieves relevant cybersecurity knowledge from ChromaDB.
4. Performs AI-assisted forensic analysis using Gemini.
5. Correlates the collected evidence.
6. Generates a professional forensic investigation report.
7. Saves the report as an HTML document.

---

## Output

The generated investigation is exported as an HTML report.

Example output:

```text
Official_Forensic_Report_PID_20295.html
```

The report contains:

- Executive Summary
- Investigation Scope
- Evidence Sources
- Process Analysis
- Core Forensic Findings
- Incident Timeline
- Technical Evidence
- MITRE ATT&CK Mapping
- Network Analysis
- Remediation Recommendations
- Raw Telemetry Appendix

---

## Concepts Demonstrated

- Digital Forensics
- Incident Response (DFIR)
- Retrieval-Augmented Generation (RAG)
- Artificial Intelligence
- Prompt Engineering
- ChromaDB
- Linux System Analysis
- Log Analysis
- Threat Hunting
- Evidence Collection
- Cryptographic Hashing
- HTML Report Generation

---

## Sample Reports

The repository includes sample forensic investigation reports generated by the system.

- Official_Forensic_Report_PID_20295.html
- Official_Forensic_Report_PID_21296.html

These reports demonstrate the structure, depth, and formatting of the automated forensic analysis.

---

## Future Improvements

- Windows Event Log Analysis
- Memory Dump Analysis
- Network Packet Capture Support
- Multi-LLM Integration
- IOC Extraction
- Malware Signature Detection
- MITRE ATT&CK Visualization
- Interactive Investigation Dashboard
- PDF Report Export
- Multi-user Case Management

---

## Disclaimer

This project is intended solely for educational purposes and authorized digital forensic investigations. Always obtain proper authorization before analyzing systems or collecting forensic evidence.

---

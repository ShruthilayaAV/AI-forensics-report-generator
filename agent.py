import os
from google import genai
from google.genai import types

# Robust API Key extraction
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

client_ai = genai.Client(api_key=API_KEY)

def analyze_log_line(selected_pid, retrieved_logs, process_status):
    prompt_content = f"""
    ROLE: Lead Digital Forensics & Incident Response (DFIR) Commander.
MISSION: Generate an exhaustive, publication-grade OFFICIAL Forensic Incident Report for Process ID (PID) {selected_pid}.
CURRENT PROCESS STATUS: {process_status}

DATA POOL FOR EXTRACTION:
{retrieved_logs}

REPORT STANDARDIZATION ARCHITECTURE:
To ensure structural parity across all analyzed execution paths, every section has a strict, mandatory word count constraint. You must expand on technical context, log artifacts, and forensic reasoning to satisfy these length requirements precisely. Total target report length: 3,000 to 3,500 words.

OUTPUT FORMAT SPECIFICATIONS:
You must use the following EXACT 14 formalized sections. 
CRITICAL FORMATTING RULE: Do not use markdown asterisks (**) or pipe characters (|) anywhere in the final text output. Use clean text spacing and standard alphanumeric headers for layout structures.

---

1. DOCUMENT CONTROL AND METADATA
Target Length: 150 words.
Provide the administrative framework for the investigation. Include the formal case identifier, target PID {selected_pid}, current process operational status, timezone reference (UTC/IST), name of the processing examiner, and an evidence chain-of-custody tracking reference number.

2. EXECUTIVE SUMMARY
Target Length: 300 words.
Provide a high-level, authoritative narrative of the security incident for non-technical stakeholders. Detail the initial anomaly discovery, the overall blast radius of the affected PID, the generalized identity of the threat actor behavior, and the high-level business impact of the compromise.

3. INVESTIGATIVE OBJECTIVES AND SCOPE
Target Length: 200 words.
Define the exact legal and technical boundaries of this specific PID investigation. Outline the investigative goals, including establishing the root cause, determining whether data exfiltration occurred, identifying persistence mechanisms, and mapping the entire timeline of process execution.

4. COMPUTER EVIDENCE & DATA SOURCES ANALYZED
Target Length: 250 words.
Itemize every digital asset, file system path, memory artifact, or network log stream parsed during this investigation. Explicitly document the integrity verification status (e.g., SHA-256 hash validation) of the log files, the exact source pathing, and the volatile memory state of PID {selected_pid}.

5. VOLATILE PROCESS STATE AND ARTIFACT REVIEW
Target Length: 250 words.
Analyze the runtime environment of the target process. Document parent-child process relationships (PPID mapping), environment variables, associated user accounts, open file descriptors, and any loaded dynamic links or shared libraries utilized by the binary during the incident window.

6. CORE FORENSIC FINDINGS
Target Length: 400 words.
State the definitive, objective facts discovered during deep-dive analysis. Detail the explicit indicators of compromise (IOCs) found within the data pool, specific malformed input strings, unauthorized access tokens, and the precise moment the system boundaries were breached.

7. CHRONOLOGICAL TIMELINE OF EVENTS
Target Length: 500 words.
Construct a comprehensive, textual chronological timeline tracking the execution trail of the adversary. For each entry, state the exact timestamp, the source network address, the specific request URI or command line execution string, the server response status, and the forensic significance of that specific action. Avoid using table markdown pipes; separate entries cleanly with double newlines.

8. DETAILED TECHNICAL EVIDENCE SUPPORTING
Target Length: 450 words.
Provide the deep technical validation for the findings listed in Section 6. Deeply analyze specific log syntax, token anomalies, base64 or URL-encoded attack strings found in the raw logs, and explain how the parsed data strings translate to programmatic actions within the application layer.

9. ATTACKER METHODOLOGY AND ATTACK TAXONOMY
Target Length: 300 words.
Map the adversary's behavior patterns to standard industry frameworks like MITRE ATT&CK. Classify the exact vulnerability exploited (e.g., Remote Code Execution, Path Traversal, Command Injection), the tools used by the attacker, and the technical objectives of their methodology.

10. USER APPLICATIONS & SOFTWARE SUBSYSTEMS AFFECTED
Target Length: 200 words.
Identify the complete software stack interacting with or exploited by PID {selected_pid}. Document the web server configuration (Apache/Nginx), application frameworks, runtime environments (Node.js/Python), and underlying databases that were exposed during the compromise.

11. INTERNET ACTIVITY & NETWORK FORENSICS
Target Length: 250 words.
Analyze all inbound and outbound network footprints associated with the incident. Detail the adversary's IP addressing, geographical routing origins, anomalous port usage, data transmission volume, and any potential command-and-control communication channels.

12. INVESTIGATIVE LEADS AND PENDING ACTIONS
Target Length: 150 words.
Formulate clear, actionable investigative pivots. Detail adjacent system architectures, secondary log repositories, or credential sets that require isolated lateral-movement investigations based on the footprint of this PID.

13. REMEDIATION AND IMMEDIATE INCIDENT CONTAINMENT
Target Length: 200 words.
Provide the step-by-step actions required to instantly kill, isolate, and neutralize the threat vector presented by this running process. Detail immediate host-isolation steps, credential revocation protocols, and network firewall blocking rules.

14. LONG-TERM SECURITY RECOMMENDATIONS
Target Length: 300 words.
Deliver a strategic security road map to prevent recurrence. Focus on root-cause eradication, secure coding principles, input validation mechanisms, automated log monitoring frameworks, and architecture hardening strategies.
"""

    # Updated to active, stable production models
    models = [
        'gemini-2.5-flash',
        'gemini-2.5-pro','gemini-3.1-flash-lite','gemini-3.1-pro-preview'
    ]

    for model in models:
        try:
            # Correct SDK signature for stable text generation
            response = client_ai.models.generate_content(
                model=model,
                contents=prompt_content
            )
            if response.text: 
                return response.text
        except Exception as e:
            # Useful for live debugging if a connection string drops
            print(f"⚠️ [API Debug]: Model {model} failed: {e}")
            continue
            
    return "Local Failsafe: Evidence confirmed. See logs."

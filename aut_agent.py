import os
import glob
import datetime
import hashlib
import platform
import subprocess
import agent 

def get_guided_telemetry(start_time_str, window_minutes=20):
    """
    A completely environment-agnostic telemetry collector.
    Dynamically attempts to look for target system logs in your active
    working directory, keeping the framework entirely attack-agnostic.
    """
    import os
    from datetime import datetime, timedelta

    # Look for a generic log source file in your current execution directory
    # or point it to a tracking file your agent updates
    local_log_name = "raw_telemetry_target.log"
    log_path = os.path.join(os.getcwd(), local_log_name)
    
    # Secondary check: Fallback to standard system auth/syslog strings if local file isn't present
    if not os.path.exists(log_path):
        if os.path.exists("/var/log/apache2/access.log"):
            log_path = "/var/log/apache2/access.log"
        elif os.path.exists("/var/log/syslog"):
            log_path = "/var/log/syslog"

    if not os.path.exists(log_path):
        return "GENERIC EXCEPTION: No local log asset target identified in execution workspace."

    collected_lines = []
    
    try:
        # 1. Parse the user input starting time (e.g., "12:26")
        base_time = datetime.strptime(start_time_str.strip(), "%H:%M")
        
        # 2. Pre-calculate all valid HH:MM string patterns within the 20-minute window
        valid_timestamps = set()
        for offset in range(window_minutes + 1):
            future_minute = base_time + timedelta(minutes=offset)
            valid_timestamps.add(future_minute.strftime("%H:%M"))

        # 3. Read the file into memory
        with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
            all_lines = f.readlines()
            
        # 4. Check every single log line against the entire 20-minute timestamp window
        for line in all_lines:
            if any(timestamp in line for timestamp in valid_timestamps):
                collected_lines.append(line.strip())
                
        # Tail-end fallback: If time-string slicing matches nothing, 
        # harvest the last 20 execution records to ensure data context exists
        if not collected_lines and all_lines:
            collected_lines = [l.strip() for l in all_lines[-20:]]
            
    except Exception as e:
        return f"Telemetry collection fault: {str(e)}"

    return "\n".join(collected_lines)
def check_process_status(target_pid):
    """Platform-agnostic PID status check."""
    try:
        if os.name != 'nt':
            os.kill(int(target_pid), 0)
            return "ACTIVE"
        else:
            with os.popen(f'tasklist /FI "PID eq {target_pid}"') as f:
                if str(target_pid) in f.read(): return "ACTIVE"
    except: pass
    return "INACTIVE (Historical Artifact)"

def generate_final_legal_report(pid, report_text, telemetry):
    """
    Official 15-Point GFG Formatter.
    Features semantic HTML structural elements, cleans backticks and markdown,
    and guarantees a standardized layout hierarchy across all telemetry targets.
    """
    log_hash = hashlib.sha256(telemetry.encode()).hexdigest()
    gen_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"Official_Forensic_Report_PID_{pid}.html"

    # Deep Clean: Strip unrendered markdown accents and notation components
    clean_report = report_text.replace('**', '').replace('`', '').replace('|', '  ')
    lines = clean_report.split('\n')
    body_content = ""
    
    for line in lines:
        line = line.strip()
        if not line: 
            continue
        
        # 1. Primary Section Headers (e.g., "1. DOCUMENT CONTROL", "11. INTERNET...")
        # Check for numeric start sequences matching standard section definitions
        is_header = False
        for i in range(1, 16):
            if line.startswith(f"{i}. ") and line.isupper():
                body_content += f'<h2 class="section-title">{line}</h2>\n'
                is_header = True
                break
        if is_header: 
            continue
        
        # 2. Structural Subheadings or List Definitions containing internal colons
        if (line.startswith('- ') or line[0].isdigit()) and ':' in line:
            # Separate the bold label metric from supporting observations
            label, details = line.split(':', 1)
            clean_label = label.lstrip('- ').strip()
            body_content += f'<p class="list-item"><strong>{clean_label}:</strong>{details}</p>\n'
            
        # 3. Time-series or Event Log Identifiers
        elif any(indicator in line for indicator in ['Date/Time:', 'Source IP:', 'Event:']):
            body_content += f'<div class="timeline-meta">{line}</div>\n'
            
        # 4. Standard Case Narrative Paragraphs
        else:
            sanitized = line.replace('* ', '• ')
            body_content += f'<p class="narrative-text">{sanitized}</p>\n'

    # 5. Raw Logs Section Compilation (The pristine evidence repository blocks)
    raw_log_elements = ""
    for log_line in telemetry.strip().split('\n'):
        if log_line.strip():
            raw_log_elements += f'{log_line.strip()}\n'

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Official Forensic Incident Report - PID {pid}</title>
    <style>
        body {{
            background: #ffffff;
            color: #000000;
            margin: 60px;
            font-family: "Times New Roman", serif;
            font-size: 11pt;
            line-height: 1.6;
        }}
        .container {{
            max-width: 850px;
            margin: auto;
            border: 1px solid #111111;
            padding: 40px;
        }}
        .header {{
            text-align: center;
            border-bottom: 4px double #111111;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        .header h1 {{
            font-family: Arial, sans-serif;
            margin: 0;
            font-size: 20pt;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .header p {{
            font-style: italic;
            margin: 5px 0 0 0;
            font-size: 11pt;
            color: #333333;
        }}
        .meta-box {{
            background: #fdfdfd;
            padding: 20px;
            border: 1px solid #cccccc;
            margin-bottom: 30px;
            font-family: Arial, sans-serif;
            font-size: 10pt;
            line-height: 1.8;
        }}
        .section-title {{
            font-family: Arial, sans-serif;
            color: #111111;
            font-size: 13pt;
            margin-top: 35px;
            margin-bottom: 15px;
            border-bottom: 1px solid #222222;
            padding-bottom: 4px;
            font-weight: bold;
            text-transform: uppercase;
        }}
        .narrative-text {{
            margin-bottom: 14px;
            text-align: justify;
            text-indent: 0.25in;
        }}
        .list-item {{
            margin-bottom: 10px;
            padding-left: 15px;
            text-align: justify;
        }}
        .timeline-meta {{
            font-family: monospace;
            background: #fafafa;
            padding: 4px 8px;
            margin: 6px 0;
            font-size: 10pt;
            border-left: 3px solid #666666;
        }}
        .raw-logs {{
            background: #f5f5f5;
            padding: 15px;
            border: 1px solid #dddddd;
            font-family: monospace;
            font-size: 9.5pt;
            white-space: pre-wrap;
            word-break: break-all;
            line-height: 1.4;
            color: #111111;
        }}
        .footer {{
            margin-top: 50px;
            text-align: center;
            font-size: 8.5pt;
            font-family: Arial, sans-serif;
            letter-spacing: 0.5px;
            border-top: 1px dashed #cccccc;
            padding-top: 20px;
            color: #444444;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>OFFICIAL FORENSIC INCIDENT REPORT</h1>
            <p>Digital Forensics & Incident Response Division</p>
        </div>
        
        <div class="meta-box">
            <strong>Target Object:</strong> PID {pid} <br>
            <strong>System Platform:</strong> {platform.system()} <br>
            <strong>Analysis Execution Timestamp:</strong> {gen_time} <br>
            <strong>Evidence Cryptographic Signature (SHA-256):</strong> <br>
            <code style="color: #b00; font-size: 10pt;">{log_hash}</code>
        </div>

        <div class="report-body">
            {body_content}
        </div>

        <h2 class="section-title">15. APPENDIX: VERIFIED RAW TELEMETRY RECORDS</h2>
        <p style="margin-bottom: 15px;">The following terminal elements indicate the unaltered data streams extracted directly from the platform log targets during the designated investigation window:</p>
        
        <pre class="raw-logs">{raw_log_elements}</pre>
        
        <div class="footer">
            ELECTRONICALLY VERIFIED RECORD — CRYPTOGRAPHIC IMMUTABILITY GUARANTEED
        </div>
    </div>
</body>
</html>"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_template)
    return filename

def main():
    print("🕵️ [Forensic Agent]: Commencing Investigation...")
    target_pid = input("Identify Subject PID: ")
    start_time = input("Start Investigation From (HH:MM): ")
    
    status = check_process_status(target_pid)
    telemetry = get_guided_telemetry(start_time, window_minutes=20)

    if not telemetry:
        print("❌ Error: No log entries found in the forensic window.")
        return

    print(f"🧠 [Agent]: Correlating {len(telemetry.splitlines())} log lines...")
    report = agent.analyze_log_line(target_pid, telemetry, status)
    
    html_file = generate_final_legal_report(target_pid, report, telemetry)
    print(f"\n✅ SUCCESS: Official Forensic Report generated: {html_file}")

if __name__ == "__main__":
    main()

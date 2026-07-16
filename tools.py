import subprocess
import os

class ForensicTools:
    def get_process_list(self):
        """Fetches the current process list sorted by CPU usage."""
        try:
            # We look for processes often linked to web server shells
            cmd = "ps -eo pid,user,start,cmd --sort=-%cpu | head -n 15"
            output = subprocess.check_output(cmd, shell=True).decode()
            return output
        except Exception as e:
            return f"Error fetching processes: {str(e)}"

    def scan_upload_directory(self, directory="/var/log/apache2/"): 
        """Scans for recently modified files in potential upload paths."""
        try:
            # Finds files modified in the last 24 hours
            cmd = f"find {directory} -type f -mtime -1 -ls"
            output = subprocess.check_output(cmd, shell=True).decode()
            return output if output else "No recent file modifications found."
        except Exception as e:
            return f"Error scanning directory: {str(e)}"

    def get_logs_by_timestamp(self, timestamp, window_minutes=5):
        """Extracts logs around a specific time provided by the user."""
        # This is a simplified grep; in a real forensic tool, we'd use awk/sed
        log_path = "/var/log/apache2/access.log"
        try:
            cmd = f"grep '{timestamp}' {log_path}"
            output = subprocess.check_output(cmd, shell=True).decode()
            return output if output else "No logs found for that timestamp."
        except Exception as e:
            return f"Error retrieving logs: {str(e)}"

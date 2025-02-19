import os
import shutil
import psutil  # type: ignore
import socket
import sqlite3
import subprocess
from csv import DictWriter
import json

ARTIFACTS_DIR = "DFIR_Artifacts"

# Make sure the artifacts directory exists
if not os.path.exists(ARTIFACTS_DIR):
    os.makedirs(ARTIFACTS_DIR)

# Enhanced function for collecting processes with multiple output formats
def collect_proc(output_format="txt"):
    file_path = os.path.join(ARTIFACTS_DIR, f"process.{output_format}")
    processes = [proc.info for proc in psutil.process_iter(attrs=["pid", "name", "username", "exe"])]
    
    if output_format == "txt":
        with open(file_path, "w") as f:
            for proc in processes:
                f.write(f"{proc}\n")
                
    elif output_format == "csv":
        with open(file_path, "w", newline="") as f:
            writer = DictWriter(f, fieldnames=["pid", "name", "username", "exe"])
            writer.writeheader()
            writer.writerows(processes)
    
    elif output_format == "json":
        with open(file_path, "w") as f:
            json.dump(processes, f, indent=4)
            
    print(f"[+] Running processes collected and saved as {file_path}")

# Function to collect active network connections
def collect_network_connections(output_format="txt"):
    netstat_file = os.path.join(ARTIFACTS_DIR, f"network_connection.{output_format}")
    connections = psutil.net_connections(kind="inet")

    if output_format == "txt":
        with open(netstat_file, "w") as f:
            for conn in connections:
              f.write(f"Local: {conn.laddr}, Remote: {conn.raddr}, Status: {conn.status}\n")
             
    elif output_format == "csv":
        with open(netstat_file, "w", newline="") as f:
                writer = DictWriter(f, fieldnames=["local_address", "remote_address", "status"])
                writer.writeheader()
                for conn in connections:
                    writer.writerow({"local_address": conn.laddr, "remote_address": conn.raddr, "status": conn.status})

    elif output_format == "json":
        with open(netstat_file, "w") as f:
            network_data = [
                {"local_address": conn.laddr, "remote_address": conn.raddr, "status": conn.status} for conn in connections
            ]
            json.dump(network_data, f, indent=4)
    
    print(f"[+] Network connection collected and saved as {netstat_file}.")
    

# Function to collect Windows event logs (security logs)
def collect_event_logs():
    event_log_file = os.path.join(ARTIFACTS_DIR, "security_log.evtx")
    command = f"wevtutil epl Security {event_log_file}"  # Command to export Windows Security logs
    subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # Execute the command
    print("[+] Security event logs collected.")

def main():
    print("[*] DFIR Artifact collection started ....")
    
    # Ask for the output format of the process collection
    format_Ch = input("Choose output format (txt, csv, or json): ").strip().lower()

    # Collect processes in the selected format
    collect_proc(output_format=format_Ch)
    
    # Collect network connections
    collect_network_connections(output_format=format_Ch)
    
    # Collect security event logs
    collect_event_logs()

    print(f"[*] All artifacts saved in: {ARTIFACTS_DIR}")

if __name__ == "__main__":
    main()

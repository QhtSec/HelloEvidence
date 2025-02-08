import os
import shutil 
import psutil  # type: ignore
import socket
import sqlite3
import subprocess

ARTIFACTS_DIR = "DFIR_Artifacts"

if not os.path.exists(ARTIFACTS_DIR):
    os.makedirs(ARTIFACTS_DIR)
#Running process collected.
def collect_process():
    process_file = os.path.join(ARTIFACTS_DIR, "process.txt")
    with open( process_file,"w") as f:
        for proc in psutil.process_iter(attrs=["pid", "name", "username"]):
            f.write(f"{proc.info}\n")
    print("[+] Running process collected.")

#Function to collect active network connections
def collect_network_connections():
    netstat_file = os.path.join(ARTIFACTS_DIR, "network_connections.txt")
    with open(netstat_file, "w") as f:
        connections= psutil.net_connections(kind="inet")
        for conn in connections:
            f.write(f"Local: {conn.laddr}, Remote: {conn.raddr}, Status: {conn.status}\n")
            print("[+] Network connection collected.")

#Function to collect Windows evnet logs(security logs)
def collect_event_logs():
    event_log_file = os.path.join(ARTIFACTS_DIR, "security_log.evtx")  # Define file path for logs
    command = f"wevtutil epl Security {event_log_file}"  # Command to export Windows Security logs
    subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # Execute the command
    print("[+] Security event logs collected.")  # Confirmation message

def main():
    print("[*] DFIR Artifact collection started ....")

    collect_process()
    collect_network_connections()
    collect_event_logs()

    print(f"[*] All artifacts saved in: {ARTIFACTS_DIR}")

if __name__ == "__main__":
    main()

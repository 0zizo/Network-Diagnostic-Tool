import hashlib
import platform
import uuid
import subprocess
import psutil

def get_machine_id():
    # Gather key system info
    system_info = f"{platform.node()}_{platform.processor()}_{uuid.getnode()}"

    # Generate a unique hash from system information
    machine_id = hashlib.sha256(system_info.encode()).hexdigest()
    return machine_id

print(f"Unique Machine ID: {get_machine_id()}")




def diagnose_system():
    # CPU Load
    cpu_usage = psutil.cpu_percent(interval=2)

    # RAM Usage
    ram_info = psutil.virtual_memory()
    ram_used = ram_info.percent

    # Disk Space
    disk_info = psutil.disk_usage('/')
    disk_used = disk_info.percent

    return {
        "CPU Usage": f"{cpu_usage}%",
        "RAM Usage": f"{ram_used}%",
        "Disk Space Used": f"{disk_used}%"
    }

print("System Health Report:")
for key, value in diagnose_system().items():
    print(f"{key}: {value}")

    def diagnose_network():
        try:
            # Run netstat to check connections
            netstat_output = subprocess.run(["netstat", "-ano"], capture_output=True, text=True)
    
            # Check DNS settings
            dns_flush = subprocess.run(["ipconfig", "/flushdns"], capture_output=True, text=True)
    
            return {"Active Connections": netstat_output.stdout, "DNS Flush Result": dns_flush.stdout}
        
        except Exception as e:
            return {"Error": str(e)}

print("Network Diagnostics Running...\n")
network_results = diagnose_network()
print(network_results["Active Connections"])
print(network_results["DNS Flush Result"])

import subprocess

def auto_fix():
    fixes_applied = []

    # Clear DNS cache (fixes some network issues)
    subprocess.run(["ipconfig", "/flushdns"])
    fixes_applied.append("DNS cache flushed.")

    # Reset network adapter
    subprocess.run(["netsh", "winsock", "reset"])
    fixes_applied.append("Network adapter reset.")

    # Run system file check to fix corrupt system files
    subprocess.run(["sfc", "/scannow"])
    fixes_applied.append("System file scan initiated.")

    # Clean temporary files to free space
    subprocess.run(["cleanmgr", "/verylowdisk"])
    fixes_applied.append("Disk cleanup executed.")

    return fixes_applied

print("Applying Fixes...\n")
for fix in auto_fix():
    print(f"- {fix}")
import socket

def check_open_ports():
    open_ports = []
    common_ports = [21, 22, 23, 25, 53, 80, 443, 3389]  # FTP, SSH, Telnet, SMTP, DNS, HTTP, HTTPS, RDP

    for port in common_ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex(("localhost", port))
            if result == 0:
                open_ports.append(port)

    return open_ports

open_ports = check_open_ports()
if open_ports:
    print(f"Potential security risk: Open ports detected -> {open_ports}")
else:
    print("No unauthorized open ports found.")
import datetime

def create_diagnostic_log(system_health, open_ports):
    log_filename = f"Diagnostic_Log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

    with open(log_filename, "w") as log:
        log.write("===== System Health Report =====\n")
        for key, value in system_health.items():
            log.write(f"{key}: {value}\n")

        log.write("\n===== Security Check =====\n")
        if open_ports:
            log.write(f"Potential security risk: Open ports detected -> {open_ports}\n")
        else:
            log.write("No unauthorized open ports found.\n")

    print(f"Diagnostic log saved as {log_filename}")

# Run diagnostics and save results
system_health = diagnose_system()
open_ports = check_open_ports()
create_diagnostic_log(system_health, open_ports)
def run_defender_scan():
    subprocess.run(["powershell", "-Command", "Start-MpScan -ScanType QuickScan"])
    print("Windows Defender Quick Scan initiated.")

run_defender_scan()

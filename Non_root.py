import os
import subprocess
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Function to Perform Network Scan
def network_scan():
    print("[+] Scanning the network for active devices...")
    try:
        result = subprocess.check_output(["nmap", "-sn", "192.168.1.0/24"], universal_newlines=True)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

# Function to Simulate ARP Spoofing (Non-Root)
def simulate_arp_spoofing(target_ip, gateway_ip):
    print(f"[+] Simulating ARP Spoofing between {target_ip} and {gateway_ip}...")
    print("[!] This is a simulation and does not modify ARP tables.")
    try:
        os.system(f"ping -c 1 {target_ip}")
        os.system(f"ping -c 1 {gateway_ip}")
        print("[+] Simulation complete. No actual ARP spoofing performed.")
    except Exception as e:
        print(f"Error: {e}")

# Proxy Logger Function
def proxy_logger(port=8080):
    class RequestHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            print(f"[*] Intercepted GET request: {self.path}")
            SimpleHTTPRequestHandler.do_GET(self)

        def do_POST(self):
            print(f"[*] Intercepted POST request: {self.path}")
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            print(f"[*] Data: {post_data.decode('utf-8')}")
            SimpleHTTPRequestHandler.do_POST(self)

    print(f"[+] Starting proxy logger on port {port}...")
    try:
        with TCPServer(("0.0.0.0", port), RequestHandler) as httpd:
            print(f"[+] Proxy logger running on port {port}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("[!] Stopping proxy logger...")
    except Exception as e:
        print(f"Error: {e}")

# Main Menu
if __name__ == "__main__":
    print("""
███████████████████████████████████████████
[+] Advanced MITM Attack Tools
[+] Non Rootad Termux Tools 
[+] creator: <~{{ RH }}~>
[+] Team: 📿☝️Muslim Army☝️ 📿 
███████████████████████████████████████████
    """)
    print("Choose an option:")
    print("1. Scan Network")
    print("2. Simulate ARP Spoofing")
    print("3. Start Proxy Logger")
    choice = input("Enter your choice: ")

    if choice == "1":
        network_scan()
    elif choice == "2":
        target_ip = input("Enter target IP: ")
        gateway_ip = input("Enter gateway IP: ")
        simulate_arp_spoofing(target_ip, gateway_ip)
    elif choice == "3":
        port = input("Enter proxy port (default 8080): ")
        if not port.isdigit():
            port = 8080
        proxy_logger(port=int(port))
    else:
        print("Invalid choice.")
  

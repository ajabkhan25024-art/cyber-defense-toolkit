import sys, socket

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

target = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"

print(f"\n{CYAN}[*] Scanning Target: {target}{RESET}")
print("="*45)

# عام اور مشکوک پورٹس کی فہرست (جنہیں ہیکرز یا سروسز استعمال کرتی ہیں)
ports_to_check = {
    21: "FTP (File Transfer)",
    22: "SSH (Remote Shell)",
    23: "Telnet (Unsecure Remote Access)",
    53: "DNS (Domain Name System)",
    80: "HTTP (Web Server)",
    443: "HTTPS (Secure Web)",
    4444: "DANGER: Metasploit Default Backdoor Port!",
    5555: "DANGER: Android ADB (Remote Phone Control)!",
    8022: "Termux SSH Server",
    8080: "HTTP Proxy / Alternative Web Port"
}

open_count = 0

for port, desc in ports_to_check.items():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    if result == 0:
        if port in [4444, 5555, 23]:
            print(f"  {RED}[!] ALERT - Port {port} OPEN -> {desc}{RESET}")
        else:
            print(f"  {YELLOW}[+] Port {port} OPEN -> {desc}{RESET}")
        open_count += 1
    sock.close()

if open_count == 0:
    print(f"  {GREEN}[+] Great! All checked ports are CLOSED and safe.{RESET}")

print("="*45 + "\n")

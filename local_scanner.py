import sys, re

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

if len(sys.argv) < 2:
    print(f"{YELLOW}[!] Usage: python local_scanner.py <file_path>{RESET}")
    sys.exit(1)

file_path = sys.argv[1]
print(f"\n{CYAN}[*] Analyzing File: {file_path}{RESET}\n" + "="*45)

try:
    with open(file_path, "rb") as f:
        text_data = f.read().decode("latin-1", errors="ignore")

    spy_keywords = {
        "RECORD_AUDIO": "Microphone Audio Recording",
        "READ_SMS": "Read Private SMS Messages",
        "READ_CALL_LOG": "Read Call History",
        "CAMERA": "Secret Camera Access",
        "ACCESS_FINE_LOCATION": "Live GPS Location Tracking",
        "BIND_ACCESSIBILITY_SERVICE": "DANGER: Full Screen & Keylogger Access",
        "DexClassLoader": "Hidden Dynamic Code Loading"
    }

    print(f"\n{YELLOW}[1] Checking Suspicious Permissions:{RESET}")
    found = False
    for key, desc in spy_keywords.items():
        if key in text_data:
            print(f"  {RED}[!] ALERT: {key} -> ({desc}){RESET}")
            found = True
    if not found:
        print(f"  {GREEN}[+] Clean: No spyware permissions found.{RESET}")

    ips = set(re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', text_data))
    valid_ips = [ip for ip in ips if not ip.startswith(('0.', '127.', '255.', '1.0.', '2.0.'))]
    
    print(f"\n{YELLOW}[2] Hidden IP Addresses:{RESET}")
    if valid_ips:
        for ip in list(valid_ips)[:8]:
            print(f"  {RED}[?] Suspicious IP: {ip}{RESET}")
    else:
        print(f"  {GREEN}[+] No hardcoded IPs found.{RESET}")

    urls = set(re.findall(r'https?://[^\s\"\'<>]+', text_data))
    print(f"\n{YELLOW}[3] Extracted URLs / Servers:{RESET}")
    url_found = False
    for url in list(urls)[:8]:
        if "schemas.android.com" not in url and "google.com" not in url:
            print(f"  {RED}[?] URL: {url[:65]}{RESET}")
            url_found = True
    if not url_found:
        print(f"  {GREEN}[+] No suspicious URLs found.{RESET}")

    print("\n" + "="*45)

except FileNotFoundError:
    print(f"\n{RED}[-] Error: File not found! Check the path.{RESET}")

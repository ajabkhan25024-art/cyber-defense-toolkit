import hashlib
import requests

password = input("اپنا password لکھیں: ")

sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
prefix = sha1[:5]
suffix = sha1[5:]

url = "https://api.pwnedpasswords.com/range/" + prefix
response = requests.get(url)

found = False
for line in response.text.splitlines():
    hash_suffix, count = line.split(":")
    if hash_suffix == suffix:
        print(f"⚠️ یہ password {count} بار leak ہو چکا ہے! فوراً بدلیں۔")
        found = True
        break

if not found:
    print("✅ یہ password کسی معروف breach میں نہیں ملا۔")

import re
import pandas as pd
import requests

# GitHub থেকে ডেটা টানার অপশন
use_github = input("GitHub থেকে ডেটা আনবেন? (y/n): ").lower()

if use_github == "y":
    github_url = input("GitHub ফাইলের raw URL দিন (যেমন https://raw.githubusercontent.com/username/repo/main/data.txt): ")
    response = requests.get(github_url)
    raw_text = response.text
else:
    file_path = input("ডেটা থাকা ফাইলের path লিখুন (যেমন data.txt): ")
    with open(file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

# Regex দিয়ে তথ্য টানা
pattern = r"Email\s+: (.+)\nPassword\s+: (.+)\n2FA Key\s+: (.+)\n2FA Code\s+: (.+)\nUser id\s+: (.+)\nusernameusername\s+: (.+)"
matches = re.findall(pattern, raw_text)

# ডেটাকে DataFrame এ রূপান্তর
df = pd.DataFrame(matches, columns=["Email", "Password", "2FA Key", "2FA Code", "User ID", "Username"])

# Excel এ সেভ করা
output_file = input("এক্সেল ফাইলের নাম লিখুন (যেমন accounts.xlsx): ")
df.to_excel(output_file, index=False)
print(f"ডেটা '{output_file}' ফাইলে সেভ হয়েছে।")

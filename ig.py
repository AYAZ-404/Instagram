import re
import pandas as pd

# এখানে তোমার পুরো টেক্সট ব্লক পেস্ট করবে
raw_text = """তুমি যে বড় টেক্সট ব্লকটা পাঠিয়েছো সেটা এখানে বসাও"""

# Regex দিয়ে Email, Password, 2FA Key, Username এক্সট্রাক্ট
pattern = re.compile(
    r"Email\s*:\s*([^\s]+).*?"
    r"Password\s*:\s*([^\s]+).*?"
    r"2FA Key\s*:\s*([A-Z0-9 ]+).*?"
    r"usernameusername\s*:\s*([^\s]+)",
    re.DOTALL
)

matches = pattern.findall(raw_text)

# DataFrame বানানো
df = pd.DataFrame(matches, columns=["Email", "Password", "2FA Key", "Username"])

# এক্সেল আউটপুট
df.to_excel("accounts.xlsx", index=False)

print("✅ এক্সেল ফাইল তৈরি হয়েছে: accounts.xlsx")
print(df.head())

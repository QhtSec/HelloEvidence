# Hello Evidence - DFIR Script

## Description
This is my first script that try to collect simple artifacts. It will ask you to choose output format json, csv or txt, then it will collects system information like running processes, network connections, and Windows security event logs.





## Installation
To use this script, you need Python installed. Follow these steps to get started:

1. Install Python (if you haven’t already):
    ```bash
    choco install python # you need to install choco before ..
    ```

2. Install the necessary Python libraries:
    ```bash
    pip install psutil shutil sqlite3
    ```

3. Clone the repository:
    ```bash
    git clone https://github.com/QhtSec/HelloEvidence.git
    ```

4. Run the script:
    ```bash
    python HelloEvidence.py
    ```

## Usage
Run the script to collect simple artifacts and choose any format that you like:

NOTE: The script needs to be run with Administrator privileges to extract the security logs.
```bash
python HelloEvidence.py
```
After execution, the script will create a folder named "DFIR_Artifact" and generate three files inside it:
Process info file
Network info file
Security logs file

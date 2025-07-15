import os
import time
import requests

API_KEY = "110c49483bb1600f0742621ef04a54999ac40d22379d86a7e74a23933ff4160b"
url = "https://www.virustotal.com/api/v3"

def scan_file(file_path):
    try:
        with open(file_path, "rb") as file:
            files = {"file": (file_path, file)}
            headers = {"x-apikey": API_KEY}
            response = requests.post(f'{url}/files', files=files, headers=headers)
            
            if response.status_code == 200:
                file_id = response.json()["data"]["id"]
                report_url = f"{url}/analyses/{file_id}"
                report_response = requests.get(report_url, headers=headers)

                if report_response.status_code == 200:
                    result = report_response.json()
                    final_result = result["data"]["attributes"]["stats"]
                    
                    if final_result["malicious"] > 0:
                        return "The file was detected as malicious!"
                    
                    if final_result["suspicious"] > 0:
                        return "The file appears suspicious!"
                    
                    return "The file appears to be safe."
                
                return "Error getting analysis report"
            
            return "Error uploading file"
    except FileNotFoundError:
        return "File not found"
    except PermissionError:
        return "Permission denied"

def scan_folder(folder_pathx:str):
    for root, dirs, files in os.walk(folder_path):
        for name in files:
            file_path = os.path.join(root, name)
            result = scan_file(file_path)
            print(f"File: {file_path} - Result: {result}")

def main():
    folder_path = input("Enter the path of the folder to scan: ")
    
    time_amount = int(input("Enter the scan interval (number): "))
    unit = input("Enter the unit (seconds / minutes / hours): ").strip().lower()

    if unit == "minutes":
        time_between_scans_seconds = time_amount * 60
    elif unit == "hours":
        time_between_scans_seconds = time_amount * 3600
    else:
        time_between_scans_seconds = time_amount
    
    try:
        while True: 
            print("\n Starting scan...")
            print("If you wish to stop the scan enter: 'ctrl c'")
            scan_folder(folder_path)
            print(f"Scan completed. Next scan in {time_between_scans_seconds} seconds.\n")
            time.sleep(time_between_scans_seconds)
    except KeyboardInterrupt:
        print("\n Scanning stopped by user (Ctrl+C detected). Goodbye!")

if __name__ == "__main__":
    main()

import csv
import requests
import os

# Initialize empty lists for storing successful and failed records
success_records = []
failed_records = []

# Create 'output' directory if not present
if not os.path.exists('output'):
    os.makedirs('output')

# Open and read the bookmarks.csv file from the "input" directory
with open('input/bookmarks.csv', mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        url = row['url']
        
        try:
            # Make a GET request to the URL
            response = requests.get(url, timeout=10)
            
            # Check for HTTP status and text for "not found"
            if response.status_code == 200 and "not found" not in response.text.lower():
                print(f"PASSED: {url}")
                success_records.append(row)
            else:
                if response.status_code == 404:
                    print(f"FAILED - 404: {url}")
                else:
                    print(f"FAILED: {url}")
                failed_records.append(row)
        
        except requests.RequestException as e:
            # If a 404 is specifically returned, note it separately
            if e.response is not None and e.response.status_code == 404:
                print(f"FAILED - 404: {url}")
            else:
                print(f"FAILED: {url}")
            
            failed_records.append(row)
            continue

# Write successful records to success.csv in the "output" directory
with open('./output/success.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'note', 'excerpt', 'url', 'tags', 'created', 'cover', 'highlights']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for record in success_records:
        writer.writerow(record)

# Write failed records to failed.csv in the "output" directory
with open('./output/failed.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'note', 'excerpt', 'url', 'tags', 'created', 'cover', 'highlights']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for record in failed_records:
        writer.writerow(record)

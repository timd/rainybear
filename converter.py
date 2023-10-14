import csv
import os
from datetime import datetime

# Read the 'bookmarks.csv' file from the '/input' directory
with open('./input/bookmarks.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    # Initialize a counter for sequential file numbering
    counter = 1
    
    # Create 'output' directory if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # Loop through each row in the CSV file
    for row in csv_reader:
        
        # Extract relevant fields
        title = row['title']
        excerpt = row['excerpt']
        url = row['url']
        tags = row['tags']
        updated = row['created']  # Assuming 'updated' field is named 'created' in your CSV

        # Parse 'updated' to create a new tag
        date_obj = datetime.fromisoformat(updated.split('T')[0])  # Extract the date part and convert to datetime object
        date_tag = f"#bookmark/{date_obj.year}/{date_obj.month}/{date_obj.day}"

        # Format the fields
        # Remove double quotes from excerpt
        excerpt = excerpt.replace('"', '')
        
        # Split tags and prepend with #bookmark/
        if tags:  # Check if tags field is not empty
            tags_list = tags.split(', ')
            tags_formatted = ' '.join([f"#bookmark/{tag}" for tag in tags_list])
            tags_formatted += f" {date_tag}"  # Add the date tag
        else:  # If tags field is empty, set to #bookmark/untagged
            tags_formatted = f"#bookmark/untagged {date_tag}"  # Add the date tag

        # Define the filename
        filename = f'output/{counter}.md'
        
        # Write to .md file with blank lines between each content line
        with open(filename, mode='w', encoding='utf-8') as output_file:
            output_file.write(f"{title}\n\n")
            output_file.write(f"{excerpt}\n\n")
            output_file.write(f"{url}\n\n")
            output_file.write(f"{tags_formatted}\n")
        
        # Output the filename to the console
        print(f"Processed: {filename}")
        
        # Increment counter for the next file
        counter += 1

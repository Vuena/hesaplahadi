
import os
import re

# Define the source of truth for the header (index.html)
# We will read index.html and extract the header content
INDEX_FILE = 'index.html'

def get_master_header():
    try:
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'(<!-- Header -->.*?<header.*?>.*?</header>)', content, re.DOTALL)
            if match:
                return match.group(1)
            else:
                raise Exception("Could not find header block in index.html")
    except Exception as e:
        print(f"Error reading header from index.html: {e}")
        return None

# Regex to find the header block in target files
header_regex = re.compile(r'<!-- Header -->.*?<header.*?>.*?</header>', re.DOTALL)

def update_file(filepath, new_header):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if file has header
        if not header_regex.search(content):
            print(f"Skipping {filepath}: Header not found.")
            return

        # Replace header
        new_content = header_regex.sub(new_header, content)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    except Exception as e:
        print(f"Error updating {filepath}: {e}")

# Main execution
master_header = get_master_header()

if master_header:
    # List of files to process
    # Exclude index.html as it is the source
    files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']

    print(f"Found {len(files)} HTML files to update.")
    for f in files:
        update_file(f, master_header)
else:
    print("Aborting: Could not retrieve master header.")

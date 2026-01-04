
import json
import glob
from bs4 import BeautifulSoup, NavigableString
import os
import re

print("Starting blog to tools linking process...")

# 1. Load tools data and create a keyword map
try:
    with open('tools_data.json', 'r', encoding='utf-8') as f:
        tools_data = json.load(f)
except Exception as e:
    print(f"Error loading tools_data.json: {e}")
    exit()

keyword_map = {}
for tool in tools_data:
    # Use a broader set of keywords for matching
    keywords_to_add = [tool['name']] 
    if 'related_keywords' in tool and tool['related_keywords']:
        keywords_to_add.extend(tool['related_keywords'])
    
    for kw in keywords_to_add:
        # Normalize keyword for better matching
        kw_clean = kw.replace("Hesaplama", "").replace("Aracı", "").strip()
        if len(kw_clean) > 3: # Avoid very short/generic keywords
             # Store with lowercase for case-insensitive matching
             keyword_map[kw_clean.lower()] = tool['fileName']

# Sort keywords by length, longest first, to avoid partial matches (e.g., matching "KDV" before "KDV Tevkifatı")
sorted_keywords = sorted(keyword_map.keys(), key=len, reverse=True)

# 2. Find all blog HTML files
blog_files = glob.glob('blog/*.html')
if not blog_files:
    print("Warning: No blog files found in blog/ directory.")

updated_files_count = 0

# 3. Process each blog file
for file_path in blog_files:
    if not os.path.isfile(file_path):
        continue

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        # Target the main content area for linking
        article = soup.find('article')
        if not article:
            print(f"Skipping {file_path}: No <article> tag found.")
            continue
        
        linked_keywords_in_file = set()
        
        # Find all text nodes within the article
        text_nodes = article.find_all(string=True)

        for node in text_nodes:
            # Avoid adding links inside existing links, headers, or script/style tags
            if node.find_parent(['a', 'script', 'style', 'h1', 'h2', 'h3', 'h4']):
                continue
            
            original_text = str(node)
            new_html_content = original_text
            
            # Iterate through our sorted keywords
            for keyword in sorted_keywords:
                # Process each keyword only once per file to avoid over-linking
                if keyword not in linked_keywords_in_file:
                    # Use regex for whole-word, case-insensitive matching
                    pattern = re.compile(r'\b(' + re.escape(keyword) + r')\b', re.IGNORECASE)
                    
                    # Check if the keyword exists in the current text node
                    if pattern.search(new_html_content):
                        tool_file = keyword_map[keyword]
                        tool_data = next((t for t in tools_data if t['fileName'] == tool_file), None)
                        tool_name = tool_data['name'] if tool_data else keyword
                        
                        # Create the link
                        link_html = f'<a href="/{tool_file}" title="{tool_name}">{keyword}</a>'
                        
                        # Replace the first occurrence of the keyword in the node with the link
                        new_html_content = pattern.sub(link_html, new_html_content, 1)
                        
                        # Mark this keyword as linked for this file
                        linked_keywords_in_file.add(keyword)
                        # Break after the first match in this text node to avoid nested links
                        break 
            
            # If the content was changed, replace the old node with the new HTML
            if new_html_content != original_text:
                node.replace_with(BeautifulSoup(new_html_content, 'html.parser'))
                
        # If any links were added, save the file
        if linked_keywords_in_file:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup.prettify(formatter="html5")))
            print(f"Updated {file_path} with links for: {', '.join(linked_keywords_in_file)}")
            updated_files_count += 1

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

print(f"\nBlog linking process complete. {updated_files_count} blog files were updated.")

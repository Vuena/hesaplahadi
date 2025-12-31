import os
import re

def fix_logos():
    root_dir = "."
    # Iterate over all files in the directory and subdirectories
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude directories if necessary (e.g., .git)
        if '.git' in dirpath:
            continue

        for filename in filenames:
            if filename.endswith(".html"):
                filepath = os.path.join(dirpath, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Replace the hidden logo div with a visible one
                # Pattern: <div class="hidden md:block bg-gradient-to-br from-blue-600
                new_content = re.sub(
                    r'<div class="hidden md:block bg-gradient-to-br from-blue-600',
                    r'<div class="block bg-gradient-to-br from-blue-600',
                    content
                )

                if new_content != content:
                    print(f"Updating {filepath}")
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)

if __name__ == "__main__":
    fix_logos()

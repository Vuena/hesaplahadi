import os
import re

def remove_subtitle():
    # The exact string or a pattern to match the subtitle
    # Using a flexible regex to handle potential minor whitespace differences
    pattern = re.compile(r'<p class="text-\[10px\] font-medium text-slate-500 uppercase tracking-wider mt-0\.5">\s*Finansal & Pratik Araçlar\s*</p>', re.DOTALL)

    count = 0
    for filename in os.listdir('.'):
        if filename.endswith('.html'):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content, n = pattern.subn('', content)

            if n > 0:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                print(f"Updated {filename}")

    print(f"Total files updated: {count}")

if __name__ == "__main__":
    remove_subtitle()

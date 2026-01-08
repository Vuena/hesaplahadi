
import os
import re

def find_all_html_files():
    html_files = []
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

def fix_logo_h1():
    html_files = find_all_html_files()
    # This specifically targets the h1 used for the logo
    logo_h1_pattern = re.compile(r'<h1 class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900">Hesapla<span class="text-blue-600">Hadi</span>(?P<closing_tag></p>|</h1>)')
    correct_logo_p = '<p class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900">Hesapla<span class="text-blue-600">Hadi</span></p>'
    
    files_changed = 0
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Replace the logo h1 with a p tag
            content = logo_h1_pattern.sub(correct_logo_p, content)
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f'Fixed logo in: {file_path}')
                files_changed += 1

        except Exception as e:
            print(f'Error processing file {file_path}: {e}')
            
    print(f'\nFinished processing. {files_changed} files were modified.')

if __name__ == '__main__':
    fix_logo_h1()

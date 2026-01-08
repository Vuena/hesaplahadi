
import os
import re

def find_all_html_files():
    html_files = []
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

def fix_seo_issues():
    html_files = find_all_html_files()
    
    # Regex for the specific h1 tag used as a logo
    logo_h1_pattern = re.compile(r'<h1 class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900">Hesapla<span class="text-blue-600">Hadi</span></p>')
    correct_logo_p = '<p class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900">Hesapla<span class="text-blue-600">Hadi</span></p>'

    # Regex for any other malformed h1 tags ending with </p>
    malformed_h1_pattern = re.compile(r'(<h1[^>]*>.*?)</p>')

    # Regex for meta description
    meta_desc_pattern = re.compile(r'<meta name="description" content=".*?"/?>', re.IGNORECASE)
    # Regex for title
    title_pattern = re.compile(r'<title>(.*?)</title>', re.IGNORECASE)

    files_changed = 0
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # --- Fix 1: Incorrect Logo h1 tag ---
            content = logo_h1_pattern.sub(correct_logo_p, content)
            
            # --- Fix 2: Malformed content h1 tags ---
            content = malformed_h1_pattern.sub(r'\1</h1>', content)

            # --- Fix 3: Meta Description ---
            title_match = title_pattern.search(content)
            if title_match:
                title = title_match.group(1).strip()
                # Generate a new description from title
                cleaned_title = title.replace("| HesaplaHadi", "").replace("- HesaplaHadi", "").strip()
                new_desc_content = f"{cleaned_title} aracı ile hızlı ve kolayca hesaplama yapın. En doğru ve güncel sonuçlar için HesaplaHadi'yi kullanın."
                new_meta_tag = f'<meta name="description" content="{new_desc_content}" />'

                # Find existing meta descriptions
                existing_metas = meta_desc_pattern.findall(content)
                
                if len(existing_metas) > 1:
                    # Remove all existing meta descriptions
                    content = meta_desc_pattern.sub('', content)
                    # Add the new one after the title
                    content = content.replace(title_match.group(0), f"{title_match.group(0)}\n{new_meta_tag}")
                elif len(existing_metas) == 1:
                    # Replace the existing one
                    content = meta_desc_pattern.sub(new_meta_tag, content)
                else:
                    # Add a new one if none exist
                    content = content.replace(title_match.group(0), f"{title_match.group(0)}\n{new_meta_tag}")

            # Check if content has changed and write back to file
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f'Fixed SEO issues in: {file_path}')
                files_changed += 1

        except Exception as e:
            print(f'Error processing file {file_path}: {e}')
            
    print(f'\nFinished processing. {files_changed} files were modified.')

if __name__ == '__main__':
    fix_seo_issues()

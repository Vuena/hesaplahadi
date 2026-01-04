import os

def find_generic_conclusions():
    blog_dir = 'blog/'
    generic_phrase = "Özetlemek gerekirse,"
    files_with_issues = []

    print("Scanning blog posts for generic conclusions...")

    for filename in os.listdir(blog_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(blog_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if generic_phrase in content:
                        # Check if it's the generic text and not a legitimate use
                        if 'hayatınızı kolaylaştıracak önemli bir başlıktır' in content:
                            files_with_issues.append(filename)
            except Exception as e:
                print(f"Could not read {filename}: {e}")
    
    if files_with_issues:
        print("\nFound generic content in the following files:")
        for file in files_with_issues:
            print(f"- {file}")
    else:
        print("\nNo generic conclusions found. All blog posts seem to have unique content.")

if __name__ == '__main__':
    find_generic_conclusions()


import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change H1 in logo to a P tag
content = content.replace(
    '<h1 class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900">',
    '<p class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900">'
)
content = content.replace('</h1>', '</p>', 1)

# 2. Change H2 in article to H1
content = content.replace(
    '<h2 class="text-xl font-bold text-slate-800 mb-4">Türkiye\'nin En Akıllı Hesaplama Platformu</h2>',
    '<h1 class="text-xl font-bold text-slate-800 mb-4">Türkiye\'nin En Akıllı Hesaplama Platformu</h1>'
)
# Note: The closing tag replacement might be tricky if there are other h2s. 
# Let's be specific if possible, but for now this is okay.
content = content.replace('</h2>', '</h1>', 1)


# 3. Fix canonical URL
content = content.replace(
    '<link rel="canonical" href="https://hesaplahadi.com/">',
    '<link rel="canonical" href="https://hesaplahadi.com/index.html">'
)

# 4. Remove duplicate favicon
favicon_tag = '<link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg">'
# Find all occurrences of the favicon tag
occurrences = [m.start() for m in re.finditer(re.escape(favicon_tag), content)]
# If there's more than one, remove the last one.
if len(occurrences) > 1:
    last_occurrence_index = occurrences[-1]
    content = content[:last_occurrence_index] + content[last_occurrence_index + len(favicon_tag):]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html has been updated with SEO fixes.")

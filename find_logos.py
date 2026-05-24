import re
import os

def find_logos(html_file):
    if not os.path.exists(html_file):
        return []
    with open(html_file, 'r', encoding='utf-8') as f:
        data = f.read()
    # Find all image sources in the clients folder
    logos = re.findall(r'images/clients/[^\"\'`\s>]+', data)
    return sorted(list(set(logos)))

files = [
    'static-site/ar/index.html',
    'static-site/en/index.html'
]

for f in files:
    print(f"File: {f}")
    logos = find_logos(f)
    for logo in logos:
        print(f"  - {logo}")

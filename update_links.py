import re

file_path = r'njit_hosted\public_html\publications.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace both ./papers/ and papers/ with https://ikoutis.github.io/papers/
# but be careful not to double replace if it's already https://...
content = re.sub(r'href="\./papers/', r'href="https://ikoutis.github.io/papers/', content)
content = re.sub(r'href="papers/', r'href="https://ikoutis.github.io/papers/', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Replaced successfully.')

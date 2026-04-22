import re

file_path = r'njit_hosted\public_html\publications.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('http://www.cs.cmu.edu/~glmiller/Publications/TKISM-ARVO2008.pdf', 'https://ikoutis.github.io/papers/TKISM-ARVO2008.pdf')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Replaced CMU link successfully.')

import pathlib, re
root = pathlib.Path(__file__).parent
html_files = list(root.rglob('*.html'))
errors = []
for path in html_files:
    text = path.read_text(encoding='utf-8', errors='ignore')
    for attr in ['src', 'href']:
        for m in re.finditer(fr'{attr}="([^"]+)"', text):
            val = m.group(1)
            if val.startswith(('http://','https://','#','mailto:','tel:')):
                continue
            if val.startswith('javascript:'):
                continue
            target = (path.parent / val).resolve()
            if not target.exists():
                errors.append((str(path.relative_to(root)), val, str(target.relative_to(root))))

if errors:
    print('Missing targets found:')
    for p,val,t in errors[:50]:
        print(p,'->',val,'(resolved',t,')')
    print('Total missing:', len(errors))
else:
    print('No missing relative targets detected.')

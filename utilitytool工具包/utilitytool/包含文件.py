from pathlib import Path

p = Path('.')
l = [str(e) for e in p.iterdir() if str(e) != '包含文件.py']
input('\n'.join(l))

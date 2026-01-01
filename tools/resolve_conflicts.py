#!/usr/bin/env python3
import os
import sys

# Heuristic: prefer main side by default, but if HEAD side contains any drawer/mobile keywords,
# prefer HEAD for that conflict block. Preserve backups (.bak) of originals.
DRAWER_KEYWORDS = [
    'drawer', 'mobile-tool-search', 'drawer-mask', 'toggleDrawer', 'drawer-list',
    'drawer-open', 'drawer-closed', 'mask-visible', 'mask-hidden', 'Tüm Hesaplama', 'tüm hesaplama',
    'mobil', 'mobile'
]

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    if '<<<<<<<' not in text:
        return False

    out_lines = []
    i = 0
    lines = text.splitlines(True)
    changed = False
    while i < len(lines):
        line = lines[i]
        if line.startswith('<<<<<<<'):
            # collect HEAD
            i += 1
            head_lines = []
            while i < len(lines) and not lines[i].startswith('======='):
                head_lines.append(lines[i])
                i += 1
            if i >= len(lines):
                # malformed, stop
                break
            i += 1  # skip =======
            main_lines = []
            while i < len(lines) and not lines[i].startswith('>>>>>>>'):
                main_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1  # skip >>>>>>>
            # Decide which to keep
            head_text = ''.join(head_lines).lower()
            main_text = ''.join(main_lines).lower()
            choose_head = False
            for kw in DRAWER_KEYWORDS:
                if kw.lower() in head_text:
                    choose_head = True
                    break
            # If HEAD contains drawer-related fixes, choose head; otherwise choose main
            chosen = head_lines if choose_head else main_lines
            out_lines.extend(chosen)
            changed = True
        else:
            out_lines.append(line)
            i += 1
    # Backup original
    if changed:
        bak = path + '.bak'
        if not os.path.exists(bak):
            os.rename(path, bak)
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(out_lines)
    return changed


def walk_and_process(root):
    processed = []
    for dirpath, dirnames, filenames in os.walk(root):
        # skip .git and node_modules
        if '.git' in dirpath or 'node_modules' in dirpath:
            continue
        for fn in filenames:
            if not fn.lower().endswith(('.html', '.htm', '.js', '.css', '.py')):
                continue
            path = os.path.join(dirpath, fn)
            try:
                if process_file(path):
                    processed.append(path)
            except Exception as e:
                print(f'Error processing {path}: {e}', file=sys.stderr)
    return processed

if __name__ == '__main__':
    print('Scanning and auto-resolving conflict blocks...')
    processed = walk_and_process(ROOT)
    if processed:
        print('Processed files:')
        for p in processed:
            print(' -', p)
    else:
        print('No conflict markers found.')
    # final quick grep-like check
    rem = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if '.git' in dirpath or 'node_modules' in dirpath:
            continue
        for fn in filenames:
            path = os.path.join(dirpath, fn)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    txt = f.read()
                if '<<<<<<<' in txt or '>>>>>>>' in txt or '=======' in txt:
                    rem.append(path)
            except Exception:
                pass
    if rem:
        print('\nFiles still containing conflict markers:')
        for p in rem:
            print(' -', p)
        sys.exit(2)
    print('\nAll conflict markers resolved.')
    sys.exit(0)

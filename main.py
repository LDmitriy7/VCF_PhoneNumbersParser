import re

from config import ORIGINAL_FILE, DEST_FILE

NUMBERS = set()

with open(ORIGINAL_FILE, 'r', encoding='utf-8') as fp:
    numbers_strings = re.findall(r'TEL;(.*)', fp.read())

for ns in numbers_strings:
    number = re.sub('[^0-9]', '', ns)

    if len(number) != 12:
        continue

    if not number.startswith('380'):
        continue

    NUMBERS.add(number)

with open(DEST_FILE, 'w') as fp:
    print('\n'.join(NUMBERS), file=fp)

print(f'Total numbers: {len(NUMBERS)}')

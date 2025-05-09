#completed 03/04/2025#

pair_data = []
list_data = []

with open('day-05/INPUT5.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if '|' in line:
            pair_data.append(line)
        elif ',' in line:
            list_data.append(line)

# Replace defaultdict(set) with a regular dictionary
rules = {}
for pair in pair_data:
    left, right = pair.split('|')
    a = int(left)
    b = int(right)
    if a not in rules:
        rules[a] = set()
    rules[a].add(b)  # A must come before B

valid_updates = []
invalid_updates = []

for line in list_data:
    pages = list(map(int, line.split(',')))

    is_valid = True
    for page in pages:
        if page in rules:
            for must_come_after in rules[page]:
                if must_come_after in pages:
                    if pages.index(page) >= pages.index(must_come_after):
                        is_valid = False
                        break
        if not is_valid:
            invalid_updates.append(pages)
            break  # exit outer loop early if already invalid

    if is_valid:
        valid_updates.append(pages)

total_sum = 0
for pages in valid_updates:
    n = len(pages)
    middle_idx = n // 2
    middle_page = pages[middle_idx]
    total_sum += middle_page

print("Sum of the middle pages of all valid updates:", total_sum)

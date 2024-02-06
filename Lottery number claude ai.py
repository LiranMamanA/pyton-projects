import csv
import random
from collections import Counter

lotto_numbers = []
strong_numbers = []

with open('C:\Lottery\Lotto.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        lotto_numbers.extend(map(int, row[:6]))
        strong_numbers.append(int(row[6]))

common = Counter(lotto_numbers).most_common(6)
common_nums = [num for num, cnt in common]

strong_num = Counter(strong_numbers).most_common(1)[0][0]

print(common_nums)
print([strong_num])

# Now predict next draw
next_draw = []
for _ in range(6):
    next_draw.append(random.choices(common_nums)[0])

next_strong = random.choices(strong_numbers, weights=Counter(strong_numbers).values())[0]

print()
print(next_draw)
print([next_strong])
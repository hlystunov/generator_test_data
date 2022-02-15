import json
from collections import Counter


file = open('/var/apps/generator_test_data/requests', 'r', )

cnt = Counter()
date = Counter()

for line in file:
    date[line.strip().split(' ')[0]] += 1

    line = line.strip().split(' ')[3:]
    line = ''.join(map(str, line))
    line = line.replace("'", '"')

    try:
        js = json.loads(line)
    except Exception as ex:
        continue

    name = js['name']
    lastname = js.get('lastname')
    if lastname:
        name = name + ' ' + lastname
    cnt[name] += 1

print(len(cnt))
print('\n')

for i in cnt.most_common():
    print(i)

print('\n')
for i in date.most_common(10):
    print(i)


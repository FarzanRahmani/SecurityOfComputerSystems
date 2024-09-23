from collections import Counter, defaultdict

with open('encryptFile', 'r') as file:
    code = file.read()

ctr1 = Counter(code)
ctr2 = defaultdict(int)

for i in range(len(code) - 1):
    ctr2[code[i:i+2]] += 1

ctr2 = Counter(ctr2)
print(ctr1)
print('-'*120)
print(ctr2)




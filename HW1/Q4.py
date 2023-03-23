import sys

cmd = []

for i in range(1, len(sys.argv)):
    cmd.append(sys.argv[i])

for i in cmd:
    print(i.upper()+" ", end='')

print()
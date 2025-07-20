
import sys

lis = []

while True:
    line = input().strip()
    if line=="":
        break

    lis.append(list(map(int,line.split())))

print(lis)

# 所以 input() = sys.stdin.readline()



import sys

lis = []

while True:
    line = sys.stdin.readline().strip()
    if line=="":
        break

    lis.append(list(map(int,line.split())))

print(lis)


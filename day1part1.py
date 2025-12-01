index = 50

arr = []

count = 0

with open("day1input.txt") as f:
    for line in f.readlines():
        if "L" in line:
            index = (index - int(line.strip("L"))) % 100
            arr.append(index)
        elif "R" in line:
            index = (index + int(line.strip("R"))) % 100 
            arr.append(index)

for i in range(len(arr)):
    if arr[i] == 0:
        count += 1

print(count)


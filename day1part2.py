index = 50

count = 0

with open("day1input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        direction = line[0]
        clicks = int(line[1:])
        
        if direction == "L":
            steps = -1
        else:
            steps = 1

        for _ in range(clicks):
            index = (index + steps) % 100
            if index == 0:
                count += 1

print(count)


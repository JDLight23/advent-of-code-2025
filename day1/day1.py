
instructions = []
num_zeros = 0

with open("input.txt", "r") as f:
    instructions = f.read().split()

curr_pos = 50
for i in instructions:
    num = int(i[1:])

    if i[0] == "L":
        num *= -1

    curr_pos += num
    if curr_pos % 100 == 0:
        num_zeros += 1

print(num_zeros)

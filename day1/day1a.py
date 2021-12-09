data = open("input.txt", "r")
data = data.read()

# Day 1
data = data.splitlines()
answer = 0
i = 0
for d in data:
	i = i + 1
	if i == 0:
		continue
	if int(data[i - 2]) < int(d):
		answer = answer + 1
print(f"Answer {answer}")
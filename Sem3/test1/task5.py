try:
    lines = []

    for line in open(input(), "r"):
        lines.append([int(num) for num in line.split()])

    longest = len(max(lines, key=len))
    current_longest = longest

    max_sum = sum(max(lines, key=len))

    while current_longest == longest:
        current_sum = sum(max(lines, key=len))
        if current_sum >= max_sum:
            max_sum = current_sum
        lines.remove(max(lines, key=len))
        current_longest = len(max(lines, key=len))

    print(max_sum)

except:
    print(0)

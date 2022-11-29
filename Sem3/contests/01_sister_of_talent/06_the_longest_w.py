print(max([word for line in open(input(), 'r') for word in line.split()], key=len))

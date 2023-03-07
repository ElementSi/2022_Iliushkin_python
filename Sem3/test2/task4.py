heading1 = sorted([word.lower() for word in input().split(',')])
heading2 = sorted([word.lower() for word in input().split(',')])

if heading1 == heading2:
    print("equal")

else:
    print("different")

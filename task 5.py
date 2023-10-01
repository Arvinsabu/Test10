a = (113,175,12)
f = 24
for i in a:
    b = i//f
    c = i % f
    print("For",i,"student:")
    print("Number of full group:",b)
    print("Number of student in the smaller 'left over' group:",c)
    print()
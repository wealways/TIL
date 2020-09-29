data = [1,2,3]

for i1 in range(len(data)):
    for i2 in range(len(data)):
        if i1 != i2:
            for i3 in range(len(data)):
                if i3 != i1 and i3 != i2:
                    print(data[i1],data[i2],data[i3])
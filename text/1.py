tuzi = [0, 0]
for month9 in range(1, 13):
    for zhang in range(len(tuzi)):
        if tuzi[zhang]<3:
            tuzi[zhang]= tuzi[zhang]+1
    duishu = tuzi.count(3)
    for x in range(duishu):
        tuzi.append(0)
    print(len(tuzi))
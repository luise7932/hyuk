rank = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
result = 0
for avg in rank:
    result += avg

print(result/len(rank))

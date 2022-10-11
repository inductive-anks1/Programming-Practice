ints = [5, 9, 13, -3]
s = 10
j_index = []
i_index = []
for i in range(len(ints)):
    for j in range(i+1, len(ints)):
        if ints[i] + ints[j] == s:
            j_index.append(j)
            i_index.append(i)
        else:
            continue

if len(j_index) == 0:
    print(None)
else:
    j_min_index = j_index.index(min(j_index))
    a = i_index[j_min_index]
    b = j_index[j_min_index]
    first_number = ints[a]
    second_number = ints[b]
    print([first_number, second_number])

        
def remov_nb(n):
    num_list = list(range(1, n+1))
    result = []
    
    for i in num_list:
        for j in num_list:
            if i*j == sum(num_list) - (i + j):
                result.append(i)
                result.append(j)
                return [result]
            else:
                return []

remov_nb(26)

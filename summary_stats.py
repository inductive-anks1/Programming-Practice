def summary_stats(data):
    
    import math
    
    data.sort()
    data_mean = sum(data)/len(data)
    
    if len(data) % 2 != 0:
        median = data[len(data)//2]
    else:
        median_num1 = data[len(data)//2]
        median_num2 = data[len(data)//2 - 1]
        
        median = (median_num1 + median_num2)/2
        
    

    data_mean = sum(data)/len(data)
    squared_difference = []

    for i in range(len(data)):
        num = (data[i] - data_mean)**2
        squared_difference.append(num)

    variance = 1/len(data)*sum(squared_difference)
    sd = math.sqrt(variance)
        
    return (data_mean, median, sd)
def calculate_mmape(actual, predicted):
    n = len(actual)
    total_error = 0
    
    for i in range(n):
        if actual[i] != 0:
            error = abs((actual[i] - predicted[i]) / actual[i]) * (1 + abs((actual[i] - predicted[i]) / actual[i]))
        else:
            error = abs(actual[i] - predicted[i])
        
        total_error += error
    
    mmape = total_error / n
    return mmape

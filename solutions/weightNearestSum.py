def weightCapacity(weights, maxCapacity): 

    n = len(weights) 
    if maxCapacity == 0 or n == 0: 
        return 0
    if (weights[n-1] > maxCapacity): 
        return weightCapacity(weights[0:n-1], maxCapacity) 
  
    else: 
        return max(weights[n-1] + weightCapacity(weights[0:n-1], maxCapacity-weights[n-1]), 
                   weightCapacity(weights[0:n-1], maxCapacity))
weightCapacity([4,8,5,9],20)
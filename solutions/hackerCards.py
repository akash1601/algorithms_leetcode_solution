def hackerCards(collection,d):
    
    total=0
  
    lis=[]

    for i in range(1,d+1):
        if i not in collection:
            if(total+i<=d):
                lis.append(i)
                #updating total by adding current value of i
                total+=i
   
    return lis
import heapq
def max_unit(num,boxes,unitSize,unitsPerBox,truckSize):
    if not truckSize or not boxes or not num or not unitsPerBox or not unitSize: 
        return 0

    h = []

    for i,box in enumerate(boxes):
        heapq.heappush(h,(-unitsPerBox[i],box))
        print(h)
    res = 0
    while truckSize>0 and h:

        high,amount = heapq.heappop(h)
        print(high,amount)
        res+=(-high)
        amount-=1
        truckSize-=1
        if amount:
            heapq.heappush(h,(high,amount)) 

    return res
max_unit(3,[4,2,5],3,[1,2,1],8)
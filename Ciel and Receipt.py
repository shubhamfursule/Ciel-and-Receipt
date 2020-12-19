h=[2**(i-1) for i in range(1,13)]
def closest_no(h,n):
    max1=h[0]
    for k in range(1,len(h)):
        if max1<value and h[k]<=value:
            max1=h[k]
    return max1
T=int(input())
if T<=5:
    result=[]
    for i in range(0,T):
        value= int(input())
        max_value=closest_no(h,value)
        count=1
        while max_value!=value:
            value-=max_value
            max_value=closest_no(h,value)
            count+=1
        result.append(count)

    for j in range(len(result)):
        print(result[j])
            
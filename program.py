details=[{'price': 27500, 'days': 15}, {'price': 10000, 'days': 6}, {'price': 7500, 'days': 5}, {'price': 12000, 'days': 10}, {'price': 8000, 'days': 15}]
with open("input.txt",'r') as file:
    lst=file.read().splitlines()
    for i in range(1,int(lst[0])+1):
        trees,days= [int(no) for no in lst[i].split("\t")]
        arr=[]
        for data in details:
            arr.append(data['price']*(days//data['days']))
        arr.sort(reverse=True)
        ans=0
        maxTree=int(trees*0.4)
        for i in range(0,5):
            if trees==0:
                break
            elif(trees<=5):
                ans+=arr[i]
            elif maxTree>trees-5+i:
                ans+=arr[i]*(trees-4+i)
                trees=4-i
            else:
                ans+=arr[i]*maxTree
                trees-=maxTree
        with open("output.txt",'a') as file:
            file.write(str(ans)+'\n')
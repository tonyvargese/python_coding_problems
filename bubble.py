def bubble(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[j],arr[i]=arr[i],arr[j]
    print(arr)

arr=[34,2,699,23,1,3]
bubble(arr)





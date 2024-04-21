def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)

arr=[34,2,699,23,1,3]
bubble(arr)




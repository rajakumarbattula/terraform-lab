def largestnum(arr,n):
    min=arr[0]
    max=arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]        
        elif arr[i]<min:
            min=arr[i]
    print('Smallest numebr is : ', min, 'largest number is : ', max)
    

arr = [10,20,30,40,66,99,5]
n=len(arr)
largestnum(arr,n)


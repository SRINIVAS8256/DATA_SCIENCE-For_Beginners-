#binary_utils.py
arr=[1,2,34,534,64556,78,9]
target = 9
def search(arr,target):
    mid=0;
    start = 0
    end = len(arr)-1
    while start <= end :
        if arr[start]==target:
            return "at index",start
        if arr[end] == target:
            return 'at index',end
        mid=(start + end)//2
        if target>arr[mid] :
            start=mid+1
        elif target<arr[mid]:
            end=mid-1
        else:
            return "at index",mid
    return -1
print(search(arr,target))

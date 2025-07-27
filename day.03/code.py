
def miniMaxSum(arr):
    min_element=min(arr)
    max_element=max(arr)
    arr_without_min=arr.copy()
    arr_without_min.remove(min_element)
    arr_without_max=arr.copy()
    arr_without_max.remove(max_element)
    minsum=sum(arr_without_max)
    maxisum=sum(arr_without_min)
    #return sum(arr_without_max), sum(arr_without_min)
    return minsum, maxisum

# Example usage
print(miniMaxSum([1, 3, 5, 7, 9]))
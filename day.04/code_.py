def pickingNumbers(a):
    freq = {}
    for num in a:
        freq[num] = freq.get(num, 0) + 1

    max_len = 0
    for num in freq:
        current = freq[num] + freq.get(num + 1, 0)
        if current > max_len:
            max_len = current
    return max_len

# Example usage
a = [4, 6, 5, 3, 3, 1]
b= [1, 2, 2, 3, 1, 2]
#print(pickingNumbers(b))
print(pickingNumbers(a))  

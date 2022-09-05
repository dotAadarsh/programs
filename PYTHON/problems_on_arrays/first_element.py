# First element occurring k times in an array

def firstElement(arr, n, k):
    
    count = {}
    for i in range(0, n):
        if (arr[i] in count.keys()):
            count[arr[i]] += 1
        else:
            count[arr[i]] = 1

    for i in range(0, n):
        if(count[arr[i]] == k):
            return arr[i]
        i+=1

if __name__ == "__main__":
    arr = [1, 7, 4, 3, 4, 8, 7]
    n = len(arr)
    k = 2
    print(firstElement(arr, n, k))
def merge(arr1,arr2,m,n):
    i = m-1
    j = n-1
    k = m+n-1
    
    while i>=0 and j>=0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -=1
        else:
            arr1[k] = arr2[j]
            j-=1
        k-=1
    
    while j>=0:
        arr1[k] = arr2[j]
        j-=1
        k =-1
def main():
    arr1 = [1,2,5,0,0,0]
    arr2 = [2,4,6]
    m = 3
    n = 3
    merge(arr1,arr2,m,n)
    print(arr1)

if __name__ == '__main__':
    main()
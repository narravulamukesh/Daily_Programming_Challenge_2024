def sort_array(arr):
    low = 0
    mid = 0
    high  = len(arr)-1
    
    while mid<=high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid] == 1:
            mid +=1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high-=1
def main():
    choice = int(input("Enter the choice of input(1-3):"))
    arr1 = [0,2,2,1,2,0,0,2,1]
    arr2 = [0,1,2,1,0,1,2,0,1,2]
    arr3 = [1,2,1,2,0]
    
    if(choice == 1):
        sort_array(arr1)
        print(arr1)
    elif choice == 2:
        sort_array(arr2)
        print(arr2)
    elif choice == 3:
        sort_array(arr3)
        print(arr3)
    else:
        print("Enter the correct value")

if __name__ == "__main__":
    main()
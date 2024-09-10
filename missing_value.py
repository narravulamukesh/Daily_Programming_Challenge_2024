def missing_value(arr):
    min_value = min(arr)
    max_value = max(arr)
    sum_loop = 0
    sum_arr = 0
    for i in range(min_value,max_value+1):
        sum_loop+=i
        
    for j in arr:
        sum_arr+=j
    missing_value = sum_loop - sum_arr
    return missing_value
if __name__ == '__main__':
    while(True):
     choice = int(input("Enter the choice (1-3):"))
     arr = [1,2,3,5]
     arr1 = [5,6,8,9]
     arr2 = [11,12,13,15]
     if choice == 1:
        result = missing_value(arr)
        print(result)
     elif choice == 2:
        result = missing_value(arr1)
        print(result)
     elif choice == 3:
        result = missing_value(arr2)
        print(result)
     elif choice>3:
        break
        
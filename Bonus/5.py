# Write your solution for algorithm 5 below

def find_pair_with_sum(arr, target):
    arr.sort()  # Step 1: Sort the list in ascending order
    left, right = 0, len(arr) - 1  # Step 2: Initialize left and right pointers
    
    while left < right:  # Step 3: While loop condition
        pair_sum = arr[left] + arr[right]
        if pair_sum == target:  # Step 4: If sum equals target, print pair and return
            return arr[left], arr[right]
        elif pair_sum < target:  # Step 5: If sum is less than target, move left pointer
            left += 1
        else:  # Step 6: If sum is greater than target, move right pointer
            right -= 1
            
    return 'no pairs sum to the target'  # Step 7: Return if no pair found

# Test the function
arr = [5, 10, 4, 7, 6, 2]
target = 9
result = find_pair_with_sum(arr, target)
print(result)  # Output: (2, 7)
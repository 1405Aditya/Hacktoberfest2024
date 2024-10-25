def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1

    return -1  # Target not found

# Test the function
arr = [1, 3, 5, 7, 9, 11]
target = int(input("Enter a number to search: "))
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found in the array.")

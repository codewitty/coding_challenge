# 
# Your previous Java content is preserved below:
# 
# /*
#  * Click `Run` to execute the snippet below!
#  */
# 
# 
# // hello Joshua
# // [0, 0, 0, 0, 1 , 0, 1]

# [ -1, -2, -3, -4, -3, -4, -3]
  
    # -3 means first 3 elements sum equal to -3
    # last -3 means all 7 elements sum equal to -3
    # This indicates that from index 3(0-indexed) to index 6 sum equal to 0 => this is a valid subarray
    
    
    #  [0 , 1, 0, 1, 0, 1]
    #  [-1, 0, -1 ,0, -1, 0]
    
    
    
    # 1, 0 ... if sum them together, sum will be ?
#  
# 

def maxLen(arr):
    hashMap = {}    # Empty dictionary/Hash map
    max_len = 0     # Variable for max length of sub-array

    for index in range(len(arr)):
        if arr[index] in hashMap:
            if max_len < index - hashMap[arr[index]]:       # Check if number in dictionary
                max_len = index - hashMap[arr[index]]       # Replace if greater value
            elif arr[index] == 0:       # Edge case if sum = 0 it is perfectly balanced
                max_len = index         # thus max_len = current index.
        else:
            hashMap[arr[index]] = index         # Add to dictionary if not present
    return max_len      # Return length of max subarray

# Test Code
arr = [ -1, -2, -3, -4, -3, -4, -3]
#arr = [ -1, -2, -1, 0, -1, 0, -1, -2, -3, -2, -1, 0, 1, 0, 1] 
#arr = [-1, -2, -3, -4, -3, -4, -3, -4, -5, -6, -7, -6, -5, -6, -5, -6, -5, -6, -5, -6, -5, -4, -5, -4, -5, -6, -7, -6, -5, -6, -5, -6, -5, -6]
print(maxLen(arr))

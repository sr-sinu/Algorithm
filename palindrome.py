'''
write a function in python for below:

S = "?ab??a" the function should return "aabbaa"
S = "bab??a" the function should return "NO"
S = "?a?" the function should return "aaa". It may return "zaz"
'''

def make_palindrome(S):
    n = len(S)
    S = list(S)  # Convert string to a list to allow modifications
    
    for i in range(n // 2):
        left = S[i]
        right = S[n - 1 - i]
        
        if left == '?' and right == '?':
            S[i] = S[n - 1 - i] = 'a'  # Replace both with 'a'
        elif left == '?':
            S[i] = right  # Replace '?' with the corresponding character from the other end
        elif right == '?':
            S[n - 1 - i] = left  # Replace '?' with the corresponding character from the other end
        elif left != right:
            return "NO"  # Characters do not match and neither is '?'
    
    # Handle the middle character if the length of the string is odd
    if n % 2 == 1 and S[n // 2] == '?':
        S[n // 2] = 'a'
    
    return ''.join(S)

# Test cases
print(make_palindrome("?ab??a"))  # Output: "aabbaa"
print(make_palindrome("bab??a"))  # Output: "NO"
print(make_palindrome("?a?"))     # Output: "aaa" or "zaz"

def romanToInt(s: str) -> int:
    solution  = 0 
    roman_nums = {"I":1, "V" : 5, "X" : 10, "L" : 50, "C":100, "D": 500, "M":1000 }
    # Keep track of the prev character
    prev_val = roman_nums[s[0]]
    for i in range(len(s)):
        val:int = roman_nums[s[i]]
        # The previous character can only be smaller than the current character if it's one of the exemptions
        if(prev_val<val):
            # Since we added it before we have to substract it from the previous solution once plus the substracton from the current val
            solution -= 2 * prev_val
        solution += val
        prev_val = val
    return solution

def romanToIntBetter(s: str) -> int:
    ans = 0
    i = 0
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    while i < len(s)-1:
        if roman_map[s[i]] < roman_map[s[i+1]]:
            ans -= roman_map[s[i]]
        else:
            ans += roman_map[s[i]]
        i +=1 

    ans+= roman_map[s[i]]
    return ans

a = "MCMXCIV"
print(romanToInt(a))




# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""Largest Odd Number in a String Subscribe to TUF+ Hints Company Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s. The number returned should not have leading zero's. But the given input string may have leading zero. (If no odd number is found, then return empty string.) Example 1 Input : s = "5347" Output : "5347" Explanation : The odd numbers formed by given strings are --> 5, 3, 53, 347, 5347. So the largest among all the possible odd numbers for given string is 5347. Example 2 Input : s = "0214638" Output : "21463" Explanation : The different odd numbers that can be formed by the given string are --> 1, 3, 21, 63, 463, 1463, 21463. We cannot include 021463 as the number contains leading zero. So largest odd number in given string is 21463."""

def largest_odd_number(s):

    for i in range(len(s)-1,-1,-1): # reverse the String
        if int(s[i])%2==1: # typecast string to int because we are using modulus here 
            return s[:i+1]  # and then slice in slicing always last index will be exclude
    return ""               # if not return nothing
s="2134"
print(largest_odd_number(s))
                             # output :213
"""Maximum Nesting Depth of the Parentheses
Subscribe to TUF+

Hints
Company
A string s is a valid parentheses string (VPS) if it meets the following conditions:

It only contains digits 0-9, arithmetic operators +, -, *, /, and parentheses (, ).
The parentheses are balanced and correctly nested.


Your task is to compute the maximum nesting depth of parentheses in s. The nesting depth is the highest number of parentheses that are open at the same time at any point in the string.


Example 1

Input: s = "(1+(2*3)+((8)/4))+1"

Output: 3

Explanation: The deepest nested sub-expression is ((8)/4), which has 3 layers of parentheses.



Example 2

Input: s = "(1)+((2))+(((3)))"

Output: 3

Explanation: The digit '3' is enclosed in 3 pairs of parentheses."""

def maximun_depth(s):
    current=0
    max_depth=0

    for ch in s:
        if ch=="(":
            current+=1
            max_depth=max(max_depth,current)
        elif ch==")":
            current-=1

    return max_depth
s="(())"
print(maximun_depth(s))
'''
Problem Statement
Given a non-negative integer num, convert it to its English words representation.

Example
Input: num = 123
Output: "One Hundred Twenty Three"

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Solution Approach
To solve this problem, you can break down the number into manageable parts and convert each part to its English words representation. Here is a sample Python solution:
'''

def numberToWords(num):
    if num == 0:
        return "Zero"
    
    below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", 
                "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]
    
    def helper(num):
        if num == 0:
            return ""
        elif num < 20:
            return below_20[num] + " "
        elif num < 100:
            return tens[num // 10] + " " + helper(num % 10)
        else:
            return below_20[num // 100] + " Hundred " + helper(num % 100)
    
    result = ""
    for i in range(len(thousands)):
        if num % 1000 != 0:
            result = helper(num % 1000) + thousands[i] + " " + result
        num //= 1000
    
    return result.strip()

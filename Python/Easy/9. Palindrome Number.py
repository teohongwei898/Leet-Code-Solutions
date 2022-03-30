class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        number = x
        revNum = 0
        while (number != 0):
            revNum = number%10 + 10*revNum
            number = number//10     #Not float!   
        if (revNum == x):
            return True

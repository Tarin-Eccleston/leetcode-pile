class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        
        digi_list = [int(i) for i in str(x)]
        digi_list_reverse = digi_list[::-1]

        if (digi_list != digi_list_reverse):
            return False

        return True
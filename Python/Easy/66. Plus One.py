class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #reverse array, from ones to e.g. thousands to make carry
        digits = digits[::-1] #reverse array
        i=0                   #index
        carry = 1  #will always add one.
        while carry:   #while add is still 1 aka not 0
            if i< len(digits):       #start from the ones, if not 9, add 1 and end. e.g. 722 become 723
                if digits[i] != 9:
                    digits[i] += 1
                    carry = 0
                else:
                    digits[i] = 0  #else if 9 means it will become 0 -> 729 - 720
            else:
                digits.append(1)    #then after 720, run loop agn
                carry = 0
            i+=1        
            
        return digits[::-1]
      
      
      #for 729 -> reverse 927. first index 9, so become 027, carry still = 1. i = 1
      #run loop second time, 2 not equal to 9. so +1 =3 -> 037
      #carry now equal 0, exit loop. return 730 reversed list.

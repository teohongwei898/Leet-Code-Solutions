    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        carry = 0
       
        result = ""
        for i in range(max(len(a),len(b))):
            if i < len(a):
                digitA = int(a[i])
            else:
                digitA = 0
            if i< len(b):
                digitB = int(b[i])
            else:
                digitB = 0
            
            total = digitA + digitB + carry
            char = str(total%2) # 1-> 1, 2-> 0, 3-> 1
            carry = str(total//2) # 1-> 0, 2->1, 3->1
            result = char + result
            
        if carry ==1:
            result= "1" + result
        return result

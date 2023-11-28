class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ones = ["I","II","III","IV","V","VI","VII","VIII","IX"]
        tens = ["X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hundreds = ["C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        thousands = ["M","MM","MMM"]
        
        roman = ""
        
        if (len(str(num))) == 1:
            return ones[num-1]
        elif (len(str(num))) == 2:
            roman+=tens[int(str(num)[0])-1]
            if int(str(num)[1]) != 0:
                roman += ones[int(str(num)[1])-1]
        
        elif (len(str(num))) == 3:
            roman+=hundreds[int(str(num)[0])-1]
            if int(str(num)[1]) != 0:
                roman += tens[int(str(num)[1])-1]
            if int(str(num)[2]) != 0:
                roman += ones[int(str(num)[2])-1]
            
        elif (len(str(num))) == 4:
            roman+=thousands[int(str(num)[0])-1]
            if int(str(num)[1]) != 0:
                roman += hundreds[int(str(num)[1])-1]
            if int(str(num)[2]) != 0:
                roman += tens[int(str(num)[2])-1]
            if int(str(num)[3]) != 0:
                roman += ones[int(str(num)[3])-1]
        return roman
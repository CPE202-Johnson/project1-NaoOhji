
def convert(num, b):
    numStrArray = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    if num/b == 0:
        if num%b!=0:
            return numStrArray[num%b]
        else:
            return ""
    else:
        return convert(num/b,b)+numStrArray[num%b]

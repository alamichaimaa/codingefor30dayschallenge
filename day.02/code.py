from datetime import datetime    
    
def timeConversion(s):   

    if s[-2:]=='AM' and s[0:2]=="12":
        return "00" + s[2:8] 
    elif s[-2:]=='AM':
        return s[:-2]
    elif s[-2:]=='PM' and s[0:2]=="12":
        return s[:-2]
    else : 
        return str(int(s[:2]) + 12) + s[2:8] 
    
#other method using datetime module
def timeConversion2(s):
    t = datetime.strptime(s, '%I:%M:%S %p')
    return t.strftime('%H:%M:%S')
 
 
#example to test the function 
if __name__ == '__main__':
    s = '10:40:22 AM'
    result = timeConversion(s)
    
    print(result + '\n')
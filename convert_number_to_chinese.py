
import string

## jiaru wan he yi

def convertShortNumToCHN(numArray):
    global dict_num_chn, dict_digit_chn
    chn_string = ""
    zero_flag = False
    for i in range(len(numArray)):            
        if numArray[i] != 0:
            if zero_flag:
                chn_string += dict_digit_chn[-1]
                zero_flag = False
            chn_string += dict_num_chn[numArray[i]]
            tmp = convertDigitPosToCHN(len(numArray)-1-i)
            if tmp != None:
                chn_string += tmp
        else:
            zero_flag = True
    return chn_string
    
    
    
    
        
def cutAndConcatenateResult(numArray):
    chn_string = ""
    if len(numArray) > 8:
        tmp = cutAndConcatenateResult(numArray[-8:])
        numArray = numArray[:-8]
        chn_string = cutAndConcatenateResult(numArray) + " YII " + tmp
        return chn_string
    elif len(numArray) > 4:
        tmp = convertShortNumToCHN(numArray[-4:])
        numArray = numArray[:-4]
        chn_string = cutAndConcatenateResult(numArray) + " WAN " + tmp
        return chn_string
    else:
        return convertShortNumToCHN(numArray)
                


def convertNumToList(number):
    numList = []
    while number / 10 != 0:
        tmp = number % 10
        numList.insert(0,tmp)
        number = (number - tmp)/10
    numList.insert(0,number)
    return numList
    
    
    
    
def convertDigitPosToCHN(digitPos):
    for item in dict_digit_chn:
        if (digitPos >= item) and (digitPos - item) % 4 == 0:
             return dict_digit_chn[item]
    return None
    
    


if __name__ == "__main__":
    dict_num_chn = {0: "", 1:" YI ", 2:" ER ", 3:" SAN ", 4:" SI ",5:" WU ", \
    6:" LIU ", 7:" QI ", 8:" BA ", 9:" JIU "}
    dict_digit_chn = {-1: " LIN ", 1:" SHI ", 2:" BAI ", 3:" QIAN"}
    
    targetNum = int(raw_input("Please type the number to be converted:\n"))
    print cutAndConcatenateResult(convertNumToList(targetNum))

#Input: A password as a string
#Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean. In the results you will see the converted results.

def checkio ( data ):    
    return (len(data)>=10) and (not data.isdigit()) and (not data.islower()) and (not data.isupper()) and (not data.isalpha())
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
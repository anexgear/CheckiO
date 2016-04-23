#Input: A password as a string (Unicode for python 2.7).
#Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean. In the results you will see the converted results.

def checkio ( data ):
    l = len ( data ) >= 10
    idig = not data.isdigit( ) 
    low = not data.islower( )
    up = not data.isupper( )
    isalp = not data.isalpha( )
        
    result = l and idig and low and up and isalp
    return result
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
import random
 
# Returns true if given two strings are same
def checkCaptcha(captcha, user_captcha):
    if captcha == user_captcha:
        return True
    return False
 
# Generates a CAPTCHA of given length
def generateCaptcha(n):
     
    # Characters to be included
    chrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
     
    # Generate n characters from above set and
    # add these characters to captcha.
    captcha = ""
    while (n):
        captcha += chrs[random.randint(1, 1000) % 62]
        n -= 1
    return captcha
 
# Driver code
n = 5 
while (n):
    captcha = generateCaptcha(5)
    print(captcha)
    if n == -1:
        break;
    n-=1

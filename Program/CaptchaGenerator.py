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
 
# Generate a random CAPTCHAfor i in range(0,6):

for i in range(0,6):
    
    captcha = generateCaptcha(5)
    print(i,captcha)
 
# Ask user to enter a CAPTCHA

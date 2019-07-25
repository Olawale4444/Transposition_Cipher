#Transposition Cipher Tool
#By Olowonyo Olawale


# myCipher Function which takes in the text string and the key value
def myCipher(plainText, key) :
    #plainText = "Sample Secret Message"
    #key = The key value/ Number of columns

    #Empyty list to be later filled up by the Cipher text
    cipherText = [" "]* key

    #clmn represents column
    for clmn in range(key):
        pointerValue = clmn
        while pointerValue < len(plainText):
            cipherText[clmn] += plainText[pointerValue]
           

            pointerValue += key
             # The while loop goes through the rows of a particular column
             # by adding the key value to the immediate character so as to
             # get to the next character and stores it in the "pointerValue"

            #print(cipherText)

    #The First two list values of the Cipher text is moved to the back 
    #to rearrange the columns and prevent it from an easy brute force attack



    firstTwo = cipherText[:2] 
    otherValues = cipherText[2:]
    
    #Final cipher text output
    print("".join(otherValues + firstTwo))
    #print(cipherText)
    
    # For a key value of 4, The keyword will be CDAB
    # For a key value of 5, The keyword will be DEABC
    # For a key value of 7, The keyword will be FGABCDE, e.t.c.

    # Since the first two values are taken to the back of the list,
    # they will be added last.

#   USER PROMPT
def userSee():
    print("Welcome to the Secure Transposition Cipher Encryptor Program 2.2.0 ! \n")

    print("Follow the Instructions to Encrypt your nmessage")
    print("Type in your secret text below \n")
    textInput = input("Enter the text to be Encrypted  ")

    print("Type in a numerical key value below")
    keyInput = input("Enter key here  ")
    intKeyInput = int(keyInput)

    print("\nProcessing ......... Encrypting..... \n ")


    print("Here's your Secure Encrypted text ;")
    myCipher(textInput, intKeyInput)


userSee()

print("\n Press 3 to Go Again ! \n " )
j = int(input(" "))
if j == 3:
    userSee()
else:
    print("Thanks for using our app, Please leave a review")


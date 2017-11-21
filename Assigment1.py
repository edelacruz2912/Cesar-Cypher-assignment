#Eduardo_De_ La_Cruz
#Cesar_cypher_HomeWork

def msnInput():
    msn = input("Enter message to be Encrypted please : ").lower()
    
    return msn


def encrypts(plainMsn):

    
    #plainMsn = "delacruz"
    array = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    key = len("delacruz")
    encryptedText = ""
    
    for ch in plainMsn:
        if(ch == " " or ch == "."): #checking if the msn has empty space or .
            encryptedText = encryptedText + ch #concatinating with empthy spaces
        else:    
            index = array.index(ch) # return the index where each letter of my lastName happen in the array
           
            newIndex = index + key #newIndex of the shifted index
          
            if(newIndex >= len(array)):# Check if the list index is out range and re assign the new index value
                newIndex = newIndex - len(array)# it is going to reset the index back to the begging of the array. array[0] 
                           
            shiftedCharacter = array[newIndex] # this get the element with the new index for the shiftedCharacter
            
            encryptedText = encryptedText + shiftedCharacter #Creating the encrypted msn by concatinating them 

    return encryptedText # return encrypted msn

def decrypttext(encryptMsn):

    
    array2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    keyNumber = len("delacruz")
    text=""
    for ch in encryptMsn:
        if(ch == " " or ch == "."):
            text = text + ch
        else:
            index = array2.index(ch)        
            oldIndex = index - keyNumber
            shiftedCharacter = array2[oldIndex]
            text = text + shiftedCharacter

    return text


    

def main():
    while(True):
        print("--------HELLO---------")
        
        msn = msnInput()
        encryptMsn = encrypts(msn)
        text = decrypttext(encryptMsn)
        print("Encrypted Message :" + " "  + encryptMsn )
        print("Decrypted Message :" + " "  + text )
      




main()

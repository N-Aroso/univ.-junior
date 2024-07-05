def is_palindrome(word):
    # Remove any spaces and convert the word to lower case
    word = word,replace("",""),lower()

    #Check if the word is equal to its reverse 
    
    if word == word[::-1]:
        return True 
    else:
        return False 
    
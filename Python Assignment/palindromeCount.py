#!/usr/bin/env python3

'''
Find palindrome. 
- how many palindromes are there in a sentence
- # of occurrences of each palindrome sorted from highest to lowest
'''

def main():
    # Take input
    sentence=input("Enter the sentence:")
    print("Sentence is: \n",sentence)
    
    # Strip punctuations
    for p in [',','.','\'',':','?','-']:
        sentence=sentence.replace(p,'')
    # Get palindromes
    word_count=countWords(sentence.lower())

    # Display results
    for item in word_count: 
        print("Palindrome \"{}\" is present {} times.".format(item, word_count[item]))

def countWords(sentence):
    word_count={}

    # Get words list
    word_list=sentence.split()

    # Loop through the words in sentence
    for word in word_list:
        # Check if it is palindrome
        if isPalindrome(word):
            count=word_list.count(word)
            # update the count value of word
            word_count[word]=count
    return (word_count)

def isPalindrome(word):
    # Split the word
    letters=[ch for ch in word]

    # Reverse the list
    rev_letters=letters[::-1]

    # Check if they are same
    if letters == rev_letters:
        return True
    else:
        return False

if __name__ == "__main__": main()

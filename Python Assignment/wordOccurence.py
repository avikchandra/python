#!/usr/bin/env python3

'''
highest occurences of words in file "sample.txt"
'''

def main():
    # Declare dict
    word_dict={}
    punct_list=[',','.','\'',':','?','-'] # list of punctuations

    # Create file object from file
    file_obj=open("sample.txt", 'r')
    word_list=[]

    # Read line from file object
    for line in file_obj:
        # Strip the punctuations from line
        for punct in punct_list:
            line=line.replace(punct,'')
        # Get words from line
        for word in line.split():
            # Append to list
            word_list.append(word.lower())

    word_dict=updateDict(word_list, word_dict)

    print("Top five word occurences: ")
    for num in range(5):
        print(findHighest(word_dict))

    # Close the file
    file_obj.close()


def updateDict(word_list, word_dict):
    # Update dictionary with word count
    for word in word_list: word_dict[word]=word_list.count(word)
    return word_dict


def findHighest(word_dict):
    # Check for occurences from dictionary
    highest_num=0
    for entry in word_dict:
        curr_count=int(word_dict[entry])
        if curr_count > highest_num:
            highest_num=curr_count
            highest_word=entry

    # Remove the word from dict
    word_dict.pop(highest_word)
    
    # Return the highest occurence
    return (highest_word, highest_num)


if __name__ == '__main__': main()

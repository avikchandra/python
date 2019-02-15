def count_letters(word_list):
    """ See question description """
    
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    for word in word_list:
        for letter in word:
            if letter in ALPHABET:
                if letter not in letter_count:
                    count = 1
                else:
                    count =  letter_count[letter] + 1
                letter_count[letter] = count

    # enter code here
    print(letter_count)
    max_count=0
    max_list=[]
    for letter in letter_count:
        cur_count=letter_count[letter]
        if cur_count >= max_count :
            max_count = cur_count
            max_list.append(letter)
        print(max_list)

    # Sort and print 
    sort_list=sorted(max_list)
    return sort_list[0]

monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"
monty_words = monty_quote.split(" ")
print(count_letters(monty_words))
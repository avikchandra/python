import re

sentence="We are at Ignite Solutions! Their email-id is careers@ignitesol.com"

word_list=re.split('[^a-zA-Z-]',sentence)
#word_list=sentence.split()
rev_word_list=[]

for word in word_list:
    ltr_list=list(word)
    rev_ltr_list=list(ltr_list[::-1])
    rev_word_list.append(''.join(rev_ltr_list))

print(' '.join(rev_word_list))
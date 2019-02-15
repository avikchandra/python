def wordGame(string):
    vowels=['A','E','I','O','U']
    str=list(string)
    length=len(str)
    count=0
    v_substr={}
    c_substr={}
    # Loop through the length
    for letter in range(length):
        # Make substrs in each loop
        for num in range(length-count):
            newstrlst=str[count:length-num]
            newstr=''.join(newstrlst)
            # Check if the first letter is vowels
            if newstrlst[0] in vowels:
                if newstr in v_substr:
                    v_substr[newstr]=v_substr[newstr]+1
                else:
                    v_substr[newstr]=1
            else:
                if newstr in c_substr:
                    c_substr[newstr]=c_substr[newstr]+1
                else:
                    c_substr[newstr]=1
        count+=1
    
    # Count scores
    total=0
    for values in v_substr.values():
        total+=values
    kevin=total
    total=0
    for values in c_substr.values():
        total+=values
    stuart=total

    # Print result
    if stuart > kevin: print("Stuart",stuart)
    elif stuart < kevin: print("Kevin",kevin)
    else: print("Draw")

s="Adidas"
wordGame(s)
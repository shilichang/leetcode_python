word1= "USA"
word2='leetcode'
word3='Google'


if word.upper()==word or word.lower()==word or word[0].upper()+word[1:].lower()==word :
    return True
else:
    return False
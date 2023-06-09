"""
1. Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls’ comments, neutralizing the threat.
Your task is to write a function that takes a string argument and returns a new string with all vowels removed.
For example, the string “Hello World!” would become “Hll Wrld”.
     Note: For this problem, ‘y’ is NOT considered a vowel

"""

# import re
# VOWELS_REGEX = r"[aeiouAEIOU]"

# def disemvowel(string_):
#     return  re.sub(VOWELS_REGEX, "", string_)

# if __name__ ==  '__main__':
#     print(disemvowel('Programming With Mosh Rocks!'))
    
    
import re 
VOWELS_REGEX = r"[aeiouAEIOU]"

def regex(string):
    return  re.sub(VOWELS_REGEX, "",string)

if __name__ == '__main__':
    print(regex("programming in python rocks"))
 
    
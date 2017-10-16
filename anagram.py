"""Find if the given two strings are anagrams of each other.
   e.g.
   input: TOM MARVOLO RIDDLE
          I AM LORD VOLDEMORT
   output : Yes
   input: xoriantsolutions
          xorandornot
   output: No
"""
from collections import Counter

def is_anagram(str1, str2):
    """Function to check if given two strings are anagram"""
    if sorted(str1) == sorted(str2):
        print "Strings are anagram!"
    else:
        print "Strings are not anagram!"
        

if __name__ == "__main__":    
    string1 = raw_input("Enter first string: ")
    str1 = Counter(char for char in string1 if char != " ")

    string2 = raw_input("Enter second string: ")
    str2 = Counter(char for char in string2 if char != " ")

    is_anagram(str1, str2)


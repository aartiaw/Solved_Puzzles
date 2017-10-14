"""Find if the given two strings are anagrams of each other.
   e.g.
   input: TOM MARVOLO RIDDLE
          I AM LORD VOLDEMORT
   output : Yes

   input: xoriantsolutions
          xorandornot
   output: No
"""

def is_anagram(str1, str2):
    """Function to check if given two strings are anagram"""
    str1.sort()
    str2.sort()

    if len(str1) != len(str2):
        print "Strings are not anagram!"
    else:
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                print "Strings are not anagram!"
                break
        print "Strings are anagram!"


if __name__ == "__main__":
    string1 = raw_input("Enter first string: ")
    str1 = [char for char in string1 if char is not " "]

    string2 = raw_input("Enter second string: ")
    str2 = [char for char in string2 if char is not " "]

    is_anagram(str1, str2)

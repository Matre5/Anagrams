# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
     print("...checking...")
     
     word_sorted = sorted(word)
     anagram_sorted = sorted(anagram)
     
     #print(word_sorted)
     #print(anagram_sorted)
     
     #the function below will check if the sorted letter are the same
     #and also check if theyre of the same length
     #if these conditions are not met it will print out not anagrams
     if (word_sorted == anagram_sorted) and (len(word_sorted) == len(anagram_sorted)):
         print(True)
         
     else:
         print(False)
         

find_anagram(word=input("The first word: "),anagram=input("The second word: "))
 
 


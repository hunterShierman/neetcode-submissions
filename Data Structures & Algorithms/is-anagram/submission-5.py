class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # thoughts
        # create a dict with all letters from first word and number of times it appears
        # iterate through each letter in the second
        #  check to see if it contains the same amount of letters
        anagram = True
        letters = {}
        letters2 = {}

        #  create a map with letters and there amount from dict one
        for letter in s:
            letters[letter] = letters.get(letter, 0) + 1

        # create a map with letters and there amount from dict two
        for letter in t: 
            letters2[letter] = letters2.get(letter, 0) + 1

        # if they are different lengths they are not anagrams
        if len(letters) != len(letters2):
            anagram = False

        else:

            # compare each letter and the amounts
            for key in letters:
                
                # check to see if the letter is in both strings
                if key not in letters2:
                    anagram = False
                    break

                # if it is in both strings check if the amount is the same
                else:
                    value1 = letters[key]
                    value2 = letters2[key]
                    if value1 != value2:
                        anagram = False



        return anagram
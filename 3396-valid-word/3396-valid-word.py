class Solution:
    def isValid(self, word: str) -> bool:
        digitsEnglish = False
        Vowel = False
        Consenant = False

        if len(word) < 3:
            return False

        if not re.fullmatch(r"[A-Za-z0-9]+", word):
            return False

        for char in word.lower():
            if char.isalpha(): 
                if char in "aeiou":
                    Vowel = True
                else:
                    Consenant = True
        return Vowel and Consenant
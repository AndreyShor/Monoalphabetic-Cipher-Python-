class MonoalphabeticCrypto:

    def __init__(self, alphabet=None):
        if alphabet is None:
            self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "!", "@"]
        else:
            self.alphabet = alphabet

    def encrypt(self, text, key):
        if self.__checkKeyDublicate(key):
            self.__createDictionary(key)
            textArray = text.lower().split(" ")
            decryptedSentence = ""
            for word in textArray:
                decryptedWord = ""
                for textLetter in word:
                    letterIndex = self.alphabet.index(textLetter)
                    decryptedWord += str(self.dictionaryList[letterIndex])
                decryptedSentence += decryptedWord + " "
            return decryptedSentence

    def decrypt(self, text, key):
        if self.__checkKeyDublicate(key):
            self.__createDictionary(key)
            textArray = text.lower().split(" ")
            encryptedSentence = ""
            for word in textArray:
                encryptWord = ""
                for textLetter in word:
                    letterIndex = self.dictionaryList.index(textLetter)
                    encryptWord += str(self.alphabet[letterIndex])
                encryptedSentence += encryptWord + " "
            return encryptedSentence

    def __createDictionary(self, key):
        keyList = list(key.lower())
        self.dictionaryList = list()

        for letter in keyList:
            self.dictionaryList.append(letter)

        for letter in self.alphabet:
            if letter not in self.dictionaryList:
                self.dictionaryList.append(letter)

    def __checkKeyDublicate(self, key):
        listKey = list(key)
        for letter in listKey:
            if listKey.count(letter) > 1:
                print("Key must don't have any duplicate letter")
                return False
        return True


test = MonoalphabeticCrypto()

key = "Ke@Yvalu!"

wordDecrypt = test.encrypt("Hello Word! and yes it is working man ", key)
print(wordDecrypt)

wordEncrypt = test.decrypt(wordDecrypt, key)
print(wordEncrypt)

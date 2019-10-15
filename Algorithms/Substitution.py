alphabet="abcçdefgğhıijklmnoöprsştuüvyz"
crypted_alphabet="zyvüutşsrpöonmlkjiıhğgfedçcba"
def setLang(self,lang):
    global alphabet
    global crypted_alphabet
    if lang == "TR":
        alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
        crypted_alphabet="zyvüutşsrpöonmlkjiıhğgfedçcba"
    if lang == "EN":
        alphabet = "abcdefghijklmnoprstuvwxyz"
        crypted_alphabet="zyxwvutsrponmlkjihgfedcba"
def encrypt(self,text):
    str.lower(text)
    encrypted=""
    for letter in text:
        letter_index = alphabet.index(letter)
        encrypted+=crypted_alphabet[letter_index]
    return encrypted
def decrypt(self,crypted_text):
    decrypted=""
    for letter in crypted_text:
        letter_index = crypted_alphabet.index(letter)
        decrypted+=alphabet[letter_index]
    return decrypted
def encrypt_menu(self):
    text=input("Please enter the text will encrypted:")
    print("Encrypted text is:\n"+self.encrypt(self,text))

def decrypt_menu(self):
    text=input("Please enter the text will decrypted:")
    print("Decrypted text is:\n"+self.decrypt(self,text))
if __name__ == "__main__":
    print("Please run Launcher.py")
    pass
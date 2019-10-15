alphabet="abcçdefgğhıijklmnoöprsştuüvyz"
def setLang(self,lang):
    global alphabet
    if lang == "TR":
        alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
    if lang == "EN":
        alphabet = "abcdefghijklmnoprstuvwxyz"
def encrypt(self,text,shifting=3):
    str.lower(text)
    encrypted=""
    for letter in text:
        letter_index = alphabet.index(letter)
        encrypted+=alphabet[(letter_index+int(shifting))%len(alphabet)]
    return encrypted
def decrypt(self,crypted_text,shifting=3):
    decrypted=""
    for letter in crypted_text:
        letter_index = alphabet.index(letter)
        if letter_index-shifting<0:
            letter_index+=len(alphabet)
        decrypted+=alphabet[(letter_index-shifting)%len(alphabet)]
    return decrypted
def encrypt_menu(self):
    text=input("Please enter the text will encrypted:")
    shift=input("Please enter the shifting number(default=3):")
    while not shift.isdigit():
        shift=input("Please enter valid shifting value.")
    print("Encrypted text is:\n"+self.encrypt(self,text,int(shift)))

def decrypt_menu(self):
    text=input("Please enter the text will decrypted:")
    shift=input("Please enter the shifting number(default=3):")
    while not shift.isdigit():
        shift=input("Please enter valid shifting value.")
    print("Decrypted text is:\n"+self.decrypt(self,text,int(shift)))

if __name__ == "__main__":
    print("Please run Launcher.py")
    pass
alphabet="abcçdefgğhıijklmnoöprsştuüvyz"
def setLang(self,lang):
    global alphabet
    if lang == "TR":
        alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
    if lang == "EN":
        alphabet = "abcdefghijklmnoprstuvwxyz"
def encrypt(self,text,a,b):
    str.lower(text)
    encrypted=""
    for letter in text:
        letter_index = alphabet.index(letter)
        crypted_index=(letter_index*a+b)%len(alphabet)
        encrypted+=alphabet[crypted_index]
    return encrypted

def decrypt(self,crypted_text,a,b):
    decrypted=""
    for letter in crypted_text:
        letter_index = alphabet.index(letter)
        encrypted_index=(find_inverse(a)*(letter_index-b))%len(alphabet)
        if encrypted_index<0:
            encrypted_index+=len(alphabet)
        decrypted+=alphabet[encrypted_index]
    return decrypted

def encrypt_menu(self):
    text=input("Please enter the text will encrypted:")
    
    a=input("Please enter the a variable:")
    while not a.isdigit():
        a=input("Please enter valid a value.")
    
    b=input("Please enter the b variable:")
    while not b.isdigit():
        b=input("Please enter valid b value.")
    a=int(a)
    b=int(b)
    print("Encrypted text is:\n"+self.encrypt(self,text,a,b))

def decrypt_menu(self):
    text=input("Please enter the text will decrypted:")

    a=input("Please enter the a variable:")
    while not a.isdigit():
        a=input("Please enter valid a value.")
    
    b=input("Please enter the b variable:")
    while not b.isdigit():
        b=input("Please enter valid b value.")
    a=int(a)
    b=int(b)

    print("Decrypted text is:\n"+self.decrypt(self,text,a,b))

def find_inverse(a):
    for i in range(len(alphabet)):
        if (a*i)%len(alphabet)==1:
            return i

            
if __name__ == "__main__":
    print("Please run Launcher.py")
    pass
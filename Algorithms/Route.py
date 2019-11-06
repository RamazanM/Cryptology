import numpy as np
from scipy.ndimage import rotate

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
def encrypt(self,text,row_len):
    encrypted=""
    for i in range(row_len-int(len(text)%row_len)):
        text+="_"
    matrix=np.array([str(letter) for letter in text])
    matrix=matrix.reshape(int(len(text)/row_len),row_len) 
    matrix=rotate_matrix_rev(matrix)
    while len(matrix)>0:
        encrypted+="".join(str(letter) for letter in matrix[0])
        matrix=np.delete(matrix,0,0)
        matrix=rotate_matrix(matrix)
    return encrypted
    
def decrypt(self,crypted_text,row_len):
    decrypted=""
    array=[]
    while len(crypted_text)>0:
        array.push([crypted_text])
    return decrypted
def encrypt_menu(self):
    text=input("Please enter the text will encrypted:")
    print("Encrypted text is:\n"+self.encrypt(self,text))

def decrypt_menu(self):
    text=input("Please enter the text will decrypted:")
    print("Decrypted text is:\n"+self.decrypt(self,text))

def rotate_matrix( m ):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
def rotate_matrix_rev( m ):
    return rotate_matrix(rotate_matrix(rotate_matrix(m)))

if __name__ == "__main__":
    print("Please run Launcher.py")
    pass
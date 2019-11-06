import numpy as np

def setLang(self,lang):
    return
def encrypt(self,text,row_len):
    encrypted=""
    for i in range(row_len-int(len(text)%row_len)):
        text+="_"
    matrix=np.array([str(letter) for letter in text])
    matrix=matrix.reshape(int(len(text)/row_len),row_len) 
    matrix=np.rot90(matrix,axes=(1,0))
    while len(matrix)>0:
        encrypted+="".join(str(letter) for letter in matrix[0])
        matrix=np.delete(matrix,0,0)
        if len(matrix) != 0:
            matrix=np.rot90(matrix)
    return encrypted
    
def decrypt(self,crypted_text,row_len):
    decrypted=""
    crypted_text=np.array([str(c) for c in crypted_text])
    array=np.zeros((row_len,int(len(crypted_text)/row_len)),"str")
    size=[int(len(crypted_text)/row_len),row_len-1]
    i=a_i=arti=0
    while len(crypted_text)>0:
        for r_i,s in enumerate(crypted_text[0:size[0]]):
            array[a_i,r_i+arti]=s
        crypted_text=np.delete(crypted_text,range(size[0]))
        size[0]-=1
        size[0],size[1]=size[1],size[0]
        array=np.rot90(array)
        if i==0:
            arti+=1
        i+=1
        if i==4:
            a_i+=1
            i=0
    array=np.rot90(array)
    for r in array:
        for s in r:
            decrypted+=s
    return decrypted
def encrypt_menu(self):
    text=input("Please enter the text will encrypted:")
    row_len=int(input("Please enter the row length:"))
    print("Encrypted text is:\n"+self.encrypt(self,text,row_len))

def decrypt_menu(self):
    text=input("Please enter the text will decrypted:")
    row_len=int(input("Please enter the row length:"))

    print("Decrypted text is:\n"+self.decrypt(self,text,row_len))

if __name__ == "__main__":
    print("Please run Launcher.py")
    pass
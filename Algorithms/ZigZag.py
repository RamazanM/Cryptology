import numpy as np

def setLang(self,lang):
    return

def encrypt(self,text,row_len):
    crypted=""
    route=1
    matrix=np.zeros((row_len,len(text)),"str")
    i=j=0
    for c in text:
        matrix[j,i]=text[0]
        text=text[1:]
        i+=1
        j+=route
        if j==row_len-1 or j==0:
            route*=-1
    for c in matrix.flatten():
        crypted+=c
    return crypted

def decrypt(self,crypted,row_len):
    i=-1
    j=0
    matrix=np.zeros((row_len,len(crypted)),"str")
    length=len(crypted)
    h=row_len+1
    route=1
    for idx in range(length):
        if len(crypted)==0:
            break
        space=2*(h-1)

        if j+space>=length or idx==0:
            i+=route
            h-=route
            j=row_len-h
            matrix[ i , j ]=crypted[0]
            crypted=crypted[1:]
        else:
            if space==0:
                space=j*2
            j+=space
            matrix[ i , j ]=crypted[0]
            crypted=crypted[1:]
            if (j+((row_len-h-1)*2))<length and i>=1 and i<row_len:
                j+=(row_len-h)*2
                matrix[ i , j ]=crypted[0]
                crypted=crypted[1:]   
    i=j=0
    encrypted=""
    for c in range(length):
        encrypted+=(matrix[j,i])
        i+=1
        j+=route
        if j==row_len-1 or j==0:
            route*=-1
    return encrypted
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
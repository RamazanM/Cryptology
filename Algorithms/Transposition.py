alphabet="abcçdefgğhıijklmnoöprsştuüvyz"
def setLang(self,lang):
    global alphabet
    if lang == "TR":
        alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
    if lang == "EN":
        alphabet = "abcdefghijklmnoprstuvwxyz"
def encrypt(self,text,keyword):
    str.lower(text)
    str.lower(keyword)
    encrypted=""
    row_len=len(keyword)
    substition_matrix=[]
    substition_order=list(range(keyword))
    for i,letter in text:
        if i%row_len==0:
            substition_matrix.append([])
        substition_matrix[len(substition_matrix)].push(letter)
    
    for i in range(keyword):
        for j in range(1,keyword):
            if alphabet.find(keyword[i])>alphabet.find(keyword[j]):
                substition_order[i],substition_order[j]=substition_order[j],substition_order[i]

    for i in substition_order:
        for row in substition_matrix:
            encrypted+=row[i]
        encrypted+=" "

    #Code will be in here

    return encrypted

def decrypt(self,text,keyword):
    decrypted=""
    str.lower(text)
    str.lower(keyword)
    row_len=len(keyword)
    substition_matrix=[]
    substition_order=list(range(keyword))

    for i in range(keyword):
        for j in range(1,keyword):
            if alphabet.find(keyword[i])>alphabet.find(keyword[j]):
                substition_order[i],substition_order[j]=substition_order[j],substition_order[i]


    #Code will be in here
    return decrypted

def encrypt_menu(self):
    text=input("Please enter the text will encrypted:")

    print("Encrypted text is:\n"+self.encrypt(self,text,a,b))

def decrypt_menu(self):
    text=input("Please enter the text will decrypted:")


    print("Decrypted text is:\n"+self.decrypt(self,text,a,b))

'''Scissor Scypher'''

msg = input("Please tell me the message to encrypt:")
shift = int(input("Shift by ="))

encrypt = ""


for i in msg:
    if i.isalpha():
        st_1 = ord(i)
        st_1 += shift
        
        if i.isupper():
            if st_1 > ord('Z'):
                st_1 -= 26
            elif st_1 < ord('A'):
                st_1 += 26
        else:
            if st_1 > ord('z'):
                st_1 -= 26
            elif st_1 < ord('a'):
                st_1 += 26
        encrypt += chr(st_1)
        
    else:
        encrypt += i
        


    
print("Encrypted : {}".format(encrypt))

shift = -shift
msg = ""
for i in encrypt:
    if i.isalpha():
        st_1 = ord(i)
        st_1 += shift
        
        if i.isupper():
            if st_1 > ord('Z'):
                st_1 -= 26
            elif st_1 < ord('A'):
                st_1 += 26
        else:
            if st_1 > ord('z'):
                st_1 -= 26
            elif st_1 < ord('a'):
                st_1 += 26
        msg += chr(st_1)
        
    else:
        msg += i
        
print("Decrypted : {}".format(msg))




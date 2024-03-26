
special=['!',',',' ','.','?']
alphabets=[chr(x).lower() for x in range(65,91)]
def ceaser_cipher_encryption(plain_text,key):
    cipher_text=''
    for i in plain_text:
        if i in special:
            cipher_text+=i
        else:
            new_pos=(alphabets.index(i)+key)%25
            cipher_text+=alphabets[new_pos]
    return cipher_text
def ceaser_cipher_decryption(cipher_text,key):
    plain_text=''
    for i in cipher_text:
        if i in special:
            plain_text+=i
        else:
            new_pos=(alphabets.index(i)-key)%25
            plain_text+=alphabets[new_pos]
    return plain_text
def vernam_cipher_encryption(plain_text,key):
    cipher_text=''
    for i,j in zip(plain_text,key):
            new_pos=ord(i)+ord(j)
            cipher_text+=chr(new_pos)
    return cipher_text
def vernam_cipher_decryption(cipher_text,key):
    plain_text=''
    for i,j in zip(cipher_text,key):
            new_pos=ord(i)-ord(j)
            plain_text+=chr(new_pos)
    return plain_text
# def find_key(cipher_dict,item_list,key_list,val):
#     pos = item_list.index(val)
#     key = key_list[pos]
#     return key
# def monoalphabetic_cipher_encryption(plain_text,cipher_dict):
#     cipher_text = ''
#     for i in plain_text:
#         cipher_text += cipher_dict[i]
#     return cipher_text
# def monoalphabetic_cipher_decryption(cipher_text,cipher_dict,item_list,key_list):
#     plain_text = ''
#     for i in cipher_text:
#         key = find_key(cipher_dict,item_list,key_list,i)
#         plain_text += key
#     return plain_text
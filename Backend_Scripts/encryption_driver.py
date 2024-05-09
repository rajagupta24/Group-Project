import Encryption_project
encryptionChoice=input("Which encryption method (ceaser,,monoalphabetic):")
option=input('Encrypt or decrypt(e/d):')
text=input("Enter a sentence(s):")
if encryptionChoice=='ceaser':
  key=int(input("Enter the key:"))
  if option=='e':
    Encrypt_text=Encryption_project.ceaser_cipher_encryption(text,key)
  if option=='d':
    Encrypt_text=Encryption_project.ceaser_cipher_decryption(text,key)
if encryptionChoice=='vernam':
  while len(key)==0:
    key = int(input("Enter the key(same length as text):"))
  if option=='e':
    Encrypt_text=Encryption_project.vernam_cipher_encryption(text,key)
  if option=='d':
    Encrypt_text=Encryption_project.vernam_cipher_decryption(text,key)
# if encryptionChoice=='monoalphabetic':
#   cipher_dict = {}
#   alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#                'v', 'w', 'x', 'y', 'z']
#   alphabet_scarm = set(alphabets)
#   for key, value in zip(alphabets, alphabet_scarm):
#     cipher_dict[key] = value
#   item_list = list(cipher_dict.values())
#   key_list = list(cipher_dict.keys())
#   if option=='e':
#     Encrypt_text=Encryption_project.monoalphabetic_cipher_encryption(text,cipher_dict)
#   if option=='d':
#     Encrypt_text = Encryption_project.monoalphabetic_cipher_decryption(text, cipher_dict, item_list, key_list)

print(Encrypt_text)

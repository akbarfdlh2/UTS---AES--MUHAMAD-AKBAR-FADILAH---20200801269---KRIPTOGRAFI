import AES as aes

print("NAMA : MUHAMAD AKBAR FADILAH")
print("NIM : 20200801269")
print("FAKULTAS : ILMU KOMPUTER")
print("JURUSAN : TEKNIK INFORMATIKA")

def print_separator_long():
    print("=======================================================================================================================================")


if __name__ == '__main__':
    KEYS = ["Muhamad Akbar Fadilah", "Esa Unggul"]
    TEXTS = ["Two One Nine Two", "This is the text"]
    for i in range(2):
        print_separator_long()
        main_key = aes.translate_string_into_hex_str(KEYS[i])
        main_text = aes.translate_string_into_hex_str(TEXTS[i])
        round_keys = aes.find_all_round_keys(main_key)
        encrypt_text = aes.encrypt(main_text, round_keys)
        encrypt_text_str = aes.translate_hex_into_str(encrypt_text)
        decrypt_text = aes.decryption(encrypt_text, round_keys)
        resolved_text = aes.translate_hex_into_str(decrypt_text)

        print("Key : \'{}\'".format(KEYS[i]))
        print("Message Text : \'{}\'".format(TEXTS[i]))
        print("Length of Text :", len(TEXTS[i]))
        print("Encrypted Text :", encrypt_text_str)
        print("Length of Encrypted Text :", len(encrypt_text_str))
        print("Resolved Text : \'{}\'".format(resolved_text))
        print("Length of Resolved Text :", len(resolved_text))
        print_separator_long()

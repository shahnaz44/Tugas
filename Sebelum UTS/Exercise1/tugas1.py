def start_program():
    while True:
        selection = input("""Silahkan input value sesuai kebutuhan anda\nInput 'E' untuk melakukan enkripsi\nInput 'D' untuk melakukan dekripsi\nInput 'Q' untuk menghentikan program[E/D/Q]\n""")
        if selection == 'E':
            inpass = input("Masukkan Password yang ingin dienkripsi: ")
            if len(inpass) <= 100:
                print(encrypt(inpass))
            else:
                print('Tidak boleh melebihi 100 karakter')
                continue
        elif selection == 'D':
            inpass = input("Masukkan Password yang ingin didekripsi: ")
            try:
                print(decrypt(inpass))
            except:
                print('Password anda tidak tidak sesuai, dimohon untuk periksa kembali')
                continue
        elif selection == 'Q':
            break
        else:
            print('Invalid Input')
            continue

def joinlist(list):
    return ''.join([i for i in list])

def lol_to_list(list): #elemen list dalam list digabung jadi list biasa
    return [j for i in list for j in i]

def chartoascii(pwd):
    listchar = list(pwd)
    return [ord(char) for char in listchar]

def asciitochar(pwd):
    return [[chr(pwd[i]),chr(pwd[i+1]), pwd[i+2]] for i in range(0,len(pwd),3)]

def val_calc(num):

    firstval = num//26 + 80
    secondval = num%26 + 80
    if firstval > secondval:
      thirdval = '+'
    else:
      thirdval = '-'

    return [firstval, secondval, thirdval]

def encrypt(passwordd):
    asciilist = chartoascii(passwordd)
    firstencrypt = list(map(val_calc, asciilist))
    encryptednum_list = lol_to_list(firstencrypt)
    encryptedpass_list = asciitochar(encryptednum_list)

    return joinlist(lol_to_list(encryptedpass_list))

#-----------------------------------------------------------------------------

def split3val(pwd):
    return [[pwd[i],pwd[i+1]] for i in range(0, len(pwd), 3)]

def val_decalc(numlist):
    return [26 * (ord(i[0]) - 80) + (ord(i[1]) - 80) for i in numlist]

def decrypt(passwordd):
    splittedpwd = split3val(passwordd)
    asciipass = val_decalc(splittedpwd)

    return joinlist([chr(i) for i in asciipass])

start_program()

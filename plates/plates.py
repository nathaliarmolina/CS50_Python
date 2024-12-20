def main():
    plate = input("Plate: ")
    plate = plate.upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(p):

    #captura comprimento da placa
    p_len = (len(p))

    #conjunto de caracteres permitidos
    permit = set("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    valid_char = set(p)

    #valida se placa só contém caracteres permitidos
    validation = valid_char.issubset(permit)

    if validation == False:
        return False

    if p_len >=2 and p_len <=6:

        #valida placa com 2 digitos e letras
        if p[0].isalpha() == False or p[1].isalpha() == False:
            return False

        # valida se comprimento for 2 digitos com letras
        if p_len == 2 and p.isalpha() == True:
            return True

       #placa com 3 digitos

        if p_len == 3:

            if p.isalpha():  #valida direto se todos os  digitos forem numericos
                return True

            if '0' in p[2]:  #invalida se tiver 0 na placa de 3 digitos
                return False
            else:
                return True

        #placa com 4 digitos
        if p_len == 4:

            if p.isalpha():  #valida direto se todos os digitos forem numericos
                return True

            if p[3].isalpha() and p[2].isdigit(): # se 4º digito for letra, não pode 3º digito ser numero
                    return False

            if p[2].isalpha():
                if p[3].isdigit() and p[3] == '0': # se 4º digito for primeiro numero, não pode ser 0
                    return False

            if p[2].isdigit() and p[2] == '0': # se 3º digito for primeiro numero, ele não pode ser 0
                    return False

            else:
                return True


        #placa com 5 digitos
        if p_len == 5:

            if p.isalpha():  #valida direto se todos os  digitos forem numericos
                return True

            if p[4].isalpha() and p[3].isdigit() or p[2].isdigit(): #se 5º dig for letra, 4º e 3º não podem ser numeros
                return False

            if p[3].isalpha() and p[2].isdigit(): #se 3º dig for letra, 2º não pode ser numero
                return False

            if p[3].isalpha() and p[4].isdigit(): #se 5º dig for o primeiro numero, não pode ser 0
                if p[4] =='0':
                    return False
                else:
                    return True

            if p[2].isalpha() and p[3].isdigit(): #se 4º dig for o primeiro numero, não pode ser 0
                if p[3] =='0':
                    return False
                else:
                    return True

            if p[1].isalpha() and p[2].isdigit(): #se 3º dig for o primeiro numero, não pode ser 0
                if p[2] =='0':
                    return False
                else:
                    return True

            else:
                return True


        #placa com 6 digitos
        if p_len == 6:

            if p.isalpha():  #valida direto se todos os  digitos forem numericos
                return True

            if p[5].isalpha() and p[4].isdigit() or p[3].isdigit() or p[2].isdigit(): #se 6º dig for letra, 5º, 4º e 3º não podem ser numeros
                return False

            if p[4].isalpha() and p[3].isdigit() or p[2].isdigit(): #se 5º dig for letra, 4º e 3º não podem ser numeros
                return False

            if p[4].isalpha() and p[5].isdigit(): #se 6º dig for o primeiro numero, não pode ser 0
                    if p[5] =='0':
                        return False
                    else:
                         return True

            if p[3].isalpha() and p[4].isdigit(): #se 5º dig for o primeiro numero, não pode ser 0
                if p[4] =='0':
                    return False
                else:
                    return True

            if p[2].isalpha() and p[3].isdigit(): #se 4º dig for o primeiro numero, não pode ser 0
                if p[3] =='0':
                    return False
                else:
                    return True

            if p[1].isalpha() and p[2].isdigit(): #se 3º dig for o primeiro numero, não pode ser 0
                if p[2] =='0':
                    return False
                else:
                    return True


    else:
        return False

main()
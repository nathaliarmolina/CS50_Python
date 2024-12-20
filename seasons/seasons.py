from datetime import date
import datetime
import re
import inflect
import sys



def main():

    p = inflect.engine() #instancia o inflect
    birth = get_birth() #captura a data de nascimento como string
    val = validate_birth(birth) #valida data com booleano

    try:
        birth_data = set_birth(birth) #converte str para date
        today_data = get_today() #get data
        total_minutes = get_minutes(today_data, birth_data) #get minutes
        words = p.number_to_words(total_minutes, andword="") #traduz em palavras
        print(words.capitalize(), "minutes")

    except:
        sys.exit("")


#Extrai os minutos totais da data atual - data de nascimento
def get_minutes(today_data, birth_data):
    delta = today_data - birth_data
    minutes = delta.days * 24 * 60
    return minutes

#input da data de nascimento
def get_birth():
    birth = input("Date of Birth: ")
    return birth

#valida se a data está no formato certo YYYY-MM-DD
def validate_birth(birth):
    val_birth = re.search(r"^\d{4}-\d{1,2}-\d{1,2}$", birth)
    if val_birth:
        return True

    else:
        print("Invalid date")
        return False

#Captura data de hoje
def get_today():
    today = datetime.date.today()
    return today

#Transforma a data de nascimento(string) em um objeto do tipo data
def set_birth(birth):
    yy_birth, mm_birth, dd_birth = birth.split("-")
    yy_birth = int (yy_birth)
    mm_birth = int (mm_birth)
    dd_birth = int (dd_birth)

    birth_data = datetime.date(yy_birth, mm_birth, dd_birth)
    return birth_data


if __name__ == "__main__":
    main()

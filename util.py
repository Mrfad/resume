from datetime import date, datetime



def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

date_str = '7-19-1975'
born = datetime.strptime(date_str, '%m-%d-%Y').date()


age = calculate_age(born)
print(age)

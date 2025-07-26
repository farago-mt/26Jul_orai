import datetime
import random
import string

def create_user_id(): #string
    alphabet = string.ascii_letters + string.digits
    id = ''
    while len(id) < 6:
        id += random.choice(alphabet)
    user_id = "user-" + id
    return user_id


def create_born_date(): #date
    date1 = datetime.date(1920, 1, 1)
    date2 = datetime.date(1980, 12, 31)
    days_between = date2 - date1
    random_day = random.randrange(days_between.days)
    born_date = date1 + datetime.timedelta(days=random_day)
    return born_date

def get_age(born_date): #int
    today = datetime.date.today()
    age = today.year - born_date.year
    return age

def get_name(names): #string
    return random.choice(names)

def create_valid_until_date(): #date
    today = datetime.date.today()
    random_day = random.randrange(1, 365)
    valid_until = today + datetime.timedelta(days=random_day)
    return valid_until

print(f'user_id: {create_user_id()}')
born_date = create_born_date()
print(f'born_date: {born_date}')
print(f'age: {get_age(born_date)}')
names = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Charlie Davis", "Emily Clark"]
print(f'name: {get_name(names)}')
print(f'vote valid: {create_valid_until_date()}')
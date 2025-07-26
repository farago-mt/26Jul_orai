# import datetime
# import random
# import string
#
# def create_user_id(): #string
#     alphabet = string.ascii_letters + string.digits
#     id = ''
#     while len(id) < 6:
#         id += random.choice(alphabet)
#     user_id = "user-" + id
#     return user_id
#
#
# def create_born_date(): #date
#     date1 = datetime.date(1920, 1, 1)
#     date2 = datetime.date(1980, 12, 31)
#     days_between = date2 - date1
#     random_day = random.randrange(days_between.days)
#     born_date = date1 + datetime.timedelta(days=random_day)
#     return born_date
#
# def get_age(born_date): #int
#     today = datetime.date.today()
#     age = today.year - born_date.year
#     return age
#
# def get_name(names): #string
#     return random.choice(names)
#
# def create_valid_until_date(): #date
#     today = datetime.date.today()
#     random_day = random.randrange(1, 365)
#     valid_until = today + datetime.timedelta(days=random_day)
#     return valid_until
#
# print(f'user_id: {create_user_id()}')
# born_date = create_born_date()
# print(f'born_date: {born_date}')
# print(f'age: {get_age(born_date)}')
# names = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Charlie Davis", "Emily Clark"]
# print(f'name: {get_name(names)}')
# print(f'vote valid: {create_valid_until_date()}')

# import json
# def json_write(path, dictionary): #pl("random_user_data.txt", users}
#     """A megadott szótárat JSON fájlba írja."""
#
#     with open(path, "w", encoding="utf-8") as file:
#         json.dump(dictionary, file, indent=4, ensure_ascii=True)
#
#
# def json_export(path, dictionary):
#     """Szűrt adatokat külön JSON fájlba ment."""
#
#     with open(path, "w", encoding="utf-8") as file:
#         json.dump(dictionary, file, indent=4, ensure_ascii=True)
#
#
# def json_load(path):
#     """Beolvassa a JSON fájl tartalmát és JSON szövegként adja vissza."""
#
#     with open(path, "r", encoding="utf-8") as file:
#         json_string = file.read()
#     return json_string

####Filters####

# def no_worker():
#     """Kiszűri a nem dolgozó felhasználókat és menti őket a no_worker.json fájlba."""
#     json_string = json_load("random_user_data.txt")
#     users = json.loads(json_string)
#
#     no_workers = []
#     for user in users:
#         if user["workstat"] == False:
#             no_workers.append(user)
#     json_export("no_worker.json", no_workers)
#
#
# def over65():
#     """Kiszűri a 65 év feletti felhasználókat, és menti őket az over65.json fájlba."""
#     json_string = json_load("random_user_data.txt")
#     users = json.loads(json_string)
#
#     over65 = []
#     for user in users:
#         if user["age"] > 65:
#             over65.append(user)
#     json_export("over65.json", over65)
#
#
# def HU_cizizen():
#     """Kiszűri a magyar állampolgárokat, és menti őket a middle_eu.json fájlba."""
#     json_string = json_load("random_user_data.txt")
#     users = json.loads(json_string)
#
#     HU_ciziten = []
#     for user in users:
#         if user["land"] == "HU".upper():
#             HU_ciziten.append(user)
#     json_export("middle_eu.json", HU_ciziten)

def expire180():
    json_string = json_load("random_user_data.txt")
    users = json.loads(json_string)

    expire180 = []
    for user in users:
        date1 = datetime.datetime.now()
        date2 = datetime.datetime.strptime(user["vote"], "%Y-%m-%d")
        difference = (date2 - date1).days
        if 0 <= difference <= 180:
            expire180.append(user)
    json_export("expire180.json", expire180)



import datetime
import random
import string
import json

#----------------------------------------------------még nincs kész----------
def check_workstatus(input_end_date):
    #if input_end_date - datetime.datetime.now() < 180:
        #return True
    return input_end_date
#----------------------------------------------------még nincs kész----------

def generate_nationality(input_data):
    return random.choice(input_data)

def generate_work_status_boolean():
    return random.choice([True, False])

def generate_workstatus_end_date():
    temp_month = int(random.randint(1,12))
    temp_year = int(datetime.date.today().strftime("%Y"))
    temp_year_plus1 = int(temp_year) + 1
    rand_year = random.choice([temp_year, temp_year_plus1])
    temp_day = random.randrange(1, calendar.monthrange(rand_year,temp_month)[1])
    return datetime.date(rand_year,temp_month,temp_day)

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

def json_write(path, dictionary): #pl("random_user_data.txt", users}
    """A megadott szótárat JSON fájlba írja."""

    with open(path, "w", encoding="utf-8") as file:
        json.dump(dictionary, file, indent=4, ensure_ascii=True)


def json_export(path, dictionary):
    """Szűrt adatokat külön JSON fájlba ment."""

    with open(path, "w", encoding="utf-8") as file:
        json.dump(dictionary, file, indent=4, ensure_ascii=True)


def json_load(path):
    """Beolvassa a JSON fájl tartalmát és JSON szövegként adja vissza."""

    with open(path, "r", encoding="utf-8") as file:
        json_string = file.read()
    return json_string


def generate_users():
    users = {}
    user = {}
    names = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Charlie Davis", "Emily Clark"]
    user_id = create_user_id()
    born_date = create_born_date()
    name = get_name(names)
    age = get_age(born_date)
    valid_until = create_valid_until_date()
    nat_list = ["HU", "EU", "USA", "SP"]
    country = generate_nationality(nat_list)
    print(country)
    worker = generate_work_status_boolean()
    # other = []
    user = {valid_until, born_date, name, age, country, worker}
    print(user)
    users[user_id] = user
    print(users[user_id])

def main():
    generate_users()

main()


# print(f'user_id: {create_user_id()}')
# born_date = create_born_date()
# print(f'born_date: {born_date}')
# print(f'age: {get_age(born_date)}')
# names = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Charlie Davis", "Emily Clark"]
# print(f'name: {get_name(names)}')
# print(f'vote valid: {create_valid_until_date()}')

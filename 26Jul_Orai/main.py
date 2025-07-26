import datetime
import random
import string
#----------------------------------------------------még nincs kész----------
def check_workstatus(input_end_date):
    #if input_end_date - datetime.datetime.now() < 180:
        #return True
    return input_end_date
#----------------------------------------------------még nincs kész----------

def generate_nationality(input_data: List):
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

print(f'user_id: {create_user_id()}')
born_date = create_born_date()
print(f'born_date: {born_date}')
print(f'age: {get_age(born_date)}')
names = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Charlie Davis", "Emily Clark"]
print(f'name: {get_name(names)}')
print(f'vote valid: {create_valid_until_date()}')

import csv
import random
import datetime
from faker import Faker
import bcrypt

fake = Faker()

# Генерация данных для таблицы "tractors"
def generate_tractors_data(num_records):
    engine_types = ['Diesel', 'Electric', 'Gasoline']
    ecological_standards = ['Euro 5', 'Euro 6', 'Euro 3']
    
    tractors = []
    for i in range(1, num_records + 1):
        tractor = {
            'model': f'{fake.word()}-{random.randint(100, 999)}',
            'release_year': random.randint(2018, 2024),
            'enginetype': random.choice(engine_types),
            'enginepower': f'{random.randint(140, 230)} HP',
            'fronttiresize': random.randint(15, 19),
            'backtiresize': random.randint(21, 25),
            'wheelsamount': random.randint(4, 8),
            'tankcapacity': random.randint(180, 330),
            'ecologicalstandart': random.choice(ecological_standards),
            'length': round(random.uniform(4.8, 5.8), 1),
            'width': round(random.uniform(2.3, 2.7), 1),
            'cabinheight': round(random.uniform(2.9, 3.4), 1)
        }
        tractors.append(tractor)
    
    return tractors

# Генерация данных для таблицы "assemblylines"
def generate_assemblylines_data(num_records):
    statuses = ['работает']
    
    assemblylines = []
    for i in range(1, num_records + 1):
        lastinspectiondate = fake.date_between(start_date='-2y', end_date='today')
        nextinspectiondate = lastinspectiondate + datetime.timedelta(days=365)
        
        assemblyline = {
            'name': f'Line {i}',
            'length': round(random.uniform(45.0, 60.0), 1),
            'height': round(random.uniform(4.5, 6.0), 1),
            'width': round(random.uniform(9.5, 12.0), 1),
            'status': random.choice(statuses),
            'production': random.randint(800, 1350),
            'downtime': random.randint(5, 20),
            'inspectionsamountperyear': 4,
            'lastinspectiondate': lastinspectiondate.strftime('%Y-%m-%d'),
            'nextinspectiondate': nextinspectiondate.strftime('%Y-%m-%d'),
            'defectrate': random.randint(3, 7)
        }
        assemblylines.append(assemblyline)
    
    return assemblylines

# Генерация данных для таблицы "details"
def generate_details_data(num_records):
    countries = ['Germany', 'USA', 'China', 'Japan', 'France', 'Italy', 'UK', 'Canada', 'India', 'Brazil', 'Australia', 'South Korea', 'Mexico', 'Russia', 'Spain']
    detailsnames = ["Гайка", "Болт", "Прокладка", "Шуруп", "Шестерня привода", "Радиатор", "Вал коленчатый", "Вал привод", "Тормозной диск", "Патрубок", "Крестовина малая", "Гидрораспределитель", "Гидроусилитель", "Рукав высокого давления", "Кольцо поршневое", "Вентиляторный ремень", "Пружинный сальник"]
    details = []
    for i in range(1, num_records + 1):
        detail = {
            'name': f'{random.choice(detailsnames)}-{chr(64 + i)}',
            'country': random.choice(countries),
            'amount': random.randint(100, 200),
            'price': round(random.uniform(40.0, 80.0), 1),
            'length': random.randint(8, 12),
            'height': random.randint(4, 6),
            'width': random.randint(2, 4)
        }
        details.append(detail)
    
    return details

# Генерация данных для таблицы "users"
def generate_users_data(num_records):
    sexes = ['м', 'ж']
    roles = ['администратор', 'оператор производства', 'специалист по обслуживанию']
    password = fake.password()

    users = []
    for i in range(1, num_records + 1):
        user = {
            'name': fake.first_name(),
            'surname': fake.last_name(),
            'fatherame': fake.first_name(),
            'department': f'Департамент {chr(random.randint(65, 67))}',
            'email': fake.email(),
            'password': bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            'dateofbirth': fake.date_of_birth(minimum_age=25, maximum_age=60).strftime('%Y-%m-%d'),
            'sex': random.choice(sexes),
            'role': random.choice(roles)
        }
        users.append(user)
    
    return users

# Генерация данных для таблицы "detailorders"
# def generate_detailorders_data(num_records):
#     statuses = ['обрабатывается', 'принят', 'доставляется', 'выполнен']
    
#     detailorders = []
#     for i in range(1, num_records + 1):
#         orderdate = fake.date_time_between(start_date='-1y', end_date='now')
        
#         detailorder = {
#             'id': i,
#             'userid': random.randint(1, num_records),
#             'requestid': random.randint(100, 200),
#             'status': random.choice(statuses),
#             'totalprice': round(random.uniform(400.0, 800.0), 1),
#             'orderdate': orderdate.strftime('%Y-%m-%d %H:%M:%S')
#         }
#         detailorders.append(detailorder)
    
#     return detailorders

# Запись данных в CSV файлы
def write_to_csv(filename, fieldnames, data):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Генерация и запись данных
num_records = 35

tractors_data = generate_tractors_data(num_records)
write_to_csv('/Users/m4ks0n/study/IU7/sem6/dbcourse/bmstu-iu7-sem6-bdcoursework/doc/testdata/tractors.csv', tractors_data[0].keys(), tractors_data)

assemblylines_data = generate_assemblylines_data(num_records)
write_to_csv('/Users/m4ks0n/study/IU7/sem6/dbcourse/bmstu-iu7-sem6-bdcoursework/doc/testdata/assemblylines.csv', assemblylines_data[0].keys(), assemblylines_data)

details_data = generate_details_data(num_records)
write_to_csv('/Users/m4ks0n/study/IU7/sem6/dbcourse/bmstu-iu7-sem6-bdcoursework/doc/testdata/details.csv', details_data[0].keys(), details_data)

users_data = generate_users_data(num_records)
write_to_csv('/Users/m4ks0n/study/IU7/sem6/dbcourse/bmstu-iu7-sem6-bdcoursework/doc/testdata/users.csv', users_data[0].keys(), users_data)

# detailorders_data = generate_detailorders_data(num_records)
# write_to_csv('detailorders.csv', detailorders_data[0].keys(), detailorders_data)

print("Data generation complete.")

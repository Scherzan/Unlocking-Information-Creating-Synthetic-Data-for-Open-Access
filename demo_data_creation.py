import csv
from datetime import date, timedelta
import random

# Define the field names
field_names = ['person_id', 'first_name', 'last_name', 'email', 'age', 'gender', 'description_of_item', 'price', 'date_transaction', 'bank_account_balance']

# Define the list of data rows
data = []

# Generate 25 random data rows
for i in range(1, 26):
    person_id = i
    first_name = random.choice(['John', 'Jane', 'Michael', 'Samantha', 'William', 'Emily', 'Andrew', 'Melissa', 'Oliver', 'Grace'])
    last_name = random.choice(['Doe', 'Smith', 'Jones', 'Lee', 'Kim', 'Nguyen', 'Wong', 'Taylor', 'Brown', 'Garcia'])
    email = first_name.lower() + '_' + last_name.lower() + '@gmail.com'
    age = random.randint(20, 50)
    gender = random.choice(['Male', 'Female'])
    description_of_item = random.choice(['Apple Watch Series 7', 'Amazon Echo Dot', 'PlayStation 5', 'Google Nest Mini', 'Samsung 55-inch Smart TV', 'Bose QuietComfort 35 II', 'Apple iPad Pro', 'Fitbit Charge 5', 'Nintendo Switch', 'Sony WH-1000XM4'])
    price = random.randint(29, 1099)
    date_transaction = (date.today() - timedelta(days=random.randint(0, 10))).strftime('%Y-%m-%d')
    bank_account_balance = random.randint(500, 20000)
    row = [person_id, first_name, last_name, email, age, gender, description_of_item, price, date_transaction, bank_account_balance]
    data.append(row)

# Write the data to a CSV file
with open('example_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

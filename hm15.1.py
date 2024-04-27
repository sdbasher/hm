import json
import csv
import random


with open('data.json', 'r') as f:
    data = json.load(f)


def generate_phone_number():
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])


with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Ім'я", "Вік", "Телефон"])
    for key, value in data.items():
        id_number = str(key)
        name = value[0]
        age = str(value[1])
        phone = generate_phone_number()
        writer.writerow([id_number, name, age, phone])

print("Дані успішно записані у файл data.csv")

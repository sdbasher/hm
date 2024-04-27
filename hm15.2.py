import pandas as pd

df = pd.read_csv('data.csv', encoding='cp1251')

df.drop(columns=['Вік'], inplace=True)

df.to_excel('data.xlsx', index=False)

print("Дані успішно збережені у файл data.xlsx")

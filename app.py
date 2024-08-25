import pandas as pd

# Загрузка данных из файла data.csv
data = pd.read_csv('data.csv')

# Вычисление средней зарплаты
average_salary = data['salary'].mean()

# Отбор сотрудников старше 30 лет
employees_above_30 = data[data['age'] > 30]

# Вывод результатов
print(f"Средняя зарплата всех сотрудников: {average_salary:.2f}")
print("Сотрудники старше 30 лет:")
print(employees_above_30)

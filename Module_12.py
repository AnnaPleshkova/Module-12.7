per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print("Процентные ставки по вкладам в банках", per_cent)
money = float(input("Введите сумму, которую планируете положить под проценты: "))
deposit = []
for i in list(per_cent.values()):
    deposit.append(float(money * i / 100))

print("Накопления за год в каждом из банков", deposit)
print("Максимальная сумма за год ", max(deposit))

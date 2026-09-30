from escpos.printer import Network
import random
import datetime

print("Let's buy something to you!")
things = {"1": 119.99, "2": 49.99, "3": 499.99, "4": 130.50, "5": 1365.99, "6": 450.35}
print("давай чо там")
total = 0

# 1. Бесконечный цикл покупки (принтер тут вообще не трогаем, чтобы не висел)
while True:
    choice = input("номер(или pay): ").strip()

    if choice.lower() == 'pay':
        break  # Выходим из цикла, если пора платить

    if choice in things:
        price = things[choice]
        # КЛАДЕМ ДЕНЬГИ В АККУМУЛЯТОР
        total += price
        print(f"Добавлен товар за {price} RUB. Текущая сумма в аккумуляторе: {total:.2f} RUB\nдавай далше че ты медлишь")
    else:
        print("Такого товара нет! Выбери от 1 до 6.")

# 2. Формируем штрихкод
codes = str(random.randint(1000, 9999))
now = datetime.datetime.now()
code_date = now.strftime("%Y")
code = code_date + codes

# Красиво форматируем дату для текста чека (без миллисекунд)
krasivo_date = now.strftime("%d.%m.%Y %H:%M:%S")

# Подключаемся к своему собственному локальному эмулятору
print("отправка...")
printer = Network("127.0.0.1", port=9100)
print("успешно")

# Печатаем всё в один аккуратный чек
printer.text(f"PURCHASE: {krasivo_date}\n")
printer.text(f"PRICE: {total:.2f} RUB\n")
printer.text("--------------------------------\n")
printer.text("bratan sps!\n")

# Печатаем штрихкод и режем бумагу
printer.barcode(code, 'EAN8')
printer.cut()

# ПРИНУДИТЕЛЬНО ВЫТАЛКИВАЕМ БАЙТЫ В СЕТЬ (для Mac)
printer.close()

print("Готово! Проверяй вкладку с портом 9646.")

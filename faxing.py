from escpos.printer import Network
import random

id = f"PyFax | fax: {random.randint(1000,9999)} id\n"

text = input("text:")

# Подключаемся к своему собственному локальному эмулятору
print("отправка...")
printer = Network("127.0.0.1", port=9100)
print("успешно")

# Факс тупо шлет
printer.text(id)
printer.text(text)

printer.cut()
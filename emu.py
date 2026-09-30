import socket

# Создаем локальный сервер, который слушает порт 9100
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9100))
server.listen(1)

print("=== ЛОКАЛЬНЫЙ ЭМУЛЯТОР ЗАПУЩЕН ===")
print("Слушаю порт 127.0.0.1:9100... Ожидаю чек/факс\n")

while True:
    conn, addr = server.accept()
    print(f"Получено подключение от {addr}")
    data = b""
    while True:
        packet = conn.recv(1024)
        if not packet:
            break
        data += packet

    print("\n--- ПОЛУЧЕН СЫРОЙ ЧЕК ---")
    # Пробуем прочитать текст, игнорируя бинарные команды штрихкода
    print(data.decode('utf-8', errors='ignore'))
    print("-------------------------\n")
    conn.close()

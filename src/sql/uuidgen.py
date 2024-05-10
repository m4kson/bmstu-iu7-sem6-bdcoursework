import uuid

def generate_uuid():
    # Генерируем UUID и возвращаем его в виде строки
    return str(uuid.uuid4())

# Пример использования
if __name__ == "__main__":
    for i in range(10):
        new_uuid = generate_uuid()
        print("Сгенерированный UUID:", new_uuid)
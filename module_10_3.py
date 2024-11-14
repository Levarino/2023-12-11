from random import randint
import time
import threading

class Bank:
    def __init__(self):
        self.balance = 0  # Баланс банка
        self.lock = threading.Lock()  # Объект Lock для безопасности потоков

    def deposit(self):
        for _ in range(100):
            balance_plus = randint(50, 500)  # Случайная сумма для пополнения
            with self.lock:  # Блокируем доступ к балансу
                self.balance += balance_plus
                print(f'Пополнение: {balance_plus} | Баланс: {self.balance}')
            time.sleep(0.001)  # Имитация времени выполнения

    def take(self):
        for _ in range(100):
            balance_minus = randint(50, 500)  # Случайная сумма для снятия
            print(f'Запрос на снятие: {balance_minus}.')
            with self.lock:  # Блокируем доступ к балансу
                if balance_minus <= self.balance:
                    self.balance -= balance_minus
                    print(f'Снятие: {balance_minus} | Баланс: {self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств.')
            time.sleep(0.001)  # Имитация времени выполнения

# Создаем объект класса Bank
bk = Bank()

# Создаем потоки для методов deposit и take
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

# Запускаем потоки
th1.start()
th2.start()

# Ждем завершения потоков
th1.join()
th2.join()

# Выводим итоговый баланс
print(f'Итоговый баланс: {bk.balance}')


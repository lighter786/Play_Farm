import time
import random
from random import randint


class Farm:
    def __init__(self):
        self.__money = 100  # Деньги
        self.__harvest = {"морковь": 0, "пшеница": 0, "картошка": 0}  # Урожай
        self.__day = 0  # Дни
        self._profit = 0
        self._quantity = 0
        self.crop = ""  # Текущая культура
        self.price = 0  # Цена текущей культуры
        
    def day_next(self):
        print("Наступила ночь")
        time.sleep(6)
        print("Наступил следующий день...")
        self.__day += 1 
        
    def profit(self):  # Прибыль
        if self.crop.lower() == "морковь":
            self._profit += random.randint(2, 7)
        elif self.crop.lower() == "пшеница":
            self._profit += 4
        elif self.crop.lower() == "картошка":
            self._profit += random.randint(3, 9)
    
    def buy_plants(self):  # Покупка семян для засева
        print("Что купим?")
        print("1.Морковь(Растет 2 дня | Стоимость 5 монет | Прибыль с одной штуки от 2 до 6 )")
        print("2.Пшеница(Растет 3 - 4 дня | Стоимость 7 монет | Прибыль с одной штуки 4)")
        print("3.Картошка(Растет 5 дней | Стоимость 10 монет | Прибыль с одной штуки от 3 до 8)")
        
        choice = input("Выберите культуру (1 - 3), или введите её название: ").lower()
        
        if choice in ["морковь", "1"]:
            self.crop = "морковь"
            self.price = 5
        elif choice in ["пшеница", "2"]:
            self.crop = "пшеница"
            self.price = 7
        elif choice in ["картошка", "3"]:
            self.crop = "картошка"
            self.price = 10
        else:
            print("Неверный ввод!")
            return
        
        print("Введите количество штук (Макс: 5 штук)")
        while True:
            try:
                quantity = int(input())
                if 1 <= quantity <= 5:
                    cost_buy = self.price * quantity
                    if cost_buy > self.__money:
                        print("Недостаточно денег!")
                        return
                    self.__money -= cost_buy
                    self._quantity = quantity
                    balance = self.__money
                    print(f"""====Вы купили:====
    Количество семян: {quantity}
    Название культуры: '{self.crop}'
    Цена покупки: {cost_buy}
    Ваш остаток {balance} монет
    ====================""")
                    break
                else:
                    print("Можно купить от 1 до 5 штук")
            except ValueError:
                print("Пожалуйста, введите число")
    
    def grow_question(self):
        print("Че посадим?)")
    
    def grow_plants(self):  # Посадка растений
        if not self.crop:
            print("Сначала купите растения!")
            return
            
        print(f"Вы посадили '{self.crop}'")
        time.sleep(2)
        print(f"{self.crop} выросла и её можно:")
        print(f"""1. Оставить себе
2. Посадить по новой
3. Продать по {self.price} рублей за штуку""")
        print("Что выберешь ты")
        try:
            choice_int = int(input())
            if choice_int == 2:
                print(f"Отлично {self.crop} посажена повторно")
            elif choice_int == 3:
                self.sale_plants()
            elif choice_int == 1:
                self.__harvest[self.crop] += self._quantity
                print(f"Вы оставили '{self.crop}' себе и теперь у вас {self.__harvest}")
                print(f"количество растений {self._quantity}")
                print(f"Урожай сохранен на складе {self.__harvest}") 
            else:
                print("Неверный выбор")
        except ValueError:
            print("Пожалуйста, введите число от 1 до 3")
    
    def sale_plants(self):  # Продажа растений
        if not self.crop:
            print("Сначала купите растения!")
            return
            
        print("Введите количество штук (Макс: 10 штук)")
        while True:
            try:
                quantity = int(input())
                if 1 <= quantity <= 10:
                    if quantity > self._quantity:
                        print(f"У вас нет столько {self.crop}! Доступно: {self._quantity}")
                        continue
                        
                    self._profit = self.price * quantity
                    self.__money += self._profit
                    self._quantity -= quantity
                    
                    print(f"""==== Продано ====
    Количество культуры: '{self.crop}' - {quantity} шт.
    Прибыль с продаж: {self._profit}
    Ваш баланс {self.__money} рублей
    ====================""")
                    break
                else:
                    print("Можно продать от 1 до 10 штук")
            except ValueError:
                print("Пожалуйста, введите число")
    
    def play(self):
        while True:
            print("\n1. Купить растения")
            print("2. Посадить растения")
            print("3. Продать растения")
            print("4. Проверить прибыль")
            print("5. Выход")
            
            choice = input("Выберите действие (1-5): ")
            
            if choice == "1":
                self.buy_plants()
            elif choice == "2":
                self.grow_plants()
            elif choice == "3":
                self.sale_plants()
            elif choice == "4":
                print(f"Текущая прибыль: {self._profit}")
            elif choice == "5":
                    print("Игра завершена")
                    print(f"""Твоя статистика за {self.__day}
                          
Деньги: 

Всего: {self.__money}рублей

Заработано за игру: {self._profit}

Урожай: {self.__harvest}

Дней прожито: {self.__day}""")
                    time.sleep(60)
                    exit()
            else:
                print("Неверный ввод, попробуйте снова")


# Создаем экземпляр фермы и запускаем игру
farm = Farm()
farm.play()
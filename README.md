# Домашнє завдання

GOIT > Курс > Python Developer > Python core > Модуль 11. Магічні методи

# Додаток Телефонна книга

У цій роботі ми продовжили розвивати нашого віртуального асистента з CLI інтерфейсом.

https://github.com/SergDulin/goit_hw-09/blob/main/goit_hw-09.py 
https://github.com/SergDulin/goit_hw-09/blob/main/goit_hw-10.py - посилання на попереднє завдання.
Наш асистент вміє взаємодіяти з користувачем за допомогою командного рядка, отримуючи команди та аргументи, та виконуючи потрібні дії. Додамо поле для дня народження Birthday. Це поле не обов'язкове, але може бути тільки одне.
Додамо функціонал роботи з Birthday у клас Record, а саме функцію days_to_birthday, яка повертає кількість днів до наступного дня народження.
Додамо функціонал перевірки на правильність наведених значень для полів Phone, Birthday.
Додамо пагінацію (посторінкове виведення) для AddressBook для ситуацій, коли книга дуже велика і потрібно показати вміст частинами, а не все одразу. Реалізуємо це через створення ітератора за записами.

## Використання

Додаток підтримує наступні команди:
- `hello`: Виводить привітальне повідомлення.
- `add [name] [phone] [birthday]`: Додає контакт з вказаним іменем та номером телефону.
- `change [name] [old phone] [new phone]`: Змінює номер телефону існуючого контакту з вказаним іменем.
- `phone [name]`: Отримує список контактів, в яких є таке ім'я. Виводить контакт: `ім'я`, `телефон`, `день народження` та `кількість днів до наступного дня народження`.
- `show all`: Відображає всі контакти в телефонній книзі. Виводить контакт: `ім'я`, `телефон`, `день народження` та `кількість днів до наступного дня народження`. 
- `good`, `bye`, `close`, `exit`: Виходить з додатку.

## Опис роботи

Цей код реалізує простий зберігач контактів з можливістю додавання, зміни та отримання номерів телефонів контактів, а також виведення всіх контактів. Він також має базовий інтерфейс командного рядка для взаємодії з користувачем.

Ім'я контакту може бути с декілька слів, необхідно мінімум одно.
Телефонів може бути декілька, мінімум один.
День народження не обов’язкове поле.
При пошуку чи зміні телефону, можливо вводити ім'я любим регістром. Команда "show all" виводить імена з великої літери.
При пошуку телефону достатньо одного імені, команда "phone" виводить список контактів в яких є таке ім'я.

## Особливості роботи

AddressBook реалізує метод iterator, який повертає генератор за записами AddressBook і за одну ітерацію повертає представлення для N записів.
Клас Record приймає ще один додатковий (опціональний) аргумент класу Birthday
Клас Record реалізує метод days_to_birthday, який повертає кількість днів до наступного дня народження контакту, якщо день народження заданий.
setter та getter логіку для атрибутів value спадкоємців Field.
Перевірку на коректність веденого номера телефону setter для value класу Phone.
Перевірку на коректність веденого дня народження setter для value класу Birthday.

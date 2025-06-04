# # name = "Alise"
# # balanse = 1000
#
# # def create_account(name, **account_details):
# #     print(f'Создан счет для {name}')
# #     for detail, values in account_details.items():
# #         print(f'{detail}: {values}')
# #
# # create_account('Alise', initial_deposit=1000, account_type="сберегательный счет", tmtrtrmt='апатпатпа')
#
# # def create_account(name, *transaction):
# #     print(f'Создан счет для {name}')
# #     for transaction in transaction:
# #         print(f'Транзакция: {transaction}')
# #
# # create_account('Alise', "JGjdn", 'Dtre')
# # initial_deposit=1111
# #
# # def create_account(name):
# #     initial_deposit=1000
# #     print(f' Создан счет для {name} с балансом {initial_deposit}')
# #
# # create_account("Artem")
#
# # transactions = [100, 200, 0, 200, -100, 500]
# #
# # def apply_transactions(transactions):
# #     balance = 0
# #     for transaction in transactions:
# #         if transaction > 0:
# #             print(f'Пополнение на сумму: {transaction}')
# #         elif transaction < 0:
# #             print(f'Снятие на сумму: {transaction}')
# #         else:
# #             print(f'Операция не удалась')
# #         balance += transaction
# #     print(f'Итоговый балансе {balance}')
# #
# # apply_transactions(transactions)
#
# def reach_min_balance(initial_balance, min_balance):
#     while initial_balance < min_balance:
#         print(f'Текущий баланс {initial_balance} меньше минимальной суммы. Добавляем депозит 100')
#         initial_balance += 100
#     print(f'Достигнут минимальный баланс: {min_balance}')
#
# # reach_min_balance(50, 200)
#
# def check_transaction(transaction):
#     if transaction > 0:
#         print(f'Поплнение')
#     elif transaction < 0:
#         print(f'Списание')
#     else:
#         print('Транзакция не изменила баланс')
#
# # transaction = [100, 0, -400, 100]
# # for t in transaction:
# #     check_transaction(t)
#
# account_action = {'initial': 0, 'kredit': 1000, 'deposit': 50}
#
# def print_account_action(action):
#     for a, b in account_action.items():
#         print(f'Действие {a}, значение {b}')
#
# # print_account_action(account_action)
#
# def safe(balance, amount):
#     try:
#         if amount > balance:
#             raise ValueError('Сумма снятия больше доступного баланса')
#         balance -= amount
#         print(f'Снятие произошло успешно. Текущий баланс равен {balance}')
#     except ValueError as error:
#         print(error)
#
# safe(100, 10)

# def add(a, b):
#     return print (a + b)  # возвращает сумму
#
# resulit = add(2, 3)  # result = 5

# for i in range(10):
    # if i == 5:
    #     break
    # if i % 2 == 0:
    #     continue
    # print(i)
def sum (a,b):
    return a + b

print(sum(3, 4))

def test_sum():
    assert sum(3,4) == 7

def test_sum_fail():
    assert sum(3,4) != 8

def test_sum_fail2():
    assert sum(3,4) != 9

def test_sum_fail3():
    assert sum(3,4) != 100


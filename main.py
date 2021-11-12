import os # Підключаємо модуль для очистки нашого терміналу
import random # Підключаємо модуль для рандомного числа

# Константа кортежів виграшних комбінацій (масив кортежів)
WIN_COMB = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7))

# відображення поля
def draw_board(board):
   for i in range(1,4): # Цикил фор (перебираємо значення від 1 до 3) працює 3 ітерації
      print(' ', board.get(i * 3 - 2), '|', board.get(i * 3 - 1), '|', board.get(i * 3), ' ') # Алгоритм який дозволяэ нам вивести поле
      if i != 3: # Блок коду іф перевіряє щоб ай не дорівнювало 3 (для того щоб було лише 2 лініє на полі)
         print(' 𑁋 ' * 4) # Не баг, а фішка) Пайтон дозволяє нам множити строки (запис еквівалентний цьому "' 𑁋 𑁋 𑁋 𑁋'")

# Функція яка вводить в словарь Х або О у вказану гравцем позицію 
def take_input(player_token, board):
   while True: # Безкінечний цикл (закінчиться - прирветься коли ми успішно присвоємо Х або О в наш dictionary (словарь) 'board')
      draw_board(board) # Функція яка відображає гравцям поле 

                           # ↓↓↓↓↓ Конкатенація строк ↓↓↓↓↓
      player_answer = input('\nКуди поставити ' + player_token + ' ? ') # Створюємо змінну і присвоюємо їй рішення гравця "куди поставити Х або О"
      os.system('cls||clear') # Очищуємо наш термінал
      try: # Блок try дозволяє нам виконати дію яка може створити помилку і зупинити програму
         player_answer = int(player_answer) # Перетворюємо строку яку обрав гравець в число

      except: # Якщо виникає помилка в конвертаціі строки на число тоді ми заходимо в блок except і повідомляємо гравця
         print('Некоректний ввід. Ви впевненні, що ввели число?\nСпробуйте ще раз')
         continue # Оператор який починає цикл спочатку (повертає нас на початок циклу)

      if player_answer >= 1 and player_answer <= 9: # Перевірка чи гравець обрав число від 1 до 9
         if(board.get(player_answer) not in "XO"):  # Перевіряємо чи яке обрав гравець не зайняте Х або О
            board[player_answer] = player_token     # Присвоюємо Х або О по ключу (наш ключ це то число яке обрав гравець)
            break                                   # Завдяки оператору break виходимо з циклу - (пририваємо)
         else:
            print('Ця позиція вже зайнята')
      else: 
         print('Некоректний ввід. Введіть число від 1 до 9')

# Перевіряємо чи є у нас переможець 
def check_win(board):
   for comb in WIN_COMB: # Циклом фор перебираємо кортежі з масива кортежів
      if board[comb[0]] == board[comb[1]] == board[comb[2]]:# Перевірка комбінацій "Х == Х == Х" або "О == О == О" якщо є ми заходимо в блок іф
         print(board.get(comb[0]), ' переміг') # Виводимо в термінал переможця
         return True # Повертаємо значення "True" яке означає, що переможець є
   return False # Повертаємо значення "False" яке означає, що переможця немає

# Знаходимо число яке призведе до перемоги або зруйнує перемогу нашому супернику в залежності від "токену"
def win_number(token, board):
   for each in WIN_COMB: # Циклом фор перебираємо кортежі з масива кортежів
         if board[each[0]] == board[each[1]] == token: # Перевірка комбінацій "Х == Х == token" або "О == О == token"
            if(str(board.get(each[2])) not in "XO"):
               board[each[2]] = 'O'
               return True
         elif board[each[0]] == token == board[each[2]]: # Перевірка комбінацій "Х == token == Х" або "О == token == О"
            if(str(board.get(each[1])) not in "XO"):
               board[each[1]] = 'O'
               return True
         elif token == board[each[1]] == board[each[2]]: # Перевірка комбінацій "token == Х == Х" або "token == О == О"
            if(str(board.get(each[0])) not in "XO"):
               board[each[0]] = 'O'
               return True
   return False

# На штучний інтелект =)
def bot(board, level = 1):
   if level >= 2:
      if win_number('O', board): # Перевіряєсо чи є в наявності число для перемоги в самій функції якщо так = True | ні = False
         return

   if level > 2:
      if win_number('X', board): # Перевіряєсо чи є в наявності число для перемоги в самій функції якщо так = True | ні = False
         return

   while True:
      temp = random.randint(1,9) # Присвоюємо будь яке число від 1 до 9
      if(str(board.get(temp)) not in "XO"): # Перевірка чи вказаному числі немає Х або О
         board[temp] = 'O'
         break

# Початок гри
def start_game(board):
   counter = 0 # Лічильник для перевірки кількості фігур на карті
   win = False # Бульова змінна яка відповідає за те чи є у нас переможець
   bot_level = 0 # Змінна яка стримує весь потенціал нашого іі

   os.system('cls||clear') # Очищуємо наш термінал
   print("\n_________Гра в хрестики нолики_________\n")# Наш заголовок
   print(' 1 - для двох гравців ')
   print(" 2 - проти комп'ютера ")
   ag_who = input(' : ') # Присвоюємо вибір гравця (1 або 2)

   if ag_who != '1': # Перевіряємо вибір гравця чи бажа він грати проти комп'ютера
      print(''' Виберіть рівень складності 
   [1] - Легкий
   [2] - Середній
   [3] - Важкий ''')
      bot_level = input(' : ') # Присвоюємо вибір гравця (рівень важкості)
      os.system('cls||clear') # Очищуємо наш термінал
   
   while not win: # <-- = (win == False) цикл закінчиться коли ми знайдемо переможця або буде нічия

      if counter % 2 == 0: #Перевірка парності лічильника (якщо парний то ходить Х якщо ні то ходить О)
         take_input('X', board) # Функція яка вводить в поле (словарь) Х або О у вказану гравцем позицію 
      else:
         if ag_who == '1': # Перевіряємо чи гравець 'Боїться' нашого штучного інтелекту 1 <= боїться
            take_input('O', board) # Функція яка вводить в поле (словарь) Х або О у вказану гравцем позицію 
         else:
            bot(board, int(bot_level)) # Хід нашого звіра о_О

      counter += 1 # Після ходу гравця збільшуємо лічильник на 1 тобто додаємо до лічильника хід гравця

      if counter > 4: # Перевірка чи було 5 ходів (чи є 5 фігур на карті якщо так то ми заходимо в блок іф і перевіряємо чи є у нас переможець)
         win = check_win(board) # Перевіряємо чи є у нас переможець (результат перевірки 'True' or 'False' присвоюємо змінній 'win' )
      
      if counter == 9 and not win: # Перевіряємо чи поле заповнено повністю і чи є у нас переможець 
         print("Перемогла дружба") # (якщо поле заповнено і переможця немає ми заходимо в блок іф і оголошуємо нічию)
         break                     # Завдяки оператору break виходимо з циклу - (пририваємо)


def main():
   while True: # Безкінечний цикл (закінчиться при умові якщо гравець не схоче грати далі)

      board = {   # створюємо dictionary (словарь) з значеннями нашого поля [за замовчуванням поле пронумероване степеневими числами]
         1: '¹',  # (коли гравець обере поле по ключу тієї цифри ми замінемо її велью (степеневе число)
         2: '²',  # на Х або О в залежності від гравця)
         3: '³',
         4: '⁴',
         5: '⁵',
         6: '⁶',
         7: '⁷',
         8: '⁸',
         9: '⁹'
         }

      start_game(board) # Функція яка починає гру (Початок гри)
      draw_board(board) # Функція яка відображає поле
      play = input('\n Греємо далі? (Так/Ні) ') # Створюємо змінну і присвоюємо їй рішення гравця "Чи бажає він грати далі"

      # ↓↓↓ Перевіряємо чи гравець хоче грати далі 
      if play.upper() != 'ТАК': # (переводимо нашу відповідь у верхній регістр тому що гравець може вводити як звеликої так і з маленької букви)
         break # Завдяки оператору break виходимо з циклу - (пририваємо)

      board.clear() # Очищуємо наш dictionary (словарь) [стираємо наше поле] в наступній ітерації ми "створюємо" нове - чисте поле
         

main()
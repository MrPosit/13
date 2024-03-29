'''Создайте мини-приложение «Шахматная доска». 
На практическом занятие вы создали игры для шахматных фигур «Король», «Ладья». 
Дополните программу следующим действиями: 
Шахматный ферзь ходит по диагонали, горизонтали или вертикали. Даны две различные 
клетки шахматной доски, определите, может ли ферзь попасть с первой клетки на вторую 
одним ходом. 
Шахматный конь ходит буквой “Г” - на две клетки по вертикали в любом направлении 
и на одну клетку по горизонтали, или наоборот. Даны две различные клетки шахматной доски, 
определите, может ли конь попасть с первой клетки на вторую одним ходом. 
Обработайте все исключения, которые могут встретиться в программе.'''

class ChessBoard:
    def __init__(self):
        self.board = [[0]*8 for _ in range(8)]
        
    def is_valid_position(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8
        
    def can_queen_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        
        if abs(start_row - end_row) == abs(start_col - end_col):
            return True
        
        if start_row == end_row or start_col == end_col:
            return True
        
        return False
        
    def can_knight_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        
        return (row_diff == 1 and col_diff == 2) or (row_diff == 2 and col_diff == 1)

def main():
    board = ChessBoard()
    
    try:
        start = tuple(map(int, input("Введите координаты начальной клетки (строка столбец): ").split()))
        end = tuple(map(int, input("Введите координаты конечной клетки (строка столбец): ").split()))
        
        if not (board.is_valid_position(*start) and board.is_valid_position(*end)):
            raise ValueError("Координаты клеток должны быть в диапазоне от 1 до 8.")
        
        if board.can_queen_move(start, end):
            print("Ферзь может попасть на вторую клетку одним ходом.")
        else:
            print("Ферзь не может попасть на вторую клетку одним ходом.")
        
        if board.can_knight_move(start, end):
            print("Конь может попасть на вторую клетку одним ходом.")
        else:
            print("Конь не может попасть на вторую клетку одним ходом.")
            
    except ValueError as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    main()



'''Выполните следующие задание: 
Функция plus_two() выполняет одну простую задачу — выводит результат сложения 
переданного в нее числа 2 и значения переменной number. В переменную number должно быть 
передано число. Обработайте ситуацию, если в эту переменную переданы данные какого-то 
другого типа. В случае ошибки напечатайте в консоли сообщение «Ожидаемый тип данных 
— число!».
Запустите код и проверьте работу кода в консоли.
Подсказка:
Используйте конструкцию try/except.В процессе поиска решения попробуйте вывести в 
консоль сумму строки и числа, изучите сообщение об ошибке.В Python есть специальное 
исключение для ситуации, если тип переданного значения не соответствует ожиданиям. '''
def plus_two(number):
    try:
        result = 2 + number
        print('Результат сложения', result)

    except TypeError:
        print('Ожидаемый тип данных — число!')

plus_two(3)
plus_two("4")


'''Напишите программу, которая позволяет получить доступ к элементу массива, индекс 
которого выходит за границы, и обработаем соответствующее исключение'''
array = [1, 2, 3, 4, 5]

try:
    index = int(input("Введите индекс элемента массива: "))
    print("Элемент с индексом", index, ":", array[index])
except IndexError:
    print("Индекс выходит за границы массива.")
except ValueError:
    print("Введите целое число в качестве индекса.")


from random import randint

class field_2048:
  def __init__(self, size: int = 4):
    self.__size = size
    self.__game_field = [[0]*4 for i in range(4)]
    # self.__game_field = [
    #   [0, 1, 2, 3],
    #   [4, 5, 6, 7],
    #   [8, 9, 10, 11],
    #   [12, 13, 14, 15]
    # ]
    self.__game_field = [
      [0, 0, 0, 0],
      [0, 0, 0, 4],
      [0, 0, 0, 4],
      [4, 2, 2, 8],
    ]
    # s/elf.set_new_value()
    self.__num_of_free_cells = size * size
    

  @property
  def field(self):
    for row in self.__game_field:
      for cell in row:
        print(f'{cell} ', end='')
      print()
  
  def get_number_of_free_cells(self):
    num = 0
    for i in range(self.__size):
      for j in range(self.__size):
        if self.__game_field[i][j] == 0:
          num += 1
    self.__num_of_free_cells = num
    return self.__num_of_free_cells
  
  def get_new_value(self) -> int:
    a = randint(0, 3)
    if a == 3:
      return 4
    else:
      return 2
    
  def get_free_cell_number(self, num_of_free_cell: int):
    cell_idx = randint(0, num_of_free_cell-1)
    return cell_idx // self.__size, cell_idx % self.__size

  def get_coords_by_number(self, num: int):
    return num // self.__size, num % self.__size

  def get_number_by_coords(self, coords) -> int:
    return self.__size*coords[0] + coords[1]

  def set_new_value(self):
    num_of_free_cell = self.get_number_of_free_cells()
    if num_of_free_cell == 0:
      return
    cell_to_insert_value = randint(0, num_of_free_cell-1)
    i_free = 0
    i = 0
    j, k = 0, 0
    while i_free < cell_to_insert_value or i < self.__size ** 2 and self.__game_field[j][k] != 0:
      if self.__game_field[j][k] == 0:        
        i_free += 1
      i += 1
      j, k = self.get_coords_by_number(i)
    # print(f'{cell_to_insert_value=}')
    # print(f'{i=}')
    # print(f'{j = }, {k = }')
    self.__game_field[j][k] = self.get_new_value()

  def get_step_code(self, step: str) -> int:
    
    if step == 'up':
      return 0
    elif step == 'left':
      return 1
    elif step == 'down':
      return 2
    elif step == 'right':
      return 3
    else:
      return -1
    # match step:
    #   case 'up':
    #     return 0
    #   case 'left':
    #     return 1
    #   case 'down':
    #     return 2
    #   case 'right':
    #     return 3
    #   case _:
    #     return -1
      
  def do_line_processing(self, line) -> None:  
    i = 0
    first_not_zero_idx = -1
    state = 0 # 0 - find_firts_not_zero, 1 - find_second_not_zero. 2 - compare values.
    while i < self.__size:
      if state == 0 and line[i] != 0:
        first_not_zero_idx = i
        state = 1
      elif state == 1 and line[first_not_zero_idx] == line[i]:
        line[first_not_zero_idx] += line[i]
        line[i] = 0
        first_not_zero_idx += 1
        state = 1
      elif state == 1 and line[i] != 0:
        first_not_zero_idx = i
        state = 0
      i += 1
    return line
  
  def is_game_over(self):
    return self.get_number_of_free_cells() == 0
  
  def shift_line(self, line):
    zero_idx = -1
    no_zero_idx = -1
    state = 0 # 0 - поиск нулевого элемента. 1 - поиск не нулевого элемента
    i = 0
    while i < self.__size:
      if state == 0 and line[i] == 0:
        zero_idx = i
        state = 1
      elif state == 1 and line[i] != 0:
        line[zero_idx] = line[i]
        line[i] = 0
        zero_idx += 1        
      i += 1
    return line 
    
  def do_step(self, step: str):
    step_code = self.get_step_code(step)
    # print(f'{step_code = }')
    if step_code == 0:
      for i in range(self.__size):
          line = []
          for j in range(self.__size):
            line.append(self.__game_field[j][i])
          self.do_line_processing(line)
          self.shift_line(line)
          for j in range(self.__size):
            self.__game_field[j][i] = line[j]
    elif step_code == 1:
      for i in range(self.__size):
        line = self.__game_field[i][:]
        self.do_line_processing(line)
        self.shift_line(line)
        for j in range(self.__size):
          self.__game_field[i][j] = line[j]
    elif step_code == 2:
      for i in range(self.__size):
        line = []
        for j in range(self.__size):
          line.append(self.__game_field[j][i])
        line.reverse()
        self.do_line_processing(line)
        self.shift_line(line)
        for j in range(self.__size):
          self.__game_field[self.__size - j - 1][i] = line[j]
    elif step_code == 3:
      for i in range(self.__size):
        line = self.__game_field[i][:]
        line.reverse()
        self.do_line_processing(line)
        self.shift_line(line)
        for j in range(self.__size):
          self.__game_field[i][self.__size - j - 1] = line[j]
    else:
      print('Ошибка, неизвестная команда.')
    
    if not self.is_game_over():
      self.set_new_value()
    else:
      print('game over')
    # match step_code:
    #   case 0:
    #     for i in range(self.__size):
    #       cur_column = []
    #       for j in range(self.__size):
    #         cur_column.append(self.__game_field[j][i])
    #   case 1:
    #     for i in range(self.__size):
    #       cur_column = self.__game_field[i][:]
    #   case 2:
    #     for i in range(self.__size):
    #       cur_column = []
    #       for j in range(self.__size):
    #         cur_column.append(self.__game_field[j][i])
    #       cur_column.reverse()
    #   case 3:
    #     for i in range(self.__size):
    #       cur_column = self.__game_field[i][:]
    #       cur_column.reverse()
  
if __name__ == '__main__':
  game = field_2048()

  # Отладка хода игрока.
  game.field
  game.do_step('right')
  print()
  game.field

  # processed_line = game.do_line_processing([2, 2, 2, 2]) # [2, 4, 2, 2]
  # print(f'{processed_line = }')
  # shift_line = game.shift_line([2, 2, 2, 2])
  # print(f'{shift_line = }')


  # Отладка появления нового значения на игровом поле.
  # for i in range(18):
  #   game.set_new_value()
  #   game.field
  #   print(game.get_number_of_free_cells())
from func_2048 import field_2048

def decimal_to_4_richn(d: int) -> str:
  res = ''
  while d > 0:
    res += str(d % 4)
    d //= 4
  # return res[::-1]
  str_res = ''
  for i in res[::-1]:
    str_res += str(i)
  return str_res

# print(decimal_to_4_richn(8))

game = field_2048()

def line_check(size: int = 4):
  for i in range(256):
    line = decimal_to_4_richn(i).rjust(4, '0')
    line_lst = [int(line[0]), int(line[1]), int(line[2]), int(line[3])]
    calculated_line = game.do_line_processing(line_lst)
    shifted_line = game.shift_line(calculated_line.copy())
    print(str(i).rjust(3), line, ' ', calculated_line, ' ', shifted_line)

line_check()
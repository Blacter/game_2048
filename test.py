from func_2048 import field_2048

def decimal_to_4_richn(d: int) -> str:
  res = ''
  while d > 0:
    res += str(d % 4)
    d //= 4
  # return res[::-1]
  str_res = ''
  for i in res:
    str_res += str(i)
  return str_res

game = field_2048()

def line_check(size: int = 4):
  for i in range(256):
    line = decimal_to_4_richn(i).rjust(4, '0')
    line_lst = [int(line[0]), int(line[1]), int(line[2]), int(line[3])]
    calculated_line = game.do_line_processing(line_lst)
    print(line, ' ', calculated_line)

line_check()


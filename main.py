import func_2048 as f

game = f.field_2048()

game.field
user_input = input('> ')

while user_input != 'exit':  
  game.do_step(user_input)
  game.field
  user_input = input('> ')
  
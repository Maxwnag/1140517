import random
min = 1
max = 100
random=random.randint(min,max)
print('=====遊戲開始=====\n')
while True:
  input_number = int(input(f"請輸入數字({min}~{max}):"))
  if( input_number == random):
   print(f"YOU WIN_The number is : { input_number }")
   break
  elif( input_number < random):
   print(f"{input_number}~{random}")
  elif( input_number > random):
   print(f"{random}~{input_number}")
print("See You Next Time")

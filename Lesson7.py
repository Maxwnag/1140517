import random
min = 1
max = 10
random=random.randint(min,max)
print('=====遊戲開始=====\n')
while True:
  input_number = int(input(f"請輸入數字({min}~{max}):"))
  if( input_number == random):
   print(f"YOU WIN_The number is : { input_number }")
   break
  elif( input_number < random):
   print(f"{input_number}~{random}")
  else:
   print("猜錯了，再大一點")
print("See You Next Time")
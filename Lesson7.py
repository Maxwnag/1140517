import random
def play_game():
  min = 1
  max = 30
  count = 0
  target = random.randint(1, 100)
  print("===============猜數字遊戲=================:\n")
  while(True):
     count += 1
     keyin = int(input("猜數字範圍{0}~{1}:".format(min, max)))
     if(keyin >=min and keyin <= max):
         if(keyin == target):
             print("賓果!猜對了, 答案是:", target)
             print("您猜了",count,"次")
             break
         elif (keyin > target):
            max = keyin
            print("再小一點")
         elif (keyin < target):
            min = keyin
            print("再大一點")
         print("您猜了",count,"次\n")
     else:
        print("請輸入提示範圍內的數字")
while True :
 play_game()
 again = input("play again(y,n):")
 if (again == 'y'):
    print('try again')
 if (again == 'n'):
    break
    print("game over")
 elif (again != 'y' or 'n'):
    print('please input y or n')
    
 
  

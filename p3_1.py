# p3_1.py
"""---第一个小游戏---"""

temp = 0
guess = 0
n = 0

while (guess != 8) and (n < 3):
     temp = input("Retry:")
     guess = int(temp)
     n = n + 1

     if guess == 8:
          print("Right!")
          print("Congratulations!")
     else:
          if guess >8:
               print("大了！")
          else:
               print("小了！")
               
     

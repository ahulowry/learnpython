# **Python 作业1：设计用户名输入接口**
===

## **作业要求**	

## **流程图**
图片:![]()

	
## **代码**
``` Python
#! /usr/bin/env python3
import sys
import os

username = 'alex'
password = 'alex123'
locked = 1

retry_counter = 0

#handle the username and passwd empty issue
while retry_counter < 3:
        user = input('Username:')
        if len(user) == 0:
                print ("Username cannot be empty!")
                continue
               
        passwd = input('Password:')
        if len(passwd) == 0 :
                print ("Password cannot be empty!")
                continue

        

#going to the loging verification part


#reading blacklist
               
        f = open('blacklist.txt','r')
        for line in f.readlines():
             # 使用line.replace('\n','') 替换换行符
             if line.replace('\n','') == user:
                  locked = 0
                  print ('Your username is locked')
                  sys.exit()
             else:
                  continue
        f.close()

        if user == username and passwd == password:       #means passed the verfication
             sys.exit ('Welcome %s login to our system!'%user)

        else:
             retry_counter += 1
             print ('Wrong username or password, you have %s more chances!'% (3-retry_counter))

             if retry_counter == 3:
                  f = open('blacklist.txt','a')
                  f.write('\n')
                  f.writelines(user)
                  f.close()
             else:
                  continue

```


## **关键语法**

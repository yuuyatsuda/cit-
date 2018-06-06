
# coding: utf-8

# In[81]:


import random

rand_num=0

while rand_num != 4:
  rand_num = random.randint(1, 20)

  if rand_num%15== 0:
    print("Fizz Buzz")
  elif rand_num%3 == 0:
    print ("Fizz")
  elif rand_num%5 == 0:
    print("Buzz")

  else:
    print(rand_num)


# In[4]:


s = 0
for x in [1, 2, 3, 4]:
  s = s + x

s


# In[19]:


myList = [5349, 5478, 5344, 4644, 4968, 6259]
a=2
for val in myList:
 val=a*val   #リスト内の値に２をかけるだけのモジュール
 print(val)


# In[21]:


from statistics import * #リスト内の合計を求めるモジュール

print(sum(      myList     ))


# In[22]:


#問題 次のプログラムの動作を説明せよ。　Ans.平均を求めるプログラム
myAvg = 0.
for val in myList:
  myAvg += val

myAvg /= len(myList)
print(myAvg)


# In[24]:


myAvg=0
#myAvg=myAvg+1000とする代わりに
myAvg += 1000#としても同じである
myAvg


# In[25]:


from statistics import *　#平均を求めるモジュール

print(mean(     myList      ))


# In[26]:


myAvg = 0.
print(myAvg)
for val in myList:
  myAvg += val
print(myAvg)

myAvg /= len(myList)
print(myAvg)


# In[27]:


mean(myList)


# In[28]:


myDic = {'aomori': 5349, 'akita': 4644, 'sendai': 5344, 'Yamagata': 4968, 'fukushima': 6259, 'morioka': 5478}#key1だけを表示する

for key in myDic:
  print(key)


# In[34]:


for key in myDic:
  print(myDic[key])


# In[47]:


#上のコードを使って，myDicの値の平均を求めよ。
s=0
for x in myDic:  
 s +=myDic[x]

s=s/len(myDic)
print(s)


# In[54]:


print(sum(myDic.values()))#()が大事！！


# In[67]:


#問３
a = 4
b = 4

if a > b:
  print('大きい')  
else: 
    print("hello")


# In[69]:


#問１
a = 4
b = 2

if a > b:
  print('大きい')  

print("hello")


# In[76]:


for x in range(10):#breakを使うと　繰り返しを中断
 if x == 3:
    break
 print(x)


# In[78]:


for x in range(10):#continueを使うと　繰り返しを一度とめて次の数値から続行
 if x == 3:
    continue
 print(x)


# In[79]:


6%3


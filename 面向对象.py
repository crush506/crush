#!/usr/bin/env python
# coding: utf-8

# In[9]:


class BMI:
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
    def say_hello(self):
        self.shuchu=self.weight/(self.height*self.height)
        print("{n}的BMI值为{m}".format(n=self.name,m=self.shuchu))
        m = self.shuchu
        if m < 18.5 : 
            print ("偏瘦")
        elif m < 24 :
            print ("正常")
        elif m < 30 :
            print ("偏胖")
        elif m > 30:
            print ("肥胖")
   


# In[12]:


zhaosi = BMI("zhaosi","18",70,1.75)


# In[13]:


zhaosi.say_hello()


# In[ ]:





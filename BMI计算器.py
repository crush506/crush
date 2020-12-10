#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter
tk = tkinter.Tk()
tk.title("BMI计算器")
tk.geometry("400x400")

Bmi1 = tkinter.StringVar()
Bmi2 = tkinter.StringVar()

label_height = tkinter.Label(tk,text = "身高")
label_height.place(x = 10,y = 10,width = 80,height = 40)
entry_height = tkinter.Entry(tk,textvariable = tkinter.StringVar())
entry_height.place(x = 90,y = 10,width = 80,height = 40)
label_m = tkinter.Label(tk,text = "m")
label_m.place(x = 170,y = 10,width = 40,height = 40)
label_weight = tkinter.Label(tk,text = "体重")
label_weight.place(x = 10,y = 60,width = 80,height = 40)
entry_weight = tkinter.Entry(tk,textvariable = tkinter.StringVar())
entry_weight.place(x = 90,y = 60,width = 80,height = 40)
label_kg = tkinter.Label(tk,text = "kg")
label_kg.place(x = 170,y = 60,width = 40,height = 40)

def bmi():
    bmi_set = round(float(entry_weight.get())/(float(entry_height.get())*float(entry_height.get())),2)
    if bmi_set < 18.5:
        result = ("您的BMI为：",bmi_set)
        zhuangtai = ("偏瘦")
    elif 18.5 <= bmi_set <= 24:
        result = ("您的BMI为：",bmi_set)
        zhuangtai = ("正常")
    elif 24 <= bmi_set <= 30:
        result = ("您的BMI为：",bmi_set)
        zhuangtai= ("偏胖")
    else:
        result = ("您的BMI为：",bmi_set)
        abc = ("肥胖")
    Bmi1.set(result)
    Bmi2.set(zhuangtai)

button_bmi = tkinter.Button(tk,text = "BMI",command = bmi)
button_bmi.place(x = 50,y = 110,width = 300,height = 40)
entry_bmi1=tkinter.Entry(tk,textvariable = Bmi1)
entry_bmi1.place(x = 30,y = 160,width = 340,height = 50)
entry_bmi2=tkinter.Entry(tk,textvariable = Bmi2)
entry_bmi2.place(x = 30,y = 210,width = 340,height = 50)

tkinter.mainloop()


# In[ ]:





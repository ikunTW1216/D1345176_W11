from tkinter import *

a = 0
def count(type):
    global a
    
    if type == 'equal':
        a = eval(a) #計算的函式
        num.set(a)
        a = 0
    
    elif type == 'empty':
        a = 0
        num.set(0)
    
    else:
        if a != 0:
            a = f'{a}{type}'
        else:
            a = f'{type}'
        num.set(a)


if __name__ == '__main__':
    window = Tk()
    window.title('計算機')
    window.geometry('425x480+500+80')
    num  = StringVar() #綁定Label的textvariable，讓他可以自動更新顯示
    num.set(0)         #g設定StrinVar的值

    #計算介面
    lab = Label(window, width=20, height=2,
                relief=SUNKEN,
                textvariable=num,
                bg='#fff',
                justify=CENTER,
                font='Arial 20 bold',
                cursor='watch')
    lab.grid(row=0, column=0, columnspan=20, sticky=NSEW, padx=5, pady=3)
    
    #數字鍵
    btn_1 = Button(window, width=5, height=2,
                    text='1',
                    foreground='#000000',
                    font='Arial 20 bold',
                    command=lambda: count(1))
    btn_1.grid(row=1, column=0, sticky=W, padx=5, pady=3)
    
    btn_2 = Button(window, width=5, height=2,
                    text='2',
                    foreground='#000000',
                    font='Arial 20 bold',
                    command=lambda: count(2))
    btn_2.grid(row=1, column=1, sticky=W, padx=5, pady=3)
    
    btn_3 = Button(window, width=5, height=2,
                    text='3',
                    foreground='#000000',
                    font='Arial 20 bold',
                    command=lambda: count(3))
    btn_3.grid(row=1, column=2, sticky=W, padx=5, pady=3)
    
    btn_4 = Button(window, width=5, height=2,
                    text='/',
                    foreground='#000000',
                    font='Arial 20 bold',
                    command=lambda: count('/'))
    btn_4.grid(row=1, column=3, sticky=W, padx=5, pady=3)
    
    btn_5 = Button(window, width=5, height=2,
                    text='4',
                    foreground='#000000',
                    font='Arial 20 bold',
                    command=lambda: count(4))
    btn_5.grid(row=2, column=0, sticky=W, padx=5, pady=3)
    
    btn_6 = Button(window, width=5, height=2,
                    text='5',
                    foreground='#000000',
                    font='Arial 20 bold',
                    command=lambda: count(5))
    btn_6.grid(row=2, column=1, sticky=W, padx=5, pady=3)
    
    btn_7 = Button(window, width=5, height=2,
                    text='6',
                    foreground='#000000',
                    font='Arial 20 bold',
                    command=lambda: count(6))
    btn_7.grid(row=2, column=2, sticky=W, padx=5, pady=3)
    
    btn_8 = Button(window, width=5, height=2,
                    text='*',
                    foreground='#000000',
                    font='Arial 20 bold',
                    command=lambda: count('*'))
    btn_8.grid(row=2, column=3, sticky=W, padx=5, pady=3)
    
    btn_9 = Button(window, width=5, height=2,
                    text='7',
                    foreground='#000000',
                    font='Arial 20 bold',
                    command=lambda: count(7))
    btn_9.grid(row=3, column=0, sticky=W, padx=5, pady=3)
    
    btn_10 = Button(window, width=5, height=2,
                    text='8',
                    foreground='#000000',
                    font='Arial 20 bold',
                    command=lambda: count(8))
    btn_10.grid(row=3, column=1, sticky=W, padx=5, pady=3)
    
    btn_11 = Button(window, width=5, height=2,
                    text='9',
                    foreground='#000000',
                    font='Arial 20 bold',
                    command=lambda: count(9))
    btn_11.grid(row=3, column=2, sticky=W, padx=5, pady=3)
    
    btn_12 = Button(window, width=5, height=2,
                    text='-',
                    foreground='#000000',
                    font='Arial 20 bold',
                    command=lambda: count('-'))
    btn_12.grid(row=3, column=3, sticky=W, padx=5, pady=3)
    
    btn_13 = Button(window, width=5, height=2,
                    text='C',
                    foreground='#000000',
                    font='Arial 20 bold',
                    command=lambda: count('empty'))
    btn_13.grid(row=4, column=0, sticky=W, padx=5, pady=3)
    
    btn_14 = Button(window, width=5, height=2,
                    text='0',
                    foreground='#000000',
                    font='Arial 20 bold',
                    command=lambda: count(0))
    btn_14.grid(row=4, column=1, sticky=W, padx=5, pady=3)
    
    btn_15 = Button(window, width=5, height=2,
                    text='=',
                    foreground='#000000',
                    font='Arial 20 bold',
                    command=lambda: count('equal'))
    btn_15.grid(row=4, column=2, sticky=W, padx=5, pady=3)
    
    btn_16 = Button(window, width=5, height=2,
                    text='+',
                    foreground='#000000',
                    font='Arial 20 bold',
                    command=lambda: count('+'))
    btn_16.grid(row=4, column=3, sticky=W, padx=5, pady=3)
    
    window.mainloop()
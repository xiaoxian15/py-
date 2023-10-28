from tkinter import *
# 创建一个根窗口
app = Tk()

# 头标签
app.title('小仙')

# 创建组件
op1 = Entry(app)
op2 = Entry(app)
# 将组件显示:pack,grid
# 方法一 包
# op1.pack()
# op2.pack(fill=BOTH)
# 格子
op1.grid(row=0, column=0)
op2.grid(row=0, column=1)


app.geometry('500x500+200+200')
# 保持窗口
mainloop()

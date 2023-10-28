from tkinter import *
# 正则表达式
import re

# 构建方法
# 正则表达式
# 需要按照正常数字排序比较
# ?一次或零次 +一次或者多次 * 零次或多次
# '^[+-]?[\d]+[.]?[\d]*$'
def input_correct():
    reg='^[+-]?[\d]+[.]?[\d]*$'
    a1=re.match(reg , op1.get())
    a2=re.match(reg , op2.get())
    return a1 and a2

def cmd_add(ops):
    is_value=input_correct()
    if(is_value):
        op1_value=float(op1.get())
        op2_value=float(op2.get())
        if(ops=='+'):
            value=round(op1_value+op2_value,2)
        elif(ops=='-'):
            value=round(op1_value-op2_value,2)
        elif(ops=='*'):
            value=round(op1_value*op2_value,2)
        elif(ops=='/'):
            value=round(op1_value/op2_value,2)
        elif(ops=='%'):
            value=round(op1_value%op2_value,2)
        elif(ops=='//'):
            value=round(op1_value//op2_value,2)
        elif(ops=='**'):
            value=round(op1_value**op2_value,2)
        res_var.set(value)
    else:
        print('请输入正确操作数')
        res_var.set('请输入正确操作数')

def clear():
    op1.delete(0,END)
    op2.delete(0,END)
    op_two.delete(0,END)
def calc_art():
    ex=op_two.get()
    # [\d]为数字
    mb='[\d]*[a-zA-Z]+'
    if(re.match(mb,ex)):
        res_str.set('输入不合法')
    else:
        # python自带函数eval可以用与计算 
        res=eval(ex)
        res_str.set(res)
    
        
# 接口
root = Tk()
root.title('小仙')

#  添加菜单
menubar=Menu(root)
menu1=Menu(menubar)
menubar.add_cascade(label='模式',menu=menu1)
menu1.add_command(label='普通',command=lambda: app.tkraise())#tkraise()作用上升至最上面
menu1.add_command(label='文艺',command=lambda: app2.tkraise())
root.config(menu=menubar)

# 设置第二套
app2=Frame(root)
app2.grid(row=0,column=0,sticky='news')
# 添加组件
op_two=Entry(app2)
btn_art=Button(app2,text='计算',command=lambda: calc_art())
clr_art=Button(app2,text='Clear',command=lambda: clear())
# 可变字符
res_str=StringVar()
res_str.set('Show new')
label_art=Label(app2,textvariable=res_str,pady=10)
# 显示
op_two.pack(fill=BOTH)
btn_art.pack(fill=BOTH)
clr_art.pack(fill=BOTH)
label_art.pack(fill=BOTH)


# 设置第一套 等同于一块空白画布
app=Frame(root)
app.grid(row=0,column=0,sticky='news')

# 组件
# 开头
la1=Label(app,text='输入1')
la2=Label(app,text='输入2')
# 输入栏
op1=Entry(app)
op2=Entry(app)
# 按键
btn_add=Button(app,text='+',padx=30,pady=10,command=lambda: cmd_add('+'))
btn_sub=Button(app,text='-',padx=30,pady=10,command=lambda: cmd_add('-'))
btn_mul=Button(app,text='*',padx=30,pady=10,command=lambda: cmd_add('*'))
btn_div=Button(app,text='/',padx=30,pady=10,command=lambda: cmd_add('/'))
btn_mod=Button(app,text='%',padx=30,pady=10,command=lambda: cmd_add('%'))
btn_flo=Button(app,text='//',padx=30,pady=10,command=lambda: cmd_add('//'))
btn_exp=Button(app,text='**',padx=30,pady=10,command=lambda: cmd_add('**'))
btn_clr=Button(app,text='Clear',padx=30,pady=10,command=clear)
# 结果
# 设置可变字符
res_var=StringVar()
res_var.set('Show result')
result=Label(app,textvariable=res_var,pady=10)

# 显示 columnspan=4合并四个格 sticky='WE'左右自动填满
la1.grid(row=0,column=0,sticky='WE')
la2.grid(row=1,column=0,sticky='WE')
op1.grid(row=0,column=1,columnspan=4,sticky='WE')
op2.grid(row=1,column=1,columnspan=4,sticky='WE')
btn_add.grid(row=2,column=0,sticky='WE')
btn_sub.grid(row=2,column=1,sticky='WE')
btn_mul.grid(row=2,column=2,sticky='WE')
btn_div.grid(row=2,column=3,sticky='WE')
btn_mod.grid(row=3,column=0,sticky='WE')
btn_flo.grid(row=3,column=1,sticky='WE')
btn_exp.grid(row=3,column=2,sticky='WE')
btn_clr.grid(row=3,column=3,sticky='WE')
result.grid(row=4,column=0,columnspan=4,sticky='WE')

# 保持显示
mainloop()
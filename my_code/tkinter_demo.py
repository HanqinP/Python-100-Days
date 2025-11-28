import tkinter
import tkinter.messagebox

flag = True

def change_label_text():
    global flag
    flag = not flag
    color, msg = ('red', 'Hello, world!') \
        if flag else ('blue', 'Goodbye, world!')
    label.config(text=msg, fg=color)
   

def confirm_to_quit():
    if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
        top.quit()

# 创建顶层窗口
top = tkinter.Tk()
# 设置窗口大小
top.geometry("240x160")
# 标题
top.title('Game')

label = tkinter.Label(top, text = 'Hello, world!', font='Arial -32', fg='red')
label.pack(expand=1)
panel = tkinter.Frame(top)

button1 = tkinter.Button(panel, text='edit', command=change_label_text)
button1.pack(side='left')

button2 = tkinter.Button(panel, text='quit', command=confirm_to_quit)
button2.pack(side='right')

panel.pack(side='bottom')
#开启主事件循环
top.mainloop()


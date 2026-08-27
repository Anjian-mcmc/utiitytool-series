'登录库'
from tkinter import *
from tkinter import messagebox as msgbx
__all__ = ['LoginFrame','LoginTk']
class LoginFrame(Toplevel):
    '登录的副窗口类'
    def __init__(self,parent,title = None,model = True,passwords = [],names = [],nameVar = None,passVar = None):
        Toplevel.__init__(self,parent)
        self.transient(parent)
        if title:
            self.title(title)
        self.passwords = list(passwords);self.names = list(names)
        self.parent = parent
        self.result = None
        self.nameVar = nameVar
        self.passVar = passVar
        frame = Frame(self)
        self.initial_focus = self.init_widgets(frame)
        frame.pack(pady = 5,padx = 5)
        self.init_buttons()
        if model:
            self.grab_set()
        if not self.initial_focus:
            self.initial = self
        self.protocol('WM_DELETE_WINDOW',self.cancel_click)
        self.geometry('+%d+%d'%(parent.winfo_rootx() + 50,parent.winfo_rooty() + 50))
        self.initial_focus.focus_set()
        self.wait_window(self)
    def init_widgets(self,master):
        Label(master,text = '用户名:',font = 12,width = 10).grid(row = 1,column = 0)
        self.name_entry = Entry(master,font = 16,textvariable = self.nameVar)
        self.name_entry.grid(row = 1,column = 1)
        Label(master,text = '密码:',font = 12,width = 10).grid(row = 2,column = 0)
        self.pass_entry = Entry(master,font = 16,textvariable = self.passVar)
        self.pass_entry.grid(row = 2,column = 1)
        return self.name_entry
    def init_buttons(self):
        f = Frame(self)
        Button(f,text = '登录',width = 10,command = self.ok_click,default = ACTIVE).pack(side = LEFT,padx = 5,pady = 5)
        Button(f,text = '取消',width = 10,command = self.cancel_click).pack(side = LEFT,padx = 5,pady = 5)
        self.bind('<Return>',self.ok_click)
        self.bind('<Escape>',self.ok_click)
        f.pack()
    def validate(self):
        getname = self.name_entry.get()
        getpass = self.pass_entry.get()
        if getname in self.names:
            if getpass in self.passwords:
                msgbx.showinfo('登录成功!','登录成功')
                return True
            else:
                msgbx.showerror(message = '密码错误!')
                return False
        else:
            msgbx.showerror(message = '用户名错误!')
            return False
    def ok_click(self,event = None):
        if not self.validate():
            self.initial_focus.set()
            return
        self.withdraw()
        self.update_idletasks()
        self.parent.deiconify()
        self.destroy()
        self.parent.focus_set()
    def cancel_click(self,event = None):
        self.parent.focus_set()
        self.destroy()

def LoginTk(names = [],passwords = [],model = True,parent = None,title = None):
    '集成调用窗口类'
    if parent:
        LoginFrame(parent,title,model,passwords,names,name,password)
        name = StringVar()
        password = StringVar()
        parent.mainloop()
    else:
        r = Tk()
        r.title(title)
        name = StringVar()
        password = StringVar()
        LoginFrame(r,title,model,passwords,names,name,password)
        r.mainloop()
    return name.get(),password.get()

if __name__ == '__main__':
    LoginTk(['1'],['1'],True,title = 'sb')

        

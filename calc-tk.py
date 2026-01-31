from tkinter import *
from math import sqrt

class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.title("现代计算器")
        self.root.configure(bg='#1E272E')  # 更深的背景色
        self.root.resizable(False, False)
        
        # 创建主框架，增加内边距和圆角效果
        self.main_frame = Frame(
            self.root,
            bg='#1E272E',
            padx=15,
            pady=15,
        )
        self.main_frame.pack(expand=True, fill='both')
        
        self.f_num = 0
        self.operation = None
        self.setup_ui(self.main_frame)
        
    def setup_ui(self, frame):
        # 创建显示框容器
        display_frame = Frame(frame, bg='#1E272E', pady=10)
        display_frame.grid(row=0, column=0, columnspan=4, sticky='nsew')
        
        # 创建显示框
        self.display = Entry(
            display_frame,
            bd=0,
            bg='#2C3E50',
            fg='#ECF0F1',
            justify=RIGHT,
            font=("Helvetica", 32, "bold"),
            insertbackground='#ECF0F1',
            relief=FLAT
        )
        self.display.pack(fill='both', padx=10, pady=5, ipady=15)
        
        # 定义按钮布局和样式
        button_layout = [
            ('C', 1, 0, '#FF3B30', '#CC2E26'),  # 红色清除键
            ('±', 1, 1, '#FF9500', '#CC7700'),  # 橙色功能键
            ('√', 1, 2, '#FF9500', '#CC7700'),  # 开方
            ('÷', 1, 3, '#FF9500', '#CC7700'),  # 更改除号显示
            
            ('7', 2, 0, '#2C3E50', '#1E2A3B'),
            ('8', 2, 1, '#2C3E50', '#1E2A3B'),
            ('9', 2, 2, '#2C3E50', '#1E2A3B'),
            ('×', 2, 3, '#FF9500', '#CC7700'),  # 更改乘号显示
            
            ('4', 3, 0, '#2C3E50', '#1E2A3B'),
            ('5', 3, 1, '#2C3E50', '#1E2A3B'),
            ('6', 3, 2, '#2C3E50', '#1E2A3B'),
            ('−', 3, 3, '#FF9500', '#CC7700'),  # 更改减号显示
            
            ('1', 4, 0, '#2C3E50', '#1E2A3B'),
            ('2', 4, 1, '#2C3E50', '#1E2A3B'),
            ('3', 4, 2, '#2C3E50', '#1E2A3B'),
            ('+', 4, 3, '#FF9500', '#CC7700'),
            
            ('0', 5, 0, '#2C3E50', '#1E2A3B', 2),
            ('.', 5, 2, '#2C3E50', '#1E2A3B'),
            ('=', 5, 3, '#007AFF', '#0062CC'),  # 蓝色等号
        ]
        
        # 创建按钮样式
        button_style = {
            'font': ('Helvetica', 16, 'bold'),
            'bd': 0,
            'padx': 25,
            'pady': 15,
            'relief': FLAT,
            'fg': '#FFFFFF'
        }
        
        # 创建数字和运算符按钮
        for button in button_layout:
            text, row, col, color, active_color, *span = button
            columnspan = span[0] if span else 1
            
            # 创建按钮容器frame来实现内边距效果
            btn_frame = Frame(frame, bg='#1E272E', padx=3, pady=3)
            btn_frame.grid(row=row, column=col, columnspan=columnspan, sticky='nsew')
            
            # 创建按钮
            btn = Button(
                btn_frame,
                text=text,
                bg=color,
                activebackground=active_color,
                activeforeground='#FFFFFF',
                **button_style
            )
            btn.pack(fill='both', expand=True)
            
            # 绑定悬停效果
            btn.bind('<Enter>', lambda e, b=btn, c=active_color: b.configure(bg=c))
            btn.bind('<Leave>', lambda e, b=btn, c=color: b.configure(bg=c))
            
            # 绑定命令
            if text == '=':
                btn.configure(command=self.calculate)
            elif text == 'C':
                btn.configure(command=self.clear)
            elif text == '√':
                btn.configure(command=self.sqrt)
            elif text == '±':
                btn.configure(command=self.toggle_sign)
            elif text == '.':
                btn.configure(command=self.add_decimal)
            elif text in '+-×÷':  # 更新运算符
                op = {'×': '*', '÷': '/'}.get(text, text)
                btn.configure(command=lambda x=op: self.set_operation(x))
            else:
                btn.configure(command=lambda x=text: self.append_number(x))
        
        # 使所有列等宽
        for i in range(4):
            frame.grid_columnconfigure(i, weight=1)
        
        # 使所有行等高
        for i in range(6):
            frame.grid_rowconfigure(i, weight=1)
    
    def add_decimal(self):
        current = self.display.get()
        if not current:
            self.display.insert(0, "0.")
        elif '.' not in current:
            self.display.insert(END, ".")
            
    def toggle_sign(self):
        try:
            current = self.display.get()
            if current:
                value = float(current)
                self.display.delete(0, END)
                self.display.insert(0, str(-value))
        except ValueError:
            pass
    
    def append_number(self, number):
        current = self.display.get()
        self.display.delete(0, END)
        self.display.insert(0, current + str(number))
    
    def clear(self):
        self.display.delete(0, END)
        self.f_num = 0
        self.operation = None
    
    def set_operation(self, op):
        try:
            current = self.display.get()
            if current:
                self.f_num = float(current)
                self.operation = op
                self.display.delete(0, END)
            elif op == '-':
                self.display.insert(0, "-")
        except ValueError:
            self.clear()
    
    def sqrt(self):
        try:
            num = float(self.display.get())
            if num < 0:
                self.display.delete(0, END)
                self.display.insert(0, "无效输入")
                return
            self.display.delete(0, END)
            result = sqrt(num)
            if result.is_integer():
                self.display.insert(0, str(int(result)))
            else:
                self.display.insert(0, str(result))
        except ValueError:
            self.clear()
    
    def calculate(self):
        if not self.operation:
            return
            
        try:
            second_number = self.display.get()
            self.display.delete(0, END)
            
            if not second_number or second_number == '-':
                second_number = '0'
            
            result = None
            if self.operation == '+':
                result = self.f_num + float(second_number)
            elif self.operation == '-':
                result = self.f_num - float(second_number)
            elif self.operation == '*':
                if not second_number:
                    result = self.f_num ** 2
                else:
                    result = self.f_num * float(second_number)
            elif self.operation == '/':
                if float(second_number) == 0:
                    self.display.insert(0, "除数不能为零")
                    return
                result = self.f_num / float(second_number)
                
            if result is not None:
                if result.is_integer():
                    self.display.insert(0, str(int(result)))
                else:
                    result_str = str(result).rstrip('0').rstrip('.')
                    self.display.insert(0, result_str)
                
        except ValueError:
            self.clear()
        finally:
            self.operation = None
    
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    calc = Calculator()
    calc.run()
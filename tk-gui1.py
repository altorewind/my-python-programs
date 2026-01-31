import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox

app=tk.Tk()
app.title('test')
app.geometry('700x800')
#text
lb=tk.Label(app,text='ggg',width=20,height=10,fg='green')
lb.pack()
#input
text=tk.Entry(app,width=20)
text.pack()
#longtext
txt=tk.Text()
txt.pack()
#button messagebox
def cc():
	lb.config(text=text.get(),width=20,fg='black')
	tkinter.messagebox.showerror('wedwdw',txt.get('1.0',tk.END))
	tkinter.messagebox.askquestion('wedwdw','dwdxwedqwdwe??')
bt=tk.Button(text='gun',width=10,fg='blue',command=cc)
bt.pack()
#radiobutton
radiobt1=tk.Radiobutton(app,text='1+1=2',value=1)
radiobt2=tk.Radiobutton(app,text='1+1=3', value=2)
radiobt1.pack()
radiobt2.pack()
#combbox
cb=ttk.Combobox(app,width=20)
cb['values']=('1','2','3','4','5')
cb.pack()
#checkbutton
checkbt1=tk.Checkbutton(app,text='asad')
checkbt2=tk.Checkbutton(app,text='dwdw')
checkbt1.pack()
checkbt2.pack()


tk.mainloop()

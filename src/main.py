import tkinter as tk

app = tk.Tk()
app.title('Video converter')
app.geometry('500x500')
app.resizable(False, False)

app.grid_columnconfigure(0, minsize=50)
app.grid_columnconfigure(1, minsize=350)

l_path = tk.Label(app, text='Путь к файлам', padx=15, pady=10)
l_path.grid(row=0, column=0)

path = tk.Entry(app)
path.grid(row=0, column=1, stick='we')

btn_run = tk.Button(app, text='Начать')
btn_run.grid(row=1, column=1)


app.mainloop()



import tkinter as tk
import main as m
import numpy as np
import matplotlib.pyplot as plt

root = tk.Tk()
root.title('Counting Seconds')
root.geometry("200x400")




button1 = tk.Button(root, text= "Linear Interpolution", command= m.Linear).pack(pady=20)

button2 = tk.Button(root, text='polynomial interpolution', width=25, command=m.polynomial)
button2.pack()

button3 = tk.Button(root, text= "Quadratic interpolution", command= m.Quadratic).pack(pady=20)


button4 = tk.Button(root, text= "Lagrange Interpolution", command= m.lagranch).pack(pady=20)

button5 = tk.Button(root, text='Newtons polynomial interpolution', width=25, command=m.Newtons)
button5.pack()
root.mainloop()

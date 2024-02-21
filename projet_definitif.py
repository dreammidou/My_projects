"""Created By Dream_midou on FEBRUARY 2024"""

# Importer Tkinter,cpuinfo,time et threading
from tkinter import Tk,Label,ttk
from cpuinfo import cpuinfo 
import time
import threading

def affichetemps():
    global L
    while True:
        date = time.strftime('%d/%m/%y %H:%M:%S',time.localtime())
        L.config(text=date)
        time.sleep(0.01)    

# create the root window
# Création d'une fenêtre, racine de l'interface
root = Tk()
root.title("CPU information")
root.geometry("350x125")

my_cpuinfo = cpuinfo.get_cpu_info()

tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Model')
tabControl.add(tab2, text ='Architecture')
tabControl.add(tab3, text ='RAM')
tabControl.add(tab4, text ='Processor speed')
tabControl.pack(expand = 1, fill ="both")

ttk.Label(tab2, 
          text =f"CPU architecture: {my_cpuinfo['arch']}").grid(column = 0, 
                               row = 0,
                               padx = 30,
                               pady = 30)

ttk.Label(tab1, 
          text =f"CPU model: {my_cpuinfo['brand_raw']}").grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)

ttk.Label(tab3, 
          text =f"Ram : {my_cpuinfo['count']} GB").grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)

ttk.Label(tab4, 
          text =f"Processor base speed: {my_cpuinfo['hz_actual_friendly']}").grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)

L = Label(root, text = "")
L.pack()
T=threading.Thread(target=affichetemps)
T.setDaemon(True)

# run the app
T.start()
# Démarrage de la boucle Tkinter qui s'interompt quand on ferme la fenêtre
root.mainloop()
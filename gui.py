from tkinter import *
from ssh import SSH
import time

ssh = SSH()
root = Tk()
root.title("Raspberry pi information")
root.geometry("600x300")

#label
lbl = Label(root, text="not connected")
lbl.grid()

# CONNECT TO SSH BUTTON
def connectSSH():
    if ssh.connected == False:
        res = ssh.connect()
        if "error" in res:
            lbl.configure(text=res["error"])
        elif "success" in res:
            lbl.configure(text=res["success"])
            fetchDataBtn.configure(state=NORMAL)

        btn.configure(text = "Disconnect to ssh")
    elif ssh.connected == True:
        ssh.disconnect()
        btn.configure(text = "Connected to ssh")
        lbl.configure(text= "not connected")
        fetchDataBtn.configure(state=DISABLED)

        
 

btn = Button(root,text="Connect to ssh", fg="red", command=connectSSH)
btn.grid(column=2, row=0)


def fetchData():
    ssh.execCommand("cd Desktop; ls; python uploadData.py")

fetchDataBtn = Button(root, text="Fetch data from raspberry pi", command=fetchData, state=DISABLED)
fetchDataBtn.grid(column=2, row=1)

# for wid in root.winfo_children():
#     wid.destroy()

root.mainloop()








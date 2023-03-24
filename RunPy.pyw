from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import validators

#window settings
root = Tk()
root.title("RunPy")
root.geometry("550x550")
root.wm_minsize(550,550)
root.configure(bg="#A5A6A6")

#define list with program paths
programs = []

#add programs to list
def add_file():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select your file", filetypes=(("All files", "*.*"),))
    if file_path == "":
        pass
    else:
        programs.append(file_path)

    for widget in FRAME.winfo_children():
        widget.destroy()

    for program in programs:
        program_label = Label(FRAME, text=program, font = ("", 12)).pack()

#add website to list
def add_website():
    link = link_entry.get()
    cleanLink = link.replace(" ", "")

    if cleanLink == "":
        pass
    else:
        is_link_valid = validators.url(cleanLink)   #checks if link is valid
            
        if is_link_valid == True:   
            programs.append(cleanLink)
            link_entry.delete(0,"end")

            for widget in FRAME.winfo_children():
                widget.destroy()

            for program in programs:
                program_label = Label(FRAME, text=program, font = ("", 12)).pack()
        else:
            tkinter.messagebox.showerror("Invalid Link", "The link you tried to add is not valid. Please make sure you add the entire link, including the 'http://' prefix.")



#Clear list
def remove_last_element():
    try:
        programs.pop(-1)
        for widget in FRAME.winfo_children():
            widget.destroy()
        for program in programs:
            program_label = Label(FRAME, text=program, font = ("", 12)).pack()
    except:
        pass

def create_file():
    if not programs:
        tkinter.messagebox.showerror("No Programs added", "You haven't added any programs yet.")
    else:
        save_path = filedialog.asksaveasfilename(initialdir="/", title="Select where you want to save your file", filetypes=[("batch file", ".bat")], defaultextension=".bat")
        with open(save_path, "w") as file:
            for program in programs:
                file.write('start "" "' + program + '"\n')
            file.close()

#window content
FRAME = Frame(root, bg="#CACACA")
FRAME.place(relwidth=0.9, relheight=0.6, relx=0.05, rely=0.05)

add_button = Button(root, text="Add file", font = ("", 18), command = add_file).place(anchor="center", rely=0.72, relx=0.5)
link_entry = Entry(root, font = ("", 18))
link_entry.place(relwidth=0.67, relheight=0.07, rely=0.785, relx=0.012)
add_website_button = Button(root, text="Add Website", font = ("",18), command = add_website).place(anchor="center", rely=0.82, relx=0.84)
remove_last_button = Button(root, text="Remove last element", font = ("",18), command = remove_last_element).place(anchor="center", rely=0.92, relx=0.3)
create_file_button = Button(root, text="Create file", font = ("",18), command = create_file).place(anchor="center", rely=0.92, relx=0.7)



root.mainloop()

from tkinter import *
import BackEnd

#functions
def get_selected_row(event):
    try:
        global selected_tuple
        index=list_display.curselection()
        selected_tuple =list_display.get(index)
        print(selected_tuple)
        # fill in fields when selecting an entry
        title_entry.delete(0,END)
        title_entry.insert(END,selected_tuple[1])
        year_entry.delete(0,END)
        year_entry.insert(END,selected_tuple[2])
        company_entry.delete(0,END)
        company_entry.insert(END,selected_tuple[3])
    except IndexError:
        pass

def view_command():
    list_display.delete(0,END)
    for row in BackEnd.view():
        list_display.insert(END,row)


def search_command():
    list_display.delete(0,END)
    for row in BackEnd.search(title_text.get(),year_text.get(),company_text.get()):
        list_display.insert(END,row)


def add_command():
    BackEnd.insert(title_text.get(),year_text.get(),company_entry.get())
    list_display.delete(0,END)
    list_display.insert(END,(title_text.get(),year_text.get(),company_text.get()))


def delete_command():
    BackEnd.delete(selected_tuple[0])

def update_command():
    BackEnd.update(selected_tuple[0],title_text.get(),year_text.get(),company_text.get())

# create window
# remember to make a grid for it
window = Tk()
window.title('my game collection')


# create the first labels for data entry windows
label_one = Label(window, text='title')
label_one.grid(row=0, column= 0)

label_two = Label(window, text='company')
label_two.grid(row=1, column=0)

label_three = Label(window, text='year')
label_three.grid(row=0, column=2)

# create data entry actions for labels
# place the input spaces next to their corresponding labels
title_text  = StringVar()
title_entry = Entry(window, textvariable=title_text)
title_entry.grid(row=0, column=1)

company_text  = StringVar()
company_entry = Entry(window, textvariable=company_text)
company_entry.grid(row=1, column=1)

year_text = StringVar()
year_entry = Entry(window, textvariable=year_text)
year_entry.grid(row=0, column=3)

# create the box that displays the list
list_display = Listbox(window, height=6, width=40)
list_display.grid(row=3,column=0,rowspan=6,columnspan=2)

# create a scoll bar
list_display_scroll = Scrollbar(window)
list_display_scroll.grid(row=1, column=2,rowspan=6)

# configure list and scrollbar objects
list_display.configure(yscrollcommand=list_display_scroll.set)
list_display_scroll.configure(command=list_display.yview)

# add bind method
list_display.bind('<<ListboxSelect>>',get_selected_row)

# add buttons
view_all_button = Button(window, text='view all', width= 12,command=view_command)
view_all_button.grid(row=3,column=3)

search_button = Button(window, text='search game', width= 12,command=search_command)
search_button.grid(row=4,column=3)

add_button = Button(window, text='Add Game', width=12,command=add_command)
add_button.grid(row=5,column=3)

update_button = Button(window, text='Update', width=12, command=update_command)
update_button.grid(row=6,column=3)

delete_button= Button(window, text='Delete Game', width=12, command=delete_command)
delete_button.grid(row=7,column=3)

close_button = Button(window, text='Close', width=12,command=window.destroy)
close_button.grid(row=8, column=3)







# loop for the program
window.mainloop()
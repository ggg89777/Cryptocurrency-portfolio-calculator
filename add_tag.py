from tkinter import *


class CreateTag:

    """Class for creating new buttons
    show_fields - adds fields when clicking the add coin button:
        create_entry - create a tag input field
        create_label - create a field to display prices
        create_entry_2 - create a field to enter the number of coins
        create_label_2 - create a field to display money
        create_del - create a button to delete fields for a given coin
    get - poll the tag input field
    get2 - poll the input field for the number of coins
    push - send data from saving to input fields
    config - display the received information in the display fields
    del_coin - remove all fields of a given coin from the window and
                the coin data from the dictionary of class instances"""

    def __init__(self, idx: int, root: Tk, dict_id: dict, calculate):
        self.idx = idx
        self.root = root
        self.dict_id = dict_id
        self.calculate = calculate
        self.new_entry = Entry(root)
        self.new_label = Label(root, text='-', font=32)
        self.new_entry2 = Entry(root)
        self.new_label2 = Label(root, text='-', font=32)
        self.del_button = Button(root, text='del', command=self.del_coin)

    def show_fields(self):
        self.new_entry.grid(row=int(self.idx)+6, column=0)  # display button in root window on grid
        self.new_label.grid(row=int(self.idx)+6, column=1)
        self.new_entry2.grid(row=int(self.idx)+6, column=2)
        self.new_label2.grid(row=int(self.idx)+6, column=3)
        self.del_button.grid(row=int(self.idx)+6, column=4)

    def get(self):
        return self.new_entry.get()

    def get2(self):
        return self.new_entry2.get()

    def push(self, str1, str2):
        self.new_entry.insert(0, str1)
        self.new_entry2.insert(0, str2)

    def config(self, text, text2=None):
        self.new_label.config(text=text)
        if text2 is not None:
            self.new_label2.config(text=text2)

    def del_coin(self):
        self.new_label.grid_forget()
        self.new_label2.grid_forget()
        self.new_entry.grid_forget()
        self.new_entry2.grid_forget()
        self.del_button.grid_forget()
        del self.dict_id[self.idx]
        self.calculate()

def counter(fu):

    """Counter function to assign each instance a unique id"""

    def inner(*a, **kw):
        inner.count += 1
        return fu(*a, **kw)

    inner.count = 0
    return inner

@counter
def generate_field(root, dict_id, calculate,  **kwargs):

    """Function for generating class instances CreateTag
    instance_id - applies if new fields are created using a button add_button
    key - the dictionary key is passed to the function if loading is from a file
    (the value in load_file must be True)"""

    load_file = kwargs.get('load_file', False)
    key = kwargs.get('key', None)

    if load_file:

        """class method calls CreateTag"""

        dict_id[key] = CreateTag(key, root, dict_id, calculate)  # write an instance of a class to a dictionary
        dict_id[key].show_fields()

    else:
        instance_id = generate_field.count

        """class method calls CreateTag"""

        dict_id[instance_id] = CreateTag(instance_id, root, dict_id, calculate)
        dict_id[instance_id].show_fields()

import time

from tkinter import *
from saving_files import dill_load, dill_dump, read_key, save_key

from tkinter import simpledialog
from threading import Thread
from add_tag import generate_field
from get_quotes import generate_dict_price


dict_id = {}  # Dictionary for storing class instances
stop = True  # Auto polling flag
delay = 5  # How many minutes should I wait before sending a request to the site?
# this is necessary so as not to use up the free limit (recommended more than 5 minutes)
apy_key = 'None'

def main():

    """Main program window module"""

    def save():

        """The function polls instances of the class and saves the values entered in entry to a file save_portfolio.pkl"""

        dict_save = {}
        for key in dict_id.keys():
            value1 = dict_id[key].get()
            value2 = dict_id[key].get2()
            dict_save[key] = [value1, value2]

        dill_dump('save/save_portfolio.pkl', dict_save)

    def load():

        """Load save_portfolio.pkl"""

        dict_save = dill_load('save/save_portfolio.pkl')

        for key in dict_save.keys():
            generate_field(root=root, dict_id=dict_id, calculate=calculate, load_file=True, key=key)
            dict_id[key].push(dict_save[key][0], dict_save[key][1])

    def object_polling():

        """The function polls instances of the class, generates one row and sends a request to coinmarketcap."""

        result_str = ''

        for key in dict_id.keys():
            get_string = str(dict_id[key].get())
            result_str = result_str + ',' + get_string

        result_str = result_str[1:]
        dict_price = generate_dict_price(result_str, apy_key)
        dill_dump('dict_price.pkl', dict_price)
        for key in dict_id.keys():
            dict_id[key].config(text=str(dict_price[dict_id[key].get()]))

    def calculate():

        """The function multiplies in a loop the prices received from the website by the number of
         coins that are entered into the input field. Next it displays the total amount of money.
         The coin prices are loaded from a previously saved dictionary dict_price.pkl"""

        dict_price = dill_load('dict_price.pkl')
        total_cash = 0

        for key in dict_id.keys():
            try:
                price = str(dict_price[dict_id[key].get()])
                cash = str(round(float(dict_price[dict_id[key].get()]) * float(dict_id[key].get2()), 2))
                dict_id[key].config(price, cash)
                total_cash += float(cash)
            except Exception:
                price = 0
                cash = 0
                dict_id[key].config(price, cash)
                total_cash += float(cash)

        total_label.config(text=str(int(total_cash)) + ' $')

    def auto_start():

        """Function to automatically update prices and calculate the total portfolio amount
        progress through the loop until the stop flag becomes true"""

        global stop
        stop = False

        def start():
            while not stop:
                object_polling()
                calculate()
                print('start')
                for i in range(1, delay * 60):  # so that the start function breaks a second after pressing stop
                    if not stop:
                        time.sleep(1)
                    else:
                        break
            print('stop')

        Thread(None, start).start()  # runs in a separate thread so that the program does not hang while waiting

    def auto_stop():
        global stop

        """Stop function auto_start. Sets the flag to true when the user clicks the stop button."""

        stop = True

    def show_delay_entry():
        global delay

        """dialog box for entering a delay"""

        result = simpledialog.askinteger("Delay", "Enter delay (min):", parent=root, minvalue=5)

        """if there is a value in the dialog box then the variable is equal to the entered value"""

        if result is not None:
            delay = result

    def show_entry_key():
        global apy_key

        """dialog box for entering a api key"""

        result = simpledialog.askstring("API_KEY", "Enter API-KEY coinmarketcap.com:", parent=root)

        """if there is a value in the dialog box then the variable is equal to the entered value"""

        if result is not None:
            apy_key = result
            save_key(apy_key)

    def initial_key_check():

        """When the program starts, the function reads the key from the file API-KEY.txt.
         If no such file exists, prompts a dialog box to enter the key"""

        global apy_key
        try:
            apy_key = read_key()
        except:
            show_entry_key()

    root = Tk()  # main program window
    root.title('Cryptocurrency portfolio calculator')  # name
    root.geometry('900x950')  # size
    button = Button(root, text='Get Coinmarketcap', command=object_polling)  # create a button in the root of the window
    button.grid(row=6, column=1, sticky=S, padx=8)  # show button in grid mode

    label_quantity = Label(root, text='enter quantity (.)')  # label enter quantity (.)
    label_quantity.grid(row=6, column=2, sticky=S, padx=8)

    button_calc = Button(root, text='calculate   $$$', command=calculate)  # button calculate $$$
    button_calc.grid(row=6, column=3, sticky=S, padx=8)

    add_button = Button(
        root,
        text='add coin',
        command=lambda: generate_field(
            root=root,
            dict_id=dict_id,
            calculate=calculate
        ))  # button add coin
    add_button.grid(row=6, column=0, padx=30)

    total_label_name = Label(root, text='TOTAL CASH:', font=("Arial", 32))  # label TOTAL CASH
    total_label_name.grid(column=2, row=2, padx=10)

    total_label = Label(root, text='------', font=("Arial", 50), background="#FFCDD2")  # initial state TOTAL CASH
    total_label.grid(column=2, row=5, padx=10)

    auto_start = Button(root, text='auto_start', font=("Arial", 8), command=auto_start)  # button auto_start
    auto_start.grid(row=0, column=0, sticky=E)

    auto_stop = Button(root, text='auto_stop', font=("Arial", 8), command=auto_stop)  # button auto_stop
    auto_stop.grid(row=0, column=1, sticky=W)

    root.option_add("*tearOff", FALSE)
    initial_key_check()  # when starting the program, check the file API-KEY.txt

    """Global menu module"""

    main_menu = Menu()
    file_menu = Menu()
    settings_menu = Menu()

    main_menu.add_cascade(label="File", menu=file_menu)
    main_menu.add_cascade(label="Settings", menu=settings_menu)

    file_menu.add_command(label="Save", command=save)
    file_menu.add_command(label="Open", command=load)
    file_menu.add_command(label="Exit")

    settings_menu.add_command(label='delay', command=show_delay_entry)
    settings_menu.add_command(label='API_KEY', command=show_entry_key)

    root.config(menu=main_menu)

    root.mainloop()  # loop until the user closes the program

if __name__ == '__main__':
    main()

from os import getcwd, path
from csv import reader, writer
from tabulate import tabulate

def open_read_csv(filename):
    filepath = path.join(getcwd(),"files",filename)
    with open(filepath, "r", newline="") as f:
        baca = list(reader(f))
        header = baca[0]
        content = baca[1:]
    
    return header, content

def open_write_all_csv(filename, ds, hd):
    filepath = path.join(getcwd(),"files",filename)
    with open(filepath, "w", newline="") as f:
        tulis = writer(f)
        tulis.writerow(hd)
        tulis.writerows(ds)

def open_append_csv(filename, ds):
    filepath = path.join(getcwd(),"files",filename)
    with open(filepath, "a", newline="") as f:
        tulis = writer(f)
        tulis.writerows(ds)

def open_append2first_csv(filename, ds):
    header, content = open_read_csv(filename)
    toinsert = ds[0]
    content.insert(0, toinsert)
    open_write_all_csv(filename, content, header)

def sort_csv_by_hd(filename, sortby:str, reverse_cond:bool = False):
    header, content = open_read_csv(filename)
    index = header.index(sortby)
    if sortby != "nominal":
        sortkey = lambda ls : ls[index]
    else:
        sortkey = lambda ls : int(ls[index])
    content.sort(key= sortkey, reverse= reverse_cond)
    open_write_all_csv(filename, content, header)

def input_normal(prompt:str):
    while True:
        try:
            ans = input(prompt+"\n")
            break
        except AssertionError as er:
            print(er)
    return ans.lower()

def input_of_options(prompt:str, ls_options:list, errormsg = "Input Tidak Valid!"):
    while True:
        try:
            ans = input(prompt+"\n")
            assert ans.lower() in ls_options, errormsg
            break
        except AssertionError as er:
            print(er)
    return ans.lower()

def input_of_yatidak(prompt:str, errormsg= "Input Tidak Valid!"):
    while True:
        try:
            ans = input(prompt+"\n")
            assert ans.lower() in ["y", "t"], errormsg
            break
        except AssertionError as er:
            print(er)
    return ans.lower()

def input_money(prompt:str):
    while True:
        try:
            amount = int(input(prompt+"\n"))
            assert amount >= 0, "Uang tidak negatif!"
            break
        except AssertionError as er:
            print(er)
        except ValueError:
            print("Masukkan uang dengan benar")
    return amount

def input_money_w_params(prompt:str, code:str, moneyparam:int):
    while True:
        try:
            amount = int(input(prompt+"\n"))
            assert amount >= 0, "Uang tidak negatif!"
            assert amount - moneyparam >= 0 if code == "0" else True, "Uang tidak cukup!"
            break
        except ValueError:
            print("Masukkan uang dengan benar")
        except AssertionError as er:
            print(er)
    return amount

def ch_color_style(value, color:str="", style:str=""):
    color, style = color.lower(), style.lower()
    fmt = {"reset" : "\033[0m",
        "bold" : "\033[1m",
        "italic" : "\033[3m",
        "underline" : "\033[4m",
        ""        :        "",
        "black" : "\033[30m",
        "red" : "\033[38;5;196m",
        "orange" : "\033[38;2;255;165;55m",
        "yellow" : "\033[38;2;255;255;0m",
        "green" : "\033[38;5;46m",
        "blue" : "\033[34m",
        "magenta" : "\033[35m",
        "purple" : "\033[38;5;165m",
        "sky" : "\033[38;5;111m",
        "tosca" : "\033[38;5;123m",
        "white" : "\033[37m"
    }
    return f"{fmt[style]}{fmt[color]}{value}{fmt['reset']}"

def display_table(values:list, header:list):
    print(tabulate(values, headers= header, tablefmt="rst", stralign= "center"))




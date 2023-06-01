from os import getcwd, path
from csv import reader, writer

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

def input_normal(prompt:str):
    while True:
        try:
            ans = input(prompt)
            break
        except AssertionError as er:
            print(er)
    return ans.lower()

def input_of_options(prompt:str, ls_options:list, errormsg = "Input Tidak Valid!"):
    while True:
        try:
            ans = input(prompt)
            assert ans.lower() in ls_options, errormsg
            break
        except AssertionError as er:
            print(er)
    return ans.lower()

def input_of_yatidak(prompt:str, errormsg= "Input Tidak Valid!"):
    while True:
        try:
            ans = input(prompt)
            assert ans.lower() in ["y", "t"], errormsg
            break
        except AssertionError as er:
            print(er)
    return ans.lower()

def input_money(prompt:str):
    while True:
        try:
            amount = int(input(prompt))
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
            amount = input(prompt)
            assert amount >= 0, "Uang tidak negatif!"
            assert amount - moneyparam >= 0 if code == "0" else True, "Uang tidak cukup!"
            break
        except AssertionError as er:
            print(er)
    return amount


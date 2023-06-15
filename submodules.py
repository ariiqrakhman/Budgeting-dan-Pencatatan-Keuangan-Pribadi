from os import getcwd, path
from csv import reader, writer
from tabulate import tabulate

# Subprogram untuk membaca isi file csv
def open_read_csv(filename):
    filepath = path.join(getcwd(), "files", filename)
    with open(filepath, "r", newline="") as f:
        # Hilangkan spasi lebih dan line kosong
        lines = filter(lambda x: x.strip(), f)  
        baca = list(reader(lines))
        header = baca[0] # Line 1 untuk header
        content = baca[1:] # Line dibawahnya untuk list
    
    return header, content

# Subprogram untuk menulis seluruh isi file csv
def open_write_all_csv(filename, ds, hd):
    filepath = path.join(getcwd(),"files",filename)
    with open(filepath, "w", newline="") as f:
        tulis = writer(f)
        tulis.writerow(hd)
        tulis.writerows(ds)

# Subprogram untuk menambah list pada akhir isi file csv
def open_append_csv(filename, ds):
    filepath = path.join(getcwd(),"files",filename)
    with open(filepath, "a", newline="") as f:
        tulis = writer(f)
        tulis.writerows(ds)

# Subprogram untuk menambah list pada awal isi file csv
def open_append2first_csv(filename, ds):
    header, content = open_read_csv(filename)
    toinsert = ds[0]
    content.insert(0, toinsert)
    open_write_all_csv(filename, content, header)

# Subprogram untuk mengurutkan list berdasarkan header pada file csv
def sort_csv_by_hd(filename, sortby:str, reverse_cond:bool = False):
    header, content = open_read_csv(filename)
    index = header.index(sortby)
    if sortby != "nominal":
        sortkey = lambda ls : ls[index]
    else:
        sortkey = lambda ls : int(ls[index])
    content.sort(key= sortkey, reverse= reverse_cond)
    open_write_all_csv(filename, content, header)

# Subprogram untuk meminta input tanpa syarat
def input_normal(prompt:str):
    while True:
        try:
            ans = input(prompt+"\n")
            assert len(ans) > 0, "Input tidak boleh kosong!"
            assert len(ans) <= 22, "Input terlalu panjang!"
            break
        except AssertionError as er:
            print(er)
    return ans.lower()

# Subprogram untuk meminta input dengan syarat list berisi string
def input_of_str_options(prompt:str, ls_options:list, errormsg = "Input Tidak Valid!"):
    while True:
        try:
            ans = input(prompt+"\n")
            assert ans.lower() in ls_options, errormsg
            break
        except AssertionError as er:
            print(er)
    return ans.lower()

# Subprogram untuk meminta input dengan syarat list bilangan bulat
def input_of_int_options(prompt:str, ls_options:list, errormsg = "Input Tidak Valid!"):
    while True:
        try:
            ans = int(input(prompt+"\n"))
            assert ans in ls_options, errormsg
            break
        except AssertionError as er:
            print(er)
        except ValueError:
            print(errormsg, f"\nmasukkan opsi yang valid: {ls_options}")
    return ans

# Subprogram untuk meminta input dengan syarat jawaban "y" atau "t"
def input_of_yatidak(prompt:str, errormsg= "Input Tidak Valid!"):
    while True:
        try:
            ans = input(prompt+"\n")
            assert ans.lower() in ["y", "t"], errormsg
            break
        except AssertionError as er:
            print(er)
    return ans.lower()

# Subprogram untuk meminta input uang normal
def input_money(prompt:str):
    while True:
        try:
            amount = int(input(prompt+"\n"))
            assert amount >= 0, "Uang tidak negatif!"
            assert amount < 10_000_000, "Uang terlalu besar!"
            break
        except AssertionError as er:
            print(er)
        except ValueError:
            print("Masukkan uang dengan benar")
    return amount

# Subprogram untuk meminta input uang bersyarat nilai
def input_money_w_params(prompt:str, code:int, moneyparam:int):
    counter = 0
    while True:
        try:
            if counter >= 3:
                return None
            amount = int(input(prompt+"\n"))
            assert amount >= 0, "Uang tidak negatif!"
            assert amount < 10_000_000, "Uang terlalu besar!"
            counter += 1
            assert moneyparam - amount >= 0 if code == 0 else True, "Uang tidak cukup!"
            break
        except ValueError:
            print("Masukkan uang dengan benar")
        except AssertionError as er:
            print(er)
    return amount

# Subprogram untuk mengganti warna dan gaya font pada terminal
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

# Subprogram untuk menampilkan tabel dengan gaya tertentu
def display_table(values:list, header:list, header_cond:bool= True):
    print(tabulate(values, headers= header if header_cond == True else False, tablefmt="rst", stralign= "right"))
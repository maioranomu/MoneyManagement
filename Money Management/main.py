import os
from datetime import datetime

run, num, money, file, logfile = True, 0, 0, "import.txt", "log.txt"

def cls():
    os.system("cls")
cls()

with open(file, "r") as f:
    try:
        money = float(f.read())
    except ValueError:
        money = input("Quantos reais você tem? ")
        money = float(money)
        with open(file, "w") as f:
            f.write(str(money))
        

def writer(ammount, op):
    global file
    global log
    global num
    global money
    log = input("Log: ")
    with open(logfile, "a") as f:
        date = datetime.now()
        if log == "":
            f.write(f"Time: {date} | Change: {op}{num} | Current: {money: .2f} | Log: Empty log")
        else:
            f.write(f"Time: {date} | Change: {op}{num} | Current: {money: .2f} | Log: {log}")
        f.write("\n")
        
    with open(file, "w") as f:
        f.write(str(ammount))    
    
    
def change(what, much = 0):
    global money
    
    if what == "add":
        money += much
        writer(str(money), "+")
    
    elif what == "rem":
        money -= much
        writer(str(money), "-")
        
    elif what == "alt":
        money = much
        writer(str(money), "=")
    
def get_decimal_part(num):
    num_str = str(num)
    try:
        if '.' in num_str:
            decimal_index = num_str.index('.')
            decimal_part = num_str[decimal_index + 1]
            return decimal_part
        else:
            return None
    except IndexError:
        return None
    
def get_decimal_part2(num):
    num_str = str(num)
    try:
        if '.' in num_str:
            decimal_index = num_str.index('.')
            decimal_part = num_str[decimal_index + 2]
            return decimal_part
        else:
            return None
    except IndexError:
        return None
    
def main():
    global run
    global num
    cls()
    actionlist = ["1", "2" ,"3", "s", "q", "h"]
    do = ""
    
    while do not in actionlist:
        cls()
        print(f"                                   Saldo atual: R${money: .2f}")
        print("[1-ADICIONAR SALDO | 2-REMOVER SALDO | 3-ALTERAR SALDO | S-VER DINHEIRO | H-HISTORICO | Q-SAIR]")
        print("-----------------------------------------------------------------------------------------------")
        do = input("\n \n \n                                          ").lower()
        
    if do == "1":
        cls()
        while True:
            num = input("Quanto você quer adicionar? [Q - CANCELAR] \n $")
            if num == "q":
                break
            
            try:
                num = float(num)
                change("add", num)
                break
            except ValueError:
                cls()
                print("Tente novamente")
                
    elif do == "2":
        cls()
        while True:
            num = input("Quanto você quer remover? [Q - CANCELAR] \n $")
            if num == "q":
                break
            try:
                num = float(num)
                change("rem", num)
                break
            except ValueError:
                cls()
                print("Tente novamente")
                
    elif do == "3":
        cls()
        while True:
            num = input("Para qual valor você quer alterar? [Q - CANCELAR] \n $").lower()
            if num == "q":
                break
            try:
                num = float(num)
                change("alt", num)
                break
            except ValueError:
                cls()
                print("Tente novamente")
        
    elif do == "s":
        cls()
        try:
            print(f"Saldo: {round(money, 2)} \n")
            seemoney = "*" * int(money)
            print("Cada moeda é 1 real:")
            
            print("\n")
            print(seemoney)
            print("\n")
            
            print("Cada moeda é 10 centavos:")
            print("\n")
            try:
                deccents = "." * int(get_decimal_part(money))
                print(deccents)
                print("\n")
            except TypeError:
                print("")
            
            print("Cada moeda é 1 centavo:")
            print("\n")
            try:
                cents = "." * int(get_decimal_part2(money))
                print(cents)
                print("\n")
            except TypeError:
                print("")
            
        except MemoryError:
            print("Você tem muito dinheiro!")
        except OverflowError:
            print("Você tem muito dinheiro!")    
        
        input("Aperte [ENTER] para sair.")
    
    elif do == "h":
        cls()
        with open(logfile, "r") as f:
            print(f.read())
            input("Aperte [ENTER] para sair.")
        
    elif do == "q":
        cls()
        run = False
        
while run == True:
    main() 

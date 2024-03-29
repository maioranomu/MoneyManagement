import os

run = True
money = 0
file = "import.txt"

def cls():
    os.system("cls")
cls()

with open(file, "r") as f:
    try:
        money = int(f.read())
    except ValueError:
        money = input("Quantos reais você tem? ")
        with open(file, "w") as f:
            f.write(money)
        

def writer(ammount):
    global file
    
    with open(file, "w") as f:
        f.write(str(ammount))    
    
def change(what, much = 0):
    global money
    if what == "add":
        money += much
        writer(money)
    
    elif what == "rem":
        money -= much
        writer(money)
        
    elif what == "alt":
        money = much
        writer(money)
    
def main():
    global run
    
    cls()
    actionlist = ["1", "2" ,"3", "s", "q"]
    do = ""
    
    while do not in actionlist:
        cls()
        print(f"Saldo atual: R${money}")
        print("[1-ALTERAR SALDO | 2-ADICIONAR SALDO | 3-REMOVER SALDO | S-VER DINHEIRO | Q-SAIR]")
        do = input("").lower()
        
    if do == "1":
        cls()
        while True:
            alt = input("Para qual valor você quer alterar? [Q - CANCELAR] ").lower()
            if alt == "q":
                break
            try:
                alt = int(alt)
                change("alt", alt)
                break
            except ValueError:
                print("Tente novamente")
        
    elif do == "2":
        cls()
        while True:
            add = input("Quanto você quer adicionar? [Q - CANCELAR] ")
            if add == "q":
                break
            
            try:
                add = int(add)
                change("add", add)
                break
            except ValueError:
                print("Tente novamente")
        
    elif do == "3":
        cls()
        while True:
            rem = input("Quanto você quer remover? [Q - CANCELAR] ")
            if rem == "q":
                break
            try:
                rem = int(rem)
                change("rem", rem)
                break
            except ValueError:
                print("Tente novamente")
                
    elif do == "s":
        cls()
        seemoney = "*" * money
        print("Cada moeda é 1 real:")
        print(seemoney)
        input("Aperte [ENTER] para sair.")
        
    elif do == "q":
        cls()
        run = False
        
while run == True:
    main() 
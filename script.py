import random 
import sqlite3
import requests


# number of ips to generate.


try:
    range_ip = int(input("[+] Quantos IP's você deseja gerar?"))
except Exception:
    print("use a valid number.")
    exit()

# If you Want save the valid results in the database.

salvar = str(input("[+] Salvar resultados no banco de dados?[Y/N]"))


if (salvar == "Y"  or salvar == "y"):
    
    print('Salvar no banco de dados.')

    # Creating the database.

    con = sqlite3.connect("easyipdb")

    cur = con.cursor()

    # Creating the table.

    cur.execute("CREATE TABLE IF NOT EXISTS tb_easyip (occurrences TEXT)")

    count = 0

    print("-- Occurences --")


    # Ip loop.

    while(count < range_ip):

        count += 1

        array_ip = [random.randint(100,200),random.randint(100,200),random.randint(100,200),random.randint(100,200)]

        format_ip = (f"https://{array_ip[0]}.{array_ip[1]}.{array_ip[2]}.{array_ip[3]}")

        try:
            response = requests.get(format_ip,timeout=1)

            if (response.status_code == 200):
                print(f"{format_ip} found!")
                cur.execute("INSERT INTO tb_easyip VALUES (?)", (f"{format_ip}",))
                con.commit()
            else:
                print(f"{response.status_code}")

        except Exception:
            pass


    # Without save.
             
else:
    print("Não salvar no banco de dados.")

    count = 0

    while(count < range_ip):

        count += 1

        array_ip = [random.randint(100,200),random.randint(100,200),random.randint(100,200),random.randint(100,200)]

        format_ip = (f"https://{array_ip[0]}.{array_ip[1]}.{array_ip[2]}.{array_ip[3]}")

        try:
            response = requests.get(format_ip,timeout=1)

            if (response.status_code == 200):
                print(f"{format_ip} found!")
            else:
               print(f"{response.status_code}")

        except Exception:
            pass
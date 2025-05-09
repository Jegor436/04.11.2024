import random

slepenais_skaitlis = random.randint(1, 100)
minejums = None

print("Uzmini skaitli no 1 līdz 100!")

while minejums != slepenais_skaitlis:
    minejums = int(input("Tavs minējums: "))

    if minejums < slepenais_skaitlis:
        print("Par mazu!")
    elif minejums > slepenais_skaitlis:
        print("Par lielu!")
    else:
        print("Apsveicu! Tu uzminēji pareizo skaitli!")




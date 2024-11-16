menu = str(input("*---------------------*\n"
                "|Menu           |preço|\n"
                "*---------------------*\n"
                "|1 Burg. 1 bebi.| 3.99|\n"
                "*---------------------*\n"
                "|2 Burg. 1 bebi.| 5.99|\n"
                "*---------------------*\n"
                "|1 Burg. 2 bebi.| 4.99|\n"
                "*---------------------*"))
match menu:
    case "1 burg. 1 bebi.":
        preço = 3.99
    case "2 burg. 1 bebi.":
        preço = 5.99
    case "1 burg. 2 bebi.":
        preço = 4.99
    case _:
        preço= 'não é um menu valido'
print(preço)
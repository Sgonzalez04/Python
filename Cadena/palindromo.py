tex = input("ingrese una palabra: ")
intex = tex[::-1]

if tex == intex:
    print("palindromo")
else:
    print("no es palindromo")

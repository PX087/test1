print("Olá Brasil")
def diga_olá():
    print("Olá da Função")
diga_olá()
def a():
    print("oi")
def b(nome):
    a()
    print(nome)
    print("tchau")
a()
b("juninho")
#------------------------------------------------------------------------------------------
def soma():
    print(1+1)
soma()
def subtracao():
    print(2568-1000)
subtracao()
def soma2(n1,n2):
    print(n1+n2)
soma2(63,8)
soma2(800,1000)
def subtracao2(n1,n2):
    print(n1-n2)
subtracao2(700,800)
subtracao2(1000,450)
subtracao2(900,800)
#------------------------------------------------------------------------------------------
nome=["abelha","girafa","porco"]
print(nome)
print(nome[0])
nome.append("cachorro")
nome.append("morcego")
nome.append("cavalo")
#-----------------------------------------------------------------------------------------
for i in range(len(nome)):
    print(i)
    print(nome[i])
    if nome[i] == "porco":
        print("Oinc")
    elif nome[i] == "cachorro":
        print("au au")
    elif nome[i] == "cavalo":
        print("relincha")
    else:
        print("eu não sou porco, nem cavalo nem cachorro")
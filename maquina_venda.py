maquina = [["id","produto","preço",'estoque'],
[1,"Coca-cola", 3.75, 2],
[2,"Pepsi", 3.67, 5],
[3,"Monster", 9.96, 1],
[4,"Café", 1.25, 100],
[5,"Redbull", 13.99, 2]]

for x in maquina:
    print(x)

def calculoTroco(valorProduto,valorInserido):
    vetor = [100,50,20,10,5,2,1,0.5,0.25,0.10,0.05,0.01]
    troco =  valorInserido - valorProduto
    for cedula in vetor:
        qtd = int(troco / cedula)
        if qtd >= 1:
            print(qtd,"cedula(s) de",cedula)
            troco -= cedula * qtd

pedido = int(input("Selecione o número do seu pedido: "))

while pedido > 0 and pedido < 6:
    if maquina [pedido] [3] == 0:
        print('estoque vazio')
        pedido = int(input('digite um produto disponível'))
    else:
        print(maquina[pedido][1],' valor =', maquina[pedido][2], "estoque restante =",maquina[pedido][3])
        valorInserido = float(input("Insira o valor: "))
        if valorInserido < maquina[pedido][2]:
            print('valor insuficiente')
        elif maquina [pedido] [3] == 0:
            print('estoque vazio')
        else:
            calculoTroco(maquina[pedido][2],valorInserido)
            maquina[pedido][3] -= 1
            print(maquina[pedido][1],"estoque =",maquina[pedido][3])
        pedido = int(input("Digite o id para continuar")) 

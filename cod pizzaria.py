total_pizzas = 0
taxa = 0
total_pedido = 0
pedidos = []
troco_opcao = 'não'
pagamento = 'outro'
continuar = '1'
nome = input("\nNome do Cliente: ")
telefone = (input("Telefone para contato: "))
while continuar == '1':
    
    print("\n" + "="*35)
    print("   PONTO 99 PIZZARIA 🍕")
    print("="*35)


    print("\n1 - Calabresa: R$25")
    print("2 - Frango: R$25")
    print("3 - Portuguesa: R$25")
    print("4 - Marguerita: R$25")
    print("5 - Chocolate com M&M: R$ 25")

    opcao = int(input("\nEscolha o sabor (1, 2, 3, 4, ou 5): "))



    while opcao < 1 or opcao > 5:
        print("Opção inválida")
        opcao = int(input("Escolha o sabor (1, 2, 3, 4, ou 5): "))

    

    if opcao == 1:
        sabor = "Calabresa"
    elif opcao == 2:
        sabor = "Frango"
    elif opcao == 3:
        sabor = "Portuguesa"
    elif opcao == 4:
        sabor = "Marguerita"
    elif opcao == 5:
        sabor = "Chocolate com M&M"

    preco = 25
    
    quantidade = int(input("Quantas pizzas? "))
    while quantidade <= 0:
        print("Quantidade inválida")
        quantidade = int(input("Quantas pizzas? "))
    total_pizzas = total_pizzas + quantidade
    pedidos.append((sabor,quantidade))
    total = preco * quantidade
    total_pedido = total_pedido + total
    print(f"Você pediu {quantidade} pizza(s) de {sabor}")
    print(f"Total geral até agora: R$ {total_pedido:.2f}")

    continuar = input("\n(1- continuar escolhendo Sabor  | 2- Finalizar pedido ): ")
    while continuar not in ['1', '2']:
        print("Opção Inválida")
        continuar = input("\n(1- continuar escolhendo Sabor  | 2- Finalizar pedido ): ")
entrega = input("Digite 1- para entrega e 2- para retirada: ")
while entrega not in ['1', '2']:
    print("Opção inválida")
    entrega = input("Digite (1- para entrega e 2- para retirada): ")
if entrega == '1':
    endereco = input("Qual seu endereço? ")
    taxa = 5
    
total_final = total_pedido + taxa    

pagamento = input("Qual será a forma de pagamento? (1- Dinheiro, 2- Pix, 3- Cartão): ")
while pagamento not in ['1', '2', '3']:
    print("Opção inválida")
    pagamento = input("Qual será a forma de pagamento? (1- Dinheiro, 2- Pix, 3- Cartão): ")

if pagamento == '1':
    troco_opcao = input("Deseja troco? Digite (1-sim ou 2-não)? ")
    while troco_opcao not in ['1', '2']:
        print("Opção Inválida")
        troco_opcao = input("Deseja troco? Digite (1-sim ou 2-não)? ")

if troco_opcao == '1':
    troco = float(input("Troco para quanto? R$ "))
    
    while troco < total_final:
        print("Troco inválido. Digite novamente.")
        troco = float(input("Troco para quanto? R$ "))

    troco_final = troco - total_final

print("\n --- DESCRIÇÃO DO PEDIDO ---")

print("Nome do cliente:",nome)

print("Telefone para contato:",telefone)

calabresa = frango = portuguesa = marguerita = chocolate = 0


for sabor, quantidade in pedidos:
    if sabor == "Calabresa":
        calabresa = calabresa + quantidade
    elif sabor == "Frango":
        frango = frango + quantidade
    elif sabor == "Portuguesa":
        portuguesa = portuguesa + quantidade
    elif sabor == "Marguerita":
        marguerita = marguerita + quantidade
    elif sabor == "Chocolate com M&M":
        chocolate = chocolate + quantidade

if calabresa > 0:
    print(f"Calabresa - {calabresa}")

if frango > 0:
    print(f"Frango - {frango}")

if portuguesa > 0:
    print(f"Portuguesa - {portuguesa}")

if marguerita > 0:
    print(f"Marguerita - {marguerita}")

if chocolate > 0:
    print(f"Chocolate com M&M - {chocolate}")

print(f"Total de Pizza(s):",total_pizzas)

print(f"Total do pedido: {total_pedido:.2f}")

if entrega == '1':
    print(f"Taxa de entrega {taxa:.2f}")

print(f"Total a pagar = R$ {total_final:.2f}")
if troco_opcao == '1':
    print(f"Troco = R$ {troco_final:.2f}")

if entrega == '1':
    print(f"Endereço para entrega:",endereco)   

if pagamento == '1':
    forma = 'Dinheiro'
elif pagamento == '2':
    forma = 'Pix'
elif pagamento == '3':
    forma = 'Cartão'
else:
    forma = 'Não informado'
print("Forma de pagamento: ",forma)





confirmacao = input("Deseja confirmar seu pedido? (1-sim  /  2-não): ").lower()
while confirmacao not in ['1', '2']:
    print("Opção inválida")
    confirmacao = input("Deseja confirmar seu pedido? (1-sim  /  2-não): ").lower()
if confirmacao == '1':
    print("\n--- PEDIDO CONFIRMADO ---")
elif confirmacao == '2':
    print("Pedido cancelado")

if entrega == '1':
    print("Tempo estimado para entrega: 80 minutos")
elif entrega == '2':
    print("Tempo estimado para retirada: 60 minutos")

print("\nObrigado pela preferência.")
print("VOLTE SEMPRE!!!")
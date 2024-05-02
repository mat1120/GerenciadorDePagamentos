print("{:=^40}".format("\033[0;33m LOJAS MWZ \033[m"))
print("="*30)

prod = float(input("Digite o preço do produto:R$"))
print("Escolha a forma de pagamento")
print("[ 1 ] á vista/cheque com 10% de desconto")
print("[ 2 ] á vista no cartão com 5% de desconto")
print("[ 3 ] 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")
opcao = int(input("Escolha uma das opções a cima: "))
if opcao not in [1, 2, 3, 4]:
    print("\033[0;31mOPÇÃO INVALIDA DE PAGAMENTO,DIGITE ENTRE AS OPÇÔES 1,2,3,4\033[m")
else:
    if opcao == 1:
        preco1 = prod - (prod * 10 / 100)
        print("Sua compra foi de {:.2f} e voce pagara R${:.2F}".format(prod,preco1))
    elif opcao == 2:
        preco2 = prod - (prod * 5 / 100)
        print("Sua compra foi de R${:.2f} e voce pagara R${:.2f}".format(prod ,preco2))
    elif opcao == 3:
        parcela = int(input("Quantas parcelas?"))
        if parcela > 2:
            print("\033[0;31mNumero de parcelas digitado invalida!Aceitamos até 2 vezes\033[m")
        total = prod
        parcelas = total / 2
        print("Voce pagara R${:.2f} divido em 2 parcelas de R${:.2f}".format(total, parcelas))
        print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(prod,total))
    elif opcao == 4:
        parcela = int(input("Quantas parcelas?"))
        if parcela < 3:
            print("\033[0;31mNumero de parcelas digitado invalida,digite 3 ou mais parcelas\033[m")
        else:
            preco3 = prod + (prod * 20 / 100)
            valor_parcela = preco3 / parcela
            print("Voce pagara R${:.2f} em {}x parcelado de R${:.2f} COM JUROS".format(prod,parcela,valor_parcela))
            print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(prod,preco3))
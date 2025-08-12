IMPOSTO = 20/100
PORCENTAGEM_DISTRIBUIDOR = 8/100

def obter_custo_fabrica():
    while True:
        try:
            custo_fabrica = float(input("Informe o preco de fabrica do carro: "))

            if custo_fabrica is not None:
                return custo_fabrica          
        
        except ValueError:
            print("Erro: Informe um valor valido!")

def obter_valor_imposto(custo_fabrica):
    return IMPOSTO * custo_fabrica

def obter_preco_final_fabrica(custo_fabrica, imposto):
    return custo_fabrica + imposto

def obter_faturamento_distribuidor(preco_fabrica):
    return PORCENTAGEM_DISTRIBUIDOR * preco_fabrica

def obter_custo_consumidor(custo_fabrica, faturamento_distribuidor):
    return custo_fabrica + faturamento_distribuidor

# Aqui fiquei em duvida se era para imprimir custo de fabrica após a aplicação de impostos ou não.
# Decidi usar o custo de fábrica (o valor que o usuário digitou).
def exibir_resultado(custo_fabrica, imposto, faturamento_distribuidor, custo_consumidor):
        print(f"\n\tPreco de fabrica: {custo_fabrica}")
        print(f"\tValor do imposto: {imposto}")
        print(f"\tFaturamento do distribuidor: {faturamento_distribuidor}")
        print("\t------------------------------------")
        print(f"\tCusto do consumidor: {custo_consumidor}\n")

def main():

    custo_fabrica = obter_custo_fabrica()
    imposto = obter_valor_imposto(custo_fabrica)
    preco_fabrica = obter_preco_final_fabrica(custo_fabrica, imposto)
    faturamento_distribuidor = obter_faturamento_distribuidor(preco_fabrica)
    custo_consumidor = obter_custo_consumidor(preco_fabrica, faturamento_distribuidor)

    exibir_resultado(custo_fabrica, imposto, faturamento_distribuidor, custo_consumidor)

if __name__ == "__main__":
    main()
IMPOSTO = 20/100
PORCENTAGEM_DISTRIBUIDOR = 8/100

def obter_custo_fabrica():
    custo_fabrica = float(input("Informe o preco de fabrica do carro: "))
    return custo_fabrica

def obter_valor_imposto(custo_fabrica):
    return IMPOSTO * custo_fabrica

def obter_preco_final_fabrica(custo_fabrica, imposto):
    return custo_fabrica + imposto

def obter_faturamento_distribuidor(preco_fabrica):
    return PORCENTAGEM_DISTRIBUIDOR * preco_fabrica

def obter_custo_consumidor(custo_fabrica, faturamento_distribuidor):
    return custo_fabrica + faturamento_distribuidor

def main():
    custo_fabrica = obter_custo_fabrica()
    imposto = obter_valor_imposto(custo_fabrica)
    preco_fabrica = obter_preco_final_fabrica(custo_fabrica, imposto)
    faturamento_distribuidor = obter_faturamento_distribuidor(preco_fabrica)
    custo_consumidor = obter_custo_consumidor(preco_fabrica, faturamento_distribuidor)

    print(f"\n\tPreco de fabrica: {preco_fabrica}")
    print(f"\tValor do imposto: {imposto}")
    print(f"\tFaturamento do distribuidor: {faturamento_distribuidor}")
    print("\t------------------------------------")
    print(f"\tCusto do consumidor: {custo_consumidor}\n")

    while True:

        try:
            if custo_fabrica is None:
                break
            custo_fabrica = obter_custo_fabrica()
            
        except ValueError:
            print("Erro: Informe um valor valido!")

if __name__ == "__main__":
    main()
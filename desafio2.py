from lxml import etree
import locale


def carregar_dados():
    #carregando os dados
    dados = etree.parse("Ano-2017.xml")
    #criando um dicionario para armazenar as caracteristicas dos deputados
    dado_deputado ={}
    #puxa todas as despessas da variavel dados
    lista_despesas = dados.findall("DESPESAS")
    #laço de repetição para puxar todas as despesas
    for despesa in lista_despesas:

        for informacao in despesa:

            atributo = informacao.getchildren()#está puxando as despesas

            if atributo[18].tag == "vlrLiquido":
                #nome do deputado
                nome = atributo[0].text 
                #De onde a despesa veio 
                categoria = atributo[8].text
                #valor da despesa 
                valor_despesa = atributo[18].text
                #Modelando o dado colocando ,00 no fim
                if "," not in valor_despesa:
                    valor_despesa = valor_despesa+",00"
                #alterando ,00 para .00
                valor_despesa = float(valor_despesa.replace(",","."))
                #laço de repetição para adicionar o nome do deputado no dicionário 
                if nome in dado_deputado:
                    dado = dado_deputado[nome]
                    if categoria in dado:
                        dado[categoria] += valor_despesa
                    else :
                        dado[categoria] = valor_despesa
                    dado_deputado[nome] = dado 
                else: 
                    dic = {}
                    dic[categoria] = valor_despesa
                    dado_deputado[nome] = dic
    return dado_deputado

def formatar_valor(valor):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    valor = locale.currency(valor, grouping=True , symbol=None)
    locale.setlocale(locale.LC_ALL, '')
    return valor
if __name__ =="__main__":
    dicionario = carregar_dados()

    while True:
        total_depesas = 0
        deputado = input("informe o nome do deputado (ou -  0  / zero para sair )  : " ).upper()
        if deputado == "0" :
            break
        elif deputado in dicionario:
            for chave,valor in dicionario[deputado].items():
                total_depesas += valor
                valor = formatar_valor(valor)

                print(f"{chave} : {valor}")
        else:
            input("Deputado não localizado,pressione qualquer tecla para ver a lista de deputados ! : ")
            for nome in dicionario.keys():
                print(nome)
        total_depesas = formatar_valor(total_depesas) 

        print(f"Total despesas : {total_depesas}")
    print("--- Obrigado por utilizar o sistema ! ---")    
        


                


    
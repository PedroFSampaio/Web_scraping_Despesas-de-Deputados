## Despesas de Deputados - Análise XML
Este projeto é um script Python que processa e exibe informações sobre despesas de deputados a partir de um arquivo XML. Ele organiza as despesas por categorias, calcula o valor total gasto por cada deputado e formata os valores para serem exibidos no formato de moeda brasileiro.
## Funcionalidades
Carregamento de Dados: O script carrega um arquivo XML contendo informações de despesas.
Organização por Deputado: As despesas são agrupadas por nome de deputado e categoria de despesa.
Consulta Interativa: O usuário pode consultar despesas de um deputado específico e ver o total de despesas por categoria.
Formatação Monetária: Os valores das despesas são formatados no estilo monetário brasileiro, com separação de milhares e símbolo de moeda.
# Exemplo de uso :
~~~
Informe o nome do deputado (ou - 0 - zero para sair) : JOÃO DA SILVA
TRANSPORTE : 1.250,00
ALIMENTAÇÃO : 800,00
Total despesas: 2.050,00 
~~~
**Se o nome do deputado não for encontrado, será apresentada uma lista de todos os deputados disponíveis.**

## Descrição Resumida do Código:
O script lê um arquivo XML contendo despesas de deputados, organiza os dados em um dicionário e oferece uma interface simples para o usuário consultar o nome de um deputado e visualizar suas despesas por categoria. O valor de cada despesa é formatado em reais (R$), e o total de despesas é calculado e exibido ao final.

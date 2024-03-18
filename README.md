<div align="center">
<h1>Análise de <em>churn</em> para uma empresa do setor financeiro 📉💼</h1>
<img src="imgs/cliente.png" height="400" alt="Mapa mental dos dados">
</div>

## Contexto 📚

 O <em>*churn*</em>, ou seja, a taxa de cancelamento de clientes, é um desafio crucial para diversas empresas. A perda de clientes pode acarretar em uma significativa redução de receita. Ao contrário da aquisição de novos clientes, que geralmente é mais custosa, a retenção apresenta um custo menor. Diante disso, torna-se essencial identificar os fatores que impulsionam a desistência e implementar estratégias para minimizar o *churn*.

A perda de clientes não se limita apenas à diminuição da receita. Ela também inclui custos adicionais para adquirir novos clientes, bem como a perda da receita recorrente, que contribue para uma previsibilidade financeira a longo prazo. Além disso, o *churn* pode afetar a reputação da empresa, já que consumidores insatisfeitos tendem a compartilhar experiências negativas com outros *leads*.

Para muitas empresas, o modelo de negócio depende significativamente da receita recorrente, proveniente da assinatura dos serviços oferecidos. Mesmo com uma taxa baixa de *churn*, a companhia pode enfrentar impactos consideráveis na receita. A Figura 1 apresenta o fluxo seguido pelos clientes da empresa contratante durante o processo de cancelamento.

<div align="center">
<img src="imgs/fluxo_cancelamento.png" alt="Fluxo de cancelamento de clientes">
<br/>
<i>Figura 1: Fluxo de cancelamento de clientes</i>
</div>

Diante desse cenário, é fundamental descobrir os fatores que levam ao *churn* e implementar estratégias para mitigar esse problema. A empresa contratante busca reconhecer o potencial *churn* com certa antecedência, a fim de tomar medidas preventivas e entender melhor os fatores que impulsionam o cancelamento. Para isso, foram coletados dados de clientes ativos e aqueles que cancelaram o serviço, com o objetivo de desenvolver um modelo preditivo para identificar clientes com maior probabilidade de cancelamento.

## Objetivo 🎯

O objetivo deste projeto é analisar os dados da empresa contratante e desenvolver um modelo preditivo para identificar clientes com maior probabilidade de cancelamento. Para isso, será utilizado um conjunto de dados, contendo informações sobre os assinantes, como quantidade de funcionários, tempo de relacionamento com a companhia, uso do serviço, entre outros.

## Dados 🗄️

O conjunto de dados é composto por 21 colunas e 7043 linhas, sendo `Churn` a variável dependente que desejamos prever. A seguir, uma visão geral das colunas do conjunto de dados:
|Variável|Descrição|Tipo|Escala|
|---|---|---|---|
|`ID`|Identificação do cliente|Qualitativo|Nominal|
|`Tipo de empresa`|Tipo de empresa|Qualitativo|Nominal|
|`Fundação da empresa`|Ano de fundação da empresa|Quantitativo discreto|Racional|
|`Possui mais de um sócio`|Se a empresa possui mais de um sócio|Qualitativo|Nominal|
|`Funcionários`|Número de funcionários|Qualitativo|Ordinal|
|`Meses de permanência`|Quantidade de meses que o cliente permaneceu com o serviço|Quantitativo discreto| Racional|
|`Utiliza serviços financeiros`|Se o cliente utiliza serviços financeiros|Qualitativo|Nominal|
|`PossuiContador`|Se o cliente possui contador|Qualitativo|Nominal|
|`Faz conciliação bancária`|Tipo de conciliação bancária|Qualitativo|Nominal|
|`Frequência de utilização de feature do sistema: Módulo financeiro`|Frequência de utilização de feature do sistema|Qualitativo|Ordinal|
|`Frequência de utilização de feature do sistema: Emissão de nota fiscal`|Frequência de utilização de feature do sistema|Qualitativo|Ordinal|
|`Frequência de utilização de feature do sistema: Integração bancária`|Frequência de utilização de feature do sistema|Qualitativo|Ordinal|
|`Frequência de utilização de feature do sistema: Módulo de vendas`|Frequência de utilização de feature do sistema|Qualitativo|Ordinal|
|`Frequência de utilização de feature do sistema: Relatórios`|Frequência de utilização de feature do sistema|Qualitativo|Ordinal|
|`Frequência de utilização de feature do sistema: Utilização de APIs de integração`|Frequência de utilização de feature do sistema|Qualitativo|Ordinal|
|`Contrato`|Tipo de contrato|Qualitativo|Nominal|
|`Emite boletos`|Se emite boletos, sendo sim ou não|Qualitativo|Nominal|
|`Tipo de pagamento`|Tipo de pagamento|Qualitativo|Nominal|
|`Receita mensal`|Receita mensal do cliente|Quantitativo contínuo|Racional|
|`Receita total`|Receita total do cliente|Quantitativo contínuo|Racional|
|`Churn`|Se o cliente abandonou o serviço|Qualitativo|Nominal|


## Metodologia 📊

Neste projeto, utilizamos dados fornecidos pela empresa interessada. A análise exploratória foi o primeiro passo para compreender o conjunto de dados e identificar possíveis problemas, como valores ausentes, outliers e inconsistências. Durante a etapa de análise exploratória dos dados, identificamos a ausência de valores para as variáveis "**possui contador**" e "**receita total**" em alguns registros, sendo 682 e 11 respectivamente.

<div align="center">
<img src="imgs/valores_ausentes.png" alt="Gráfico destacando valores ausentes">
<br/>
<i>Figura 2: Frequência de valores ausentes por variável.</i>
</div>

Em nossa investigação, como apresentado Tabela 1, podemos verificar que clientes com receita total ausente tiveram meses de permanência zerados, nos levando a supor que, no momento da coleta, eles haviam adquirido o serviço a pouco tempo.

<div align="center">
<i>Tabela 1: Clientes com receita total ausente e meses de permanência zerados.</i>

|   id | tipo_de_empresa   |   fundacao_da_empresa | possui_mais_de_um_socio   | funcionarios           |   receita_total |   meses_de_permanencia | churn   |
|-----:|:------------------|----------------------:|:--------------------------|:-----------------------|----------------:|-----------------------:|:--------|
|  489 | Micro empresa     |                  2019 | Sim                       | 6 ou mais funcionários |             nan |                      0 | Não     |
|  754 | Pequena empresa   |                  2019 | Não                       | 6 ou mais funcionários |             nan |                      0 | Não     |
|  937 | Micro empresa     |                  2020 | Sim                       | 6 ou mais funcionários |             nan |                      0 | Não     |
| 1083 | Pequena empresa   |                  2020 | Sim                       | 6 ou mais funcionários |             nan |                      0 | Não     |
| 1341 | Micro empresa     |                  2019 | Sim                       | 6 ou mais funcionários |             nan |                      0 | Não     |
| 3332 | Pequena empresa   |                  2016 | Sim                       | 6 ou mais funcionários |             nan |                      0 | Não     |
| 3827 | Pequena empresa   |                  2016 | Sim                       | 6 ou mais funcionários |             nan |                      0 | Não     |
| 4381 | Micro empresa     |                  2017 | Sim                       | 6 ou mais funcionários |             nan |                      0 | Não     |
| 5219 | Pequena empresa   |                  2018 | Sim                       | 6 ou mais funcionários |             nan |                      0 | Não     |
| 6671 | Micro empresa     |                  2016 | Sim                       | 6 ou mais funcionários |             nan |                      0 | Não     |
| 6755 | Pequena empresa   |                  2020 | Não                       | 6 ou mais funcionários |             nan |                      0 | Não     |
</div>

Para lidar com os valores ausentes, optamos por preencher os valores ausentes da variável "**receita total**" com o valor da "**receita mensal**" na modelagem, notamos que ao multiplicar a receita mensal pelo tempo de permanência, obtemos um valor próximo da receita total. A Tabela 2 apresenta a comparação entre a receita total corrigida e a receita total original. Quando o total de mês de permanência é igual a 1, a receita total corrigida foi igual a receita mensal.


<div align="center">
<i>Tabela 2: Comparação entre a receita total corrigida e a receita total original.</i>

|       |   receita_mensal |   meses_de_permanencia |   receita_total_corrigida |   receita_total |
|:------|-----------------:|-----------------------:|--------------------------:|----------------:|
| count |        7025      |              7025      |                   7025    |         7025    |
| mean  |          64.8319 |                32.4531 |                   2285.39 |         2285.54 |
| std   |          30.0765 |                24.5374 |                   2264.71 |         2266.78 |
| min   |          18.25   |                 1      |                     18.8  |           18.8  |
| 25%   |          35.65   |                 9      |                    399.6  |          402.6  |
| 50%   |          70.4    |                29      |                   1396.8  |         1399.35 |
| 75%   |          89.9    |                55      |                   3792.25 |         3801.3  |
| max   |         118.75   |                72      |                   8550    |         8684.8  |
</div>


Com relação a variável "**possui contador**", a razão provável para isso pode ser oriúnda de vários fatores como:

- O cliente não quis informar.
- O atributo poderia não existir na época em que os dados foram coletados.
- Distração do preenchimento do formulário.
- Problemas técnicos na coleta de dados.
- A informação não era conhecida na época da coleta de dados.


### Análise exploratória dos dados

A análise exploratória dos dados foi realizada com o intuito de compreender o comportamento das variáveis e identificar possíveis padrões. A Figura 3 apresenta a distribuição da variável dependente, **churn**, que indica se o cliente cancelou o serviço. Aproximadamente 26,5% dos registros do conjunto de dados correspondem a clientes que cancelaram o serviço.

<div align="center">
<img src="imgs/distribuicao_churn.png" alt="Distribuição da variável churn" height="150">
<br/>
<i>Figura 3: Distribuição da variável churn.</i>
</div>


A análise comparativa da "**receita mensal**" entre clientes que cancelaram o serviço e aqueles que permaneceram ativos revelou uma diferença na tendência dos dados. Observamos que clientes que tinham uma receita mensal maior tinham mais churn. Já para a variável "**meses de permanência**", notamos que a maioria dos clientes que cancelaram o serviço permaneceu por um período menor em comparação com os clientes ativos. A Figura 4 apresenta um histograma comparativo de todas as variáveis numéricas.

<div align="center">
<img src="imgs/hist_numericas.png" alt="Histograma das variáveis numéricas">
<br/>
<i>Figura 4: Histograma das variáveis numéricas</i>
</div>

Com relação as variáveis nominais, há aquelas que se encaixam na frequência de uso do sistema e as demais. Para o uso do sistema, a maioria dos usuários faz *pouco uso* das features do sistema. Quando olhamos por frequência de uso, notamos que os clientes que cancelaram o serviço utilizavam menos as features do sistema em comparação com os clientes ativos. A Figura 5 apresenta um gráfico comparativo da frequência de uso das features do sistema. Daqueles que deram *churn*, a *feature* de *pouco uso* mais utilizada foi o "**módulo financeiro**", seguido pelo "**módulo de vendas**".

<div align="center">
<img src="imgs/freq_uso_sistema.png" alt="Frequência de uso das features do sistema">
<br/>
<i>Figura 5: Frequência de uso das features do sistema</i>
</div>

Já para as demais variáveis nominais, notamos que a maioria dos clientes que cancelaram o serviço tinham **contrato** *mês-a-mês*, *emitiam boletos* e a **forma de pagamento** preferida via *boleto*. A Figura 6 apresenta um gráfico comparativo das variáveis nominais.

<div align="center">
<img src="imgs/variaveis_nominais.png" alt="Gráfico comparativo das variáveis nominais">
<br/>
<i>Figura 6: Gráfico comparativo das variáveis nominais</i>
</div>

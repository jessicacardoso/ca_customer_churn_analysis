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

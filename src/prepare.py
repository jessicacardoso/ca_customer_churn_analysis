import pandas as pd
import pandas_gbq
from loguru import logger
from sklearn.model_selection import train_test_split

from src.utils import lru_cache_disk


def categorize_column(
    data: pd.DataFrame, column: str, categories: list[str] | None = None
) -> pd.Categorical:
    """Converte uma coluna em uma categoria pandas.

    Args:
        data (pd.DataFrame): DataFrame contendo os dados.
        column (str): Nome da coluna a ser categorizada.
        categories (list[str], optional): Lista de categorias.
        Defaults to None.

    Returns:
        pd.Categorical: Coluna categorizada.
    """
    return pd.Categorical(data[column], categories=categories, ordered=True)


@lru_cache_disk(maxsize=1)
def load_data(
    project_id: str, database_name: str, table_name: str
) -> pd.DataFrame:
    """Carrega os dados do BigQuery.

    Args:
        project_id (str): ID do projeto do BigQuery.
        database_name (str): Nome do banco de dados.
        table_name (str): Nome da tabela.

    Returns:
        pd.DataFrame: Dados carregados.
    """
    query = f"""
    SELECT
        *
    FROM
        `{project_id}.{database_name}.{table_name}`
    """
    logger.info(f"Carregando dados do BigQuery: {query}")
    return pandas_gbq.read_gbq(query, project_id=project_id)


def split_data(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Separa os dados em treino e teste.

    Args:
        data (pd.DataFrame): Dados carregados do BigQuery.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: Dados de treino e teste.
    """

    return train_test_split(
        data, test_size=0.2, random_state=42, stratify=data["churn"]
    )


def prepare_data(
    project_id: str, database_name: str, table_name: str
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Carrega os dados do BigQuery e separa em treino e teste.

    Args:
        project_id (str): ID do projeto do BigQuery.
        database_name (str, optional): Nome do banco de dados.
        Defaults to "churn".
        table_name (str, optional): Nome da tabela. Defaults to "data".

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: Dados de treino e teste.
    """
    data = load_data(
        project_id=project_id,
        database_name=database_name,
        table_name=table_name,
    )

    # Categorizando as variáveis
    service_categories = ["Nunca utilizou", "Pouco uso", "Uso frequente"]
    categorical_columns = [
        ("funcionarios", ["até 5 funcionários", "6 ou mais funcionários"]),
        ("contrato", ["Mês-a-mês", "Trimestral", "Anual"]),
        ("frequencia_de_pagamento", ["mês a mês", "pagamento único"]),
        ("_emissao_de_nota_fiscal", service_categories),
        ("_integracao_bancaria", service_categories),
        ("_modulo_de_vendas", service_categories),
        ("_modulo_financeiro", service_categories),
        ("_relatorios", service_categories),
        ("_utilizacao_de_apis_de_integracao", service_categories),
        ("tipo_de_empresa", ["Micro empresa", "Pequena empresa"]),
        ("faz_conciliacao_bancaria", None),  # automática', manual ou não faz
        ("forma_de_pagamento", None),  # Boleto ou Cartão de crédito
        ("possuicontador", None),  # Não, Sim ou NaN
    ]

    for column, categories in categorical_columns:
        if categories:
            data[column] = categorize_column(data, column, categories)
        else:
            data[column] = pd.Categorical(data[column])

    data = data.set_index("id")
    data = data.drop_duplicates()

    train, test = split_data(data)
    logger.info(f"Dados de treino: {train.shape}")
    logger.info(f"Dados de teste: {test.shape}")
    return train, test

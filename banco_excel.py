# -*- coding: utf-8 -*-
"""
Módulo de acesso a dados via Microsoft Excel (openpyxl + pandas).
Substitui a conexão com PostgreSQL. Os dados são armazenados em 'churras.xlsx'
com duas planilhas: Pessoa e Juiz.
"""
import pandas as pd
import os
from datetime import date

_EXCEL_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "churras.xlsx")


def _load():
    """Lê as planilhas do Excel e retorna dois DataFrames: Pessoa e Juiz."""
    if not os.path.exists(_EXCEL_FILE):
        inicializar_banco()
    df_pessoa = pd.read_excel(_EXCEL_FILE, sheet_name="Pessoa")
    df_juiz = pd.read_excel(_EXCEL_FILE, sheet_name="Juiz")
    df_pessoa["id"] = pd.to_numeric(df_pessoa["id"], errors="coerce").fillna(0).astype(int)
    df_juiz["pessoa_id"] = pd.to_numeric(df_juiz["pessoa_id"], errors="coerce").fillna(0).astype(int)
    return df_pessoa, df_juiz


def _save(df_pessoa, df_juiz):
    """Salva os DataFrames no arquivo Excel."""
    with pd.ExcelWriter(_EXCEL_FILE, engine="openpyxl") as writer:
        df_pessoa.to_excel(writer, sheet_name="Pessoa", index=False)
        df_juiz.to_excel(writer, sheet_name="Juiz", index=False)


def inicializar_banco():
    """Cria o arquivo Excel com dados iniciais (executado automaticamente na primeira vez)."""
    if os.path.exists(_EXCEL_FILE):
        return
    df_pessoa = pd.DataFrame({
        "id": [1, 2, 3],
        "nome": ["João Silva", "Maria Garcia", "Peter Jones"],
        "pais_origem": ["Brasil", "Espanha", "Estados Unidos"],
        "telefone": [None, None, None],
        "data_nascimento": [None, None, None],
    })
    df_juiz = pd.DataFrame({
        "pessoa_id": [1, 2, 3],
        "data_inicio": [date(2020, 9, 12), date(2010, 3, 15), date(2019, 11, 30)],
        "cargo": ["Chef Executivo", "Crítica Gastronômica", "Mestre Churrasqueiro"],
    })
    _save(df_pessoa, df_juiz)
    print("Arquivo 'churras.xlsx' criado com dados iniciais.")


def get_paises():
    """Retorna lista ordenada de países distintos."""
    df_pessoa, _ = _load()
    return sorted(df_pessoa["pais_origem"].dropna().unique().tolist())


def get_cargos():
    """Retorna lista ordenada de cargos distintos."""
    _, df_juiz = _load()
    return sorted(df_juiz["cargo"].dropna().unique().tolist())


def get_total_juizes():
    """Retorna o total de juízes cadastrados."""
    _, df_juiz = _load()
    return len(df_juiz)


def get_total_paises():
    """Retorna a quantidade de países distintos representados."""
    df_pessoa, _ = _load()
    return int(df_pessoa["pais_origem"].dropna().nunique())


def get_total_mestres():
    """Retorna o total de Mestres Churrasqueiros."""
    _, df_juiz = _load()
    return int((df_juiz["cargo"] == "Mestre Churrasqueiro").sum())


def get_juizes(filtro_pais=None, filtro_cargo=None):
    """
    Retorna lista de tuplas (id, nome, pais_origem, cargo, data_inicio).
    Filtros por país e por cargo são aplicados com lógica OR.
    """
    df_pessoa, df_juiz = _load()
    df = df_juiz.merge(df_pessoa, left_on="pessoa_id", right_on="id")

    if (filtro_pais and filtro_pais != "Todos") or (filtro_cargo and filtro_cargo != "Todos"):
        mask = pd.Series(False, index=df.index)
        if filtro_pais and filtro_pais != "Todos":
            mask = mask | (df["pais_origem"] == filtro_pais)
        if filtro_cargo and filtro_cargo != "Todos":
            mask = mask | (df["cargo"] == filtro_cargo)
        df = df[mask]

    df = df.sort_values("id")
    resultado = []
    for _, row in df.iterrows():
        data = row["data_inicio"]
        if pd.isna(data):
            data = date.today()
        elif hasattr(data, "date") and callable(data.date):
            data = data.date()
        resultado.append((int(row["id"]), str(row["nome"]), str(row["pais_origem"]), str(row["cargo"]), data))
    return resultado


def inserir_juiz(nome, pais_origem, cargo, telefone, data_nascimento, data_inicio):
    """Insere um novo juiz nas planilhas Pessoa e Juiz."""
    df_pessoa, df_juiz = _load()
    next_id = int(df_pessoa["id"].max()) + 1 if len(df_pessoa) > 0 else 1

    nova_pessoa = pd.DataFrame([{
        "id": next_id,
        "nome": nome,
        "pais_origem": pais_origem,
        "telefone": telefone,
        "data_nascimento": data_nascimento,
    }])
    novo_juiz = pd.DataFrame([{
        "pessoa_id": next_id,
        "data_inicio": data_inicio,
        "cargo": cargo,
    }])

    df_pessoa = pd.concat([df_pessoa, nova_pessoa], ignore_index=True)
    df_juiz = pd.concat([df_juiz, novo_juiz], ignore_index=True)
    _save(df_pessoa, df_juiz)
    return next_id


def excluir_juiz(juiz_id):
    """Remove o juiz e a pessoa associada pelo ID."""
    df_pessoa, df_juiz = _load()
    df_juiz = df_juiz[df_juiz["pessoa_id"] != juiz_id]
    df_pessoa = df_pessoa[df_pessoa["id"] != juiz_id]
    _save(df_pessoa, df_juiz)

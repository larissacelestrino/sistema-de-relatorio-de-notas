import streamlit as st
import matplotlib.pyplot as plt
import os

# Caminho do arquivo de armazenamento
ARQUIVO = "alunos.txt"

# Função para salvar aluno no arquivo
def salvar_aluno(nome, serie, nota1, nota2, nota3):
    with open(ARQUIVO, "a") as f:
        f.write(f"{nome},{serie},{nota1},{nota2},{nota3}\n")

# Função para ler alunos do arquivo
def ler_alunos():
    alunos = []
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 5:
                    nome, serie, n1, n2, n3 = partes
                    alunos.append({
                        "nome": nome,
                        "serie": serie,
                        "nota1": float(n1),
                        "nota2": float(n2),
                        "nota3": float(n3)
                    })
    return alunos

# Função para calcular média final de um aluno
def media_final(aluno):
    return (aluno["nota1"] + aluno["nota2"] + aluno["nota3"]) / 3

# Função para calcular média geral por série
def media_geral_serie(serie, alunos):
    notas = [media_final(a) for a in alunos if a["serie"] == serie]
    if notas:
        return sum(notas) / len(notas)
    return 0

# --- Interface Streamlit ---
st.title("Sistema de Notas de Alunos")

menu = st.sidebar.selectbox("Menu", ["Cadastrar Aluno", "Visualizar Relatórios"])

if menu == "Cadastrar Aluno":
    st.subheader("Cadastro de Aluno")
    nome = st.text_input("Nome do Aluno")
    serie = st.selectbox("Série", ["1D", "2D", "3D"])
    nota1 = st.number_input("Nota 1", min_value=0.0, max_value=10.0, step=0.1)
    nota2 = st.number_input("Nota 2", min_value=0.0, max_value=10.0, step=0.1)
    nota3 = st.number_input("Nota 3", min_value=0.0, max_value=10.0, step=0.1)
    
    if st.button("Salvar"):
        if nome.strip() != "":
            salvar_aluno(nome, serie, nota1, nota2, nota3)
            st.success(f"Aluno {nome} cadastrado com sucesso!")
        else:
            st.error("Digite um nome válido.")

elif menu == "Visualizar Relatórios":
    st.subheader("Relatórios de Notas")
    alunos = ler_alunos()
    
    if not alunos:
        st.warning("Nenhum aluno cadastrado ainda.")
    else:
        series = sorted(list(set([a["serie"] for a in alunos])))
        serie_selecionada = st.selectbox("Selecione a série", series)
        
        # Média geral da série
        media_serie = media_geral_serie(serie_selecionada, alunos)
        st.write(f"Média geral da série {serie_selecionada}: {media_serie:.2f}")
        
        # Distribuição das médias
        nomes = [a["nome"] for a in alunos if a["serie"] == serie_selecionada]
        medias = [media_final(a) for a in alunos if a["serie"] == serie_selecionada]
        
        if nomes:
            fig, ax = plt.subplots()
            ax.bar(nomes, medias, color='skyblue')
            plt.xticks(rotation=45, ha="right")
            ax.set_ylabel("Média Final")
            ax.set_title(f"Médias dos Alunos - {serie_selecionada}")
            st.pyplot(fig)
        else:
            st.info("Nenhum aluno nesta série.")

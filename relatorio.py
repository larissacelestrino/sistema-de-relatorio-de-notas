import streamlit as st
import matplotlib.pyplot as plt
from classes import aluno, notas_salvar, notas_separar


st.title(" Sistema de Relatórios de Notas")
nova_nota=[]
nota1d=[]
nota2d=[]
nota3d=[]
menu = st.selectbox("Menu", ["Cadstrar", "1D", '2D', "3D"])
if menu == "Cadstrar":
    st.subheader("Cadastro de notas")
    nome = st.text_input("Nome do alno")
    classe = st.selectbox("Selecione a turma", ("1D", '2D', '3D'))
    nota1 = st.number_input("Primeira nota", min_value=0.0, max_value=10.0)
    nota2 = st.number_input("Segunda nota", min_value=0.0, max_value=10.0)
    nota3 = st.number_input("Terceira nota", min_value=0.0, max_value=10.0)     
    if st.button ("Registrar nota"):
        nova_nota=aluno(nome, classe, nota1, nota2, nota3)
        notas_salvar([nova_nota])
        if classe == "1D":
            nota1d = notas_separar("1D")
        elif classe == "2D":
            nota2d = notas_separar("2D")
        elif classe == "3D":
            nota3d = notas_separar("3D")

if menu in ["1D", "2D", "3D"]:
    st.subheader(f"media geral e grafico de notas")
    alunos = notas_separar(menu)
    if alunos:
        medias = []
        nomes = []
        for nome, n1, n2, n3 in alunos:
            media = (n1 + n2 + n3) / 3
            medias.append(media)
            nomes.append(nome)

    media_geral = sum(medias) / len(medias)
    st.write(f"Média geral da sala: {media_geral}")
    if st.button("mostrar grafico com medias"):
        fig, ax = plt.subplots()
        plt.bar(nomes, medias)
        plt.ylim(0, 10)
        plt.ylabel('medias')
        plt.title('Gráfico de medias')
        st.pyplot(fig)

                
                    



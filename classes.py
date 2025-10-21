class aluno:
    def __init__(self, nome, idade, nota1, nota2, nota3):
        self.nome = nome
        self.idade = idade
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        def __str__(self):
            return (f"{self.nome}, {self.idade}, {self.nota1}, {self.nota2}, {self.nota3} \n")
def notas_salvar(aluno):
    with open("aluno.txt", "a") as arquivo:
            for a in aluno:
                arquivo.write(f" {a.nome}, {a.idade}, {a.nota1}, {a.nota2}, {a.nota3}\n")
def notas_separar(turma):
     alunos_turma=[]
     with open("aluno.txt", "r") as arquivo:
                for linha in arquivo:
                    partes = [p.strip() for p in linha.strip().split(",")]
                    classe= partes[1]
                    nome = partes[0]
                    nota1 = float(partes[2].strip())
                    nota2 = float(partes[3].strip())
                    nota3 = float(partes[4].strip())
                    if classe == turma:
                        alunos_turma.append((nome, nota1, nota2, nota3))
                return  alunos_turma

     
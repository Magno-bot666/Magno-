def insirir_nota():
    notas=[]
    for i in range(10):
        nota = int(input(f'Digite a nota do aluno { i + 1 }:'))

        notas.append(nota)
    return notas

def exibirN(notas):
    print('Notas em ordem decrescente')
    for nota in sorted(notas):
        print(nota)
    
    print('Notas em ordem decrescente')
    for nota in sorted(notas, reverse=True):
        print(nota)

def sla():
    notas = insirir_nota()
    exibirN(notas)
    notas_dez = notas.count(10)
    print(f'Quantidade de notas 10: {notas_dez}')
    
sla()  
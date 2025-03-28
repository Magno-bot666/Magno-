def ordenar_notas(notas):
    notas_crescentes = sorted(notas)
    notas_decrescentes = sorted(notas, reverse=True)

    print("Notas em ordem crescente:")
    print(notas_crescentes)
    
    print("Notas em ordem decrescente:")
    print(notas_decrescentes)

notas = []

for i in range(10):
    while True:
        try:
            nota = float(input(f"Digite a nota do aluno {i+1} (0 a 10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Por favor, insira uma nota válida entre 0 e 10.")
        except ValueError:
            print("Por favor, insira um número válido.")

ordenar_notas(notas)

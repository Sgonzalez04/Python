materias = ["fisica", "matematicas", "quimica", "historia", "lengua"]
aux = materias.copy()
i = 0
notas = []
while i < len(materias):
    nota = float(input(f"Ingrese la nota para {materias[i]}: "))
    if nota > 3:
        aux.remove(materias[i])
        notas.append(nota)    
    i += 1

print(notas)
print(aux)

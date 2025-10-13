materias = {
    'Matematicas':None,
    'Fisica':None,
    'Quimica':None,
    'Historia':None,
    'Lengua':None
}

for materia in materias:
    nota = input(f'Ingrese su nota en {materia} ')
    materias[materia] = nota

print(materias)


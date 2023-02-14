# Analizador léxico

file = open("read.py")

operadores = {
    '=': 'Operador Asignacion',
    '+': 'Operador Adición',
    '-': 'Operador sustracción',
    '/': 'Operador división',
    '*': 'Operador multiplicación',
    '<': 'Operador menor'
}

llaves_operadores = operadores.keys()

tipos_datos = {
    'int': 'Tipo Entero',
    'float': 'Punto flotante',
    'char': 'Tipo caracter',
    'long': 'Tipo long int'
}

llaves_tipos_datos = tipos_datos.keys()

simbolos_puntuacion = {
    ':': 'Dos puntos',
    ';': 'Punto y coma',
    '.': 'Punto',
    ',': 'Coma'
}
llaves_simbolo_puntuacion = simbolos_puntuacion.keys()

identificadores = {
    'x': 'id',
    'y': 'id',
    'z': 'id',
    'f': 'id'
}
llaves_identificador = identificadores.keys()

a = file.read()

numeroLinea = 0
# Obtenemos el código y lo dividimos por cada salto de línea
program = a.split('\n')
for line in program:
    
    numeroLinea = numeroLinea + 1
    print('Linea#', numeroLinea, "\n", line)

    tokens = line.split(' ')
    print("Los tokens son ", tokens)

    print('Linea#', numeroLinea, "Propiedades \n")
    for token in tokens:
        if token in llaves_operadores:
            print("El operador es ", operadores[token])
        
        if token in llaves_tipos_datos:
            print('El tipo de dato es: ', tipos_datos[token])
        
        if token in llaves_simbolo_puntuacion:
            print(token, 'El símbolo de puntuación es ', simbolos_puntuacion[token])
        
        if token in identificadores:
            print(token, "Identificador: ", [token])
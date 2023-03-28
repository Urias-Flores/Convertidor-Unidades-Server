import matplotlib.pyplot as plt
import numpy as np
import prettytable as pt
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.optimizers import Adam
from Utils import getInputValues
import os

print('Creando modelo...')
inputLayer = Dense(units = 1, input_shape=[3])
layer1 = Dense(units = 4)
layer2 = Dense(units = 4)
outputLayer = Dense(units = 1)
model = Sequential([inputLayer, layer1, layer2, outputLayer])
print('Modelo creado!')
os.system('pause')
os.system('cls')

print('Compilando modelo...')
model.compile( optimizer = Adam(0.1), loss = 'mean_squared_error')
print('Modelo compilado')
os.system('pause')
os.system('cls')

print('Obteniendo datos...')
values = getInputValues()
inputs = np.array(values[0])
outputs = np.array(values[1])
print('Datos obtenidos exitosamente!')
print('-------- Resumen de datos ----------')
table = pt.PrettyTable(['Index', 'Value', 'InputType', 'OutputType', 'Result'])
for index in range(0, len(inputs)):
    row = [index, inputs[index][0], inputs[index][1], inputs[index][2], outputs[index]]
    table.add_row(row)
print(table)
os.system('pause')
os.system('cls')

print('Entrenando modelo...')
nTrain = int(input('Ingrese el numero de entrenamientos: '))
for i in range (0, nTrain):
    print(f'Entrenando ({i + 1}/{nTrain})')
    model.fit(inputs, outputs, epochs = 500, verbose = False)
print('Modelo entrenado exitosamente!')
os.system('pause')
os.system('cls')

while True:
    os.system('cls')
    print('--------- Compilacion y entrenamiento exitoso ----------')
    print('1. Probar')
    print('2. Entrenar nuevamente')
    print('2. Guardar modelo')
    print('0. Salir')
    option = int(input('Seleccione una opcion: '))

    match option:
        case 1:
            value = int(input('Ingrese su valor de entrada: '))
            inputType = int(input('Ingrese el tipo de datos de entrada: '))
            outputType = int(input('Ingrese el tipo de dato de salida: '))
            testValue = np.array([[value, inputType, outputType]])
            print(f'Valor de prueba: {testValue}')
            print(f'Resultados: {model.predict(testValue)}')
        case 2:
            print('Entrenando nuevamente...')
            model.fit(inputs, outputs, epochs = 500, verbose = False)
            print('Modelo entrenado exitosamente!')
        case 3:
            model.save('conversion.h5')
            print('Modelo guardado exitosamente!')
        case 0:
            break
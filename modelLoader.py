import numpy as np
import random
import prettytable as pt
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.optimizers import Adam

def convertToMeters(value):
    return value * 1000

def convertToGrams(value):
    return value * 1000

def convertToPounds(value):
    return value * 2204.62

def getValues():
    nValues = int(input('Ingrese el numero de valores de prueba: '))
    type = 1
    inputValues = []
    outputValues= []
    values = []
    while type <= 3:
        for index in range (0, nValues + 1):
            randomNumber = random.randint(0, 500)
            inputValues.append(randomNumber)
            match type:
                case 1:
                    outputValues.append(convertToMeters(randomNumber))
                case 2:
                    outputValues.append(convertToGrams(randomNumber))
                case 3:
                    outputValues.append(convertToPounds(randomNumber))
        values.append(inputValues.copy())
        values.append(outputValues.copy())
        inputValues.clear()
        outputValues.clear()
        type += 1
    return values

def createModel():
    layer1 = Dense(units=3, input_shape = [1])
    layer2 = Dense(units=3)
    outputLayer = Dense(units=1)
    return Sequential([layer1, layer2, outputLayer])

def compileModel(model):
    model.compile( optimizer = Adam(0.5), loss = 'mse')

def trainModel(model, nTrain, x_train, y_train):
    print('Comenzando entrenamiento de modelo...')
    for n in range(0, nTrain):
        model.fit(x_train, y_train, epochs = 500, verbose = False)
        print(f'Entrenando ({n+1}/{nTrain})')

def saveModel(model, name):
    model.save(name)

def Init():
    values = getValues()

    KmMInfo = {
        'kmValues' : values[0],
        'mValues' : values[1],
        'name' : 'KmM.h5'
    }

    KgGInfo = {
        'kgValues': values[2],
        'gValues': values[3],
        'name': 'KgG.h5'
    }

    TonLInfo = {
        'tonValues': values[4],
        'poundValues': values[5],
        'name': 'TonL.h5'
    }

    info = {1 : KmMInfo, 2 : KgGInfo, 3 : TonLInfo}

    #Creacion de cada modelo
    modelKmM = createModel()
    modelKgG = createModel()
    modelTonePouns = createModel()

    #Compilacion de cada modelo
    compileModel(modelKmM)
    compileModel(modelKgG)
    compileModel(modelTonePouns)

    #Entranamiento de cada modelo
    nTrain = int(input('Ingrese el numero de entrenamientos de cada modelo: '))
    trainModel(modelKmM, nTrain, KmMInfo['kmValues'], KmMInfo['mValues'])
    trainModel(modelKgG, nTrain, KgGInfo['kgValues'], KgGInfo['gValues'])
    trainModel(modelTonePouns, nTrain, TonLInfo['tonValues'], TonLInfo['poundValues'])
    models = [modelKmM, modelKgG, modelTonePouns]
    counter = 1
    for model in models:
        while True:
            print('--------- Compilacion y entrenamientos exitoso ----------')
            print('1. Probar')
            print('2. Entrenar nuevamente')
            print('3. Guardar modelo')
            print('0. Salir')
            option = int(input('Seleccione una opcion: '))

            match option:
                case 1:
                    testValue = int(input('Ingrese su valor de entrada: '))
                    print(f'Valor de prueba: {testValue}')
                    print(f'Resultados: {model.predict([testValue])}')
                case 2:
                    print('Entrenando nuevamente...')
                    valueNames = {
                        1 : { 'Entries' : 'kmValues', 'Outputs' : 'mValues'},
                        2 : { 'Entries' : 'kgValues', 'Outputs' : 'gValues'},
                        3 : { 'Entries' : 'tonValues', 'Outputs' : 'poundValues'}
                    }
                    currentInfo = info[counter]
                    trainModel(
                        model,
                        1,
                        currentInfo[valueNames[counter]['Entries']],
                        currentInfo[valueNames[counter]['Outputs']])
                    print('Modelo entrenado exitosamente!')
                case 3:
                    saveModel(model, info[counter]['name'])
                    print('Modelo guardado exitosamente!')
                case 0:
                    break
        counter += 1

Init()
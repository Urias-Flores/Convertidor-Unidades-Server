import random
#Relacion de unidades

#Unidades de longitud
#milimetros = 1
#centimetros = 2
#metros = 3
#kilometros = 4
#pulgadas = 5
#pies = 6

#Unidades de masa
#gramos = 7
#miligramos = 8
#kilogramos = 9
#tonelados = 10

#Unidades de temperatura
#Celsius = 11
#Farenheti = 12
#Kelvin = 13

#Conversiones de longitud
def convertToMilimeters(Value, Type):
    relation = {
        1 : 1,
        2 : 10,
        3 : 1000,
        4 : 1000000,
        5 : 25.4,
        6 : 304.8
    }
    return float(Value * relation[Type])

def convertToCentimeters(Value, Type):
    relation = {
        1: 0.1,
        2: 1,
        3: 100,
        4: 100000,
        5: 2.54,
        6: 30.48
    }
    return float(Value * relation[Type])

def convertToMeters(Value, Type):
    relation = {
        1: 0.001,
        2: 0.01,
        3: 1,
        4: 1000,
        5: 0.0254,
        6: 0.3048
    }
    return float(Value * relation[Type])

def convertToKilometers(Value, Type):
    relation = {
        1: 0.000001,
        2: 0.00001,
        3: 0.002,
        4: 1,
        5: 0.0000254,
        6: 0.0003048
    }
    return float(Value * relation[Type])

def convertToInches(Value, Type):
    relation = {
        1: 0.0393701,
        2: 0.393701,
        3: 39.371,
        4: 39370.1,
        5: 1,
        6: 12
    }
    return float(Value * relation[Type])

def convertToFoot(Value, Type):
    relation = {
        1: 0.0393701,
        2: 0.0328084,
        3: 3.28,
        4: 3280.84,
        5: 0.83333333,
        6: 1
    }
    return float(Value * relation[Type])

#Unidades de masa
def convertToGram(Value, Type):
    relation = {
        7: 1,
        8: 0.001,
        9: 1000,
        10: 1000000,
    }
    return float(Value * relation[Type])

def convertToMiligram(Value, Type):
    relation = {
        7: 1000,
        8: 1,
        9: 1000000,
        10: 1000000000,
    }
    return float(Value * relation[Type])

def convertToKilogram(Value, Type):
    relation = {
        7: 0.001,
        8: 0.000001,
        9: 1,
        10: 1000,
    }
    return float(Value * relation[Type])

def convertToTone(Value, Type):
    relation = {
        7: 0.000001,
        8: 0.000000001,
        9: 0.001,
        10: 1,
    }
    return float(Value * relation[Type])

#Unidades de temperatura
def convertToCelsius(Value, Type):
    relation = {
        11: Value,
        12: (5/9) * (Value - 32),
        13:  Value - 273.15
    }
    return float(relation[Type])

def convertToFarenheit(Value, Type):
    relation = {
        11: (Value * (9/5)) + 32,
        12: Value,
        13: ((Value - 273.15) * (9/5)) + 32
    }
    return float(relation[Type])


def convertToKelvin(Value, Type):
    relation = {
        11: Value + 273.15,
        12: ((Value - 32) * (5/9))+273.15,
        13: Value
    }
    return float(relation[Type])

def getInputValues():
    counter = 0
    inputs = []
    outputs = []
    nValues = int(input('Ingrese el numero de datos de prueba por tipo de conversion: '))
    for inputType in range(1, 13+1):
        for outputType in range(1, 13+1):
            for index in range(1, nValues + 1):
                Value = random.randint(1, 500)
                #Value = float(index)
                counter += 1
                if inputType in (1, 2, 3):
                    match outputType:
                        case 1:
                            inputs.append([Value, inputType, outputType])
                            outputs.append(convertToMilimeters(Value, inputType))
                        case 2:
                            inputs.append([Value, inputType, outputType])
                            outputs.append(convertToCentimeters(Value, inputType))
                        case 3:
                            inputs.append([Value, inputType, outputType])
                            outputs.append(convertToMeters(Value, inputType))
                        case 4:
                            inputs.append([Value, inputType, outputType])
                            outputs.append(convertToKilometers(Value, inputType))
                        case 5:
                            inputs.append([Value, inputType, outputType])
                            outputs.append(convertToInches(Value, inputType))
                        case 6:
                            inputs.append([Value, inputType, outputType])
                            outputs.append(convertToFoot(Value, inputType))
                if inputType in (7, 8, 9, 10):
                    match outputType:
                        case 7:
                            inputs.append([Value, inputType, outputType])
                            outputs.append(convertToGram(Value, inputType))
                        case 8:
                            inputs.append([Value, inputType, outputType])
                            outputs.append(convertToMiligram(Value, inputType))
                        case 9:
                            inputs.append([Value, inputType, outputType])
                            outputs.append(convertToKilogram(Value, inputType))
                        case 10:
                            inputs.append([Value, inputType, outputType])
                            outputs.append(convertToTone(Value, inputType))
                if inputType in (11, 12, 13):
                    match outputType:
                        case 11:
                            inputs.append([Value, inputType, outputType])
                            outputs.append(convertToCelsius(Value, inputType))
                        case 12:
                            inputs.append([Value, inputType, outputType])
                            outputs.append(convertToFarenheit(Value, inputType))
                        case 13:
                            inputs.append([Value, inputType, outputType])
                            outputs.append(convertToKelvin(Value, inputType))

    print(f'Numero de datos generados: {counter}')
    return [inputs, outputs]

def printData():
    inputs = getInputValues()
    for index in range(0, len(inputs[0])):
        entry = inputs[0][index]
        out = inputs[1][index]
        print(f'Entrada de datos: {entry}')
        print(f'Resultado: {out}')

#printData()
import tensorflow as tf

modelo = tf.keras.models.load_model('Models/KmM.h5')
modelo1 = tf.keras.models.load_model('Models/KgG.h5')
modelo2 = tf.keras.models.load_model('Models/TonL.h5')

def convertToMeter(km):
    global modelo
    return modelo.predict([km])

def convertToKilogram(g):
    global modelo1
    return modelo1.predict([g])

def convertToPounds(tone):
    modelo2
    return modelo2.predict([tone])
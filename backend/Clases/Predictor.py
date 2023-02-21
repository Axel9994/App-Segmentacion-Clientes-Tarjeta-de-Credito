from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from joblib import load

class Predictor:

    def __init__(self):
        self.pipeline = load('/app/Clases/pipeline.joblib')
        self.descripcion = {
            1: "Consumidor de balance alto y consumo frecuente",
            2: "Consumidor de balance bajo y consumo frecuente",
            3: "Consumidor de balance alto y consumo poco frecuente",
            4: "Consumidor de balance bajo y consumo poco frecuente"
        }

    def transformar(self, X):
        return [[
            float(X['BALANCE']),
            float(X['PURCHASES']),
            float(X['CASH_ADVANCE']),
            float(X['PURCHASES_FREQUENCY']),
            float(X['CASH_ADVANCE_FREQUENCY']),
            float(X['CREDIT_LIMIT']),
            float(X['PAYMENTS'])
        ]]


    def predecir(self, X):
        XN = self.transformar(X)
        return self.pipeline.predict(XN)[0] + 1
    
    def obtenerDescripcion(self , cluster):
        
        return self.descripcion[cluster]


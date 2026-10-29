import pandas as pd
import numpy as np

serie_amigos = ["Nicole", "Alejandra", "Karla", "Edgar", "Erick", "Cristian"]
print("---Serie listado de amigos NC 0120---")
amigos = pd.Series(serie_amigos)
print(amigos)

serie_billetes = [20, 50, 100, 200, 500, 1000]
print("---Serie listado Valor de billeteras MX NC 0120---")
amigos = pd.Series(serie_billetes)
print(amigos)

serie_billetes = [20, 50, 100, 200, 500, 1000]
serie_billeteras = ["Veinte", "Cincuenta", "Cien", "Doscientos", "Quinientos", "Mil"]
print("---Serie listado nombre y valor de billeteras MX NC 0120---")
tablabilletes = pd.Series(serie_billetes,serie_billeteras)
print(tablabilletes)
# diccionario dataframe
# diccionario de valor monedas y nombre
dic_monedas={
    "serie_billetes":[20, 50, 100, 200, 500, 1000],
    "serie_billeteras":["Veinte", "Cincuenta", "Cien", "Doscientos", "Quinientos", "Mil"]

}
tablabilletes=pd.DataFrame(dic_monedas,index=["A","B","C","D","E","F"])
print(tablabilletes)

print("Casa de cambio de Nicole Robles NC 0120")
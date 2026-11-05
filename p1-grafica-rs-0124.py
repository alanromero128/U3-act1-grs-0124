import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#crearemos nuestra tabla y la guardaremos con pandas
# tenemos 5 listas de redes sociales con 4 elementos por lista
fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkdin', 7277, False, 2012]
# Creamos una lista de listas 
lista_redes_sociales=[fb,twt,ig,wsp,tel,lkn]
#print(lista_redes_sociales)
# utilizar panda para organizar la tabla (DatFrame o marco de datos)
df_redes_sociales=pd.DataFrame(lista_redes_sociales,columns=["Nombre","Cantidad","Es_FB","Año"])
print(df_redes_sociales)
df_redes_sociales.to_csv("redessociales.csv",index=False)
# Crear grafica de lineas 
# Donde X es Nombre en el eje horizontal 
# donde Y es Cantidad en el eje vertical   
plt.plot(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.title("Grafica redes sociales 0124")
plt.xlabel("Nombre de las redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
# creamos grafica de puntos
plt.scatter(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.show()
# Grafica de barras
plt.bar(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
#Etiquetas y titulo
plt.title("Redes Sociales 0124")
plt.xlabel("Las redes")
plt.ylabel("Cantidad de usuarios")
#mostrar grafica
plt.show()
#ordenar la grafica de barras de manera decendente
#de la mas grande a la mas pequeña
df_rs_ordenar=df_redes_sociales.sort_values("Cantidad",ascending=False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"])
plt.show()
# coloreando barra
df_rs_ordenar=df_redes_sociales.sort_values("Cantidad",ascending=False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"],     
color=[ "b","g","c","m","y","r"] ) 
plt.show()
# Grafica de pastel 
#plt.plot(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.pie(df_redes_sociales["Cantidad"],labels=df_redes_sociales["Nombre"])
plt.show()
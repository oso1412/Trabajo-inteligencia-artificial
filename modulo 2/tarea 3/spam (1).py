# Estas librerías se deben instalar si no las tiene. Use pip install pandas numpy nltk scikit-learn
import tkinter as tk  # Para la interfaz gráfica
from tkinter import filedialog, messagebox, ttk  # Componentes adicionales de la interfaz
import pandas as pd  # Para manipular el dataset en formato tabla
import numpy as np  # Para operaciones matemáticas y de arrays
import re  # Para expresiones regulares, limpieza de texto
import unicodedata  # Para eliminar acentos
import nltk  # Para procesamiento de lenguaje natural
from nltk.corpus import stopwords  # Palabras vacías (stopwords) en español
from sklearn.feature_extraction.text import TfidfVectorizer  # Vectorización TF-IDF

nltk.download('stopwords')  # Descarga lista de palabras vacías
nltk.download('punkt')  # Tokenizador de palabras

# Cargar las stopwords en español
stop_words = set(stopwords.words('spanish'))

# Función para eliminar acentos del texto
def quitar_acentos(texto):
    texto = unicodedata.normalize('NFKD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')
    return str(texto)

# Función para limpiar el texto: pasar a minúsculas, quitar acentos y símbolos no alfanuméricos
def limpiar_texto(texto):
    texto = texto.lower().strip()
    texto = quitar_acentos(texto)
    texto = re.sub(r"[^a-z0-9\s]", "", texto)
    return texto

# Cargar el dataset CSV (debe estar en la ruta indicada o cambiar la ruta)
df = pd.read_csv("./data/spam_ham_dataset2.csv")
    
# Normalizar etiquetas ('spam' o 'ham') y limpiar los mensajes
df["etiqueta"] = df["etiqueta"].astype(str).str.lower().str.strip()
df["mensaje_limpio"] = df["mensaje"].astype(str).apply(limpiar_texto)

# Vectorizar el texto usando TF-IDF (en inglés por defecto)
vectorizer = TfidfVectorizer(stop_words="english")
X_tfidf = vectorizer.fit_transform(df["mensaje_limpio"])
palabras = vectorizer.get_feature_names_out()  # Lista de palabras usadas

# Separar mensajes spam y no spam (ham)
spam = df[df["etiqueta"] == "spam"]
ham = df[df["etiqueta"] == "ham"]

# Calcular probabilidades base de spam y ham
P_spam = len(spam) / len(df)
P_no_spam = len(ham) / len(df)

# Vectorizar ambos subconjuntos
X_spam = vectorizer.transform(spam["mensaje_limpio"])
X_ham = vectorizer.transform(ham["mensaje_limpio"])

# Suavizado (Laplace) para evitar ceros
alpha = 1
P_caracteristicas_spam = (np.sum(X_spam.toarray(), axis=0) + alpha) / (np.sum(X_spam.toarray()) + alpha * len(palabras))
P_caracteristicas_no_spam = (np.sum(X_ham.toarray(), axis=0) + alpha) / (np.sum(X_ham.toarray()) + alpha * len(palabras))

# Función para clasificar un correo como spam o ham usando Naive Bayes con log-probabilidades
def clasificar_correo(texto):
    texto = limpiar_texto(texto)
    texto_vectorizado = vectorizer.transform([texto]).toarray()[0]
    log_P_spam = np.log(P_spam) + np.sum(np.log(P_caracteristicas_spam) * texto_vectorizado)
    log_P_no_spam = np.log(P_no_spam) + np.sum(np.log(P_caracteristicas_no_spam) * texto_vectorizado)
    return "spam" if log_P_spam > log_P_no_spam else "ham"

# Evaluación básica del modelo
df["prediccion"] = df["mensaje_limpio"].apply(clasificar_correo)
precision = np.mean(df["prediccion"] == df["etiqueta"])  # Exactitud del modelo
recuperacion = np.sum((df["prediccion"] == "spam") & (df["etiqueta"] == "spam")) / df["etiqueta"].value_counts().get("spam", 1)  # Recall

#INTERFAZ GRAFICA#
ventana = tk.Tk()
ventana.title("Detector de Spam - Interfaz")
ventana.geometry("1500x750")

# Contenedor principal
frame = tk.Frame(ventana)
frame.pack(pady=10, padx=10, fill="both", expand=True)

#Panel izquierdo: caja de texto para ingresar mensaje#
entrada_texto = tk.Text(frame, height=20, width=60)
entrada_texto.pack(side="left", padx=10, pady=10, fill="both", expand=True)

#Panel central: botones y resultados#
panel_centro = tk.Frame(frame)
panel_centro.pack(side="left", padx=10)

# Función que analiza el texto ingresado y muestra la clasificación
def analizar_texto():
    texto = entrada_texto.get("1.0", "end").strip()
    salida_resultado.config(state="normal")
    salida_resultado.delete("1.0", "end")
    
    if texto == "":
        # Si no hay texto, solo muestra métricas del modelo
        salida_resultado.insert("end", f"Precisión del modelo: {precision:.4f}\n")
        salida_resultado.insert("end", f"Recall (solo spam): {recuperacion:.4f}\n")
    else:
        # Clasifica el texto y muestra resultado + métricas
        clasificacion = clasificar_correo(texto)
        salida_resultado.insert("end", f"Resultado del análisis:\n\n")
        salida_resultado.insert("end", f"Clasificación del correo: {clasificacion.upper()}\n")
        salida_resultado.insert("end", f"Precisión del modelo: {precision:.4f}\n")
        salida_resultado.insert("end", f"Recall (solo spam): {recuperacion:.4f}\n")
    
    salida_resultado.config(state="disabled")

# Limpia el texto ingresado y los resultados
def limpiar_entrada():
    entrada_texto.delete("1.0", "end")
    salida_resultado.config(state="normal")
    salida_resultado.delete("1.0", "end")
    salida_resultado.config(state="disabled")

# Botones para analizar y limpiar
tk.Button(panel_centro, text="Analizar", command=analizar_texto).pack(pady=5)
tk.Button(panel_centro, text="Limpiar", command=limpiar_entrada).pack(pady=5)

# Caja de texto para mostrar resultados
salida_resultado = tk.Text(panel_centro, height=10, width=50, state="disabled")
salida_resultado.pack(pady=10)

# Panel derecho: muestra una tabla con parte del dataset#
frame_tabla = tk.Frame(frame)
frame_tabla.pack(side="right", padx=10, pady=10, fill="both", expand=True)

# Tabla con mensajes y etiquetas (sin predicción)
tabla = ttk.Treeview(frame_tabla, columns=("mensaje", "etiqueta"), show="headings")
tabla.heading("mensaje", text="Mensaje")
tabla.heading("etiqueta", text="Etiqueta")
tabla.column("mensaje", width=400)
tabla.column("etiqueta", width=80)

# Scroll para la tabla
scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
tabla.pack(fill="both", expand=True)

# Llenar la tabla con los primeros 100 mensajes del dataset
for _, fila in df.head(100).iterrows():
    tabla.insert("", "end", values=(fila["mensaje"][:100], fila["etiqueta"]))

# Ejecutar la aplicación
ventana.mainloop()

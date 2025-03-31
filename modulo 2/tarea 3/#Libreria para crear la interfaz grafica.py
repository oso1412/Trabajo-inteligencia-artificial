#Libreria para crear la interfaz grafica
import tkinter
#Libreria para abrir archivos
from tkinter import filedialog
#Libreria para mostrar mensajes de advertencia
from tkinter import messagebox
#Libreria para detectar las palabras mal escritas#Libreria para detectar las palabras mal escritas
from spellchecker import SpellChecker
#Libreria para eliminar singnos de puntuacion
import re

#Eligiendo el idioma español para que reconozca las palabras mal escritas
spell = SpellChecker(language='es')
#Palabras que pusimos para saber si se identifica como spam
frases_spam = {"gratis", "gana dinero", "trabajo desde casa", "ingresos extra", "hazte rico rápido", "dinero fácil", "ingresos garantizados", "oportunidad única", "sin inversión", "multiplica tus ganancias", "premio", 
"has ganado", "lotería", "descuento", "oferta exclusiva", "última oportunidad", "aprovecha ahora", "no lo dejes pasar", "compra ahora", "solo por tiempo limitado", "50 porciento de descuento", 
"ahorra dinero", "sin costo", "suscripción gratuita", "tarjeta de crédito", "sin compromiso", "no requiere tarjeta de crédito", "sin riesgos", "pago inmediato", "transacción segura", "publicidad masiva", "promociona"
"tu negocio", "aumenta tus ventas", "consigue más clientes", "estrategia de marketing", "crecimiento explosivo", "garantizado", "acción inmediata", "no lo pienses más", "hazlo ahora", "urgente", "tiempo limitado", 
"solo por hoy", "felicidades", "pérdida de peso", "pastillas milagrosas", "sin dieta ni ejercicio", "cura garantizada", "remedio natural", "solución definitiva", "clic", "pierdas", "iphone","$", "has sido seleccionado"}

#Funcion para limpiar el texto poniendo todo en minusculas y eliminando los signos de puntuacion
def limpiar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'[.,!¡?¿"():;-_]', '', texto)
    return texto

#Función para analizar el texto
def analizar_texto():
    texto = limpiar_texto(entrada_texto.get("1.0", "end"))
    palabras = texto.split()
    palabras_limpias = palabras
    #Detección de spam
    spam_detectado = [frase for frase in frases_spam if frase in texto]
    #Detección de palabras mal escritas
    palabras_mal_escritas = spell.unknown(palabras_limpias)
    #Mostrar resultados
    salida_resultado.config(state="normal")
    salida_resultado.delete("1.0", "end")
    if spam_detectado or palabras_mal_escritas:
        messagebox.showwarning("Advertencia", "El correo es spam.")
        salida_resultado.insert("end", f"Palabras spam detectadas: {', '.join(spam_detectado)}\n")
        salida_resultado.insert("end", f"Palabras mal escritas detectadas: {', '.join(palabras_mal_escritas)}\n")
    if not spam_detectado and not palabras_mal_escritas:
        salida_resultado.insert("end", "El texto es seguro.\n")
    salida_resultado.config(state="disabled")

#Función para abrir un archivo y cargarlo en el cuadro de texto
def abrir_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
            entrada_texto.delete("1.0", "end")
            entrada_texto.insert("1.0", contenido)

#Función para limpiar los cuadros de texto
def limpiar_cuadros():
    entrada_texto.delete("1.0", "end")
    salida_resultado.config(state="normal")
    salida_resultado.delete("1.0", "end")
    salida_resultado.config(state="disabled")

#Crear la ventana principal
ventana = tkinter.Tk()
ventana.title("Detector de Spam")
ventana.geometry("1500x750")
#Marco de la ventana
frame = tkinter.Frame(ventana)
frame.pack(pady=10, padx=10, fill="both", expand=True)
#Cuadro de texto del correo
entrada_texto = tkinter.Text(frame, height=10, width=50)
entrada_texto.pack(side="left", padx=10, pady=10, fill="both", expand=True)
#Marco de botones para que esten alineados en el medio
boton_frame = tkinter.Frame(frame)
boton_frame.pack(side="left", padx=10)
#Botones
boton_analizar = tkinter.Button(boton_frame, text="Analizar", command=analizar_texto)
boton_analizar.pack(pady=5)
boton_abrir = tkinter.Button(boton_frame, text="Abrir Archivo", command=abrir_archivo)
boton_abrir.pack(pady=5)
boton_limpiar = tkinter.Button(boton_frame, text="Limpiar", command=limpiar_cuadros)
boton_limpiar.pack(pady=5)
#Cuadro de la salida de resultados
salida_resultado = tkinter.Text(frame, height=10, width=50, state="disabled")
salida_resultado.pack(side="right", padx=10, pady=10, fill="both", expand=True)

tkinter.mainloop()
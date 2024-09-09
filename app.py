# Importamos las librerías necesarias de NLTK (Natural Language Toolkit)
import nltk
from nltk.corpus import wordnet as wn  # WordNet es una base de datos léxica que ayuda con la lematización y sinónimos
from nltk.stem import WordNetLemmatizer  # WordNetLemmatizer se utiliza para reducir las palabras a su forma base o lemma
from nltk.corpus import stopwords  # Stopwords contiene palabras comunes que suelen ser filtradas en tareas de procesamiento de lenguaje
# Descargar los recursos necesarios para que NLTK funcione correctamente
nltk.download('wordnet')  # Descarga WordNet para lematización
nltk.download('omw-1.4')  # Descarga recursos adicionales de WordNet necesarios para algunos idiomas
nltk.download('stopwords')  # Descarga la lista de stopwords en varios idiomas
# Creamos una instancia del lematizador de WordNet
lemmatizer = WordNetLemmatizer()
# Definimos listas de palabras emocionales predefinidas
palabras_positivas = ['feliz', 'contento', 'alegre', 'entusiasmado', 'emocionado']  # Lista de palabras con connotaciones positivas
palabras_tristes = ['bajon', 'triste', 'angustiado', 'deprimido', 'desalentado']  # Lista de palabras con connotaciones negativas
# Función para obtener la forma base (lemma) de una palabra, tratándola como un adjetivo (common para emociones)
palabras_rac = []
def obtener_lemma(palabra):
    # Lematiza la palabra ingresada, primero conviertiéndola a minúsculas
    lemma = lemmatizer.lemmatize(palabra.lower(), wn.ADJ)  # Especificamos wn.ADJ para tratar la palabra como un adjetivo
    return lemma  # Devolvemos la forma base de la palabra
# Función para clasificar una palabra como Positiva, Triste o Neutral
def clasificar_palabra(palabra):
    palabra_lemma = obtener_lemma(palabra)  # Obtenemos la forma base (lemma) de la palabra ingresada
    # Comprobamos si la palabra lematizada está en la lista de palabras positivas
    if palabra_lemma in [obtener_lemma(p) for p in palabras_positivas]:  
        return 'Positiva'  # Retornamos 'Positiva' si la palabra coincide con alguna de la lista de palabras positivas
    # Comprobamos si la palabra lematizada está en la lista de palabras tristes
    elif palabra_lemma in [obtener_lemma(p) for p in palabras_tristes]:  
        return 'Triste'  # Retornamos 'Triste' si la palabra coincide con alguna de la lista de palabras tristes
    elif palabra_lemma in [obtener_lemma(p) for p in palabras_rac]:  
        return 'Rac'  # Retornamos 'Triste' si la palabra coincide con alguna de la lista de palabras tristes
    else:
        return 'Neutral'  # Retornamos 'Neutral' si la palabra no coincide con ninguna lista
# Bucle infinito para recibir palabras del usuario hasta que se decida detener el programa
while True:
    print()
    print()
    print()
    print()
    palabra = input("Ingresa una palabra: ")  # Solicita una palabra al usuario
    resultado = clasificar_palabra(palabra)  # Clasifica la palabra ingresada
    print(f'La palabra "{palabra}" es clasificada como {resultado}')  # Muestra el resultado de la clasificación
    print("¿Es correcto?")  # Pregunta al usuario si la clasificación fue correcta
    print("1) SI.\n2) Era Positiva.\n3) Era Triste.\n4) Era Rac.")  # Opciones para reclasificar si fue incorrecto
    definir = input("Valor: ")  # Recibe la respuesta del usuario
    # Dependiendo de la respuesta, ajusta las listas de palabras
    if definir == "2":  # Si el usuario indica que la palabra era positiva
        palabras_positivas.append(palabra)  # Añade la palabra a la lista de palabras positivas
    elif definir == "3":  # Si el usuario indica que la palabra era triste
        palabras_tristes.append(palabra)  # Añade la palabra a la lista de palabras tristes
    elif definir == "4":  # Si el usuario indica que la palabra era triste
        palabras_rac.append(palabra)  # Añade la palabra a la lista de palabras tristes
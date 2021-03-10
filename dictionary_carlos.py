import pickle


def repasar_palabras(dic):
    for es, ing in dic.items():
        resp = input('Escribe la palabra en ingles "{}": '.format(es))
        if resp == ing:
            print ("Bien!.")
        else:
            print ('Mal, la palabra correcta es "{}".'.format(ing))

def añadir_palabras(dic):
    x = input("Palabra en español: ")
    y = input("Palabra en ingles: ")
    dic[x] = y

def cargar_diccionario():
    try:
        with open("traducciones.dat", "rb") as f:
            return pickle.load(f)
    except (OSError, IOError) as e:
        return dict()

def guardar_diccionario(dic):
    with open("traducciones.dat", "wb") as f:
        pickle.dump(dic, f)

def traducir_frase(dic):
    for es, ing in dic.items():
        resp = input('Escribe la frase en español: '.format(es))
        resp_list = resp.split(" ")
        translation_words = [dic[word] if word in dic.keys() else word for word in resp_list]
        translated_sentence = " ".join(translation_words)
        print(translated_sentence)

def main():
    dic = cargar_diccionario()
    menu ='''
    1. Repasar palabras.
    2. Añadir palabras.
    3. Guardar y salir.
    4. Traducir frase
    '''

    while True:
        print(menu)
        decision = input("¿Que quieres hacer?: ")
        if decision == "1":
            repasar_palabras(dic)
        elif decision == "2":
            añadir_palabras(dic)
        elif decision == "3":
            guardar_diccionario(dic)
        elif decision == "4":
            traducir_frase(dic)
            break
        else:
            print('Ha ocurrido algo, por favor, intentelo de nuevo.')

if __name__ == '__main__':
    main()

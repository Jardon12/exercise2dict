import pickle


def repasar_palabras(dic): # for reviewing the words
    for es, ing in dic.items():
        resp = input('Write the word in english "{}": '.format(es))
        if resp == ing:
            print ("Congrats!.")
        else:
            print ('Sorry, the right word was "{}".'.format(ing))
        continuar = input("Do you want to keep reviewing? ")
        while continuar == "yes":
            for es, ing in dic.items():
                resp = input('Write the word in english "{}": '.format(es))
                if resp == ing:
                    print("Congrats!.")
                else:
                    print('Sorry the right word was "{}".'.format(ing))
        break

def añadir_palabras(dic):
    # for adding new words to the dictionary
    x = input("Spanish word: ")
    y = input("English word: ")
    if x in dic.keys(): #checks if the word is already included
        print("This word is already included. Please try again")
    else:
        dic[x] = y

def cargar_diccionario():
    try:
        with open("traducciones.dat", "rb") as f:
            return pickle.load(f)
    except (OSError, IOError) as e:
        return dict()

def guardar_diccionario(dic):
    # for save
    with open("traducciones.dat", "wb") as f:
        pickle.dump(dic, f)

def traducir_frase(dic):
    for es, ing in dic.items():
        resp = input('Write the spanish sentence:  '.format(es))
        resp_list = resp.split(" ")
        translation_words = [dic[word] if word in dic.keys() else word for word in resp_list]
        translated_sentence = " ".join(translation_words)
        print(translated_sentence)
        break
def mostrar_diccionario(dic):
    for es, ing in dic.items():
        print(es, "->", ing)

def main():
    dic = cargar_diccionario()
    menu ='''
    1. Review words.
    2. Add words.
    3. Translate sentence.
    4. Show dictionary. 
    5. Save and exit.
    '''

    while True:
        print(menu)
        decision = input("What do you want to do?: ")
        if decision == "1":
            repasar_palabras(dic)
        elif decision == "2":
            añadir_palabras(dic)
        elif decision == "3":
            traducir_frase(dic)
        elif decision == "4":
            mostrar_diccionario(dic)
        elif decision == "5":
            guardar_diccionario(dic)
            break
        else:
            print('Something happened. Please try again.')

if __name__ == '__main__':
    main()

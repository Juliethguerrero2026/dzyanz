 def registrarPersonas():
    #Variables
    individuo={}
    nombre= input ("como te llamas")
    individuo ["Nombre"]=nombre
    edad= int (input("¿Cuantos años tienes?"))
    individuo ["edad"]=edad
    ciudad= input ("¿En que ciudad vives?")
    individuo["Ciudad"]=ciudad

    generos=["hombre", "mujer"]
    generoValido=False
    while generoValido!=True:
        print(generos)
        genero= input("Cual es tu genero")

        if genero in generos:
            individuo ["Genero"]=genero
            generoValido=True
            
    generoQueBusca=["hombre","mujer"]
    generoValido=False
    while generoValido!=True:
        print(generoQueBusca)
        genero= input("¿Cual es tu genero de interes?")

        if genero in generoQueBusca:
            individuo ["Genero"]=genero
            generoValido=True
    
    edadMinima=18
    edadMaxima=100
    individuo ["¿Rango de edad que buscas?"]=edadMinima,edadMaxima
    listaDeIntereses: ["Hobbies","Signo Zodiacal","musica","comida"]
    individuo ["Intereses"]=listaDeIntereses
    print (individuo)
    return(individuo)
    

def mostrarPersonas(personas):
    print (personas)
    
def main ():
    cuantasPersonas= int (input ("¿Cuantas Personas se van a registrar?"))
    #Registrando Personas
    personas={}
    for i in range (0,cuantasPersonas):
        print("i",i)
        print(personas)
        personas[i]=registrarPersonas()
    #Mostar Personas
    mostrarPersonas (personas)

main()

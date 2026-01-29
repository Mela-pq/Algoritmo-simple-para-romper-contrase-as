import time
import itertools

def fuerza_bruta():
    contraseña_prueba="7a"
    #contraseña_prueba="pl12"
    #contraseña_prueba="Pa$5"
    
    
    caracteres=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
                ,"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","@","#","$","%","^","&","*","(",")",
                "-","=","+","{","}","[","]","|",":",";","'",'"',"<",">",",",".","?","/","`","~"," "]
    
    intentos= 0
    tiempo_inicio=time.time()
    longitud_maxima = 6
    
    for longitud in range(1,longitud_maxima +1):
        #print("Longitud de la contraseña",longitud)
        
        
        for combinacion in itertools.product(caracteres, repeat=longitud):
            intento = ''.join(combinacion)
            intentos += 1
            
            if intento == contraseña_prueba:
                tiempo_total = time.time() - tiempo_inicio
                print("Contraseña encontrada:", intento)
                print("Intentos realizados:", intentos)
                print(f"Tiempo transcurrido:{tiempo_total:.2f} segundos")
                return
            
    print("No se encontró la contraseña")

fuerza_bruta()

#Intento uno (no usa fuerza bruta)
    #resultado=[]
    #desifrar=list(contraseña_prueba)
    #print(desifrar)
    #for i in desifrar:
    #    for j in caracteres:
    #        intentos+=1
    #        if i==j:
    #            resultado.append(j)
    #            break
    #Usa fuerza bruta
    #print("Contraseña encontrada: " + ''.join(resultado))
    #print("Intentos realizados: " ,intentos)  
    #print("Tiempo transcurrido: ",time.time()-tiempo_inicio,"segundos")
        
    

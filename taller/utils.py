def ingresardatonumero(enunciado):
    dato=input(enunciado)
    
    while (True):
        if dato.isdigit():
            print("entero")
            return int(dato)
            break
        else: 
            print("no es entero")
            break
            
    
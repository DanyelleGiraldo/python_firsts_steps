import json

def generardatos():
    campers= [
        
    ]
    nombres= ["daniel", "juanito", "steven"]
    apellidos=["x", "l", "y"]
    direcciones= ["caracoli", "guanta", "giron"]
    acudiente= ["mama", "papa", "abuela"]
    telefono = ["123", "321", "213"]
    estado= ["activo", "inactivo"]

    for i in range(0,33,1):
        obj= {}
        obj["nroid"]= i+1
        obj["nombre"]= nombres[i%3]
        obj["apellidos"]= apellidos[i%3]
        obj["direccion"]= direcciones[i%3]
        obj["acudiente"]= acudiente[i%3]
        obj["telefonocelular"]= telefono[i%3]
        obj["estado"]= estado[i%2]
        campers.append(obj)
    return campers
    
campers= generardatos()

def añadirusuarios():
    

campers_objetos= json.dumps(campers, indent=1)
f= open("noentendi/estudiantes.json", "w")
f.write(campers_objetos)
f.close()

print("menu")#seguir



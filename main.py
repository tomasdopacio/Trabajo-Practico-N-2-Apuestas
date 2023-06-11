import csv

#validaciones 
def validation_yes_no(respuesta)->bool:
    return respuesta not in ["s" , "n"]

def validation_1_2(respuesta)->bool:
    return respuesta not in ["1", "2"]

def validation_mail(mail, lista_de_mails)->bool:
     return "@" not in mail or mail in lista_de_mails or ".com" not in mail 


#lee el archivo csv y lo convierte en una lista                
def lista_informacion_de_usuarios()->list:
    lista_info = []

    with open("usuarios.csv") as archivo_csv:
        csv_reader = csv.reader(archivo_csv)

        for listas_csv in csv_reader:
            lista_info.append([listas_csv[0], listas_csv[1], listas_csv[2], listas_csv[3],listas_csv[4],listas_csv[5]])

    return lista_info

#lee archivos csv y lo convierte en un diccionario 
def diccionario_infromacion_usuarios()->dict:
    diccionario_info = {}
    with open("usuarios.csv") as archivo_csv:
        csv_reader = csv.reader(archivo_csv)

        for listas_csv in csv_reader:
            #"id" : {"userName": , "password": , "cantidadApostada":, "fechaUltimaApuesta": , "dineroDisponible": }
            diccionario_info[listas_csv[0]] = {"username": listas_csv[1], "password": listas_csv[2], "cantidadApostada": listas_csv[3], "fechaUltimaApuesta":listas_csv[4], "dineroDisponible":listas_csv[5]  }

    return diccionario_info



#Aca va el programa y todas sus funciones
def menu()->None:
    print("usted a ingresado al menu o sea ingreso sesion exitosamente")




def iniciar_sesion()-> None:

    validacion = "1"
    while(validacion == "1"):
        dic_ingresado = diccionario_infromacion_usuarios()
        mail = input("ingrese su mail: ")


        if mail in list(dic_ingresado.keys()):
            print("su mail es correcto")
            validacion = "0"

        elif mail not in list(dic_ingresado.keys()):
            print("su mail no se encuentra en nustro sistema")
            qst = input("si quiere ingresar un nuevo usuario ingrese (1) si quiere intentarlo de nuevo ingrese (2): ")
            while (validation_1_2(qst)):
                qst = input("Intente denuevo, (1)- nuevo usuario (2)- intentar de nuevo con otro mail: ")
            
            if(qst == "1"):
                creacion_usuario()
           
            print("intentemoslo denuevo")

    password = input("Ingrese la contraseña")
    while (password != dic_ingresado[mail]["password"]):
            print("contraseña incorrecta")
            password = input("Ingrese de nuevo la contraseña, si quiere salir ingrese (SALIR) en mayusculas ")
            if password == "SALIR":
                break 

    if password == dic_ingresado[mail]["password"]:
        menu()        

         
    




def creacion_usuario()-> None:   
    dic_ingresado = diccionario_infromacion_usuarios()
    list_ingresada = lista_informacion_de_usuarios()
    

    print("Bienvenido a #Jugarsela# ingrese sus datos para continuar")
    #ingreso del mail
    mail = input("Ingrese su mail: ")
    lista_de_mails = list(dic_ingresado.keys())
    while(validation_mail(mail, lista_de_mails)):
         mail = input("Su mail ya existe en el sistema o es incorrecto: ")
    
    #ingreso de username
    username = input("Ingrese su nombre usuario: ")

    #ingreso de password
    password = input("Ingrese su contraseña: ")
    
    print("Su informacion fue ingresada con exito")

    #Ingreso de usuario a la lista para despues que se suba al usuarios.csv
    nuevo_usuario = [mail, username, password, 0,0,0]
    list_ingresada.append(nuevo_usuario)
    
    #Sube la lista anterior con los usuarios ya existentes mas la nueva con el nuevo usuario al archivo usuarios.csv   
    with open("usuarios.csv", 'w', newline ='') as archivo_csv:
        writer = csv.writer(archivo_csv, delimiter=",")       
        writer.writerows(list_ingresada)




def inicio()->None:
    qst = input("¿Es un usuario nuevo? s/n: ")
    while(validation_yes_no(qst)):
        qst = input("Hubo un error: ¿Es un usuario nuevo? s/n: ")

    if(qst == "s"):
        creacion_usuario()
            
    iniciar_sesion()  
         

def main() -> None:
    inicio()

      
main()
from mysql.connector import connect, Error
import psutil as p
import schedule

config = {
  'user': 'root',
  'password': 'sptech',
  'host': 'localhost',
  'database': 'mobanking'
}

import time

#Configuração dos inserts, ou seja, vamos criar uma máquina com id 10 e inserir na empresa 1

idEmpresa = 3
idMaquina = 0


def add_maquina():
    global idMaquina
    global idEmpresa
    try:
        db = connect(**config)
        if db.is_connected():
            db_info = db.get_server_info()
            print('Connected to MySQL server version -', db_info)

            with db.cursor() as cursor:
                query1 = ("INSERT INTO servidor (id, fkEmpresa, status) VALUES (%s, %s, %s);")
                value1 = [idMaquina, idEmpresa, 'ativo']  
                cursor.execute(query1, value1)
                print(cursor.rowcount, "Adicionando máquina...")
                
                db.commit()

            cursor.close()
        db.close()

    except Error as e:
        print('Error to connect with MySQL -', e)   

def verificar_maquina():
        global idMaquina
        try:
            db = connect(**config)
            if db.is_connected():
                db_info = db.get_server_info()
                print('Connected to MySQL server version -', db_info)
                
                with db.cursor() as cursor:
                    query = ("select id from servidor order by id desc limit 1")
                    cursor.execute(query)
                    result = cursor.fetchone()  # Obter o primeiro resultado
                    
                    if result:
                        id = result[0]
                        
                        # Verifica se o plano é 'Básico'
                        if idMaquina > 0:
                            print("maquina já existe")
                            
                        else:
                            print("Adicionando nova máquina")
                            idMaquina = id + 1
                            add_maquina()
                            
                    else:
                        print("Nenhum valor encontrado.")

                
                    cursor.close()
                    db.close()

        except Error as e:
            print('Error to connect with MySQL -', e)
    
def capturar_dados_pro():
    global idMaquina
    
    ram = p.virtual_memory().percent
    cpu = p.cpu_percent(interval=1)

    servicoCpu = 1
    servicoRam = 2
    servicoHd = 3
    hd = p.disk_usage('C:\\')
    hd = hd[1] / (1024 ** 3)  # Converter para GB
    hd = round(hd, 0)
    

    try:
        db = connect(**config)
        if db.is_connected():
            db_info = db.get_server_info()
            print('Connected to MySQL server version -', db_info)
            
            with db.cursor() as cursor:
                query1 = ("INSERT INTO registro (fkServidor, fkServico, valor) VALUES (%s, %s, %s);")
                value1 = [idMaquina, servicoRam, ram]  
                cursor.execute(query1, value1)
                print(cursor.rowcount, "registro inserido na primeira query")
                
                query2 = ("INSERT INTO registro (fkServidor, fkServico, valor) VALUES (%s, %s, %s);")
                value2 = [idMaquina, servicoCpu, cpu]
                cursor.execute(query2, value2)
                print(cursor.rowcount, "registro inserido na segunda query")
                
                query2 = ("INSERT INTO registro (fkServidor, fkServico, valor) VALUES (%s, %s, %s);")
                value2 = [idMaquina, servicoHd, hd]
                cursor.execute(query2, value2)
                print(cursor.rowcount, "registro inserido na terceira query")
                
                db.commit()

            cursor.close()
        db.close()

    except Error as e:
        print('Error to connect with MySQL -', e)   
    
def capturar_dados_basico():
    global idMaquina
    ram = p.virtual_memory().percent
    cpu = p.cpu_percent(interval=1)
    servicoCpu = 1
    servicoRam = 2

    try:
        db = connect(**config)
        if db.is_connected():
            db_info = db.get_server_info()
            print('Connected to MySQL server version -', db_info)
            
            with db.cursor() as cursor:
                query1 = ("INSERT INTO registro (fkServidor, fkServico, valor) VALUES (%s, %s, %s);")
                value1 = [idMaquina, servicoRam, ram]  
                cursor.execute(query1, value1)
                print(cursor.rowcount, "registro inserido na primeira query")
                
                query2 = ("INSERT INTO registro (fkServidor, fkServico, valor) VALUES (%s, %s, %s);")
                value2 = [idMaquina, servicoCpu, cpu]
                cursor.execute(query2, value2)
                print(cursor.rowcount, "registro inserido na segunda query")
                
               
                # Confirmar as mudanças no banco de dados
                db.commit()

            cursor.close()
        db.close()

    except Error as e:
        print('Error to connect with MySQL -', e)   
  
def add_servico_monitorado_pro():
    global idMaquina
    cpu_freq = p.cpu_freq()

# Converte a frequência máxima de MHz para GHz
    capacidadeTotalCpu = cpu_freq.max / 1000
    capacidadeTotalRam = round(p.virtual_memory().total / (1024 ** 3), 0)
    capacidadeTotalDisco = round(p.disk_usage('/').total / (1024 ** 3),0)

    try:
        db = connect(**config)
        if db.is_connected():
            db_info = db.get_server_info()
            print('Connected to MySQL server version -', db_info)
            
            with db.cursor() as cursor:
                
                query1 = ("INSERT INTO servico_monitorado (fkServidor, fkServico, capacidadeTotal) VALUES (%s, 1, %s);")
                value1 = [idMaquina, capacidadeTotalCpu ] 
                cursor.execute(query1, value1)          
                print(cursor.rowcount, "registro inserido na primeira query")
                
                query2 = ("INSERT INTO servico_monitorado (fkServidor, fkServico, capacidadeTotal) VALUES (%s, 2, %s);")
                value2 = [idMaquina, capacidadeTotalRam]  
                cursor.execute(query2, value2)
                print(cursor.rowcount, "registro inserido na segunda query")
                
                query3 = ("INSERT INTO servico_monitorado (fkServidor, fkServico, capacidadeTotal) VALUES (%s, 3, %s);")
                value3 = [idMaquina, capacidadeTotalDisco]  
                cursor.execute(query3, value3)
                print(cursor.rowcount, "registro inserido na terceira query")
               
                db.commit()

            cursor.close()
        db.close()
        
    except Error as e:
        print('Error to connect with MySQL -', e)   
             
def configuracao_pro():
    global idMaquina
    global idEmpresa
    try:
        db = connect(**config)
        if db.is_connected():
            db_info = db.get_server_info()
            print('Connected to MySQL server version -', db_info)
            
            with db.cursor() as cursor:
                
                query = ("INSERT INTO servidor (id, fkEmpresa, funcao) VALUES (%s,%s,'Servidor');")
                value = [idMaquina, idEmpresa] 
                cursor.execute(query, value)
                print(cursor.rowcount, "registro inserido na query")
                
               
                # Confirmar as mudanças no banco de dados
                db.commit()

            cursor.close()
        db.close()
        
    except Error as e:
        print('Error to connect with MySQL -', e)   
        print("Iniciando add_servico_monitorado_pro()")
        add_servico_monitorado_pro()
        print("add_servico_monitorado_pro() concluída")
        
def add_servico_monitorado_basico():
    global idMaquina

    try:
        db = connect(**config)
        if db.is_connected():
            db_info = db.get_server_info()
            print('Connected to MySQL server version -', db_info)
            
            with db.cursor() as cursor:
                
                query1 = ("INSERT INTO servico_monitorado (fkServidor, fkServico) VALUES (%s, 1);")
                value1 = [idMaquina] 
                cursor.execute(query1, value1)          
                print(cursor.rowcount, "registro inserido na primeira query")
                
                query2 = ("INSERT INTO servico_monitorado (fkServidor, fkServico) VALUES (%s, 2);")
                value2 = [idMaquina]  
                cursor.execute(query2, value2)
                print(cursor.rowcount, "registro inserido na segunda query")
                
                
               
                db.commit()

            cursor.close()
        db.close()
        
    except Error as e:
        print('Error to connect with MySQL -', e)         
                
def configuracao_basico():
    global idMaquina
    global idEmpresa
    try:
        db = connect(**config)
        if db.is_connected():
            db_info = db.get_server_info()
            print('Connected to MySQL server version -', db_info)
            
            with db.cursor() as cursor:
                
                query = ("INSERT INTO servidor (id, fkEmpresa, funcao) VALUES (%s,%s,'Servidor');")
                value = [idMaquina, idEmpresa] 
                cursor.execute(query, value)
                print(cursor.rowcount, "registro inserido na query")
                
               
                # Confirmar as mudanças no banco de dados
                db.commit()

            cursor.close()
        db.close()
        

        
    except Error as e:
        print('Error to connect with MySQL -', e) 
        print("Iniciando add_servico_monitorado_basico()")
        add_servico_monitorado_pro()
        print("add_servico_monitorado_basico() concluída")

def inicio():
    try:
        db = connect(**config)
        if db.is_connected():
            db_info = db.get_server_info()
            print('Connected to MySQL server version -', db_info)
            
            with db.cursor() as cursor:
                query = ("select fkPlano from empresa where id = 3")
                cursor.execute(query)
                result = cursor.fetchone()  # Obter o primeiro resultado
                
                if result:
                    plano = result[0]
                    
                    # Verifica se o plano é 'Básico'
                    if plano == 1:
                        print("Plano basico ok")
                        verificar_maquina()
                        configuracao_basico()
                        for _ in range(80):  
                            capturar_dados_basico()
                            time.sleep(5)  
                        
                    else:
                        print("Plano Pro ou intermediario ok")
                        verificar_maquina()
                        configuracao_pro()
                        for _ in range(80):  
                            capturar_dados_pro()
                            time.sleep(5) 
                        
                else:
                    print("Nenhum valor encontrado.")

            
                cursor.close()
                db.close()

    except Error as e:
        print('Error to connect with MySQL -', e)
    
 
def agendar_tarefa_semanal():
    print("Agendando a tarefa semanal...")
    # Executa a função inicio uma vez por semana (por exemplo, todo domingo às 10h)
    schedule.every().sunday.at("10:00").do(inicio)

    while True:
        schedule.run_pending()
        time.sleep(60)  # Verifica a cada minuto se há uma tarefa agendada   
        
inicio()
agendar_tarefa_semanal()
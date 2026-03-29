import consolidacion
import enviar_email
import pandas as pd
from config import plantillas_correo
import os
import glob
import re

def obtener_ultimo_consolidado():
    """Obtiene el archivo consolidado más reciente"""
    archivos = glob.glob('datasets/ProgramacionGeneral*.xlsx')
    
    if not archivos:
        return None
    
   
    def get_version(archivo):
        match = re.search(r'ProgramacionGeneral_?(\d*)\.xlsx', archivo)
        if match:
            if match.group(1):
                return int(match.group(1))
            else:
                return 1 
        return 0
    
    archivos_ordenados = sorted(archivos, key=get_version, reverse=True)
    return archivos_ordenados[0]

def cargar_destinatarios():
    try:
        df = pd.read_excel('config/destinatarios.xlsx')
        return df.to_dict('records')
    except Exception as e:
        print(f"Error cargando destinatarios: {e}")
        return []

def agrupar_por_tipo(destinatarios):
    grupos = {}
    for item in destinatarios:
        tipo = item['Tipo']
        if tipo not in grupos:
            grupos[tipo] = []
        grupos[tipo].append(item['Correo'])
    return grupos

def main():
    print("="*50)
    print("INICIANDO PROCESO DE CONSOLIDACIÓN")
    print("="*50)
    
   
    archivo_nuevo = consolidacion.consolidar_archivos()
    if not archivo_nuevo:
        print("No se pudo consolidar el archivo")
        return
    
    print(f"\n Nuevo archivo generado: {archivo_nuevo}")
    
    archivo_consolidado = obtener_ultimo_consolidado()
    if not archivo_consolidado:
        print("No se encontró el archivo consolidado")
        return
    
    print(f"Enviando archivo: {archivo_consolidado}")
    
    todos_destinatarios = cargar_destinatarios()
    if not todos_destinatarios:
        print("No se encontraron destinatarios")
        return
    
    grupos = agrupar_por_tipo(todos_destinatarios)
    print(f"\nGrupos encontrados: {list(grupos.keys())}")
    
    exitos = 0
    fallos = 0
    
    for tipo, correos in grupos.items():
        print(f"\n{'='*30}")
        print(f"Enviando a grupo: {tipo}")
        print(f"Correos: {correos}")
        
        asunto, cuerpo = plantillas_correo.get_plantilla(tipo)
        
        print(f"Asunto: {asunto}")
        
        resultado = enviar_email.enviar_informe_por_email(
            archivo=archivo_consolidado,
            destinatarios=correos,
            asunto=asunto,
            mensaje=cuerpo
        )
        
        if resultado:
            print(f"Correo enviado al grupo {tipo}")
            exitos += 1
        else:
            print(f"Error enviando correo al grupo {tipo}")
            fallos += 1
    
    print("\n" + "="*50)
    print("PROCESO TERMINADO")
    print(f"Envíos exitosos: {exitos}")
    print(f"Envíos fallidos: {fallos}")
    print(f"Archivo generado: {archivo_consolidado}")
    print("="*50)

if __name__ == "__main__":
    main()
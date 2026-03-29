import pandas as pd
import glob
import os
import re

def obtener_siguiente_version():
    """Obtiene el siguiente número de versión para el archivo consolidado"""
    archivos = glob.glob('datasets/ProgramacionGeneral*.xlsx')
    
    if not archivos:
        return 1
    
    max_version = 0
    for archivo in archivos:
        
        match = re.search(r'ProgramacionGeneral_?(\d*)\.xlsx', archivo)
        if match:
            if match.group(1):
                version = int(match.group(1))
            else:
                version = 1  
            if version > max_version:
                max_version = version
    
    return max_version + 1

def consolidar_archivos():
    archivos = glob.glob('datasets/Programacion*.xlsx')
    print(f"Archivos encontrados: {len(archivos)}")
    
    if not archivos:
        print("No hay archivos para consolidar")
        return None
    
    dfs = []
    for archivo in archivos:

        if 'ProgramacionGeneral' in archivo: 
            continue
            
        nombre_archivo = os.path.basename(archivo)
        sede = nombre_archivo.replace('Programacion', '').replace('.xlsx', '')
        
        try:
            df_raw = pd.read_excel(archivo, header=None)
            
            fila_inicio = None
            for idx, row in df_raw.iterrows():
                for val in row:
                    if pd.notna(val) and str(val).strip() == 'N°':
                        fila_inicio = idx
                        break
                if fila_inicio is not None:
                    break
            
            if fila_inicio is None:
                print(f"  - {sede}: No se encontró estructura válida, omitiendo")
                continue
            
            headers = df_raw.iloc[fila_inicio].values
            df = df_raw.iloc[fila_inicio + 1:].reset_index(drop=True)
            
            df.columns = [str(h).strip() if pd.notna(h) else f'col_{i}' for i, h in enumerate(headers)]
            
            df = df.dropna(axis=1, how='all')
            
            primera_col = df.columns[0]
            df = df[df[primera_col].notna()]
            
            if 'N°' in df.columns:
                df = df.drop(columns=['N°'])
            
            df['Sede'] = sede
            
            print(f"  - {sede}: {len(df)} registros")
            dfs.append(df)
            
        except Exception as e:
            print(f"  - Error en {sede}: {str(e)}")
            continue
    
    if not dfs:
        print("No hay datos para consolidar")
        return None
    
    df_combinado = pd.concat(dfs, ignore_index=True, sort=False)
    
    df_combinado.insert(0, 'N°', range(1, len(df_combinado) + 1))
    
    version = obtener_siguiente_version()
    
    if version == 1:
        archivo_salida = 'datasets/ProgramacionGeneral.xlsx'
    else:
        archivo_salida = f'datasets/ProgramacionGeneral_{version}.xlsx'
    
    # Guardar archivo
    df_combinado.to_excel(archivo_salida, index=False)
    
    print(f"\n Consolidado guardado: {archivo_salida}")
    print(f"Total registros: {len(df_combinado)}")
    print(f"Versión: {version}")
    
    return archivo_salida
from datetime import datetime

def get_fecha_actual():
    return datetime.now().strftime("%d/%m/%Y")

def get_plantilla(tipo='programacion'):
    """Retorna asunto y cuerpo según el tipo de reporte"""
    fecha = get_fecha_actual()
    
    if tipo == 'programacion':
        asunto = f"Reporte Consolidado de Programacion - {fecha}"
        cuerpo = f"""
Buenos dias,

Adjunto el reporte consolidado de programacion correspondiente al {fecha}.
Este archivo contiene la informacion de todas las sedes.

Saludos cordiales,
Area de RRHH
        """
    elif tipo == 'guardia':
        asunto = f"Reporte de Guardia - {fecha}"
        cuerpo = f"""
Buenos dias,

Adjunto el reporte de programacion para el personal de guardia correspondiente al {fecha}.

Saludos cordiales,
Area de RRHH
        """
    else:
        asunto = f"Reporte Consolidado - {fecha}"
        cuerpo = f"""
Buenos dias,

Adjunto el reporte consolidado correspondiente al {fecha}.

Saludos cordiales,
Area de RRHH
        """
    
    return asunto, cuerpo
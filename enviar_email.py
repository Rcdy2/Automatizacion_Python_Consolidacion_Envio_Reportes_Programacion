import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  
from email.mime.application import MIMEApplication
import os

def enviar_informe_por_email(archivo, destinatarios, asunto, mensaje):
    from config.credentials import USER_MAIL, PASSWORD
    

    if not os.path.exists(archivo):
        print(f"Error: El archivo {archivo} no existe")
        return False
    
    try:
        # Conectar al servidor SMTP
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(USER_MAIL, PASSWORD)
            
            # Crear mensaje
            msg = MIMEMultipart()
            msg['From'] = USER_MAIL
            msg['To'] = ', '.join(destinatarios)
            msg['Subject'] = asunto
            msg.attach(MIMEText(mensaje, 'plain', 'utf-8'))
            
            # Adjuntar archivo
            with open(archivo, 'rb') as adj:
                nombre_archivo = os.path.basename(archivo)
                parte = MIMEApplication(adj.read(), Name=nombre_archivo)
                parte['Content-Disposition'] = f'attachment; filename="{nombre_archivo}"'
                msg.attach(parte)
            
            # Enviar correo
            server.sendmail(USER_MAIL, destinatarios, msg.as_string())
            print(f"Correo enviado exitosamente a: {', '.join(destinatarios)}")
            return True
            
    except Exception as e:
        print(f"Error enviando correo: {str(e)}")
        return False
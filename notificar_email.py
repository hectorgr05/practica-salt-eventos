#!/usr/bin/env python3
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
REMITENTE = "hectorgaru8@gmail.com"
CONTRASEÑA = "spmlflmqivgxmiuf"
DESTINATARIO = "hectorgaru8@gmail.com"

if len(sys.argv) < 3:
    print("Error: Faltan parametros")
    sys.exit(1)

ip_nodo = sys.argv[1]
rol_nodo = sys.argv[2]

msg = MIMEMultipart()
msg['From'] = REMITENTE
msg['To'] = DESTINATARIO
msg['Subject'] = "[SaltStack] Evento: Aprovisionamiento Exitoso"

cuerpo = f"""
Hola Héctor,

Se ha completado con éxito el aprovisionamiento del nodo.

Detalles del evento detectado:
---------------------------------------
Dirección IP: {ip_nodo}
Rol del nodo: {rol_nodo}
---------------------------------------

Saludos,
Servidor SaltStack Centralizado (localhost)
"""

msg.attach(MIMEText(cuerpo, 'plain'))

try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(REMITENTE, CONTRASEÑA)
    server.sendmail(REMITENTE, DESTINATARIO, msg.as_string())
    server.quit()
    print("Notificación enviada correctamente por correo.")
except Exception as e:
    print(f"Error al enviar correo: {e}")

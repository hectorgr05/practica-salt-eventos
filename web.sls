include:
  - base

nginx:
  pkg.installed

enviar_notificacion_evento:
  cmd.run:
    - name: python3 /usr/local/bin/notificar_email.py "127.0.0.1 (Localhost)" "Servidor Web (Nginx)"
    - require:
      - pkg: nginx 

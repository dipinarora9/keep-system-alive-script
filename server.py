from time import sleep
from flask import Flask
from w import ToastNotifier

app = Flask(__name__)
askToast = ToastNotifier()
confirmToast = ToastNotifier()
accidentalToast = ToastNotifier()

allowed = False


def allow():
    global allowed
    allowed = True
    print(f'Allowed - {allowed}')


def disallow():
    global allowed
    allowed = False
    print(f'Allowed - {allowed}')


def disallow_and_toast():
    disallow()

    accidentalToast.show_toast(
        title="Dipin's says",
        msg="Shutdown process stopped",
    )


@app.route('/')
def done():
    disallow()
    askToast.show_toast(title="Dipin's asking",
                        msg="Computer band krdu?",
                        callback_on_click=allow)
    if allowed:
        confirmToast.show_toast(title="Dipin says",
                                msg="Computer will be shutdown soon.",
                                callback_on_click=disallow_and_toast)

    return "<h1>Accepted</h1>" if allowed else "<h1>Rejected</h1>"


app.run('0.0.0.0', 34917)

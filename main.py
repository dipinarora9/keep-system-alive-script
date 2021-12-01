from w import ToastNotifier

toast = ToastNotifier()
toast.show_toast(title="Notification",
                 msg="Hello, there!",
                 callback_on_click=lambda: print("Clicked!"))

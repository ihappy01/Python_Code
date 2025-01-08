# from PythonSelFramework.April_2023.locators import message

alert ="Storage almost full or space is running out"
clear_alert = "Alert is cleared now and you have enough space"

message = "ytyyuyy cleared now"

def popup_text():
    print(alert)
    print(clear_alert)

    if "Storage almost full" in message or "cleared now" in message:
        print("Alert is raised")
    else:
        print("Alert is not raised")


popup_text()


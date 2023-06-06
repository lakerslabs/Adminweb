import datetime

def get_current_datetime():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Ejemplo de uso
current_datetime = get_current_datetime()
print(current_datetime)

#importamos datetime
from datetime import datetime
#funcion para filtrar fecha
def validar_fecha_domingo(dia_insertador):
    if dia_insertador.strip().lower() == "domingo":
        return True
    else:
        return False
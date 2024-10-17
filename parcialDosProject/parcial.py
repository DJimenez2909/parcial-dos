# variables del nivel directivo
bonificacion_alta= 0.20
bonificaciones_baja= 0.10

bonificaciones= 0.15
bonificacion = 0.05

print("salario base mensual")
print("cargo el empleado")
print("nivel del desempeño")


def calcular_bonificaciones(salari_base,nivel, desempeño):
    if nivel == "directivo":
        if desempeño== "alto":
            bonificacion_alta= 0.20*salari_base



        elif desempeño == "medio":
            bonificaciones_baja ==0.10*salari_base
        else:
            bonificacion=0


    elif nivel== "operativo":
        if desempeño == "alto":
            bonificaciones =0.15*salari_base
        elif desempeño =="medio":
            bonificacion= 0.05*salari_base
        else:
            bonificacion=0
    else:
        tatal= salari_base+salari_base
        return  tatal
        print("----resumen del pago----")



empleasdos =[{"salari_base":3000000, "nivel"}]






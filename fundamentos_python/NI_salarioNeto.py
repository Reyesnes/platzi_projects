# PROGRAMA PARA REALIZAR EL CALCULO DE SALARIO NETO EN NICARAGUA

# 1) INTRODUCCION
'''
    En Nicaragua para calcular el Salario Neto hay que realizar ciertos cálculos de deducción
    Estos cálculos son:
    1) Cálcular el INSS Laboral, el cuál corresponde al 7% del Total de los ingresos del mes
    2) Cálcular el IR, el cuál se calcula en base a una tabla progresiva
'''

'''
La tabla para calcular el IR es la siguiente:
    Renta Imponible             | Impuesto Base |   Porcentaje Aplicable    |   Sobre Exceso de
    0.01        - 100,000       | 0.00          |   0.00%                   |   0
    100,000.01  - 200,000       | 0.00          |   15.00%                  |   100,000
    200,000.01  - 350,000       | 15,000        |   20.00%                  |   200,000
    350,000.01  - 500,000       | 45,000        |   25.00%                  |   350,000
    500,000.01  - a más         | 82,500        |   30.00%                  |   500,000
'''

# 2) CODIGO PROGRAMA

# 2.1) User Inputs
input_salario_base = float(input("Ingrese el salario base: "))
input_comisiones = float(input("Ingrese el valor de las comisiones: "))
input_HE = float(input("Ingrese el valor de las Horas Extras: "))
input_OI = float(input("Ingrese el valor de Otros Ingresos: "))

# 2.2) Declaración de variables - parametros iniciales:
porc_inss_lab = 0.07
salario_total = input_salario_base + input_comisiones + input_HE + input_OI
dict_ingresos = (
    {
        'Salario_base =>': input_salario_base,
        'Comisiones =>': input_comisiones,
        'Horas_extras =>': input_HE,
        'Otros_ingresos =>': input_OI
    }
)

monto_inss_laboral = round(float(salario_total * porc_inss_lab), 2)
neto_recibido = round(float(salario_total - monto_inss_laboral), 2)
proy_meses = 12
expectativa_anual = neto_recibido * proy_meses

# 2.3) Definición de variables tabla progresiva (deducible, alicuota, imp_base)

# 2.3.1) Calculo Deducible Según Tabla Progresiva:
if expectativa_anual > 0 and expectativa_anual <= 100000:
    deducible = 0
elif expectativa_anual > 100000 and expectativa_anual <= 200000:
    deducible = 100000
elif expectativa_anual > 200000 and expectativa_anual <= 350000:
    deducible = 200000
elif expectativa_anual > 350000 and expectativa_anual <= 500000:
    deducible = 350000
elif expectativa_anual > 500000:
    deducible = 500000
else:
    deducible = 0

# 2.3.2) Calculo Alicuota porcentual Según Tabla Progresiva:
if expectativa_anual > 0 and expectativa_anual <= 100000:
    alicuota = 0
elif expectativa_anual > 100000 and expectativa_anual <= 200000:
    alicuota = 0.15
elif expectativa_anual > 200000 and expectativa_anual <= 350000:
    alicuota = 0.2
elif expectativa_anual > 350000 and expectativa_anual <= 500000:
    alicuota = 0.25
elif expectativa_anual > 500000:
    alicuota = 0.3
else:
    alicuota = 0

# 2.3.3) Calculo Impuesto Base Según Tabla Progresiva
if expectativa_anual > 0 and expectativa_anual <= 100000:
    imp_base = 0
elif expectativa_anual > 100000 and expectativa_anual <= 200000:
    imp_base = 0
elif expectativa_anual > 200000 and expectativa_anual <= 350000:
    imp_base = 15000
elif expectativa_anual > 350000 and expectativa_anual <= 500000:
    imp_base = 45000
elif expectativa_anual > 500000:
    imp_base = 82500
else:
    imp_base = 0

# 2.4 Calculo de IR correspondiente:

salario_menos_deducible = expectativa_anual - deducible
resultado = salario_menos_deducible * alicuota
IR_anual = round(float(resultado + imp_base), 2)
IR_mensual = round(float(IR_anual / proy_meses), 2)

# 2.5 Calculo del Salario Neto a recibir:
salario_neto_recibir = round(float(salario_total - monto_inss_laboral - IR_mensual), 2)

# 2.6 Calculo de aportación patronal
inss_patronal = salario_total * 0.225
inatec = salario_total * 0.02

# 3) PRINTS
borde_encabezado = '*-' * 20

# 3.1) Detalle de ingresos brutos recibidos
print(borde_encabezado)
print("I) DETALLE DE INGRESOS BRUTOS RECIBIDOS 👇🏼:")
print(borde_encabezado)

print("Detalle de ingresos brutos =>", list(dict_ingresos.items()))
print('Total Ingresos del mes =>', salario_total)

# 3.2) Detalle proceso de cálculo IR
print(borde_encabezado)
print("II) DETALLE PROCESO DE CALCULO DEL IR 👇🏼:")
print(borde_encabezado)

print('Total Ingresos del mes =>', salario_total)
print('(-) INSS Laboral => ', monto_inss_laboral)
print('(=) Neto recibido => ', neto_recibido)
print('(x12) Expectativa anual => ', expectativa_anual)
print('(-) Deducible => ', deducible)
print('(=) Salario menos deducible => ', salario_menos_deducible)
print('(x) Alicuota % => ', alicuota)
print('(+) Impuesto Base => ', imp_base)
print('(=) IR Anual a Deducir => ', IR_anual)
print('(=) Deducción de impuesto sobre la Renta (IR) => ', IR_mensual)

# 3.3) Resultado de Salario Neto a Recibir
print(borde_encabezado)
print("III) RESULTADO SALARIO NETO A RECIBIR 👇🏼:")
print(borde_encabezado)

print('(=) Salario Neto a Recibir => ', salario_neto_recibir)

# 3.4) Detalle Patronal
print(borde_encabezado)
print("IV) DETALLE PATRONAL 👇🏼:")
print(borde_encabezado)
print('----> INSS Patronal:  => ', inss_patronal)
print('----> INATEC:         => ', inatec)

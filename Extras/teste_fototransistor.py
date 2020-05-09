#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Teste Fototransitores

# --------------------------------------------------------

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Chamada da interface i2c
i2c = busio.I2C(board.SCL, board.SDA)

# Criando um objeto ADC com a interface i2c
ads_a = ADS.ADS1115(i2c, address=0x48)
ads_b = ADS.ADS1115(i2c, address=0x49)


# Criando entradas para leituras dos canais do dois conversores AD
a0 = AnalogIn(ads_a, ADS.P0)
a1 = AnalogIn(ads_a, ADS.P1)
a2 = AnalogIn(ads_a, ADS.P2)
a3 = AnalogIn(ads_a, ADS.P3)

b0 = AnalogIn(ads_b, ADS.P0)
b1 = AnalogIn(ads_b, ADS.P1)
b2 = AnalogIn(ads_b, ADS.P2)
b3 = AnalogIn(ads_b, ADS.P3)

# 1º valor raw e 2º valor da tensão
while True:
    print("A0:{:>5} A1:{:>5} A2:{:>5} A3:{:>5} \tB0:{:>5} B1:{:>5} B2:{:>5} B3:{:>5}".format(a0.value, a1.value, "-", a3.value, b0.value, b1.value, "-", b3.value))
    time.sleep(0.5)

#Programa de conversao de °C para °F

temp = float(input('\nInforme a temperatura em °C: '))
conv = ((9 * temp) / 5) + 32
print("A temperatura de {}°C corresponde a {}°F! ".format(temp, conv))

temp1 = float(input('\nInforme a temperatua em °F: '))
conv1 = (temp1 - 32) * 5/9
print('A temperatura de {}F° corresponde a {}C°'.format(temp1, conv1))
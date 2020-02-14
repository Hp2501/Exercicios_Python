
m = int(input('\nDigite um valor em metro(s): '))#valor digitado em metros
km = m * 0.001#valor em kilometros
hm = m * 0.01#valor em hectometro
dam = m * 0.1#valor em decametro
cm = m * 100#valor em centimetros
mm = m * 1000#valor em milimetros
print('{} Metro(s) equivale a {:.3f} Kilometros'.format(m, km))
print('{} Metro(s) equivale a {:.2f} Hectometro'.format(m, hm))
print('{} Metro(s) equivale a {} Decametro'.format(m, dam))
print('{} Metro(s) equivale a {} Centimetros'.format(m, cm))
print('{} Metro(s) equivale a {} Milimetros'.format(m, mm))

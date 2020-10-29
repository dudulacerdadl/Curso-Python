speed = float(input('Digite a sua velocidade: '))

if speed > 80:
    trafficTicket = (speed - 80) * 7
    print('Você está dirigindo a {}Km/h, e ultrapassou o limite de velocidade.\nSerá multado em R$ {:.2f}'.format(speed, trafficTicket))
else:
    print('Você está dirigindo a {}Km/h, Boa Viagem!'.format(speed))

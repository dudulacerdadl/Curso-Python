num = float(input('Digite um número em metros: '))

print('O número distância digitada foi {}m \nEm quilómetros: {}km \nEm hectómetro: {}hm \nEm decâmetros: {}dam \nEm decímetro: {}dm \nEm centrímetros: {}cm \nEm milímetros: {}mm'.format(num, (num / 1000), (num / 100), (num / 10), (num * 10), (num * 100), (num * 1000)))

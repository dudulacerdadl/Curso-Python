from math import radians, sin, cos, tan

ang = float(input('Digite um ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print('O seno vale {:.2f}, o cosseno {:.2f} e a tangênte {:.2f}'.format(sen, cos, tan))

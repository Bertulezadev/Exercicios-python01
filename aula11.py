largura = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
área = largura * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}n2.'.format(largura, alt, área))
tinta =  área / 2
print('Para pintar a parede você precisa de {}l de tinta.'.format(tinta))

'''
Implemente um programa que leia o destino do passageiro, se a viagem inclui retorno
(ida e volta) e informar o preço da passagem conforme a tabela a seguir:
Região Norte Ida:R$ 500,00 Volta: R$ 900,00
Região Nordeste Ida: R$ 350,00 Volta: R$ 650,00
Região Centro-Oeste Ida: R$ 350,00 Volta: R$ 600,00
Região Sul Ida: R$ 300,00 Volta: R$ 550,00
'''

print('Olá, essas são as opções de viagens que você pode fazer \nRegião Norte\nRegião Nordeste\nRegião Centro-Oeste\n- Região Sul')
viagem = str(input('Digite qual região você quer viajar: ')).upper()
idavolta = str(input('Sua viagem é de ida e volta? (s/n)')).upper()

if viagem == 'REGIÃO NORTE' and idavolta == 'N':
    print(f'Sua viagem vai custar R$ 500,00')
elif viagem == 'NORTE' and idavolta == 'S':
    print('Sua viagem vai custar R$ 1400,00')
elif viagem == 'NORDESTE' and idavolta == 'N':
    print('Sua viagem vai custar R$ 350,00')
elif viagem == 'NORDESTE' and idavolta == 'S':
    print('Sua viagem vai custar R$ 1000,00')
elif viagem == 'CENTRO-OESTE' and idavolta == 'N':
    print('Sua viagem vai custar R$ 350,00')
elif viagem == 'CENTRO-OESTE' and idavolta == 'S':
    print('Sua viagem vai custar R$ 950,00')
elif viagem == 'SUL' and idavolta == 'N':    
    print('Sua viagem vai custar R$ 300,00')
elif viagem == 'SUL' and idavolta == 'S':
    print('Sua viagem vai custar R$ 850,00')
else:
    print('Algum dado está errado, tente digitar apenas (norte, sul, etc.)')
    

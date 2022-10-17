def voto(nasc: int):
    """ Tells the user if he's apt to vote
    Args:
        nasc (int): User's birth year
    """

    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        v = 'NEGADO!'
    elif idade < 18 or idade > 65:
        v = 'OPCIONAL'
    else:
        v = 'OBRIGATÓRIO'
    return f'Com {idade} anos: VOTO {v}'


# Programa principal
print('=' * 30)
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))

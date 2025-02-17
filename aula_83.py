def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y

def criar_multiplicacao(multiplidor):
    def multiplica(numero):
        return numero * multiplidor
    return multiplica

# -------------------------------------------------

print(executa(lambda x, y: x + y,2, 5))

# duplica = criar_multiplicacao(2)
duplica = executa(lambda m: lambda n: n*m, 2)
print(duplica(2))

print(executa(lambda *args: sum(args), 2, 43, 23, 675, 69))

# 1- Em uma instrução print, o que acontece se você omitir um dos parênteses ou ambos?

  # print('ola' -> SyntaxError: ( was never clossed

# 2- Se estier tentando imprimir um string, o que aocntece se omitir uma das aspas ou ambas?

  #print(Texto sem aspas) -> SyntaxError: invalid syntax. Perhaps you forgot a comma?

# 3- Voc"e pode usar um sinal de menos para fazer um numero negativo como -2. O que acontece se pusar um sinal de mais antes de um numero? E se escrever assim 2 ++ 2?

print(+4)
print(2 ++ 2) # O python consegue executar sem erros

# 4- Na notacao matematica, zeros a esquerda sao aceitaveis, como em 02. O que acontece se você tentar usar isso no Python?

# print(01) -> SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

# 5 O que acontece se você tiver dois valores sem nenhum operador entre eles?

# print(2 4) -> SyntaxError: invalid syntax. Perhaps you forgot a comma?
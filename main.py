print(
    "Olá.Neste episódio vamos aprender como verificar a classe de uma variável."
)

print("Vamos definir a variável a, b e c.")

a = 34
b = 16.7
c = 'Mariana'

print(type(a))
print(type(b))
print(type(c))

print(1 + 1)

print(a + 2)
print(a / 2)
print(a * 2 / 2)
print(3**2)
print(5 % 2)

x = 45

y = 2

print(x / y)

print("AGORA VEREMOS OUTRAS FUNCIONALIDADES EM PYTHON!")

lista = [1.0, 2, 'pollyana', [4, 5, 6]]
print(type(lista))

print(lista[0])
print(lista[3])
print(lista[1:])

string = 'python'

print(string[:4])
print(string[1:])
print(string[:])

dic = {'valor1': 1, 'valor2': 2}
print(dic)
print(type(dic))
print(dic['valor1'])

dic1 = {'lista1': [2, 4, 6], 'str': 'Toronto'}
print(dic1['lista1'])
print(dic1['str'])

t = (1, 2, 3)
print(type(t))
print(t[0])

lista[0] = 5.7
print(lista[0])

print(1 == 1)
print(3.0 == 3)
print('A' == 'a')
print(a == 15)
print(a < 100)
print(b > 10)
print(4 != 4.2)

print((a > 30) and (a >= 34))
print ((b == 0) or (b > 15))
print((b == 0)) 

z = 'reprovado'
w = 8
if w > 7:
  z = 'Aprovado'
elif w > 5:
 z = 'recuperação'
else:
    z = 'reprovado'
print(z)


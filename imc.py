nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura ** 2)  # ** usa - se para calcular altura ao quadrado

print(nome, ", seu IMC é de {:.1f}".format(imc))

if imc < 18.5:
    print("Você está abaixo do peso ideal")
elif imc >=18.5 and imc < 25:
    print("Você está com o peso ideal!")
elif 25 <= imc < 30:
    print("Você está em sobrepeso")
elif 30 <= imc < 40:  # pode abreviar o código
    print("Você está em obesidade.")
elif imc >= 40:
    print("Você está em obesidade mórbida. Consulte seu médico.")


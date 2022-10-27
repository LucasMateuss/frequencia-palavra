from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

# Abre o arquivo
with open("portuguese.txt", encoding="utf-8") as file:
    text = file.read().lower()
with open("esperanto.txt", encoding="utf-8") as file2:
    text2 = file2.read().lower()

# Limpa o arquivo
TEXTO_LIMPO = ''
for i in text:
    if i.isalpha() or i == " ":
        TEXTO_LIMPO += i

TEXTO_LIMPO2 = ''
for i in text2:
    if i.isalpha() or i == " ":
        TEXTO_LIMPO2 += i

# Deixa somente letras
letras = [l for l in TEXTO_LIMPO if l.isalpha()]
letras2 = [l for l in TEXTO_LIMPO2 if l.isalpha()]


# Vê a frequência das letras
frequencia = Counter(letras)
frequencia2 = Counter(letras2)


# Cria o Gráfico
rotulo, valor = zip(*frequencia.most_common(5))
rotulo2, valor2 = zip(*frequencia2.most_common(5))
plt.title('Frequência de letras em Portugês')
plt.subplot(1,2,1)
plt.bar(rotulo, valor, color = 'red', label = 'Português')
plt.legend()
plt.subplot(1,2,2)
plt.bar(rotulo2, valor2, color = 'green', label = "Esperanto")
plt.legend()
plt.show()
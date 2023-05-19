import matplotlib.pyplot as plt

# Pedir ingreso de datos numéricos
vulnerabilidades_criticas = int(input("Ingrese el número de vulnerabilidades críticas: "))
vulnerabilidades_altas = int(input("Ingrese el número de vulnerabilidades altas: "))
vulnerabilidades_medias = int(input("Ingrese el número de vulnerabilidades medias: "))
vulnerabilidades_bajas = int(input("Ingrese el número de vulnerabilidades bajas: "))
vulnerabilidades_informativas = int(input("Ingrese el número de vulnerabilidades informativas: "))

# Crear el gráfico de barras
categorias = ['Críticas', 'Altas', 'Medias', 'Bajas', 'Informativas']
valores = [vulnerabilidades_criticas, vulnerabilidades_altas, vulnerabilidades_medias, vulnerabilidades_bajas, vulnerabilidades_informativas]
colores = ['#7b2cbf', '#ff4d4d', '#ff9933', '#66ccff', '#3366ff']

plt.bar(categorias, valores, color=colores)

# Agregar etiquetas y título
plt.xlabel("Categorías de vulnerabilidades")
plt.ylabel("Número de vulnerabilidades")
plt.title("Gráfico de vulnerabilidades")

# Agregar valores encima de cada barra
for i in range(len(valores)):
    plt.text(i, valores[i], str(valores[i]), ha='center', va='bottom')

# Guardar gráfico en formato PNG
plt.savefig('grafico_vulnerabilidades.png')

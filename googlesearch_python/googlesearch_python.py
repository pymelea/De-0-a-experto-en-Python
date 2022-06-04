# pip install googlesearch-python
from googlesearch import search

# Texto para buscar
query = 'pythoncu'

# Hacer la búsqueda y crear lista con los links de los resultados
result = list(
    search(
        query,
        lang='es-cu',
        num_results=10,
    )
)

# Mostrar resultados
print(result)

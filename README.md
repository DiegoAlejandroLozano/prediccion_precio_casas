# Calculo del precio de vivienda

Librerías utilizadas: `Pandas`, `Numpy`, `Matplotlib`, `Seaborn`, `Scikit-Learn` y `Keras`.

El presente proyecto predice los precios de vivienda utilizando el algoritmo de regresión polinomial, los algoritmos de regresión robusta RANSAC y HUBER y por último, a través de redes neuronales. Antes de implementar algún algoritmo de regresión y realizar la predicción con las variables descriptoras, se realizó el proceso de limpieza de los datos en el cual se elimina los valores faltantes, se elimina las columnas irrelevantes, se verifica que no hayan columnas repetidas y otros procedimientos de limpieza que se puede encontrar en el archivo `limpieza_datos.ipynb` dentro del directorio `work_notebooks`.

Una vez implementados los algoritmos y realizas las predicciones, se evalúa el desempeño de cada algoritmo a través del $R^2 score$ y a través de la raíz cuadrada del error cuadrático promedio $(RMSE)$.

Para correr el repositorio de forma local se debe crear un entorno virtual con el siguiente comando:

    Python3 -m venv nombre_entorno_virtual

Se debe activar el entorno virtual e instalar todas las librerías especificadas en el archivo “requirements.txt” con el siguiente comando:

    pip install -r requirements.txt

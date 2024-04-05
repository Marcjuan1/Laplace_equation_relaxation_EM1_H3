# Laplace_equation_relaxation_EM1_H3
Este es un programa Python que resuelve la ecuación de Laplace utilizando el método de relajación. Permite especificar condiciones de frontera personalizadas y devuelve la solución numérica/analítica de la ecuación de Laplace (se realizan comparaciones tales como el error porcentual).
Asegúrate de tener python instalado en tu sistema. Así como las dependencias de numpy, matlplotlib.

Clona este repositorio en tu máquina local o descarga el código fuente como un archivo ZIP.
Abre tu terminal y navega hasta el directorio donde se encuentra el código.
Ejecuta el siguiente comando para iniciar el programa: python laplace_solver.py
El programa cuenta con un main, de modo que una vez se ha ejecutado pide al usario ingresar las condiciones de frontera y condiciones iniciales de intéres. Para correr del test, solo necesita asignar la misma magnitud de V0 pero con signos opuestos en los bordes inferior y superior de la malla. Y para los extremos derecho e izquierdo, asigne un 0. Sí quiere probar escenarios distintos al test solo necesita jugar con los parámetros que puede asignar.

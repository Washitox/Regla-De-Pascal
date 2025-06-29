# 📐 Implementación de la Regla de Pascal (Recursividad en Python)

Este trabajo consiste en la implementación de la **Regla de Pascal** usando el principio de **recurrencia** para calcular coeficientes binomiales. Se utiliza el lenguaje de programación **Python**, aplicando una función recursiva dentro de una clase.

---

## 📜 Código completo

![image](https://github.com/user-attachments/assets/ccb563fb-cee0-41aa-ac6f-db7920c752c0)

---

## ⚙️ Explicación de las funciones

### 🔹 `__init__`

- Es el **constructor de la clase** en Python.
- `__init__` es un **método especial** que se ejecuta automáticamente cuando se crea una instancia de una clase.
- En este caso, contiene `pass` porque no se necesita inicializar ningún atributo.

![image](https://github.com/user-attachments/assets/2285ecf1-1e9e-4834-9027-fcf58761a230)

### 🔹 `calcular_combinacion(self, n, k)`

- Es la función **recursiva principal**, y se basa en la **Regla de Pascal**:

![image](https://github.com/user-attachments/assets/46769e44-5d76-427e-997f-d42352ae6094)

  \[
  \binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}
  \]

![image](https://github.com/user-attachments/assets/a3a7fdd4-3b87-45bd-9d6c-7da4d4709f3e)

- La función se llama a sí misma dos veces con valores menores:
  - `calcular_combinacion(n - 1, k - 1)`
  - `calcular_combinacion(n - 1, k)`
  
- Esta operación se repite hasta alcanzar los **casos base**, donde:
  - Si `k == 0` o `k == n`, entonces retorna `1`.

### 🔹 Función `main`

![image](https://github.com/user-attachments/assets/642db5f5-a92d-4814-a534-b88687090116)

- Se crea una instancia de la clase `ReglaDePascal`.
- Se aplican **valores predefinidos** (`n = 4`, `k = 2`).
- En la línea 7 se llama a la función `calcular_combinacion()` para ejecutar el cálculo.
- Se imprime el resultado final en la consola con la función `print`.

### 🖥️ Resultado esperado al ejecutar el código:

```
El valor de C(4, 2) es: 6
```

---

### 🖼️ Ejecución del código

_🔽 Aquí puedes incluir una captura de pantalla mostrando el programa corriendo en el terminal o editor:_

![image](https://github.com/user-attachments/assets/a8f6a1a8-64a7-431c-a3e8-f1d2b01449e8)



## 🔗 Repositorio en GitHub

Aquí puedes acceder al código completo en GitHub:

https://github.com/Washitox/Regla-De-Pascal.git 

---

## 🧑‍🤝‍🧑 Autores

- **Estudiante 1**: _Washington Villares_

---

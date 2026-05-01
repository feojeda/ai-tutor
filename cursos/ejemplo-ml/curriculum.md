# Curso: Machine Learning desde cero

**Objetivo:** Entender qué es ML, cómo funciona un modelo simple, y entrenar tu primer clasificador.

**Duración estimada:** 4-5 sesiones de 30-45 minutos cada una.

**Prerrequisitos:** Python básico (variables, funciones, listas). No necesitas saber matemáticas avanzadas.

---

## Sesión 1 — ¿Qué es Machine Learning?

### Objetivo
Entender la diferencia entre programación tradicional y ML. Saber identificar problemas que ML puede resolver.

### Conceptos
- Programación tradicional vs ML: reglas explícitas vs aprender de datos
- Tipos de ML: supervisado, no supervisado, por refuerzo
- Ejemplos cotidianos: recomendaciones, spam, reconocimiento de voz

### Ejercicio (5 min)
Clasifica estos problemas como "ML útil" o "ML innecesario":
1. Predecir el precio de una casa basado en sus características
2. Sumar dos números
3. Detectar si un email es spam
4. Encontrar la palabra más larga en un texto

### Check de comprensión
El tutor preguntará: "Explícame con tus palabras la diferencia entre programación tradicional y ML."

---

## Sesión 2 — Tu primer modelo: Regresión Lineal

### Objetivo
Entender qué es un modelo, qué son los parámetros, y cómo un modelo "aprende" ajustando números.

### Conceptos
- Modelo como función matemática: y = w·x + b
- Parámetros (w, b) — los números que el modelo ajusta
- Error / pérdida — qué tan mal predice el modelo
- Gradiente — la dirección para mejorar

### Ejercicio (10 min)
```python
# Sin usar librerías de ML, ajusta w y b a mano
# para que esta función prediga correctamente:

def predecir(horas_estudio):
    w = ???  # ¡ajústalo!
    b = ???  # ¡ajústalo!
    return w * horas_estudio + b

# Datos reales:
# 1 hora  → nota 2
# 2 horas → nota 4
# 3 horas → nota 6
# 4 horas → nota 8
# 5 horas → nota 10

# Verifica tu modelo:
for h in [1, 2, 3, 4, 5]:
    print(f"{h}h → nota {predecir(h)}")
```

### Check de comprensión
"Si w=0, ¿qué predice el modelo sin importar las horas de estudio? ¿Qué significa eso?"

---

## Sesión 3 — Entrenamiento real con scikit-learn

### Objetivo
Entrenar un modelo de regresión lineal con datos reales usando scikit-learn.

### Conceptos
- Train/test split — por qué separamos datos
- `.fit()` — el modelo aprende
- `.predict()` — el modelo predice
- Métricas: MAE, MSE, R² — cómo medir qué tan bueno es

### Ejercicio (15 min)
```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Dataset: casas en Santiago
# [metros_cuadrados, num_habitaciones, antiguedad]
X = [
    [60, 2, 15], [80, 3, 10], [100, 3, 5],
    [120, 4, 2], [150, 4, 1], [200, 5, 0],
    [70, 2, 20], [90, 3, 8], [110, 3, 3],
    [130, 4, 1], [160, 5, 0],
]
y = [80, 110, 150, 180, 220, 300, 85, 130, 160, 200, 250]  # precio en UF

# 1. Divide en train/test (80/20)
# 2. Entrena un LinearRegression
# 3. Predice y calcula el error
# 4. ¿Qué feature pesa más? (mira model.coef_)
```

### Check de comprensión
"¿Por qué separamos los datos en train y test? ¿Qué pasaría si evaluamos con los mismos datos que usamos para entrenar?"

---

## Sesión 4 — Clasificación

### Objetivo
Entender la diferencia entre regresión y clasificación. Entrenar un clasificador simple.

### Conceptos
- Regresión vs Clasificación: predecir número vs predecir categoría
- Regresión Logística — el clasificador más simple
- Matriz de confusión — qué acierta y qué confunde
- Accuracy, Precision, Recall — más allá del porcentaje de aciertos

### Ejercicio (15 min)
```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Dataset: ¿el cliente comprará? (0=no, 1=sí)
# [edad, ingreso_mensual_k, visitas_web, tiempo_en_sitio_min]
X = [
    [25, 800, 5, 3], [30, 1200, 8, 7], [22, 600, 2, 1],
    [35, 1500, 10, 12], [28, 900, 6, 4], [40, 2000, 12, 15],
    [19, 400, 1, 1], [45, 1800, 7, 8], [33, 1100, 9, 10],
    [27, 700, 3, 2], [38, 2500, 15, 20], [23, 500, 4, 3],
]
y = [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0]

# 1. Entrena un LogisticRegression
# 2. Muestra la matriz de confusión
# 3. ¿Cuál es la feature más importante para predecir?
# 4. ¿El modelo es mejor detectando compradores o no-compradores?
```

### Check de comprensión
"Si un modelo tiene 95% de accuracy pero nunca detecta la clase minoritaria, ¿es buen modelo?"

---

## Sesión 5 — Overfitting y buenas prácticas

### Objetivo
Entender por qué un modelo puede ser "demasiado bueno" y cómo evitarlo.

### Conceptos
- Overfitting vs Underfitting
- Validación cruzada
- Regularización (L1/L2)
- El pipeline real: datos → limpieza → entrenamiento → evaluación → despliegue

### Ejercicio final
Toma cualquier dataset de [Kaggle](https://kaggle.com) o [UCI ML Repository](https://archive.ics.uci.edu/) y aplica todo lo aprendido:
1. Carga y explora los datos
2. Limpia valores nulos
3. Entrena un modelo (regresión o clasificación)
4. Evalúa con train/test split
5. Explica tus resultados al tutor

---

## Recursos complementarios

- [3Blue1Brown: Neural Networks](https://youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) — visualizaciones excelentes
- [scikit-learn tutorials](https://scikit-learn.org/stable/tutorial/index.html)
- [Kaggle Learn](https://www.kaggle.com/learn) — cursos interactivos gratis
- [Made With ML](https://madewithml.com/) — de beginner a producción

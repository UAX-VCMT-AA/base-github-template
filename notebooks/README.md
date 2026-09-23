# Notebooks

Aquí van los Jupyter Notebooks de exploración, prototipado y experimentación (EDA, pruebas de modelos, visualización de resultados, etc.).

## Convención de nombres

Se recomienda prefijar cada notebook con un número de orden que indique la secuencia lógica del trabajo, por ejemplo:

```
01-exploracion_datos.ipynb
02-entrenamiento_cnn.ipynb
03-evaluacion_resultados.ipynb
```

## Buenas prácticas

- Los notebooks son para explorar y explicar, no para producción: el código reutilizable debe vivir en [`src/`](../src) y ser importado desde aquí.
- Antes de hacer commit, limpia las salidas pesadas (imágenes grandes, logs largos) para no engordar el repositorio.
- Recuerda que las salidas de `.ipynb_checkpoints/` ya están excluidas mediante el `.gitignore`.

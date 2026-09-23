# Plantilla de repositorio — Aprendizaje Automático (UAX)

![CI](https://github.com/UAX-VCMT-APAUT/base-github-template/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.13%2B-blue?logo=python&logoColor=white)
![Poetry](https://img.shields.io/badge/poetry-managed-blue?logo=poetry&logoColor=white)
![Conda](https://img.shields.io/badge/conda-supported-44A833?logo=anaconda&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)
![Ruff](https://img.shields.io/badge/lint-ruff-D7FF64?logo=ruff&logoColor=black)
![License](https://img.shields.io/badge/license-Apache%202.0-green)

Plantilla base de repositorio para las prácticas de **Aprendizaje Automático** (UAX): estructura de proyecto, gestión de entornos, control de versiones y CI listos para usar en proyectos de Deep Learning (CNN, RNN, RAG, etc.).

Su objetivo es que dediquéis el tiempo a entrenar y evaluar vuestros modelos, no a montar la infraestructura del repositorio desde cero.

## Índice

- [Estructura del repositorio](#estructura-del-repositorio)
- [Configuración del entorno](#configuración-del-entorno)
- [Variables de entorno (.env)](#variables-de-entorno-env)
- [Reproducibilidad e hiperparámetros](#reproducibilidad-e-hiperparámetros)
- [.gitignore](#gitignore)
- [Integración continua (GitHub Actions)](#integración-continua-github-actions)
- [Flujo de trabajo recomendado](#flujo-de-trabajo-recomendado)
- [Buenas prácticas para los commits](#buenas-prácticas-para-los-commits)
- [Licencia](#licencia)

## Estructura del repositorio

```
base-github-template/
├── .github/
│   └── workflows/
│       └── ci.yml            # Pipeline de integración continua (lint + tests)
├── app/                      # Demo web del proyecto (Streamlit / Hugging Face Spaces)
├── docs/                     # Documentación extendida del proyecto
├── data/                     # Carpeta para almacenamiento de datos (NO se versionan)
├── models/                   # Checkpoints y pesos entrenados (NO se versionan)
├── notebooks/                # Jupyter Notebooks de exploración y experimentación
├── presentations/            # Slides usadas en exposiciones y entregas
├── src/                      # Código fuente reutilizable del proyecto
│   ├── data/                 # Carga y preprocesado de datos (Dataset, DataLoader...)
│   ├── models/               # Arquitecturas de los modelos (CNN, RNN, RAG...)
│   ├── training/             # Bucles de entrenamiento y evaluación
│   ├── utils/                # Funciones auxiliares (métricas, logging, seeds...)
│   └── config.py             # Semilla e hiperparámetros del experimento
├── tests/                    # Tests unitarios (pytest)
├── .env.example               # Plantilla de variables de entorno
├── .gitignore
├── LICENSE
└── README.md
```

> **Nota sobre `models/` vs `src/models/`:** `models/` (raíz) guarda los **artefactos entrenados** (pesos, checkpoints), que pesan mucho y no se suben a Git. `src/models/` guarda el **código** que define las arquitecturas de esos modelos, que sí se versiona.


## Configuración del entorno

Hay varias formas de gestionar el entorno de Python. Esta plantilla es compatible con las tres; **elegid una sola** para vuestro proyecto y no las mezcléis.

> **¿Y si dejo varios a la vez (`pyproject.toml`, `requirements.txt`, `environment.yml`)?** Técnicamente no pasa nada: cada herramienta solo lee su propio archivo, no interfieren entre sí. El problema es de mantenimiento: si instaláis un paquete con una herramienta y no lo reflejáis en las demás, esos archivos se quedan desactualizados y dejan de ser fiables. Por eso, para vuestro proyecto real, elegid uno y no os compliquéis manteniendo los tres.

### Opción 1 · Poetry

Gestiona a la vez el entorno virtual y las dependencias, y genera un lockfile (`poetry.lock`) que fija las versiones exactas instaladas. Útil cuando queréis que el proyecto se instale igual en cualquier máquina sin sorpresas de versiones.

**Para crear el proyecto desde cero** (genera el `pyproject.toml`):

```bash
poetry init                            # responde las preguntas y crea pyproject.toml
poetry add numpy pandas matplotlib scikit-learn torch transformers jupyter python-dotenv
poetry add --group dev pytest ruff     # dependencias solo de desarrollo
```

**Para instalar un proyecto que ya tiene `pyproject.toml`** (p. ej. al clonar el repo):

```bash
poetry install          # crea el entorno e instala las dependencias de pyproject.toml
poetry shell             # activa el entorno virtual
```

### Opción 2 · venv + pip

La herramienta estándar de Python, sin nada externo que instalar. Útil si ya estáis cómodos con `pip` y no necesitáis nada más.

**Crear y activar el entorno:**

```bash
python -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate
```

Si tenéis varias versiones de Python instaladas y el comando `python`/`python3` por defecto no coge la que queréis, primero comprobad cuáles tenéis disponibles.

En **Windows (PowerShell)**, con el Python Launcher (`py`):

```powershell
py --list
```

Y creáis el entorno indicando la versión que queráis usar, por ejemplo Python 3.11:

```powershell
py -3.11 -m venv .venv
```

En **macOS / Linux**, para ver las versiones instaladas:

```bash
ls /usr/bin/python3*
# o, si usáis pyenv:
pyenv versions
```

Y para crear el entorno con una versión concreta (equivalente al `py -3.11` de Windows):

```bash
python3.11 -m venv .venv
```

**Instalar paquetes según los vayáis necesitando:**

```bash
pip install numpy pandas matplotlib scikit-learn torch transformers jupyter python-dotenv
```

**Al final** (no al principio), cuando el entorno ya tenga instalado todo lo que usa el proyecto, generad el `requirements.txt` congelando las versiones exactas:

```bash
pip freeze > requirements.txt
```

**Para instalar desde un `requirements.txt` que ya existe** (p. ej. al clonar el repo):

```bash
pip install -r requirements.txt
```

### Opción 3 · Conda

Gestiona no solo paquetes de Python sino también librerías y binarios del sistema (por ejemplo, versiones concretas de CUDA para entrenar con GPU). Útil en proyectos de Deep Learning cuando necesitáis ese tipo de dependencias no-Python.

**Crear y activar el entorno:**

```bash
conda create -n aa-template python=3.11
conda activate aa-template
```

**Instalar paquetes según los vayáis necesitando:**

```bash
conda install numpy pandas matplotlib scikit-learn jupyter
pip install torch transformers python-dotenv   # lo que no esté en conda, con pip dentro del propio entorno
```

**Al final**, generad el `environment.yml` a partir de lo que hayáis instalado (`--from-history` evita volcar dependencias transitivas y detalles específicos de vuestro sistema operativo, para que el archivo sea portable):

```bash
conda env export --from-history > environment.yml
```

**Para instalar el entorno desde un `environment.yml` que ya existe** (p. ej. al clonar el repo):

```bash
conda env create -f environment.yml
conda activate aa-template

# Si más adelante añadís dependencias nuevas a environment.yml:
conda env update -f environment.yml --prune
```

En los tres casos, las dependencias de partida orientativas son: `numpy`, `pandas`, `matplotlib`, `scikit-learn`, `torch`, `transformers`, `jupyter` y `python-dotenv`. Añadid o quitad paquetes según las necesidades de vuestro proyecto.

## Variables de entorno (.env)

El `.env` es **solo para secretos**: claves de API y tokens que dependen de cada persona/entorno y que nunca deben subirse al repositorio (por ejemplo, para consumir modelos de OpenAI o HuggingFace en un proyecto de RAG).

1. Copiad `.env.example` a `.env`:
   ```bash
   cp .env.example .env
   ```
2. Rellenad vuestras claves reales en `.env`.
3. `.env` está excluido en el `.gitignore`: nunca se subirá a GitHub. `.env.example` sí se versiona, como documentación de qué variables espera el proyecto.

Para cargar las variables en vuestro código Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

## Reproducibilidad e hiperparámetros

La semilla aleatoria y los hiperparámetros (`batch_size`, `learning_rate`, `epochs`...) van en [`src/config.py`](src/config.py): son parte del experimento y deben quedar versionados en Git para que el resultado sea reproducible.

```python
from src.config import config

print(config.seed, config.batch_size, config.learning_rate, config.epochs)
```

Podéis modificar esos valores directamente o crear instancias distintas de `Config` para comparar configuraciones. Si el proyecto crece y necesitáis probar muchas combinaciones de hiperparámetros, valorad herramientas como archivos YAML por experimento o `Hydra`/`argparse`; para el alcance de estas prácticas, un único `config.py` es suficiente.

## .gitignore

El `.gitignore` incluido cubre lo habitual en un proyecto de Deep Learning:

- Entornos virtuales (`.venv/`, `venv/`, `.conda/`) y cachés de Python (`__pycache__/`, `*.pyc`).
- Checkpoints de Jupyter (`.ipynb_checkpoints/`).
- Archivos de entorno (`.env`), **excepto** `.env.example`.
- Contenido de `data/` y `models/` (los datos y los pesos entrenados no se versionan; solo la estructura de carpetas vía `.gitkeep`).
- Formatos de modelo pesados (`*.pt`, `*.pth`, `*.h5`, `*.onnx`, `*.pkl`...).
- Carpetas de logs y tracking de experimentos (`wandb/`, `mlruns/`, `lightning_logs/`...).
- Archivos propios del sistema operativo y del editor (`.DS_Store`, `.vscode/`, `.idea/`...).

Si vuestro proyecto genera otro tipo de artefacto pesado, añadidlo al `.gitignore`.

## Integración continua (GitHub Actions)

El workflow en [`.github/workflows/ci.yml`](.github/workflows/ci.yml) se ejecuta automáticamente en cada `push` y `pull request` contra `main`, y hace dos cosas:

1. **Lint** del código con [`ruff`](https://docs.astral.sh/ruff/), para detectar errores de estilo y problemas comunes.
2. **Tests** con `pytest` sobre la carpeta [`tests/`](tests).

Esto ayuda a detectar errores pronto y mantiene el código en un estado consistente. Podéis ejecutar los mismos checks en local antes de hacer commit:

```bash
ruff check .
pytest -q
```

## Flujo de trabajo recomendado

1. Cread una rama por funcionalidad o experimento (`feature/entrenamiento-cnn`, `fix/preprocesado-datos`...).
2. Explorad y prototipad en `notebooks/`.
3. Una vez que el código funcione, migradlo a módulos reutilizables en `src/`.
4. Añadid tests básicos en `tests/` para las funciones críticas (preprocesado, métricas...).
5. Documentad decisiones relevantes en `docs/` y subid vuestras diapositivas a `presentations/`.
6. Abrid un Pull Request hacia `main`; la CI se ejecutará automáticamente.

## Buenas prácticas para los commits

Usamos [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/): mensajes cortos, en imperativo y con un tipo que indica qué clase de cambio es. El formato es:

```
<tipo>[ámbito opcional]: <descripción en imperativo, minúscula, sin punto final>
```

| Tipo | Cuándo usarlo |
|---|---|
| `feat` | Código nuevo que añade funcionalidad (un modelo, una función, un módulo) |
| `fix` | Corrección de un bug |
| `docs` | Solo documentación (README, `docs/`, comentarios) |
| `chore` | Mantenimiento que no es código de la app (config, plantillas, `.gitignore`, `.env.example`) |
| `ci` | Cambios en GitHub Actions / pipelines de integración continua |
| `test` | Añadir o modificar tests |
| `refactor` | Reestructurar código sin cambiar su comportamiento |
| `style` | Formato (espacios, imports...) sin afectar la lógica |
| `perf` | Mejora de rendimiento |
| `build` | Cambios en dependencias o en la configuración del entorno |

Ejemplos:

```
feat(models): añadir arquitectura CNN base
fix(data): corregir normalización incorrecta del dataset
docs: documentar el uso de config.py en el README
ci: añadir workflow de lint y tests
```

Reglas generales:

- Un commit, un propósito: evitad mezclar en el mismo commit cosas que no tienen relación.
- Descripción en imperativo ("añadir", no "añadido" ni "añadiendo").
- Si el cambio necesita más contexto, añadid un cuerpo separado del título por una línea en blanco explicando el *por qué*, no solo el *qué*.

## Licencia

Este proyecto está bajo licencia [Apache 2.0](LICENSE).

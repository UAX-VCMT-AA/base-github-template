# App

Carpeta para la demo web del proyecto, cuando la práctica pida exponer el modelo con una interfaz.

## Opción 1 · Streamlit (en local)

Instalad Streamlit en vuestro entorno (ver [Configuración del entorno](../README.md#configuración-del-entorno)):

```bash
pip install streamlit
```

Y ejecutad la app en local desde la raíz del repo:

```bash
streamlit run app/app.py
```

## Opción 2 · Gradio, para publicarla como Hugging Face Space

Los **Hugging Face Spaces** es una web propia de Hugging Face donde construís la interfaz con **Gradio**, su SDK nativo. Es una alternativa a Streamlit, pensada específicamente para vivir en un Space.

```bash
pip install gradio
python app/app.py
```

## Subir el modelo entrenado (Hugging Face Models)

Esto aplica **igual si desplegáis con Streamlit o con Gradio**: la app desplegada **no tiene acceso a vuestra carpeta `models/` en local**. Esos archivos están excluidos de Git (ver [.gitignore](../README.md#gitignore)) y, aunque no lo estuvieran, la app no corre en vuestro ordenador. El modelo entrenado hay que subirlo a algún sitio accesible desde internet para que la app lo descargue al arrancar.

Lo recomendado es subirlo al **Hugging Face Model Hub** ([huggingface.co/new](https://huggingface.co/new)). El Model Hub solo es almacenamiento de modelos: no importa si vuestra interfaz está hecha con Streamlit o con Gradio, sirve exactamente igual para las dos.

```bash
pip install huggingface_hub
huggingface-cli login
huggingface-cli upload <usuario>/<nombre-del-modelo> ./models/mi_modelo
```

Y cargarlo desde la app con `huggingface_hub` (o con `from_pretrained` si es un modelo de `transformers`):

```python
from huggingface_hub import hf_hub_download

modelo_path = hf_hub_download(repo_id="<usuario>/<nombre-del-modelo>", filename="modelo.pt")
```

## Base de datos (si el proyecto la necesita)

Igual que el modelo, si vuestra app necesita una base de datos (por ejemplo, para un proyecto de RAG con metadatos, o para guardar resultados), **no vale con tener un archivo de base de datos dentro del repo**: no es su sitio. La base de datos debe estar publicada en un servicio accesible desde internet, igual que el modelo.

Alternativas gratuitas habituales:

- **[Supabase](https://supabase.com)** — Postgres gestionado, capa gratuita generosa.
- **[Neon](https://neon.tech)** — Postgres serverless, capa gratuita.
- **[MongoDB Atlas](https://www.mongodb.com/atlas)** — MongoDB gestionado, clúster gratuito (M0).
- **[Turso](https://turso.tech)** — SQLite distribuido, capa gratuita.

Para un proyecto de RAG, muchas veces no hace falta ni eso: una base de datos vectorial como **[Chroma](https://www.trychroma.com)** (embebida, sin servidor) o **[Pinecone](https://www.pinecone.io)** (capa gratuita en la nube) puede ser suficiente.

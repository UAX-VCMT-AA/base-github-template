"""Configuración y parámetros del experimento.

La semilla aleatoria y los hiperparámetros SÍ deben versionarse:
forman parte del experimento y son necesarios para poder reproducirlo.

Modifica estos valores directamente o crea nuevas instancias de
`Config` para probar distintas configuraciones.
"""

from dataclasses import dataclass


@dataclass
class Config:
    seed: int = 42
    batch_size: int = 32
    learning_rate: float = 1e-3
    epochs: int = 10


config = Config()

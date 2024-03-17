import os
from pathlib import Path

ruta_principal = Path("/Users/claudiainzunza/Desktop/Recetas")
numero_recetas = 0

file_count = len([f for f in ruta_principal.cwd().rglob('*') if f.is_file()])

print(file_count)

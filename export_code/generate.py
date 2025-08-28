import os


def convert_script_markcdown(files: list, path: str, title:str="Codigo exportado"):
    """
    Convierte archivos de script a markdown.
    
    Args:
        files (list): Lista de archivos a convertir.
        path (str): Ruta donde se guardarán los archivos convertidos.
    """
    with open(path, 'w', encoding='utf-8') as md:
        md.write(f"# {title}\n\n")
        
        for file in files:
            nombre = os.path.basename(file)
            md.write(f"## {nombre}\n\n")
            md.write("```python\n")
            
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    md.write(f.read())
            except Exception as e:
                md.write(f"Error al leer el archivo {nombre}: {e}\n")
                
            md.write("\n```\n\n")
    
    print(f"Archivos convertidos y guardados en {path}")
    
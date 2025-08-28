from export_code.convert import convertir_md_a_pdf
from export_code.generate import convert_script_markcdown

scripts = [
    "data/data_clientes.py",
    "src/cajero.py",
    "src/clientes.py",
    "main.py"
]

path_md = "Codigo.md"
path_pdf = "Codigo_PDF.pdf"

convert_script_markcdown(scripts, path_md, title="codigo prueba")
convertir_md_a_pdf(path_md, path_pdf)

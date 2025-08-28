from export_code.convert import convertir_md_a_pdf
from export_code.generate import convert_script_markcdown

scripts = [
    "Carteras/Naturgy/file_management.py",
    "Carteras/Naturgy/db_operations.py",
    "Carteras/Naturgy/text_query.py",
    "Carteras/Naturgy/transformers/base.py",
    "Carteras/Naturgy/transformers/data_transformers.py",
    "Carteras/Naturgy/transformers/DateTransformers.py",
    "Carteras/Naturgy/transformers/FloatTransformers.py",
    "Carteras/Naturgy/transformers/IntegerTransformer.py",
    "Carteras/Naturgy/transformers/StringTransformer.py"
]

path_md = "Codigo.md"
path_pdf = "Codigo_PDF.pdf"

convert_script_markcdown(scripts, path_md, title="codigo prueba")
convertir_md_a_pdf(path_md, path_pdf)

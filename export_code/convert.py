import markdown
import pdfkit

# Ruta al ejecutable
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

def convertir_md_a_pdf(ruta_md: str, ruta_pdf: str):
    try:
        # 1. Leer el Markdown
        with open(ruta_md, 'r', encoding='utf-8') as f:
            md_text = f.read()

        # 2. Convertir a HTML
        html_text = markdown.markdown(md_text, extensions=['fenced_code', 'codehilite'])

        # 3. Convertir HTML a PDF
        pdfkit.from_string(html_text, ruta_pdf, configuration=config)

        print(f"✅ PDF generado correctamente en: {ruta_pdf}")

    except Exception as e:
        print(f"❌ Error al generar el PDF: {e}")

from flask import Flask, request, send_file
import json
from fpdf import FPDF
import io

app = Flask(__name__)

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Historia Clínica', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_section(self, title, content):
        self.chapter_title(title)
        self.chapter_body(content)

@app.route('/guardar_pdf', methods=['POST'])
def guardar_pdf():
    data = request.get_json()

    pdf = PDF()
    pdf.add_page()
    pdf.add_section("Nombre del Paciente", data['nombre'])
    pdf.add_section("Fecha", data['fecha'])
    pdf.add_section("Edad", data['edad'])
    pdf.add_section("Vacunas", data['vacunas'])
    pdf.add_section("Neurodesarrollo", data['neurodesarrollo'])
    pdf.add_section("Alimentación", data['alimentacion'])
    # Agrega más secciones según los datos recibidos

    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    return send_file(pdf_output, as_attachment=True, download_name="historia_clinica.pdf", mimetype='application/pdf')

if __name__ == "__main__":
    app.run(debug=True)

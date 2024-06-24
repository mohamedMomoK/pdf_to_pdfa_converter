from flask import Flask, render_template, request, redirect, url_for, send_file
import pdftopdfa
import os

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('pdf_to_pdfa.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return redirect(redirect.url)
    file = request.files('file')
    if file.filename =='':
        return redirect(request.url)
    if file:
        pdfa_variation = request.form.get('pdfa_variation')
        converted_file_path = pdftopdfa.convert_to_pdfa(file, pdfa_variation)
        return send_file(converted_file_path, as_attachment= True)
    return redirect(url_for('index'))

if __name__ == '__name__':
    app.run(debug=True, port=5001)

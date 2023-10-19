import PyPDF2

# Abra o arquivo PDF em modo de leitura binária
with open('/home/gustavomaxwell/importPyPDF/seuarquivo.pdf', 'rb') as pdf_file:
    # Crie um objeto PDFReader
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Verifique o número de páginas no PDF
    num_pages = len(pdf_reader.pages)
    print(f'O PDF possui {num_pages} páginas.')

    # Inicialize uma string vazia para armazenar o texto extraído
    text = ''

    # Loop através de todas as páginas e extraia o texto
    for page in pdf_reader.pages:
        text += page.extract_text()

# Agora você tem todo o texto do PDF armazenado na variável 'text'
# Você pode fazer o que quiser com o texto, como salvá-lo em um arquivo, processá-lo, etc.
# Por exemplo, para salvar o texto em um arquivo de texto:
with open('texto_do_pdf.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.write(text)



print(text)

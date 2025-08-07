import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

# Configurações dos cartões (ajuste conforme necessário)
CARD_WIDTH = 285  # em pontos (10,06 cm)
CARD_HEIGHT = 162  # em pontos (5,72 cm)
MARGEM_ESQUERDA = 12  # em pontos (0,43 cm)
MARGEM_SUPERIOR = 15  # em pontos (0,54 cm)

# PDF_ORIGINAL = "cartao_pdf/JORGE_31_07_2025.pdf"
# LISTA_PRESENCA = "cartao_pdf/JORGE_31_07_2025.txt"
# OUTPUT_DIR = "cartoes_gerados"

def ler_lista_presenca(path):
    with open(path, "r", encoding="utf-8") as f:
        nomes = [linha.strip() for linha in f if linha.strip()]
    return nomes

def recortar_cartoes(pdf_path):
    reader = PdfReader(pdf_path)
    cartoes = []
    for page_num, page in enumerate(reader.pages):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        n_col = int((width - MARGEM_ESQUERDA) // CARD_WIDTH)
        n_row = int((height - MARGEM_SUPERIOR) // CARD_HEIGHT)
        for row in range(n_row):
            for col in range(n_col):
                x0 = MARGEM_ESQUERDA + (col * CARD_WIDTH)
                y1 = height - (MARGEM_SUPERIOR + row * CARD_HEIGHT)
                x1 = x0 + CARD_WIDTH
                y0 = y1 - CARD_HEIGHT
                # Adiciona também o número da página para corte correto
                cartoes.append((page_num, x0, y0, x1, y1))
    return cartoes, reader


def gerar_cartao_pdf(nome, template_pdf, crop_box, idx, output_dir):
    page_num, x0, y0, x1, y1 = crop_box
    writer = PdfWriter()
    page = template_pdf.pages[page_num]
    page.cropbox.lower_left = (x0, y0)
    page.cropbox.upper_right = (x1, y1)
    writer.add_page(page)
    buffer = BytesIO()
    writer.write(buffer)
    buffer.seek(0)
    # Escrever nome no cartão
    output = BytesIO()
    c = canvas.Canvas(output, pagesize=(CARD_WIDTH, CARD_HEIGHT))
    c.setFont("Helvetica-Bold", 16)
    # c.drawCentredString(CARD_WIDTH/2, 20, nome)
    c.save()
    # Mesclar nome ao cartão
    nome_pdf = PdfReader(BytesIO(output.getvalue()))
    cartao_pdf = PdfReader(buffer)
    cartao_page = cartao_pdf.pages[0]
    cartao_page.merge_page(nome_pdf.pages[0])
    final_writer = PdfWriter()
    final_writer.add_page(cartao_page)
    with open(f"{output_dir}/{nome.replace(' ', '_')}.pdf", "wb") as f:
        final_writer.write(f)

def main(pdf_path, lista_path, output_dir):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    nomes = ler_lista_presenca(lista_path)
    cartoes, template_pdf = recortar_cartoes(pdf_path)
    if len(cartoes) < len(nomes):
        print(f"Quantidade de acessos insuficientes, faltam {len(nomes) - len(cartoes)} acessos")
        return

    for idx, nome in enumerate(nomes):
        gerar_cartao_pdf(nome, template_pdf, cartoes[idx], idx, output_dir)
    for idx in range(len(nomes), len(cartoes)):
        gerar_cartao_pdf(f"convidado_{idx - len(nomes) + 1:02d}", template_pdf, cartoes[idx], idx, output_dir)

if __name__ == "__main__":
    main()
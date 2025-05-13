from datetime import datetime
import os
import re
import fitz
from pdf2image import convert_from_path
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

poopler = r"C:\poppler-24.08.0\Library\bin"

pastaNF = "./NFs"
regex1 = {
    "cnpjEncontrados": r"\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}",
    "numeroNota": r"&num=(\d+)&",
    "datas": r"(\d{2}/\d{2}/\d{4})",
    "ValorNF": r"(?<!\d)\b(?:\d{1,3}(?:\.\d{3})*|\d{1,4})\,\d{2}\b(?!\d)",
    "ChaveAcesso": r"\d{4}(?: \d{4}){10}",
}

"""NOTAS BRISA
    FILIAL: 04.418.538/0001-71 [0]
    FORNECEDOR: 77.765.840/0001-70 [2]
    
    for arquivo in os.listdir(pastaNF):
        with fitz.open(pastaNF + "\\" + arquivo) as pdf:
            if "contabilista" not in arquivo:
                break
            text = ""
            for page in pdf:
                text += page.get_text() + "\n"
                
            chave = re.findall(regex1["ChaveAcesso"], text)
            chave = chave[0].replace(" ", "") if chave else None
            
            numero_nf = int(chave[25:34])
            serie_nf = int(chave[22:25])
            cnpjFornecedor = chave[6:20]
            
            cnpj = re.findall(regex1["cnpjEncontrados"], text)
            cnpjFilial = cnpj[0].replace(".", "").replace("/", "").replace("-", "") if cnpj else None
            print(cnpjFilial, cnpjFornecedor, numero_nf, serie_nf)
            datas = re.findall(regex1["datas"], text)
            dataEmissao = datas[0] if datas else None
            print(dataEmissao)
            
            valorNF = re.findall(regex1["ValorNF"], text)
            valorNF = (
                    max([float(v.replace(".", "").replace(",", ".")) for v in valorNF])
                    if valorNF
                    else None
                )
            print(valorNF)
"""

"""MAURICIO NOTA SERVICO BRISA
for arquivo in os.listdir(pastaNF):
        pdf_path = pastaNF + "\\" + arquivo
        if "mauricio" in arquivo:
            paginas = convert_from_path(pdf_path, dpi=300, poppler_path=poopler)
            for i, imagem in enumerate(paginas):
                text = pytesseract.image_to_string(imagem, lang="eng")
            cnpj = re.findall(regex1["cnpjEncontrados"], text)
            datas = re.findall(regex1["datas"], text)
            valorNF = re.findall(regex1["ValorNF"], text)

            cnpjFilial = cnpj[1].replace(".", "").replace("/", "").replace("-", "")
            cnpjFornecedor = cnpj[0].replace(".", "").replace("/", "").replace("-", "")
            
            valorNF = re.findall(regex1["ValorNF"], text)
            valorNF = (
                    max([float(v.replace(".", "").replace(",", ".")) for v in valorNF])
                    if valorNF
                    else None
                )
            datas_convertidas = []
            for data in datas:
                try:
                    datas_convertidas.append(
                        datetime.strptime(data, "%d/%m/%Y")
                    )
                except ValueError:
                    pass  # Ignora datas inválida
            
            dataEmissao = min(datas_convertidas) if datas_convertidas else None
            dataEmissao = dataEmissao.strftime("%d/%m/%Y") if dataEmissao else None

            print(cnpjFilial, cnpjFornecedor, dataEmissao, valorNF)

"""


def main():
    for arquivo in os.listdir(pastaNF):
        pdf_path = pastaNF + "\\" + arquivo
        if "prixx" in arquivo:
            paginas = convert_from_path(pdf_path, dpi=300, poppler_path=poopler)
            for i, imagem in enumerate(paginas):
                text = pytesseract.image_to_string(imagem, lang="eng")
            cnpj = re.findall(regex1["cnpjEncontrados"], text)
            datas = re.findall(regex1["datas"], text)
            valorNF = re.findall(regex1["ValorNF"], text)

            cnpjFilial = cnpj[0].replace(".", "").replace("/", "").replace("-", "")
            
            chave = re.findall(regex1["ChaveAcesso"], text)
            chave = chave[0].replace(" ", "") if chave else None
            
            numero_nf = int(chave[25:34])
            serie_nf = int(chave[22:25])
            cnpjFornecedor = chave[6:20]
            
            
            valorNF = re.findall(regex1["ValorNF"], text)
            valorNF = (
                    max([float(v.replace(".", "").replace(",", ".")) for v in valorNF])
                    if valorNF
                    else None
                )
            datas_convertidas = []
            for data in datas:
                try:
                    datas_convertidas.append(
                        datetime.strptime(data, "%d/%m/%Y")
                    )
                except ValueError:
                    pass  # Ignora datas inválida
            
            dataEmissao = min(datas_convertidas) if datas_convertidas else None
            dataEmissao = dataEmissao.strftime("%d/%m/%Y") if dataEmissao else None

            print(cnpjFilial, cnpjFornecedor, dataEmissao, valorNF, numero_nf, serie_nf)


main()

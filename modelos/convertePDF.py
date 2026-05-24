import subprocess
from pathlib import Path

def filtrar_e_converter_para_pdf(pasta_analises, termo_filtro):
    caminho_pasta = Path(pasta_analises)
    # Filtra os arquivos .docx com base no termo fornecido
    arquivos_docx = [
        arq for arq in caminho_pasta.glob("*.docx") 
        if termo_filtro.lower() in arq.name.lower()
    ]
    
    if not arquivos_docx:
        print(f"Nenhum arquivo encontrado com o termo '{termo_filtro}' em {pasta_analises}")
        return

    print(f"Encontrados {len(arquivos_docx)} arquivos para conversão...")

    for docx_path in arquivos_docx:
        pdf_path = docx_path.with_suffix('.pdf')
        print(f"Convertendo: {docx_path.name} -> {pdf_path.name}")
    
        try:
            # Executa a conversão baseada no Sistema Operacional Linux
                subprocess.run([
                    'libreoffice', 
                    '--headless', 
                    '--convert-to', 'pdf', 
                    '--outdir', str(caminho_pasta), 
                    str(docx_path)
                ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                # exclui o arquivo .docx somente se o PDF foi gerado com sucesso
                if pdf_path.exists() and pdf_path.stat().st_size > 0:
                    docx_path.unlink()
                    print(f"  ↳ [SUCESSO] {docx_path.name} excluído do diretório.")
                else:
                    print(f"  ↳ [ALERTA] Falha ao gerar o PDF. O arquivo original .docx foi mantido.")

        except Exception as e:
                print(f"  ↳ [ERRO] Falha no processamento do arquivo {docx_path.name}: {e}")            
    print("Processo de conversão concluído!")

filtrar_e_converter_para_pdf(
        pasta_analises='analises',
        termo_filtro='Positiva'
    )
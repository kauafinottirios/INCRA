from modelos.preencherDados import preencher_modelo
from modelos.convertePDF import filtrar_e_converter_para_pdf

def criar_modelo_gru_positiva(dadosProcesso):
    # ler os dados do arquivo txt e armazenar em um dicionário
    dicionario = {
        '[processo]': dadosProcesso[0],
        '[sipra]': dadosProcesso[1],
        '[dataTitulo]': dadosProcesso[2],
        '[beneficiario]': dadosProcesso[3],
        '[cpf]': dadosProcesso[4],
        '[PA]': dadosProcesso[5],
        '[numLote]': dadosProcesso[6],
        '[municipio]': dadosProcesso[7],
        '[analise]': dadosProcesso[8],
        '[nupRequerimento]': dadosProcesso[9],
        '[nupExtrato]': dadosProcesso[10],
        '[nupGuiaGRU]': dadosProcesso[11],
        '[nupMemoria]': dadosProcesso[12]
    }

    # preencher o template com os dados do dicionário
    preencher_modelo(
        caminho_template='modelos/templates/template_GRU_Positiva.docx',
        pasta_destino='modelos/analises',
        nome_arquivo_saida=f'kauã - {dicionario["[processo]"]} - GRU Positiva.docx',
        dados=dicionario
    )

    filtrar_e_converter_para_pdf(
        pasta_analises='modelos/analises',
        termo_filtro='positiva'
    )
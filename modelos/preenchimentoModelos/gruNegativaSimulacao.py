from modelos.preencherDados import preencher_modelo

def criar_modelo_gru_negativa_simulacao(dadosProcesso):
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
        '[nupDespacho]': dadosProcesso[11],
        '[nupSimulacao]': dadosProcesso[12],
        '[nupReqCondicoes]': dadosProcesso[13]
    }

    # preencher o template com os dados do dicionário
    preencher_modelo(
        caminho_template='modelos/templates/template_GRU_Negativa_Simulacao.docx',
        pasta_destino='modelos/analises',
        nome_arquivo_saida=f'kauã - {dicionario["[processo]"]} - GRU Negativa com Simulacao.docx',
        dados=dicionario
    )

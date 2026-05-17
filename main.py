from modelos.gruPositiva import criar_modelo_gru_positiva
from modelos.gruPositivaPendencia import criar_modelo_gru_positiva_pendencia

# ler os dados do arquivo txt e armazenar em um dicionário

def constroi_dicionario(dados):
    dicionario = {
        'processo': dados[0],
        'sipra': dados[1],
        'dataTitulo': dados[2],
        'beneficiario': dados[3],
        'cpf': dados[4],
        'PA': dados[5],
        'numLote': dados[6],
        'municipio': dados[7],
        'analise': dados[8]
    }
    return dicionario


def ler_dados():
    dados = []
    dicionario = {}
    with open('dadosTitulos.txt', 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(', ')
            dicionario = constroi_dicionario(dados)
            match dicionario['analise']:
                case 'gruPositiva':
                    criar_modelo_gru_positiva(dicionario)
                case 'gruPositivaPendencia':
                    criar_modelo_gru_positiva_pendencia(dicionario)
                case _:
                    print('Análise desconhecida')         


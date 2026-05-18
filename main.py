from modelos.gruPositiva import criar_modelo_gru_positiva
from modelos.gruPositivaPendencia import criar_modelo_gru_positiva_pendencia
from modelos.gruNegativaSimulacao import criar_modelo_gru_negativa_simulacao
from modelos.gruNegativaSoDespacho import criar_modelo_gru_negativa_so_despacho
from modelos.gruNegativaQuitacao import criar_modelo_gru_negativa_quitacao
from modelos.gruNegativaSemTA import criar_modelo_gru_negativa_sem_ta
from modelos.tcuNegativaSemTA import criar_modelo_tcu_negativa_sem_ta
from modelos.tcuNegativaSimulacao import criar_modelo_tcu_negativa_simulacao
from modelos.tcuNegativaOutroBeneficiario import criar_modelo_tcu_negativa_outro_beneficiario

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

def seleciona_modelo(analise, dadosTitulo):
    match analise:
        case 'gruPositiva':
            criar_modelo_gru_positiva(dadosTitulo)
        case 'gruPositivaPendencia':
            criar_modelo_gru_positiva_pendencia(dadosTitulo)
        case 'gruNegativaSimulacao':
            criar_modelo_gru_negativa_simulacao(dadosTitulo)
        case 'gruNegativaSoDespacho':
            criar_modelo_gru_negativa_so_despacho(dadosTitulo)
        case 'gruNegativaQuitacao':
            criar_modelo_gru_negativa_quitacao(dadosTitulo)
        case 'gruNegativaSemTA':
            criar_modelo_gru_negativa_sem_ta(dadosTitulo)
        case 'tcuNegativaSemTA':
            criar_modelo_tcu_negativa_sem_ta(dadosTitulo)
        case 'tcuNegativaSimulacao':
            criar_modelo_tcu_negativa_simulacao(dadosTitulo)
        case 'tcuNegativaOutroBeneficiario':
            criar_modelo_tcu_negativa_outro_beneficiario(dadosTitulo)
        case _:
            print('Análise desconhecida')


def ler_dados(arquivo_dados):
    dados = []
    with open(arquivo_dados, 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(', ')
            dicionario = constroi_dicionario(dados)
            seleciona_modelo(dicionario['analise'], dicionario)         

ler_dados('dadosTitulos.txt')
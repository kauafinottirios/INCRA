from modelos.preenchimentoModelos.gruPositiva import criar_modelo_gru_positiva
from modelos.preenchimentoModelos.gruPositivaPendencia import criar_modelo_gru_positiva_pendencia
from modelos.preenchimentoModelos.gruNegativaSimulacao import criar_modelo_gru_negativa_simulacao
from modelos.preenchimentoModelos.gruNegativaSoDespacho import criar_modelo_gru_negativa_so_despacho
from modelos.preenchimentoModelos.gruNegativaQuitacao import criar_modelo_gru_negativa_quitacao
from modelos.preenchimentoModelos.gruNegativaSemTA import criar_modelo_gru_negativa_sem_ta
from modelos.preenchimentoModelos.tcuNegativaSemTA import criar_modelo_tcu_negativa_sem_ta
from modelos.preenchimentoModelos.tcuNegativaSimulacao import criar_modelo_tcu_negativa_simulacao
from modelos.preenchimentoModelos.tcuNegativaOutroBeneficiario import criar_modelo_tcu_negativa_outro_beneficiario


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
            print(f'Dados lidos: {dados}')
            seleciona_modelo(dados[8], dados)         


ler_dados('dadosTitulos.txt')
## AUTOMAÇÕES DE FLUXO DOS PROCESSO
O presente repositório será usado para armazenar programas para automatizar:
* preenchimento de modelos de análises;
* preenchimento da planilha de relatório;

### Tipos de análises:
* gruPositiva
* gruPositivaPendencia
* gruNegativaSimulacao
* gruNegativaSoDespacho
* gruNegativaQuitacao
* gruNegativaSemTA
* tcuNegativaSemTA
* tcuNegativaSimulacao
* tcuNegativaOutroBeneficiario

Os dados dos processos analisados devem estar em um arquivo _.txt_ estruturados da seguinte maneira:
* processo, sipra, data de emissao do Titulo, nome do beneficiario, cpf, PA, nº lote, município, tipo de analise, nupRequerimento

**os dados devem seguir estritamente a ordem acima e ser separados por ', '**

### Futuras melhorias
* deixar a entrada de dados menos estrita
* selecionar o arquivo de dados no gerenciador de arquivos
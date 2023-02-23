################################################################################
# Filtro de dict_msg depreciativas
# 
# Original Version: Joao Vitor - 13/01/2023
# Latest Version: Roberta Ramos & Joao Vitor - 19/01/2023
################################################################################

### BIBLIOTECAS ###

import pandas as pd

### MAIN ###
caminho_do_arquivo = r"C:\Users\joaov\Documentos\Code\Github\Python_projects\DataScience\filtro_depreciativas\dados_brutos.CSV"
df = pd.read_csv(caminho_do_arquivo, delimiter=",", encoding="ISO-8859-1")

print("Bem-vindo ao programa de filtragem das dict_msg depreciativas!")
print("Caracteristicas do arquivo:")
print("Linhas: ", len(df.index), "linhas")
print("Colunas: ", len(df.columns.values), "\n")

#print("Cabecalho: ", list(df.columns.values))

df['Concatenacao'] = df['Concatenacao'].str.strip()
df['Concatenacao'] = df['Concatenacao'].str.upper()

df_filtrado = pd.DataFrame()

dict_msg = {
        "cobranca_prazo": ["UMA\s+SEMANA\s+SEM\s+INTERNET","MAIS\s+DE\s+12H","SEM\s+INTERNET\s+HÁ\s+24H","PRECISO\s+TRABALHAR","PERDI\s+UM\s+DIA\s+DE\s+TRABALHO","TRABALHO\s+HOME\s+OFFICE","AGUARDANDO","AGUARD?","ALGUMA\s+PREVIS?O","PRECISO\s+QUE\s+RESOLVA","SEM\s+INTERNET\s+J?","DESDE\s+A\s+MADRUGADA\s+SEM\s+INTERNET","DESDE\s+ONTEM","ISSO\s+TUDO","IMPOSS?VEL\s+FICAR\s+ESSE\s+TEMPO","J?\s+PASSOU\s+8H","J?\s+PASSOU\s+3\s+MINUTOS","PREVIS?O","RESOLV?M\s+LOGO","QUERO\s+ISSO\s+PRA\s+HOJE","QUERO\s+AGORA","RESOLVERAM","T?M\s+?\s+M?S\s+QUE\s+N?O\s+RESOLVE","QUANT?\s+DEMORA","URG?NCIA","N?O\s+PODEM\s+DEMORA?","N?O\s+PODE\s+DEMORA","N?O\s+PODE\s+DEMORA?","V?M\s+QUE\s+HORA","V?M\s+QUE\s+HORA?","QUE\s+HORA?","MAIS\s+R?PIDO\s+POSS?VEL","PRIORIDADE","PRECISO\s+DA\s+INTERNET","EA?","E\s+AÍ","QUANDO","NO\s+AGUARD?","IRIA\s+VI?\s+HOJE","MUITO\s+TEMPO","QUINZE\s+DIAS","72H","24H","12H","24\s+HORA?","72\s+HORA?","TUDO\s+ISTO","TUDO\s+ISSO","AGUARDA?","VOU\s+FICAR","PRAZO","36H","QUANTO\s+TEMPO","T?M\s+?\s+DIAS","PASSOU\s+?\s+DIAS","PASSARAM\s+?\s+DIAS","ESPERANDO","ESTAMOS\s+DESDE","J?\s+T?M\s+TR?S\s+DIAS","QUE\s+HORAS","8\s+HORAS","O\s+QUE\s+ACONTECEU","VAI\s+HOJE","DESDE\s+DIA","MUITO\s+TEMPO","N?O\s+APARECEU","NINGU?M\s+APARECEU","AINDA\s+ESPERANDO","PRIORIDADE","4\s+HORAS","4H","PERDI\s+UM\s+DIA\s+DE\s+TRABALHO","PRECISO\s+PRA\s+HOJE","PRECISO\s+PARA\s+HOJE","QUANDO","SABER\s+POSIÇ?AO","SABER\s+POSIC?O","FALARAM\s+ISSO\s+ONTEM","FALARAM\s+?STO\s+ONTEM","AT?\s+AGORA\s+NADA","NADA\s+AINDA","12\s+HORAS","DEMORA","DEMORAR","PASSOU\s+DO\s+TEMPO","FALARAM\s+ISSO\s+ONTEM","24H","SEMANA","SEMANAS","PRA\s+HOJE","PARA\s+HOJE","TODO\s+ESSE\s+TEMPO","ESSE\s+TEMPO\s+TODO","SOLU??O","QUERO\s+SOLU??O","QUERO\s+UMA\s+RESPOSTA","QUERO\s+UMA\s+POSI??O","S?\s+VAI\s+VOLTAR","S?\s+VAI\s+VOLTA","TRABALHO\s+COM\s+INTERNET","TRABALHO\s+COM\s+A\s+INTERNET","FOI\s+FALADO\s+ONTEM","DESDE\s+ONTEM","POSI??O","8","URGENTE","PRECISO\s+R?PIDO","7\s+DIAS","SETE\s+DIAS","7\s+DIA","PRECISO\s+DE\s+AGORA","PRECISO\s+PRA\s+AGORA","PRECISO\s+PARA\s+AGORA","VC\s+IR?\s+AMANH?","VAI\s+VIR\s+AMANH?","VAI\s+VIM\s+AMANH?","E\s+AI","E\s+AGORA","J?\s+ARRUMARAM","N?O\s+POSSO\s+ESPERAR","N?O\s+POSSO\s+ESPERA","SABER\s+ANDAMENTO","SABER\s+SOBRE\s+O\s+ANDAMENTO","V?O\s+VIM","ESTOU\s+PRECISANDO\s+DA\s+INTERNET","CAD?\s+INTERNET","CAD?\s+A\s+INTERNET","VERIFICOU","PASSARAM\s+3\s+MINUTOS","J?\s+FORAM\s+3\s+MINUTOS","J?\s+PASSOU\s+3\s+MINUTOS","OITO\s+HORAS","QUINTA?FEIRA","HORAS\s+NA\s+ESPERA","ARRUMOU?","HORAS\s+SEM","TRABALHO\s+USANDO\s+INTERNET","INTERNET\s+PARA\s+TRABALHAR","INTERNET\s+PRA\s+TRABALHAR","PRECISO\s+DE\s+RESPOSTA","PRECISO\s+DE\s+UMA\s+RESPOSTA","3\s+MINUTOS","3\s+DIAS","VAI\s+RESOLVER","CAD?\s+A\s+RESPOSTA","N?O\s+TEM\s+COMO\s+VIR\s+ANTES","MAIS\s+DE\s+UM\s+M?S","TERIA\s+COMO\s+SER\s+RESOLVIDO\s+HOJE","AINDA\s+EM\s+MANUTEN??O","ALGUMA\s+NOVIDADE","QUERO\s+RESOLVER\s+AGORA","T?M\s+MAIS\s+DE\s+12\s+HS","ALGUM\s+RETORNO","J?\s+T?M\s+MAIS\s+DE\s+15\s+DIAS","AINDA\s+N?O\s+RETORNOU","J?\s+ERA\s+PRA\s+TER\s+RESOLVIDO","J?\s+SE\s+PASSARAM\s+MAIS\s+DE","AINDA\s+N?O\s+TIVE\s+RETORNO","PASSARAM\s+TR?S\s+MINUTOS","J?\s+PASSOU\s+2\s+HORAS","N?O\s+COMPARECEU","N\s+COMPARECEU","N\s+COMPARECE","N?O\s+COMPARECE","VINHA\s+HOJE","DISSERAM\s+QUE\s+VIRIA\s+HOJE","CAD?\s+O\s+TECNICO","CAD?\s+O\s+CARA","N?O\s+APARECEU","N\s+APARECEU","N\s+APARECE","N?O\s+APARECE","N?O\s+VEIO","N\s+VEIO","N?O\s+V?M","N\s+V?M","MARCADO\s+PRA\s+HOJE","MARCADO\s+PARA\s+HOJE","NINGU?M\s+V?M","NINGU?M\s+V?IO","N?O\s+V?IO","PASSOU\s+O\s+HOR?RAIO\s+AGENDADO","PASSOU\s+DO\s+HOR?RIO\s+AGENDADO","N?O\s+APARECEU\s+NINGU?M","FICOU\s+DE\s+IR\s+ONTEM\s+E\s+N?O\s+FOI","N?NCA\s+VAI\s+ESSE\s+T?CNICO","N?NCA\s+V?M\s+ESSE\s+T?CNICO","ERA\s+PRO\s+T?CNICO\s+IR\s+AT?","ERA\s+PARA\s+O\s+T?CNICO\s+VIR\s+AT?","AGENDEI\s+COM\s+UM\s+T?CNICO\s+ELE\s+N?O\s+APARECEU","T?CNICO\s+IR\s+HOJE\s+CEDO\s+ELE\s+N?O\s+FOI"],
        "sem_internet": ["SE?\s+INTERNET","FIOS\s+DE\s+CONEX?O","PEGOU\s+FOGO","N?O\s+RESOLVEU","N\s+RESOLVEU","N\s+RESOLVE","N?O\s+RESOLVE","N\s+DEU\s+CERTO","N?O\s+DEU\s+CERTO","INTERNET\s+CONTINUA\s+RUIM","CAMINH?O","CABO","FIBRA","FIO","N?O\s+EST?\s+INDO","N\s+EST?\s+INDO","N\s+T?\s+INDO","N?O\s+FUNCIONA","N?O\s+FUNCIONOU","N?O\s+EST?\s+FUNCIONANDO","N?O\s+T?\s+FUNCIONANDO","N\s+T?\s+FUNCIONANDO","N?O\s+VOLTA","N?O\s+VOLTOU","N\s+VOLT?","SEM\s+ACESSO","ROUBO\s+DE\s+CABO","SEM\s+NET","SAIU\s+DO\s+AR","FORA\s+DO\s+AR","N\s+EST?\s+FUNCIONADO","DEFEITO","SEM\s+SINAL","N?O\s+CONSIGO\s+ABRI","N\s+CONSIGO\s+ABRI","N?O\s+CONSIGO\s+ABRIR","NADA\s+FUNCINA","QUEIMADO","APAGOU\s+TUDO","TUDO\s+APAGADO","N\s+T?\s+PEGANDO","N?O\s+T?\s+PEGANDO","N?O\s+EST?\s+PEGANDO","ARREBENTADO","ARREBENTOU","SEM\s+NET","N?O\s+FUNCIONO","N?O\s+ADIANTOU","N?O\s+ADIANTO","N\s+ADIANTO","5\s+MINUTOS","CONTINUO\s+?EM\s+INTERNET","N?O\s+F?NCIONA","INTERNET\s+N?O\s+F?NCIONA","N?O\s+T?\s+CONECTANDO","N\s+T?\s+CONECTANDO","N?O\s+EST?\s+CONECTANDO","NADA\s+RESOLVIDO","SEM\s+FUNCIONAR","SEM\s+FUNCIONA","N?O\s+RESOLVIDO","N\s+RESOLVIDO","N?O\s+NORMALIZOU","N?O\s+TEM\s+INTERNET","N?O\s+T?\s+FUNCIONANDO","N?O\s+TENHO\s+INTERNET","PRECISO\s+INTERNET","SEM\s+CONEX?O","N?O\s+T?M\s+ACESSO","N?O\s+CONSIGO\s+CONECTAR","FIZ\s+OS\s+PROCEDIMENTOS\s+E\s+NADA"],
        "sol_tec": ["MODEM\s+RUIM","MODEM\s+QUEBRADO","AGENDAMENTO","SUPORTE\s+T?CNICO","T?CNICO","AGENDAR","AGENDA","VISITA","CONCERTAR","CONCERTA","REPARO","T?CNICA","CHAMADO","ESPECIALISTA","TROCAR\s+MODEM","TROCA\s+MODEM","TROCA\s+DE\s+MODEM","APARELHO\s+QUEBROU","APARELHO\s+QUEBRADO","MODEM\s+QUEIMOU","SOLICITAR\s+A\s+TROCA\s+DE\s+M?DEM","SOLICITAR\s+TROCA\s+DE\s+M?DEM","MODEM\s+QUEBROU"],
        "info_fatura": ["FATURA","PAGAR","DESCONTO\s+NA\s+FATURA","DESCONTO\s+FATURA","VOU\s+PAGAR\s+O\s+MESMO\s+VALOR","VOU\s+PAGA\s+O\s+MESMO\s+VALO","C?DIGO\s+DE\s+BARRAS","C?DIGO","REEMBOLSO","DESCONTO","DESCONTAR","DESCONTO","BOLETO","CONTA","COBRANÇA\s+INDEVIDA","CONTA","SEGUNDA\s+VIA"],
        "cancelamento": ["CA?CELAMENTO","CANCELAR","VOU\s+PARA\s+CLARO","VOU\s+PARA\s+OI","VOU\s+PARA\s+VIVO","VOU\s+MUDAR\s+DE\s+OPERADORA","VOU\s+MUDA\s+DE\s+OPERADORA","QUERO\s+CANCELA","VOU\s+CANCELA"],
        "qualidade": ["INSTABILIDADE","BAIXA\s+VELOCIDADE","QUEDAS\s+CONSTANTES","QUEDAS\s+CONSTANTE","QUEDA\s+CONSTANTES","QUEDA\s+CONSTANTE","TODA\s+SEMANA","TODO\s+DIA","TODOS\s+OS\s+DIAS","PORCARIA","DEFEITO","TODA\s+HORA","PROBLEMA","CONSTANTEMENTE","CAINDO","ANATEL","TODA\s+NOITE","TODAS\s+AS\s+NOITES","INST?VEL","OSCILANDO","OSCILA","ALCANCE","DIMINUI","DIMINUIU","REDE\s+2G","LENT?","LENTID?O","RUIM","BAIXA","HORR?VEL","MAIS\s+N?O\s+NO\s+CEL","MAIS\s+N?O\s+NO\s+CEL","MUITO\s+ABAIXO","ABAIXO","CONTRATAD?","WIFI","WI-FI","???\s+MEGAS","??\s+MEGAS","???\s+MEGA","??\s+MEGA","2G","TODA\s+VEZ\s+AGORA","S?\s+VIVE\s+ASSIM","RECORRENTE","FALHANDO","2\s+G","METADE","PAGO","N?O\s+CONSIGO\s+TER\s+UM\s+DIA","N?O\s+T?M\s+UM\s+DIA","TOD?\s+M?S","CAI","CAINDO","RECLAMA??O","SIDO\s+CONSTANTE","TRAVA","QUEDAS","SINAL\s+FRACO","PORCARIA","EST?\s+ACONTECENDO\s+TODA\s+SEMANA","MUITO\s+BAIXO","ACONTECENDO\s+FREQU?NTEMENTE","RECLAMAR\s+DA\s+BANDA\s+LARGA","MINHA\s+INTERNET\s+N?O\s+PRESTA","SINAL\s+FICA\s+MUITO\s+FRACO"],
        "insatisfacao": ["TUDO\s+ISSO","SERVI?O\s+PRESTADO","ABSURDO","BRINCADEIRA","BRINCADERA","PALHA?ADA","FALTA\s+DE\s+RESPEITO","FALTA\s+RESPEITO","LIXO","PQP","MERDA","RID?CULO","PORCARIA","INSUSTENT?VEL","TIM","COMO\s+SEMPRE","DESRESPEITO","ADVOGADO","MERDA","FILHA\s+DA\s+PUTA","FDP","SFD","FUDE","FUDER","FODE","FODER","P?SSIMO\s+ATENDIMENTO","TOMAR\s+NO","TOMA\s+NO","DESISTO","CONTRATO","?DIO","TRISTE","INSATISFEITO","CARALHO","PUTA","DECP??O","LAMENT?VEL","PAGO\s+PRA\s+N?O\s+TER\s+INTERNET","N?O\s+CONCORDO","N\s+CONCORDO","MENTIRA","AFF","QUE\s+ISSO","N?O\s+AGUENTO\s+MAIS","IRRESPONS?VEIS","DESGRA?A","MDS","MEU\s+DEUS","RID?CULO","POXA","N?O\s+?\s+POSS?VEL","SEMPRE\s+A\s+MESMA\s+RESPOSTA","RESPOSTA\s+?\s+SEMPRE\s+A\s+MESMA","PUTZ","FODA","VERGONH?","PROCON","VAGABUND?","NOVAMENTE","INFERN?","DISCURSO","P?SSIM?","PUXA","HIT?RIA","CU","CÚ","MISERIC?RDIA","MENTIROS?S","SACANAGEM","REEMBOL","SACO\s+CHEIO","CARAMBA","CARACA","ARROMBADOS","VTNC","BOSTA","IN?TIL","PIOR\s+OPERADORA","DEIXANDO\s+?\s+DESEJAR","DEIXA\s+?\s+DESEJAR","DEIXANDO\s+?\s+DESEJA","HORROR","NOTA\s+ZERO","DIF?CIL","INSATISFEIT?","SACANAGEM","ABORRECID?","PORRA","INACREDITVEL","N?O\s+ACREDITO","N\s+ACREDITO","SEMPRE\s+A\s+MESMA\s+COISA","CACETE","SERVE\s+PRA\s+NADA","SERVE\s+PARA\s+NADA","BOSTA","INSATISFEIT?\s+COM\s+O\s+SERVI?O","FALTA\s+DE\s+RESPEITO","IN?TEIS","PELO\s+AMOR\s+DE\s+DEUS","N?O\s+ACEITO\s+ISSO","VOC?S\s+S?O\s+UMA\s+PIADA","VCS\s+S?O\s+UMA\s+PIADA","PIADA""DE\s+NOVO\s+ISSO"]
}

print("Aplicando", len(dict_msg), "filtros... \n")
for lista in dict_msg:
    for valor in dict_msg[lista]:
        df_filtrado = pd.concat([df_filtrado, df[df.Concatenacao.str.contains(valor, True)]])
        # df_filtrado = pd.concat([df_filtrado, df[df.Concatenacao.str.contains(dict_msg, True)]])
        # print(df_filtrado)
        

print("Filtragem realizada com sucesso.")
print("Agradecemos a preferencia!")

"""
dataframe final =  {
            "service": df['Service'],
            "mensagem do cliente": df['Concatenacao'],
            "tabulacao da mensagem depreciativa": [],
            "data": df['Data'],
            "analise sistemica": [], 
            "resumo analise sistemica do processo de triagem": [],
            "tabulacao de conclusao": df['Mensagem Anterior'],
            "status": [],
        }

Dataframe final terá:
        'resumo analise sistemica do processo de triagem' = vazio
        'analise sistemica' = vazio
        'status' = vazio

A coluna 'tabulação conclusão' é igual coluna 'mensagem anterior', no entanto... 
se houver "Vi que existe uma instabilidade na sua região" na coluna mensagem anterior
preencher o novo dataframe assim:
        'tabulacao de conclusao' = "Retorno de Massiva"
        'resumo analise sistemica do processo de triagem' = "Retido - Falha Massiva"
        'analise sistemica' = "Ticket Não Aberto"
        'status' = "Ticket Não Aberto"
        
"""

def parse_row(row):
    if row[0] == 'DT_NOTIFIC':
        return row
    print(row)
    print(len(row))
    row[16] = get_CS_GESTANT_desc(row[16])
    row[17] = get_CS_RACA_desc(row[17])
    row[19] = get_CS_ESCOL_N_desc(row[19])
    row[27] = get_CS_ZONA_desc(row[27])
    row[79] = get_SUPORT_VEN_desc(row[79])
    row[80] = get_RAIOX_RES_desc(row[80])
    row[85] = get_TP_AMOSTRA_desc(row[85])
    row[107] = get_CLASSI_FIN_desc(row[107])
    row[109] = get_CRITERIO_desc(row[109])
    row[110] = get_EVOLUCAO_desc(row[110])
    row[128] = get_TOMO_RES_desc(row[128])
    row[145] = get_TP_SOR_desc(row[145])
    row[148] = get_CS_RACA_desc(row[148])
    row[28] = get_yes_or_no(row[28])
    row[29] = get_yes_or_no(row[29])
    row[31] = get_yes_or_no(row[31])
    row[32] = get_yes_or_no(row[32])
    row[33] = get_yes_or_no(row[33])
    row[34] = get_yes_or_no(row[34])
    row[35] = get_yes_or_no(row[35])
    row[36] = get_yes_or_no(row[36])
    row[37] = get_yes_or_no(row[37])
    row[38] = get_yes_or_no(row[38])
    row[39] = get_yes_or_no(row[39])
    row[41] = get_yes_or_no(row[41])
    row[42] = get_yes_or_no(row[42])
    row[43] = get_yes_or_no(row[43])
    row[44] = get_yes_or_no(row[44])
    row[45] = get_yes_or_no(row[45])
    row[46] = get_yes_or_no(row[46])
    row[47] = get_yes_or_no(row[47])
    row[48] = get_yes_or_no(row[48])
    row[49] = get_yes_or_no(row[49])
    row[50] = get_yes_or_no(row[50])
    row[51] = get_yes_or_no(row[51])
    row[52] = get_yes_or_no(row[52])
    row[53] = get_yes_or_no(row[53])
    row[57] = get_yes_or_no(row[57])
    row[69] = get_yes_or_no(row[69])
    row[76] = get_yes_or_no(row[76])
    row[83] = get_yes_or_no(row[83])
    row[114] = get_yes_or_no(row[114])
    row[124] = get_yes_or_no(row[124])
    row[125] = get_yes_or_no(row[125])
    row[126] = get_yes_or_no(row[126])
    row[137] = get_yes_or_no(row[137])
    #for i in range(0, len(row)):
    #    if i == 16:
    #        new_row[i] = get_CS_GESTANT_desc(row[i])
    #    elif i == 17:
    #        new_row[i] = get_CS_RACA_desc(row[i])
    #    elif i == 19:
    #        new_row[i] = get_CS_ESCOL_N_desc(row[i])
    #    elif i == 27:
    #        new_row[i] = get_CS_ZONA_desc(row[i])
    #    elif i == 79:
    #        new_row[i] = get_SUPORT_VEN_desc(row[i])
    #    elif i == 80:
    #        new_row[i] = get_RAIOX_RES_desc(row[i])
    #    elif i == 85:
    #        new_row[i] = get_TP_AMOSTRA_desc(row[i])
    #    elif i == 107:
    #        new_row[i] = get_CLASSI_FIN_desc(row[i])
    #    elif i == 109:
    #        new_row[i] = get_CRITERIO_desc(row[i])
    #    elif i == 110:
    #        new_row[i] = get_EVOLUCAO_desc(row[i])
    #    elif i == 128:
    #        new_row[i] = get_TOMO_RES_desc(row[i])
    #    elif i == 145:
    #        new_row[i] = get_TP_SOR_desc(row[i])
    #    elif i == 148:
    #        new_row[i] = get_CS_RACA_desc(row[i])
    #    elif i == 28 or 29 or 31 or 32 or 33 or 34 or 35 or 36 or 37 or 38 or 39 or 41 or 42 or 43 or 44 or 45 or 46 or 47 or 48 or 49 or 50 or 51 or 52 or 53 or 57 or 69 or 76 or 83 or 114 or 124 or 125 or 126 or 137:
    #        new_row[i] = get_yes_or_no(row[i])
    #    else:
    #        new_row[i] = row[i]
    print(row)
    return row

def get_CS_GESTANT_desc(CS_GESTANT):
    if CS_GESTANT == '1':
        return 'Primeiro Trimestre'
    elif CS_GESTANT == '2':
        return 'Segundo Trimestre'
    elif CS_GESTANT == '3':
        return 'Terceiro Trimestre'
    elif CS_GESTANT == '4':
        return 'Idade Gestacional Ignorada'
    elif CS_GESTANT == '5':
        return 'Não'
    elif CS_GESTANT == '6':
        return 'Não se aplica'
    elif CS_GESTANT == '9':
        return 'Ignorado'
    else:
        return 'Ignorado'

def get_CS_RACA_desc(CS_RACA):
    if CS_RACA == '1':
        return 'Branca'
    elif CS_RACA == '2':
        return 'Preta' 
    elif CS_RACA == '3':
        return 'Amarela'
    elif CS_RACA == '4':
        return 'Parda'
    elif CS_RACA == '5':
        return 'Indígena'
    elif CS_RACA == '9':
        return 'Ignorado'
    else:
        return 'Ignorado'

def get_CS_ESCOL_N_desc(CS_ESCOL_N):
    if CS_ESCOL_N == '0':
        return 'Sem escolaridade/Analfabeto'
    elif CS_ESCOL_N == '1':
        return 'Fundamental 1º ciclo (1ª a 5ª série)'
    elif CS_ESCOL_N == '2':
        return 'Fundamental 2º ciclo (6ª a 9ª série)' 
    elif CS_ESCOL_N == '3':
        return 'Médio (1º ao 3º ano)'
    elif CS_ESCOL_N == '4':
        return 'Superior'
    elif CS_ESCOL_N == '5':
        return 'Não se aplica'
    elif CS_ESCOL_N == '9':
        return 'Ignorado'
    else:
        return 'Ignorado'

def get_CS_ZONA_desc(CS_ZONA):
    if CS_ZONA == '1':
        return 'Urbana'
    elif CS_ZONA == '2':
        return 'Rural' 
    elif CS_ZONA == '3':
        return 'Periurbana'
    elif CS_ZONA == '9':
        return 'Ignorado'
    else:
        return 'Ignorado'

def get_SUPORT_VEN_desc(SUPORT_VEN):
    if SUPORT_VEN == '1':
        return 'Sim, invasivo'
    elif SUPORT_VEN == '2':
        return 'Sim, não invasivo'
    elif SUPORT_VEN == '3':
        return 'Não'
    elif SUPORT_VEN == '9':
        return 'Ignorado'
    else:
        return 'Ignorado'

def get_RAIOX_RES_desc(RAIOX_RES):
	if RAIOX_RES == '1':
	    return 'Normal'
    elif RAIOX_RES == '2':
        return 'Infiltrado intersticial'
    elif RAIOX_RES == '3':
        return 'Consolidação'
    elif RAIOX_RES == '4':
        return 'Misto'
    elif RAIOX_RES == '5':
        return 'Outro'
    elif RAIOX_RES == '6':
        return 'Não realizado'
    elif RAIOX_RES == '9':
        return 'Ignorado'
    else:
        return 'Ignorado'

def get_TP_AMOSTRA_desc(TP_AMOSTRA):
	if TP_AMOSTRA == '1':
		return 'Secreção de Nasoorofaringe'
	elif TP_AMOSTRA == '2':
		return 'Lavado Broco-alveolar'
	elif TP_AMOSTRA == '3':
		return 'Tecido post-mortem'
	elif TP_AMOSTRA == '4':
		return 'Outra, qual?'
	elif TP_AMOSTRA == '5':
		return 'LCR'
	elif TP_AMOSTRA == '9':
		return 'Ignorado'
    else:
        return 'Ignorado'


def get_CLASSI_FIN_desc(CLASSI_FIN):
	if CLASSI_FIN == '1':
		return 'SRAG por influenza'
	elif CLASSI_FIN == '2':
		return 'SRAG por outro vírus respiratório'
	elif CLASSI_FIN == '3':
		return 'SRAG por outro agente etiológico, qual:'
	elif CLASSI_FIN == '4':
		return 'SRAG não especificado'
	elif CLASSI_FIN == '5':
		return 'SRAG por COVID-19'
	elif CLASSI_FIN == '9':
		return 'Ignorado'
    else:
        return 'Ignorado'


def get_CRITERIO_desc(CRITERIO):
	if CRITERIO == '1':
		return 'Laboratorial'
	elif CRITERIO == '2':
		return 'Clínico Epidemiológico'
	elif CRITERIO == '3':
		return 'Clínico'
	elif CRITERIO == '4':
		return 'Clínico Imagem'
	elif CRITERIO == '9':
		return 'Ignorado'
    else:
        return 'Ignorado'


def get_EVOLUCAO_desc(EVOLUCAO):
	if EVOLUCAO == '1':
		return 'Cura'
	elif EVOLUCAO == '2':
		return 'Óbito'
	elif EVOLUCAO == '3':
		return 'Óbito por outras causas'
	elif EVOLUCAO == '9':
		return 'Ignorado'
    else:
        return 'Ignorado'


def get_TOMO_RES_desc(TOMO_RES):
	if TOMO_RES == '1':
		return 'Tipico COVID-19'
	elif TOMO_RES == '2':
		return 'Indeterminado COVID-19'
	elif TOMO_RES == '3':
		return 'Atípico COVID-19'
	elif TOMO_RES == '4':
		return 'Negativo para Pneumonia'
	elif TOMO_RES == '5':
		return 'Outro'
	elif TOMO_RES == '6':
		return 'Não realizado'
	elif TOMO_RES == '9':
		return 'Ignorado'
    else:
        return 'Ignorado'


def get_TP_AM_SOR_desc(TP_AM_SOR):
	if TP_AM_SOR == '1':
		return 'Sangue/plasma/soro'
	elif TP_AM_SOR == '2':
		return 'Outra, qual?'
	elif TP_AM_SOR == '9':
		return 'Ignorado'
    else:
        return 'Ignorado'   


def get_TP_SOR_desc(TP_SOR):
	if TP_SOR == '1':
		return 'Teste rápido'
	elif TP_SOR == '2':
		return 'Elisa'
	elif TP_SOR == '3':\
		return 'Quimiluminescência'
	elif TP_SOR == '4':
		return 'Outro, qual'
	elif TP_SOR == '9':
		return 'Ignorado'
    else:
        return 'Ignorado'

def get_yes_or_no(cod):
    if cod == '1':
        return 'Sim'
    elif cod == '2':
        return 'Não'
    elif cod == '9':
        return 'Ignorado'
    else:
        return 'Ignorado'
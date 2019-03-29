# coding: utf-8
#
# QSAPJ
#
# Código desenvolvido em linguagem Python que trata o arquivo que contém o Quadro de Sócios e Administradores das Pessoas Jurídicas (QSAPJ) disponível no sítio da Receita Federal do Brasil (RFB) e, em seguida, gera um arquivo TXT com os dados separados por ponto e vírgula.
# 
# Versão: 28.03.2019
# 
# Licenciamento: GNU General Public License v3.0
# 
# Informações:
# 
# 1) http://receita.economia.gov.br/orientacao/tributaria/cadastros/consultas-cnpj
# 
# 2) http://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-abertos-do-cnpj

import os
import requests
import string

class QSAPJ:
    
    def __init__(self, uf, nome):
        url = "http://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/consultas/download/Socios"
        extensao = ".txt"
        self.uri = url + uf.upper() + extensao
        self.nomearq = nome + uf.upper() + extensao
        self.dados = [["TIPO", "CNPJ", "INDICADOR_CPF_CNPJ", "CPF_CNPJ_DO_SOCIO", "QUALIFICACAO_DO_SOCIO", "NOME_EMPRESARIAL_OU_NOME_DO_SOCIO"]]
    
    # Copia o arquivo TXT disponível no sítio da RFB
    def CopiarArquivo(self, uri, nomearq):
        r = requests.get(uri)
        try:
            r.raise_for_status()
        except Exception as exc:
            mensagem = "Há um problema: %s" % (exc)
            print(mensagem)
        
        endereco = os.path.join(os.getcwd(), nomearq)
        with open(endereco, 'wb') as arquivo:
            for chunk in r.iter_content(100000):
                arquivo.write(chunk)
    
    # Copia o conteúdo do arquivo TXT
    def CopiarDados(self, nomearq):
        endereco = os.path.join(os.getcwd(), nomearq)
        with open(endereco, 'rt', encoding='ISO-8859-1') as arquivo:
            texto = arquivo.readlines()
        
        for i in texto:
            aux = []
            tipo = i[:2]
            if tipo == "01": # Tipo = 01 - Informação da empresa
                aux.append(i[:2])
                aux.append(i[2:16])
                aux.append('')
                aux.append('')
                aux.append('')
                aux.append(i[16:166].rstrip())
                self.dados.append(aux)
            elif tipo == "02": # Tipo = 02 - Informação do sócio
                aux.append(i[:2])
                aux.append(i[2:16])
                aux.append(i[16:17])
                aux.append(i[17:31])
                aux.append(i[31:33])
                aux.append(i[33:183].rstrip())
                self.dados.append(aux)
            else:
                print("Erro: tipo desconhecido.")
    
    # Gera um novo arquivo TXT
    def GerarArquivo(self, nomearq, dados):
        endereco = os.path.join(os.getcwd(), nomearq)
        with open(endereco, 'wt') as arquivo:
            for i in dados:
                arquivo.write(';'.join(i))
                arquivo.write('\n')

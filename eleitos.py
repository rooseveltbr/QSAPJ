# coding: utf-8
#
# Eleitos
#
# Código desenvolvido em linguagem Python que busca pelos candidatos eleitos no Quadro de Sócios e Administradores das Pessoas Jurídicas (QSAPJ).
#
# Versão: 09.04.2019
#
# Autor: Roosevelt Gonçalves Oliveira - https://github.com/rooseveltbr
#
# Licenciamento: GNU General Public License v3.0
#
# Informações sobre Eleições, CNPJ e QSAPJ:
#
# 1) http://www.tse.jus.br/eleicoes/estatisticas/estatisticas-eleitorais
#
# 2) http://receita.economia.gov.br/orientacao/tributaria/cadastros/consultas-cnpj
#
# 3) http://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-abertos-do-cnpj

from unicodedata import normalize
import csv
import os

def RemoverAcento(texto):
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

class Eleitos:

    def __init__(self, nome):
        extensao = ".csv"
        self.nomearq = nome + extensao
    
    # Busca eleitos no QSAPJ
    def BuscarQSAPJ(self, qsapj, nomearq):
        endereco = os.path.join(os.getcwd(), nomearq)
        with open(endereco, 'rt', encoding='ISO-8859-1') as arquivo:
            dados = csv.DictReader(arquivo, delimiter=';')
            for i in dados:
                candidato = RemoverAcento(i['Nome do candidato'])
                cargo = RemoverAcento(i['Cargo'].lower())
                try:
                    munic = RemoverAcento(i['Município']) + "/"
                except:
                    munic = ""
                uf = i['UF']
                for j in qsapj:
                    if (candidato in j) == True:
                        print(candidato, ", ", cargo, " de ", munic, uf, ", compõe o QSA de:\n", sep="")
                        for k in qsapj:
                            if (j[1] in k) == True:
                                print(k[4], k[5])
                        print("\n")


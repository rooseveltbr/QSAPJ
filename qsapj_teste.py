# coding: utf-8
#
# Teste QSAPJ
#
# Versão: 28.03.2019
#
# Licenciamento: GNU General Public License v3.0

from qsapj import QSAPJ

uf = input("Informe a sigla da UF de interesse: ")

nome = input("Informe um nome para gerar os arquivos: ")

qsapj = QSAPJ(uf, nome)

qsapj.CopiarArquivo(qsapj.uri, qsapj.nomearq)

qsapj.CopiarDados(qsapj.nomearq)

qsapj.GerarArquivo(qsapj.nomearq, qsapj.dados)

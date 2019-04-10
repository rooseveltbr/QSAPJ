# coding: utf-8
#
# Testes
#
# Versão: 09.03.2019
#
# Autor: Roosevelt Gonçalves Oliveira - https://github.com/rooseveltbr
#
# Licenciamento: GNU General Public License v3.0

from qsapj import QSAPJ
from eleitos import Eleitos

uf = input("Informe a sigla da UF de interesse: ")

nome = input("Informe um nome para gerar os arquivos: ")

qsapj = QSAPJ(uf, nome)

qsapj.CopiarArquivo(qsapj.uri, qsapj.nomearq)

qsapj.CopiarDados(qsapj.nomearq)

qsapj.GerarArquivo(qsapj.nomearq, qsapj.dados)

# Copie o arquivo dos eleitos disponível no sítio do TSE: http://www.tse.jus.br/eleicoes/estatisticas/estatisticas-eleitorais

nome_eleitos = input("Informe o nome do arquivo dos eleitos: ")

eleitos = Eleitos(nome_eleitos)

eleitos.BuscarQSAPJ(qsapj.dados, eleitos.nomearq)

# coding: utf-8
from owlready2 import *

#Import das ontologias
ontoFake = get_ontology("c:/Users/Bruno/Documents/Ontology/OntoFake.owl")
ontoFake.load()

ontoJuris = get_ontology("c:/Users/Bruno/Documents/Ontology/OntoJuris.owl")
ontoJuris.load()

#print("\n####################### Classes da ontologia para fake news #######################")
#print(list(ontoFake.classes()))

print("\n####################### Reações #######################")
with ontoFake:
     class Informacao(Thing):
          def take(self): print("Essa é uma informação que não tem tipificação.")

     class Fato (Thing):
          pass

     class Fake(Thing):
          pass

     class PossuiCaracteristica(Informacao >> Fake):
          python_name = "Tipo_fake"

#################################################################################################################

     class Ofensa(Informacao):
          equivalent_to = [Informacao & PossuiCaracteristica.exactly(1, Fake)]
          def take(self): print("Ofensa")

     class OfensaAReputacao(Informacao):
          equivalent_to = [Informacao & PossuiCaracteristica.exactly(5, Fake)]
          def take(self): print("Ofensa a reputacao")

     class DivulgacaoFalsa(Informacao):
          equivalent_to = [Informacao & PossuiCaracteristica.exactly(6, Fake)]
          def take(self): print("Divulgacao falsa")

     class FalsaAcusacao(Informacao):
          equivalent_to = [Informacao & PossuiCaracteristica.exactly(7, Fake)]
          def take(self): print("Falsa acusacao")

     class Tumulto(Informacao):
          equivalent_to = [Informacao & PossuiCaracteristica.exactly(8, Fake)]
          def take(self): print("Tumulto")


with ontoJuris:
     class Valores(Thing):
          def take(self): print("Um bem foi afetado.")

     class LeisAplicaveis(Thing):
          pass

     class Tem_acusacao (Valores >> LeisAplicaveis):
          python_name  = "Tipo_acusacao"

     class Calunia(Valores):
          equivalent_to = [Valores & Tem_acusacao.exactly(3, LeisAplicaveis)]
          def julg(self): print("Crime: Art. 138 do Código Penal \n- Lei nº 2.848 de 07 de Dezembro de 1940 \n As penas principais são: \n Detenção de 6 meses a 2 anos.")

     class ContravencoesPenais(Valores):
          equivalent_to = [Informacao & Tem_acusacao.exactly(2, LeisAplicaveis)]
          def julg(self): print("Crime: Art. 5º do Código Penal \n- lei nº 3.688, de 3 de Outubro Dde 1941. \n As penas principais são: \n I - prisão simples. \n II - multa.")

     class DivulgacoesFalsas(Valores):
          equivalent_to = [Valores & Tem_acusacao.exactly(4, LeisAplicaveis)]
          def julg(self): print("Crime: Art. 323 do Código Eleitoral \n- Lei nº 4.737 de 15 de Julho de 1965. \n As penas principais são: \n Detenção de 2 meses a 1 ano mais multa.")

     class Difamacao(Valores):
          equivalent_to = [Informacao & Tem_acusacao.exactly(5, LeisAplicaveis)]
          def julg(self): print("Crime: Art. 139 do Código Penal  \n- Lei nº 2.848 de 07 de Dezembro de 1940/ e do Art. 325 do Código Eleitoral - Lei nº 4.737 de 26 de Dezembro de 1996. \n As penas principais são: \n Detenção 3 meses a 1 ano.")

     class Injuria(Valores):
          equivalent_to = [Informacao & Tem_acusacao.exactly(6, LeisAplicaveis)]
          def julg(self): print("Crime: Art. 140 do Código Penal \n- Lei nº 2.848 de 07 de Dezembro de 1940/ e 326 do Código Eleitoral \n- Lei nº 4.737 de 15 de Julho de 1965.\n As penas principais são: \n Detenção de até 6 meses.")

#OntoFake  ################################################################################################################
#Termos para fake news: Ofensa
ofender = Fake("ofender")
insulto = Fake("insulto")
afronta = Fake("afronta")
hostilidade = Fake("hostilidade")

#Termos para fake news: Ofensa a reputação
ofenderReputacao = Fake("ofenderReputacao")
ofensaImagem = Fake("ofenderImagem")
ofensaNome = Fake("ofenderNome")
ofensaFama = Fake("ofenderFama")
ofensaPrestigio = Fake("ofenderPrestigio")

#Termos para fake news: Divulgação falsa
divulgacaoFalsa = Fake("divulgacaoFalsa")
propagandaFalsa = Fake("propagandaFalsa")
comunicacaoFalsa = Fake("comunicacaoFalsa")
exposicaoFalsa = Fake("exposicaoFalsa")
publicacaoFalsa = Fake("publicacaoFalsa")
difusaoFalsa = Fake("difusaoFalsa")

#Termos para fake news: Acusação falsa
acusacaoFalsa = Fake("acusacaoFalsa")
incriminacao = Fake("incriminacao")
imputacao = Fake("imputacao")
denunciaFalsa = Fake("denunciaFalsa")
indicacaoFalsa = Fake("indicacaoFalsa")
confisaoFalha = Fake("confisaoFalsa")
delacaoFalsa = Fake("delacaoFalsa")

#Termos para fake news: Tumulto
tumultoar = Fake("tumultoar")
confusao  = Fake("confusao")
desordem = Fake("desordem")
excitacao = Fake("excitacao")
rebeliao = Fake("rebeliao")
revolta  = Fake("revolta")
contenda  = Fake("contenda")
discordia  = Fake("discordia")


#OntoJuris  ################################################################################################################
#Termos para lei de: Calúnia
calunia = LeisAplicaveis("calunia") 
mentira = LeisAplicaveis("Mentir")
falsidade = LeisAplicaveis("Falsificar")

#Termos para lei de: Contravenções penais
contravencoes = LeisAplicaveis("contravencoes")
violacao = LeisAplicaveis("Violar")

#Termos para lei de: Divulgações falsas
falsasDivulgacoes = LeisAplicaveis("falsasDivulgacoes")
disseminar = LeisAplicaveis("DisseminacaoFalsas")
vulgarizarInformacoes = LeisAplicaveis("VulgarizarInformacoes")
exporDadosFalsos = LeisAplicaveis("FalsaExposicaodeInformacao")

#Termos para lei de: Difamação
difamar = LeisAplicaveis("difamar")
fofocar = LeisAplicaveis("FalsificarInformacoesSobreAlguem")
desonra = LeisAplicaveis("Desonrar")
falsidade = LeisAplicaveis("FalsaInformacaoOfensa")
boato = LeisAplicaveis("FalsasConversaSobre")

#Termos para lei de: Injúria
injuriar = LeisAplicaveis("injuriar")
abuso = LeisAplicaveis("AbusoOfender")
xingamento = LeisAplicaveis("Ofensas")
escandalo = LeisAplicaveis("escandalo")
agressaoVerbal = LeisAplicaveis("agressaoVerbal")
provocacao = LeisAplicaveis("provocacao")

#OntoJuris  ################################################################################################################

AllDifferent ([
          calunia,
               mentira,
               falsidade,
          contravencoes,
               violacao,
          falsasDivulgacoes,
               disseminar,
               vulgarizarInformacoes,
               exporDadosFalsos,
          difamar,
               fofocar,
               desonra,
               falsidade,
               boato,
          injuriar,
               abuso,
               xingamento,
               escandalo,
               agressaoVerbal,
               provocacao
               ])

#OntoFake  ################################################################################################################

AllDifferent ([
               ofender, 
                    insulto,
                    afronta,
                    hostilidade,
               ofenderReputacao, 
                    ofensaImagem,
                    ofensaFama,
                    ofensaNome,
                    ofensaPrestigio,
               divulgacaoFalsa, 
                    propagandaFalsa,
                    comunicacaoFalsa,
                    exposicaoFalsa,
                    publicacaoFalsa,
                    difusaoFalsa,
               acusacaoFalsa,
                    incriminacao,
                    imputacao,
                    denunciaFalsa,
                    indicacaoFalsa,
                    confisaoFalha,
                    delacaoFalsa,
               tumultoar,
                    confusao,
                    desordem,
                    excitacao,
                    rebeliao,
                    revolta,
                    contenda,
                    discordia
               ])

#Intancias para raciocinar  ################################################################################################################
acusacao1 = Informacao(Tipo_fake = [ofender, insulto, afronta, hostilidade])
julgamento1 = Valores(Tipo_acusacao  = [calunia, mentira, falsidade])

#############################################
acusacao2 = Informacao(Tipo_fake = [ofenderReputacao, ofensaImagem, ofensaFama, ofensaNome, ofensaPrestigio])
julgamento2 = Valores(Tipo_acusacao  = [contravencoes, violacao])

#############################################
acusacao3 = Informacao(Tipo_fake = [divulgacaoFalsa, propagandaFalsa, comunicacaoFalsa, exposicaoFalsa, publicacaoFalsa, difusaoFalsa])
julgamento3 = Valores(Tipo_acusacao  = [falsasDivulgacoes, disseminar, vulgarizarInformacoes, exporDadosFalsos])

#############################################
acusacao4 = Informacao(Tipo_fake = [acusacaoFalsa, incriminacao, imputacao, denunciaFalsa, indicacaoFalsa, confisaoFalha, delacaoFalsa])
julgamento4 = Valores(Tipo_acusacao  = [difamar, fofocar, desonra, falsidade, boato])

#############################################
acusacao5 = Informacao(Tipo_fake = [tumultoar, confusao, desordem, excitacao, rebeliao, revolta, contenda, discordia])
julgamento5 = Valores(Tipo_acusacao  = [injuriar, abuso, xingamento, escandalo, agressaoVerbal, provocacao])

#########

close_world(Valores)
close_world(Informacao)

#################################################################################################################

sync_reasoner_hermit()

acusacao1.take()
acusacao2.take()
acusacao3.take()
acusacao4.take()
acusacao5.take()

julgamento1.julg()
julgamento2.julg()
julgamento3.julg()
julgamento4.julg()
julgamento5.julg()


#elif acusacao2.take() == 'Ofensa a reputacao':
#elif acusacao3.take() == 'Divulgacao falsa':
#elif acusacao4.take() == 'Falsa acusacao':
#elif acusacao5.take() == 'Tumulto':
#else: print('Nenhuma condição aceita!')
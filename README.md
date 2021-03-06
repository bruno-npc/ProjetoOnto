![Build Status](https://travis-ci.org/joemccann/dillinger.svg)
# Uma Abordagem Ontológica para Inferir Implicação Penal para Fake News

Modelos ontológicos formalizados na Lógica Descritiva para indexar Fake News e para representar uma porção do conhecimento jurídico-normativo, provendo assim um serviço de inferências lógicas para implicação jurídica (penal ou eleitoral) das notícias falsas.

## _Repositorio dedicado a parte tecnica do projeto finalizado_
Dispõe das ontologias criadas, chamadas de "OntoFake" para definir fake news, e "OntoJuris" para implicações penais sobre fake news.

# Documentação
Baseado na metodologia "methontology".
- Link: [Documentação do projeto]

# OntoFake

- Ontology Metrics

![ImageMetrics](https://raw.githubusercontent.com/bruno-npc/ProjetoOnto/main/Img/OntoFake/OntoFake_Metrics.png)

- Classes

![ImageClasses](https://raw.githubusercontent.com/bruno-npc/ProjetoOnto/main/Img/OntoFake/OntoFake_Classes.png)

- Object Properties

![ImageObjectProperties](https://raw.githubusercontent.com/bruno-npc/ProjetoOnto/main/Img/OntoFake/OntoFake_Object%20Properties.png)

- Individuals

![ImageIndividuals](https://raw.githubusercontent.com/bruno-npc/ProjetoOnto/main/Img/OntoFake/OntoFake_Individuals.png)

- OWLViz

![ImageOWLViz]()

# _Descrição OntoFake_

Para a criação da estrutura básica dessa ontologia, foram realizadas pesquisas para se obter as devidas leis que se aplicam às Fake News, seus artigos na legislação e penalidades. Essa fase do projeto contou com uma entrevisa a um especialista da área legislativa, onde foram apresentados pelo entrevistado os sites “datajud” (https://www.cnj.jus.br/sistemas/datajud/), uma base nacional de dados do poder judiciário, o que complementou os próximos passos do projeto como “Testes e simulação das tipificações penais com Fake News reais”, e o portal “lexml” (https://www.lexml.gov.br/) , para facilitar a identificação e composição de informações, legislativas e jurídicas, principalmente com documentos oficiais.

Também contando com uma análise sobre a categorização de como são vistas as notícias em portais específicos para tratar notícias falsas, que caminham entre o “fato” e o “fake”, tendo os mais diversos termos entre estes, como por exemplo, “Contraditório”, “Verdadeiro, mas” e tantos outros.
Buscando obter uma melhor elaboração da ontologia desenvolvida, a pesquisa empenhou-se em obter a maior quantidade de dados possíveis nos portais específicos, que foram: 

| Portal | Link |
| ------ | ------ |
| Agência Lupa | [Agência Lupa] |
| Fato ou Fake | [Fato ou Fake] |
| Agência Pública | [Agência Pública] |
| E-Farsas | [E-Farsas] |
| Fake Check | [Fake Check] |
| Comprova | [Comprova] |
| Aos Fatos | [Aos Fatos] |
| Boatos | [Boatos] |

Onde cada portal possui métodos diferentes para categorizar suas publicações, variando entre uma pesquisa direta na fonte para validação das notícias, ou validação em bancos de dados, que possuem as informações corretas.

Cada portal teve os seguintes aspectos observados para o levantamento de dados referentes a pesquisa, inicialmente
- Nomeação.
- Data de criação do portal.
- Quantidade de publicações, quando disponíveis tais dados (referindo-se ao montante de notícias já analisadas pela página). 
- Metodologia empregada por cada portal para o tratamento dos dados.
- Forma com que categorizam cada postagem.

Sabendo o ano de criação dos portais, em conjunto com seus números de publicações, é possível ter uma relação maior entre acontecimentos sociais e históricos que criam uma maior disseminação de fake news, tendo como exemplos reais os períodos eleitorais ou a atual situação de pandemia.

Também para o desenvolvimento da OntoFake, foi preciso uma pesquisa para obter termos que indicam fake news, que foi realizada através do Google Forms, onde foi solicitado aos participantes que indicassem expressões/palavras relativas a fake news que já tiveram contato ou ouviram, tendo foco apenas na expressão "Fake News", onde foi possível obter 25 respostas distintas.

Através da pesquisa de termos, os dados puderam ser utilizados tanto na criação da ontologia que requer diversas atualizações, quanto em sua avaliação, após serem iniciados os testes, tendo um montante de palavras que podem ser endereçadas a ontologia.


- Resultados
- Exemplo



# OntoJuris

- Ontology Metrics

![ImageMetrics](https://raw.githubusercontent.com/bruno-npc/ProjetoOnto/main/Img/OntoJuris/OntoJuris_Metrics.png)

- Classes

![ImageClasses](https://raw.githubusercontent.com/bruno-npc/ProjetoOnto/main/Img/OntoJuris/OntoJuris_Classes.png)

- Object Properties

![ImageObjectProperties](https://raw.githubusercontent.com/bruno-npc/ProjetoOnto/main/Img/OntoJuris/OntoJuris_Object%20Properties.png)

- Individuals

![ImageIndividuals](https://raw.githubusercontent.com/bruno-npc/ProjetoOnto/main/Img/OntoJuris/OntoJuris_Individuals.png)

- OWLViz

![ImageOWLViz]()

# _Descrição OntoJuris_

Para a estruturação da ontologia jurídica, foram utilizadas as leis que já tiveram aplicação de alguma forma em julgamentos contendo fake news, essa estrutura foi feita pensada para integrar com a ontologia OntoFake, por ter um “objeto” em comum entre as duas, sendo esse objeto o que é afetado da vítima que sofre a fake news e sob o que será avaliado o julgamento na ontologia jurídica, sendo este objeto a classe na OntoJuris "Bem_da_Vitima" e na OntoFake, o objeto sendo dividido em três diferentes tipos "Bem Físico", "Bem Psicologico" e "Bem social", todos contam como o mesmo bem que afeta a vitima, mas pode tratar diferentemente dependendo da gravidade na situação.

- Resultados
- Exemplo

# Ferramentas

| Ferramenta | Link | Documentação |
| ------ | ------ | ------ |
| Protégé | [Protégé] | [Protégé Documentação] |
| OWL Ready 2 | [OWLReadY2] | [OWLReadY2 Documentação] |





[Protégé]: <https://protege.stanford.edu/>
[Protégé Documentação]: <http://protegeproject.github.io/protege/>
[OWLReadY2]: https://owlready2.readthedocs.io/en/latest/install.html
[OWLReadY2 Documentação]: <https://owlready2.readthedocs.io/en/v0.37/>

[Documentação do projeto]: <https://docs.google.com/document/d/10wbhdbD41sRw3ecqzUnioNWRpebr5X1IsvKHNioq050/edit?usp=sharing>

[Agência Lupa]: <https://piaui.folha.uol.com.br/lupa/>
[Fato ou Fake]: <https://g1.globo.com/fato-ou-fake/>
[Agência Pública]: <https://apublica.org/>
[E-Farsas]: <https://www.e-farsas.com/>
[Fake Check]: <https://nilcfakenews.herokuapp.com/>
[Comprova]: <https://projetocomprova.com.br/>
[Aos Fatos]: <https://www.aosfatos.org/>
[Boatos]: <https://www.boatos.org/>

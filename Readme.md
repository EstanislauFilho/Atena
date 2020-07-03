# Atena

:![alt text](https://raw.githubusercontent.com/EstanislauFilho/Atena/master/Imagens/pare1.gif):

## Resumo

Veículos autônomos são robôs que dispõem de sensores e sistemas avançados de controle que lhes permitem movimentar de forma independente e sem intervenção de um motorista humano. Esses robôs têm sido desenvolvidos
como solução para o problema dos acidentes de trânsito que causam grande número de vítimas. Neste trabalho, o objetivo é simular um mini veículo autônomo capaz de parar frente a obstáculos, seguir a pista corretamente e interpretar a sinalização de trânsito em um cenário dinâmico para se chegar a um destino determinado inicialmente.

O protótipo de baixo custo utiliza um computador Raspberry-Pi e uma câmera para executar ações como: identificação de placas de sinalização, detecção de delimitações da pista, acionamento da buzina, além de determinar o controle de movimentação e velocidade. Para detecção e reconhecimento da sinalização horizontal e vertical, são utilizados algoritmos de visão computacional. Algoritmos de controle de movimentação e velocidade foram implementados para possibilitar o movimento do robô no ambiente. 

Palavras-chave: Inteligência Artificial. Veículo autônomo. Educação.


## 1. Introdução

Um robô autônomo é um sistema que dispõe de sensores e outros sistemas de hardware e software que lhe permitem movimentar de forma independente e sem intervenção humana. Robôs autônomos têm sido desenvolvidos para solucionar problemas em diversas áreas, tais como medicina, indústria, logística, entretenimento e também no trânsito das cidades.

Os robôs que atuam no trânsito têm que ser capazes de interpretar corretamente as informações do seu ambiente, evitar situações perigosas para as pessoas e para ele mesmo, movimentar-se de acordo com as normas de trânsito e alcançar o seu destino, tarefas que são bastante desafiadoras tanto para robôs quanto para seres humanos. O Código de Trânsito Brasileiro (CTB) define regras específicas de circulação que devem ser respeitadas por todos os usuários da via. 

A partir daí, surge a necessidade de criar métodos mais interativos de aprendizagem, sendo a robótica uma grande aliada do processo.
Neste contexto, este projeto trabalha com alguns aspectos da dinâmica do trânsito utilizando um mini robô autônomo em um cenário urbano com vias, placas, pedestres, dentre outros elementos.

### 1.1 Objetivos

O objetivo do trabalho é possibilitar, com a utilização de um protótipo de veículo elétrico em um cenário educativo, a demonstração de conceitos de robótica e também o aprendizado da dinâmica do trânsito, como por exemplo:
* Controle de movimentação e velocidade;
* Detecção de delimitações da pista;
* Parada obrigatória;
* Detecção de faixa de pedestres;
* Detecção de outras placas;
* Leitura dos caracteres das placas de localização;
* Funcionamento do semáforo;
* Navegação até o destino escolhido; e
* Parada ao detectar obstáculos dinâmicos.


## 2. Desenvolvimento do projeto

O robô construído para o projeto possui um computador embarcado Raspberry Pi, uma câmera, um sensor de distância à laser, fototransistores, uma ponte H, motores, baterias, e sua estrutura foi desenvolvida com madeira MDF e uma chapa metálica. Os dados dos sensores são utilizados pelos algoritmos de visão computacional para obter informações sobre o ambiente. Algoritmos de controle de movimentação e velocidade foram implementados para possibilitar o movimento do robô no cenário.

As seções a seguir apresentam as tarefas realizadas em cada etapa do projeto e, quando necessário, a fundamentação teórica resumida dos conceitos envolvidos. 

### 2.1. Desenvolvimento do Protótipo 

Esta etapa consistiu em:
* Elaboração do Projeto do Protótipo;
* Configurações do Raspberry Pi 3 B+;
* Implementação dos Componentes e Sensores;
* Montagem do Protótipo; e
* Testes Básicos.

Iniciamos nosso projeto desenvolvendo um protótipo de carro elétrico, com capacidade de embarcar os componentes eletrônicos propostos. Em seguida, realizamos a instalação e configuração dos softwares necessários para o funcionamento do computador embarcado Raspberry Pi. Uma rede virtual privada (VNC) foi criada para que fosse possível acessar remotamente o computador embarcado no robô, permitindo a transmissão das imagens para um monitor externo. Alguns itens como parafusos, espaçadores e Jumpers foram necessários para a montagem do protótipo e o modo de fixação e adaptação de cada elemento do projeto no chassi foi pensado com intuito de facilitar a mobilidade do protótipo.

![alt text](https://raw.githubusercontent.com/EstanislauFilho/Atena/master/Imagens/Atena.png)

O protótipo pode ser considerado de baixo custo, pois seu custo total é inferior a R$ 600,00.

### 2.2. Desenvolvimento da Pista 

Esta etapa consistiu em:
* Definição do Projeto da Pista; 
* Obtenção de Material para a Pista;
* Desenvolvimento da Pista; e 
* Desenvolvimento Cenário (Construções e Personagens).

Na segunda etapa, definimos o projeto da pista, cujo o trajeto desenvolvido foi o mais apropriado dadas as limitações mecânicas do robô. As madeiras para construção da pista foram doadas pela empresa Madeireira Paranaense, apoiadora do projeto e, de posse das mesmas, iniciamos o processo de pintura e criação do trajeto através da fixação das fitas isolantes. 

![alt text](https://raw.githubusercontent.com/EstanislauFilho/Atena/master/Imagens/Pista.png)

Posteriormente, criamos o cenário por meio do reaproveitamento de materiais recicláveis como caixas de papelão e palitos. Os personagens e veículos de plástico foram obtidos em uma loja de brinquedos.

![alt text](https://raw.githubusercontent.com/EstanislauFilho/Atena/master/Imagens/Cenario_1.png)

![alt text](https://raw.githubusercontent.com/EstanislauFilho/Atena/master/Imagens/Cenario_2.png)

### 2.3. Preparação das Imagens e Objetos e Treinamento 

Esta etapa consistiu em:
* Definição das placas e objetos que foram utilizados na pista;
* Impressão e montagem das placas e semáforos;
* Coleta das fotos das placas, objetos, pedestres e imagens negativas; e
* Realização do treinamento dos classificadores.

As principais tarefas são detalhadas nas subseções a seguir.

#### 2.3.1. Detecção de Placas de Sinalização

Nesta etapa foram trabalhados os seguintes algoritmos:
* Haar Cascade
* Algoritmo OCR 
* Algoritmo HSV
* Tesseract e Pytesseract

Para realizar a detecção e identificação das placas de trânsito, utilizou-se um algoritmo de Aprendizado de Máquina chamado classificador em cascata (Haar Cascade), que identifica objetos baseado em uma base de dados contendo imagens positivas e imagens negativas. O classificador em cascata consiste de estágios, em que cada estágio é formado por classificadores mais simples (fracos) (BATISTA, 2017). Para o classificador conseguir diferenciar os objetos das imagens, é necessário realizar um treinamento com imagens positivas e negativas, que irá resultar em um modelo que descreve como são as características do objeto da categoria escolhida. As características escolhidas foram as de Haar.

A imagem a seguir mostra exemplos de placas utilizadas:
![alt text](https://raw.githubusercontent.com/EstanislauFilho/Atena/master/Imagens/Placas.png)

Especificamente para as placas de localização, aplicou-se o algoritmo de OCR para identificar quais caracteres estavam presentes nelas. Para isso, empregou-se o Tesseract que é uma OCR engine de código aberto (HOFFSTAETTER, 2019). Além do Haar Cascade e do OCR, o algoritmo de detecção de cores via HSV foi empregado com o objetivo de isolar a imagem da placa para uma melhor detecção e, além disso, gerar mais um parâmetro seguro de identificação de todas as placas.  

O Tesseract foi desenvolvido entre 1984 e 1994 nos laboratórios de pesquisa da HP como um projeto de pesquisa PhD. A motivação de sua criação era desenvolver uma OCR engine precisa e robusta, o que, na época, não existia. A partir de 2005, a HP tornou seu código aberto e, desde então, muitos colaboradores, cada vez mais, tem melhorado seu código e desempenho. 

#### 2.3.2. Detecção de pista

Através da imagem capturada pela câmera foi possível fazer a detecção da pista e suas respectivas faixas. A primeira imagem corresponde à imagem original com a visão do robô. Na segunda imagem, utilizou-se a função de desenho de linhas da biblioteca OpenCV (cv2.line) para fazer o desenho dos retângulos vermelho e verde. Cada retângulo foi criado a partir da definição de 4 pontos (x,y).

![alt text](https://raw.githubusercontent.com/EstanislauFilho/Atena/master/Imagens/deteccao_pista_1.png)

Os quatros pontos que definem o retângulo vermelho e os quatro pontos que definem o retângulo verde foram associados aos vetores denominados "pontos_pista" e "pontos_destino", respectivamente. Com esses vetores, foi possível utilizar as funções de transformação e consolidação perspectiva, que faz transformações geométricas de imagens 3D para uma nova dimensão 2D, permitindo sua exibição e manipulação, conforme a imagem abaixo.

![alt text](https://raw.githubusercontent.com/EstanislauFilho/Atena/master/Imagens/deteccao_pista_2.png)

Para fazer a detecção das faixas, utilizaram-se das duas regiões de interesse para criar duas novas imagens correspondentes às faixas da esquerda e da direita.
Com a criação das duas imagens correspondentes às regiões de interesse da faixa esquerda e direita, foi realizado a aplicação de alguns filtros para: conversão para escala de cinza, aplicação da função para distorção da imagem (cv2.GaussianBlur), binarização da imagem (cv2.inRagen), e a detecção de bordas com a função cv2.Canny.

Por fim, depois de realizado o processo de detecção das bordas, foi efetuada a detecção de contornos através da função cv2.moments, para calcular a área e o centróide da imagem. Com isso, duas linhas brancas pequenas, uma horizontal e outra vertical, foram criadas cujo ponto de interseção entre elas que corresponde ao centróide da imagem. Como esse centro de massa da imagem oscila conforme o robô se movimenta, é possível determinar quando o robô está saindo da faixa.

![alt text](https://raw.githubusercontent.com/EstanislauFilho/Atena/master/Imagens/deteccao_pista_3.png)

#### 2.3.3. Montagem do Semáforo

O semáforo foi construído a partir de projeto obtido no site Thingiverse e impresso em impressora 3D pela professora Sílvia Albuquerque do DECOM/CEFET-MG. 

![alt text](https://raw.githubusercontent.com/EstanislauFilho/Atena/master/Imagens/semaforo.png)

O semáforo possui três leds de alto brilho das cores vermelho, verde e amarelo. Os leds são controlados por um microcontrolador Arduino que alterna a sequência de acionamento deles, de forma a imitar um semáforo real. Os leds vermelho e verde permanecem acesos por 15 segundos, enquanto que o amarelo fica aceso por 5 segundos.

#### 2.3.4. Detecção de obstáculos

   Para detectar impedimentos na pista, foi implementado um algoritmo em linguagem C++ utilizando a biblioteca CImg (TSCHUMPERLÉ, 2003). Para cada quadro (frame) obtido da câmera do robô, são realizados os passos explicados a seguir.

* Inicialmente, é feito um borramento na imagem utilizando o filtro da mediana (função blur_median), que suaviza a imagem, ou seja, remove pequenos detalhes da imagem e possibilita preencher pequenas descontinuidades em linhas (GONZALEZ, 2003).

* A imagem filtrada é então convertida para escala de cinza utilizando a média ponderada dos canais R (Red - vermelho), G (Green - verde) e B (Blue - azul): 

                                 valor do pixel = 0.299*R + 0.587*G + 0.114*B

* É realizada uma binarização simples utilizando um limiar cujo valor é 140. 

* A imagem é cortada (função crop) para eliminar regiões que não são de interesse na detecção, por exemplo regiões mais distantes do robô. O resultado das quatro primeiras etapas podem ser vistas na figura abaixo (à direita).

*  Aplica-se o algoritmo Flood Fill (função draw_fill) para encontrar todos os pixels pretos que estejam ligados, partindo da parte central inferior da imagem. Esses pixels tendem a ser área livre da pista.
O Flood Fill é um algoritmo que encontra pixels conectados cuja cor é similar ao pixel de origem (semente), gerando uma área que pode ser considerada uniforme na imagem. É como se houvesse uma "inundação" em alguma parte da imagem e somente os pixels de cores similares que estivessem interligados fossem "molhados". 

* São analisados então 15 perfis (linhas) da imagem, isto é, é realizada a contagem de pixels de cada cor seguidos (pixels contíguos de mesma cor formam uma região). Os impedimentos na pista são detectados a partir dessa análise. Por exemplo, uma região vermelha entre duas brancas e com largura suficiente para a passagem do robô pode indicar pista livre. Faixa de pedestre também é detectada pela repetição do padrão da faixa (por exemplo, se houver mais de quatro repetições do padrão preto/branco, com uma largura mínima para cada região e se a medida das regiões não variar muito, há indicativo de faixa de pedestres). Após a análise de cada perfil, os perfis das metades superior (e da inferior) da imagem são combinados para gerar o resultado final. A figura a seguir mostra os perfis utilizados na imagem de exemplo.

![alt text](https://raw.githubusercontent.com/EstanislauFilho/Atena/master/Imagens/obstaculo_1.png)


#### 2.4. Implementação e Teste de Algoritmos no Robô

Os principais módulos da arquitetura de navegação podem ser vistos no esquema a seguir. A implementação dos módulos foi realizada em linguagem Python utilizando as bibliotecas OpenCV (OPENCV, 2019) e Pytesseract (HOFFSTAETTER, 2019).

![alt text](https://raw.githubusercontent.com/EstanislauFilho/Atena/master/Imagens/arquitetura.png)

O robô possui determinadas configurações de hardware que devem ser administradas pelo programa principal. O robô também possui sensores, estes são responsáveis por coletar informações referentes ao mundo externo. Esses dados coletados pelos sensores são recebidos pelo programa principal que repassa os mesmos até chegar no script de tratamento. 

O script de tratamento é responsável por tratar os dados obtidos pelos sensores, ou seja, ele indica quando há a presença de obstáculos, de sinalização, avisa quando o robô está saindo da faixa e também trata a missão definida pelo usuário, que é recepcionada pela interface.

O script gerenciador vai gerenciar a utilização dos motores de acordo com as regras pré-definidas e de acordo com o tratamento dos sensores.


## 3. Resultados

Os experimentos com cada módulo mostraram o potencial da metodologia aplicada para a simulação da dinâmica do trânsito. Como resultados do projeto, podem-se citar o robô, o cenário e as implementações realizadas que permitem a demonstração de: controle de movimentação e velocidade; detecção de delimitações da pista; parada obrigatória; detecção de faixa de pedestres; detecção de outras placas; leitura dos caracteres das placas de localização; funcionamento do semáforo; navegação até o destino escolhido; e parada ao detectar obstáculos dinâmicos. Cada módulo pode ser executado separadamente, permitindo verificar o funcionamento dos algoritmos e conceitos teóricos. 

Entretanto, devido a limitações do Raspberry Pi, ainda não foi possível testar todos os módulos integrados. Verificou-se em alguns testes que o Raspberry Pi não conseguiu processar todos esses módulos simultaneamente. Por exemplo, em testes cujo objetivo era que o robô navegasse um determinado percurso, detectasse e obedecesse as placas de pare, de pedestre, de desvio e o semáforo. Nestes testes, inicialmente o robô andava corretamente no trajeto, mas em algum momento ele não conseguia identificar e/ou processar a ação correspondente a uma placa, ou então em outro momento ele conseguia identificar e processar as placas ou semáforo, mas repentinamente saía do trajeto mesmo com os fototransistores. Concluiu-se então que quando o robô sai da pista é devido ao fato que o Raspberry não conseguiu obter e interpretar o valor do fototransistor antes robô executar a ação de virar/corrigir para dentro da faixa.

Em relação ao ambiente escolhido, que foi um cenário em miniatura construído com fundo preto e a pista delimitada por linhas brancas, construções de papel e personagens de brinquedo (como mostrado em figuras anteriores), há vantagens e desvantagens. Esse tipo de ambiente, por um lado, facilita a detecção das faixas e obstáculos devido ao alto contraste das cores escolhidas para a pista. Por outro lado, a possibilidade de alterações, como o surgimento de obstáculos imprevistos, aumenta a dificuldade dos algoritmos.


## 4. Considerações finais

O protótipo desenvolvido poderá ser usado para realizar demonstrações que facilitem o aprendizado de estudantes sobre as aplicações de sistemas inteligentes e possibilitará que educadores trabalhem com as placas de sinalização, regras de circulação para pedestres e motoristas, esquemas referenciais e a importância de respeitar as normas de trânsito de forma lúdica.

As crianças poderiam aprender o conceito de automação em si. No sentido de que a robótica surge para tornar ações mecânicas em ações facilmente realizadas por máquinas.
Para alunos do ensino médio, o projeto introduz circuitos e componentes eletrônicos necessários para sua realização. Dessa forma, entender o circuito é entender o funcionamento e a criação do robô. Além disso, os conceitos e as bibliotecas de programação também poderiam ser aprendidos através desse projeto.
Os alunos do ensino superior aprenderiam as mesmas coisas dos alunos do ensino médio, porém com um rigor teórico maior.

Como trabalhos futuros, será realizada a integração de todos os módulos, a alteração do computador embarcado ou utilização de uma outra máquina com maior poder de processamento com um modelo cliente-servidor. Além disso, novas funcionalidades poderão ser implementadas, tais como a detecção de outras placas de sinalização.


## Referências

BATISTA, N. Projeto - Etapa 3: Treinamento. Belo Horizonte: CEFET-MG, 2017. Disponível em: <https://sites.google.com/site/nataliacefetmg>. Acesso em 17 out. 2019.

GONZALEZ, R. e Woods, R. Processamento de Imagens Digitais. Editora Edgard Blücher, primeira edição, 2003.

HOFFSTAETTER, S. et al. Pytesseract. Versão 0.3.0. [S.l.]: Python Software Foundation, 2019. Disponível em: <https://pypi.org/project/pytesseract>. Acesso em: 17 out. 2019.

OPENCV. Versão 3.4.4. [S.l.]: 2019. Disponível em: <https://opencv.org>. Acesso em: 17 out. 2019.

TSCHUMPERLÉ, D. The CImg Library. INRIA Sophia-Antipolis: Odyssée group, 2003. Disponível em: <http://cimg.eu/>. Acesso em: 17 out. 2019.


## Desenvolvido com

* [Python Software Foundation](https://maven.apache.org/) - Linguagem de programação;
* [OpenCV](https://opencv.org/) - Biblioteca de Visão Computacional desenvolvido pela Intel em 1999;
* [PyCharm](https://www.jetbrains.com/pycharm/) - IDE de desenvolvimento.

## Contribuição

Leia Contribuindo.md para obter detalhes sobre o processo de envio de solicitações pull ao desenvolvedor.

## Versão

Para as versões disponíveis, consulte as tags neste repositório.

## Autores

* **Audryo Aparecido da Terra Caldeira Júnior** - *Estudante de Engenharia de Mecânica no* [CEFET-MG](http://www.cefetmg.br/)
* **Estanislau de Sena Filho** - *Estudante de Engenharia de Computação no* [CEFET-MG](http://www.cefetmg.br/)
* **Italo Gustavo Donato Cordeiro** - *Estudante de Engenharia de Computação no* [CEFET-MG](http://www.cefetmg.br/)
* **João Paulo Gonçalves de Souza** - *Estudante de Engenharia de Computação no* [CEFET-MG](http://www.cefetmg.br/)
* **Marina Bernardes Diniz** - *Estudante de Engenharia de Computação no* [CEFET-MG](http://www.cefetmg.br/)


## Orientadora

* **Natália Cosse Batista** - *Professora D.Sc. do Departamento de Computação do* [CEFET-MG](http://www.cefetmg.br/)
 
## Licença

Este não é um projeto licenciado. Seu objetivo é exclusivo para estudar e aprender sobre visão computacional.

## Agradecimentos

* Professora Sílvia Albuquerque
* Madeireira Paranaense  
* PrintBH Produções 
* Itamar Gonçalves


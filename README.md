# FaceOnCrawling
WebCrawling que verifica atividade ou inatividade(ativada, desativada) em conta do facebook, atravez de requicições.

#### Info
Desenvolvido por um cara, que gostava de uma garota, mas essa garota quase nunca ficava online, e ele estava com saudades, e fez esse script, que verifica se ela re-ativou o facebook, notificando-o para que possam ter alguns minutos de felicidade conversando.. T^T </3

#### reqs
FOC(FaceOnCrawling), é basicamente uma versão v2.0 do bot VFO, porem mais eficaz, leve e instavel, no bot, eu utilizava o Selenium como drive o firefox, sem falar do vitual diplay, isso comia muita memoria ram, então, eu fui dar uma estudada, sobre crawling e requisições, e resolvi fazer um v2 mais minimalista e de melhor performance.


#### instalar requisitos(LINUX):
> sudo pip3 install -r requeriments.txt

(colorama, urllib3, argparse)

#### Uso (TERMINAL LINUX)
Você pode usar o Script, tanto com parametros pelo terminal, quanto sem (recomendo com parametros).
> ./FaceOnCrawling.py -u https://www.facebook.com/link_do_perfil

ou

> ./FaceOnCrawling --url https://www.facebook.com/link_do_perfil 

para um help basico, digite:

> ./FaceOnCrawling -h

ou

> ./FaceOnCrawling --help

### @
Ou você pode colar o link a ser verificado no arquivo link.txt (recomendo com parametros), enfim, façam bom uso, Abração do tio sz.

## OBS: sempre utilize o url facebook desktop > (https://www.) e não o mobile > (http://m.) pois o unico que retorna o codigo é a versão desktop.


> ~ by Rob ~

~ FaceOnCrawling by Rob ~

FaceOnCrawling é um Web crawling (Script que pega informações na internet), uma versão mais instavel do
Bot_VFO (Bot que upei que faz quase o mesmo, mas usando o Selenium, que é bem mais pesado), que funciona de forma
mais leve, rapida e com uma melhor aparencia (pelo menos eu acho), enfim, para usa-lo você pode usar tanto
por parametros(via terminal que eu recomendo mais):

$./WebOnCrawking -u www.facebook.com/link_id_do_seu_perfil
$./WebOnCrawking --url www.facebook.com/link_id_do_seu_perfil

Ou colando o link do perfil a ser verificado no arquivo "link.txt" (que eu não recomendo pois deu alguns bugs
acima da minha capacidade de conhecimento, por enquanto!), bom, basicamente o script faz a requisição web para
certa pagina no facebook, e verifica se o codigo foi 404 (que dá quando a pagina não existe mais, ou nunca existiu)
e retorna, por padrão eu coloquei para, se der erro, o programa vai reverificar a cada 5 minutos, porem isso é totalmente
opcional, caso não queira esperar basta cancelar, fechar, ou se entende de programação, comente a parte do codigo com
a função secundaria (tá todo comentado o codigo) e retira o atalho na função base, espero ter ajudado quem ou estava
procurando demo de webcrawling com python, ou até mesmo alguem que estava procurando um script que verifica a atividade
e inatividade de um perfil.
Abraço do tio Rob <3

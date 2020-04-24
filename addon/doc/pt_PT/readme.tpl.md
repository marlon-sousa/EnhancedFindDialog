# EnhancedFindDialog for NVDA ${addon_version}

Complemento para implementar alguns melhoramentos no diálogo de localização do NVDA:

* histórico de pesquisa

## Descarregar
Descarregue aqui o [extra Enhanced Find Dialog ${addon_version}](https://github.com/marlon-sousa/EnhancedFindDialog/releases/download/${addon_version}/EnhancedFindDialog-${addon_version}.nvda-addon)

## Recursos

### Histórico de pesquisa
Em muitas páginas da internet e de outros aplicativos, a maneira mais rápida de aceder a determinados locais específicos é usando o comando "search", geralmente vinculado às teclas "ctrl+nvda+f".

O diálogo de pesquisa permite-nos escrever um texto e, pressionando "enter", sermos colocados na próxima ocorrência desse texto, se ele existir.

Em muitos casos, visitará os mesmos locais de uma página ou, até, as mesmas páginas,durante a mesma sessão do NVDA. Por isso, precisará procurar os mesmos termos, especialmente se essa for a única maneira de aceder rapidamente a um link ou secção desse site.

Este é, em especial, o caso de pessoas que trabalham, no seu quotidiano, com sistemas baseados na Web.

No entanto, o NVDA não mantém um histórico dos termos anteriormente pesquisados, o que diminui a sua produtividade, porque, a menos que esteja pesquisando exactamente o mesmo termo da sua última pesquisa, precisará escrevê-lo novamente.

Este extra mantém um histórico de pesquisas, que permanece enquanto o NVDA estiver em execução. Portanto, quando pressionar as teclas para fazer a pesquisa, se já tiver pesquisado por um dado termo ou expressão, basta pressionar a seta para baixo e escolher os termos anteriormente pesquisados, para realizar uma nova pesquisa e voltar ao local desejado.

É claro que pode escrever sempre novos termos. Nesse caso, eles também serão adicionados à lista, na próxima vez que activar a caixa de diálogo de pesquisa.

#### Como funciona?

Basta instalar o extra. Quando este for activado, através das teclas "ctrl+nvda+f", como habitualmente faz para o diálogo de pesquisa do NVDA, pressionar as setas para cima e para baixo, no campo de edição, permitir-lhe-á navegar pela lista de termos e expressões anteriormente pesquisados.

Pode, a qualquer momento e desde que disso necessite, escrever um novo termo, como de costume.

## Contribuir

## Criar  o extra

Para  isso, vai precisar de:

* python 3.6 ou superior
* O pip deve estar configurado
* scons (pip install scons)
* markdown (pip install markdown)
* comando msgfmt. A maneira mais simples de obtê-lo é instalar o git e, na instalação, escolher a opção para tornar as ferramentas do bash disponíveis para o prompt de comandos

Uma vez que estes ítems estejam instalados, basta escrever scons na pasta raíz do projecto para criar o extra  

## Contribuir para as traduções

### Traduzir o extra

Assumindo que já tenha o ambiente configurado para construir o extra (veja item acima), para criar um ficheiro ".pot", onde ficarão todas as mensagens para a  tradução, basta escrever scons pot, na pasta raíz do projecto.

A partir deste ficheiro base, é possível construir os ficheiros ".po" de tradução para o seu idioma.

Os idiomas  já traduzidos podem ser encontrados na pasta addon/docs/locale.

### Traduzir a documentação

As documentações de tradução devem ser geradas a partir de ficheiros ".tpl.md" (não de ficheiros ".md").

Por isso, excepto no ficheiro "readme.md", na raíz do projecto, não encontrará outros ficheiros ".md" versionados.

Os ficheiros ".tpl.md" são ficheiros markdown normais, excepto por um recurso a mais: se  usar ${[var]} em qualquer lugar do texto, [var] será substituído por uma variável com o mesmo nome ddefinida em buildVars.py.
Caso não haja uma variável com o mesmo nome, a substituição não acontece.

Isto é útil, por exemplo, para fazer com que a documentação reflicta limks ou número de versão do extra automaticamente, sem que precise ser reescrita.

Para traduzir a documentação, traduza o ficheiro "readme.tpl.md", na raíz do projecto. O ficheiro traduzido deve ser colocado na pasta addon/locale/[lang] e deve chamar-se "readme.tpl.md".

As variáveis ${[var]} não devem ser alteradas. Escreva scons na raíz do projecto para que a documentação HTML e markdown seja criada.
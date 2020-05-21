# EnhancedFindDialog for NVDA ${addon_version}

Extra  para implementar alguns melhoramentos no diálogo de pesquisa do NVDA:

* histórico de pesquisa
* Continuidade de pesquisa, configurado por perfil
* distinção entre maiúsculas e minúsculas, configurado por perfil
* Informações contextuais nas pesquisas

## Descarregar
Descarregar the [Enhanced Find Dialog ${addon_version} addon](https://github.com/marlon-sousa/EnhancedFindDialog/releases/download/${addon_version}/EnhancedFindDialog-${addon_version}.nvda-addon)

## Recursos

### Histórico de pesquisa

Em muitas páginas da internet e de outros aplicativos, a maneira mais rápida de aceder a determinados locais específicos é usando o comando "search", geralmente vinculado às teclas "ctrl+nvda+f".

O diálogo de pesquisa permite-nos escrever um texto e, pressionando "enter", sermos colocados na próxima ocorrência desse texto, se ele existir.

Em muitos casos, visitará, várias vezes, os mesmos locais de uma página ou, até, as mesmas páginas,durante a mesma sessão do NVDA. Por isso, precisará procurar os mesmos termos, especialmente se essa for a única maneira de aceder rapidamente a um link ou secção desse site.

Este é, em especial, o caso de pessoas que trabalham, no seu quotidiano, com sistemas baseados na Web.

No entanto, o NVDA não mantém um histórico dos termos anteriormente pesquisados, o que diminui a sua produtividade, porque, a menos que esteja a pesquisar exactamente o mesmo termo da sua última pesquisa, precisará escrevê-lo novamente.

Este extra mantém um histórico de pesquisas, que permanece enquanto o NVDA estiver em execução. Portanto, quando pressionar as teclas para fazer a pesquisa, se já tiver pesquisado por um dado termo ou expressão, basta pressionar a seta para baixo e escolher os termos anteriormente pesquisados, para realizar uma nova pesquisa e voltar ao local desejado.

É claro que pode escrever sempre novos termos. Nesse caso, eles também serão adicionados à lista, na próxima vez que activar a caixa de diálogo de pesquisa.

#### Como funciona?

Basta instalar o extra. Quando este for activado, através das teclas "ctrl+nvda+f", como habitualmente faz para o diálogo de pesquisa do NVDA, pressionar as setas para cima e para baixo, no campo de edição, permitir-lhe-á navegar pela lista de termos e expressões anteriormente pesquisados.

Pode, a qualquer momento e desde que disso necessite, escrever um novo termo, como de costume.

### Continuidade das pesquisas

A continuidade da pesquisa é um recurso que, se configurado, não considera a posição actual em que está, num texto, quando realiza pesquisas.

Isto significa que, se procurar algo que não está presente abaixo da sua posição actual, a pesquisa será realizada desde o início do texto para verificar se esse termo existe em algum lugar do documento.

Isto é especialmente importante para indivíduos que trabalham com sistemas baseados na Web e precisam encontrar um determinado botão ou parte do texto, independentemente de onde se encontrem na página.

Esta opção é específica para um perfil, o que significa que pode ter um perfil onde ela esteja activa e outro onde não esteja.

#### Como funciona?

Basta instalar o extra. Quando activada, a caixa de diálogo Localizar oferecerá uma caixa de selecção chamada continuidade de pesquisa.

Se estiver marcada:

1. Se procurar um termo e ele for encontrado abaixo da posição actual, o cursor será colocado nesse texto.
2. Se este termo não for encontrado abaixo da posição actual, será pesquisado na parte superior do texto.
3. Se o termo for encontrado, um bipe curto será produzido para o informar que o texto encontrado está acima da sua posição actual e o cursor é colocado nessa posição.
4. Se esse termo não for encontrado, a mensagem de texto não encontrado será mostrada.

Alterar essa caixa de selecção e realizar uma pesquisa guardará o novo estado (marcado ou desmarcado) para o perfil activo. Cancelar a pesquisa não mudará o seu estado no perfil activo, mesmo se a tiver alterado antes de cancelar a pesquisa.

### distinção entre maiúsculas e minúsculas

O NVDA já oferece a caixa de selecção de distinção entre maiúsculas e minúsculas para permitir pesquisas considerando este caso. Este extra estende essa funcionalidade guardando o estado dessa caixa de selecção no perfil activo, para que possa ter perfis configurados de maneira diferente.

#### Como funciona?

Basta instalar o extra. Alterar a caixa de selecção de distinção entre maiúsculas e minúsculas e executar uma pesquisa salvará o novo estado (marcado ou desmarcado) para o perfil activo. Cancelar a pesquisa não mudará o seu estado no perfil activo, mesmo se a tiver alterado antes de cancelar a pesquisa.

### informações contextuais nas pesquisas

Actualmente, sem este extra, o modo como o NVDA se comporta, quando um termo de pesquisa é encontrado, é o seguinte: O cursor é colocado na posição do termo pesquisado e apenas esse termo é pronunciado.

Isto torna-se algo problemático quando precisa pesquisar várias vezes por algum termo (usando o NVDA + f3) porque a primeira coisa que ouve é o próprio termo pesquisado, o que é redundante, pois acaba de fazer uma pesquisa por ele!

Este extra coloca o cursor na posição do termo, mas, em vez de ler o próprio termo, lê a linha completa, fornecendo o contexto em que esse termo foi encontrado.

Por exemplo, suponha que esteja a pesquisar "Marlon", porque sabe que existe um botão, em qualquer lugar da página,  chamado "Marcar Marlon". Não deseja procurar o termo "marcar", porque existem outros botões chamados "marcar x e marcar z" e deseja encontrar somente o botão "Marcar Marlon".

Aqui está o texto:

Excluir comentários de Marlon

responder directamente a Marlon

Indicar Marlon como spammer

Marcar Marlon em uma resposta

Se pesquisasse "Marlon", antes deste bloco", ouviria
"Marlon"

Se mantivesse pressionado NVDA + f3, ouviria
"Marlon"

Marlon como spammer

Marlon em uma resposta

Isto reduziria a sua produtividade, porque, primeiro, ouviria apenas marlon, sem saber nada sobre essa ocorrência.

Na próxima vez, ouviria Marlon e teria que esperar que o spammer fosse falado, porque também não saberia o que há sobre Marlon neste texto.

Da mesma forma, da próxima vez, precisaria esperar que o resto da frase fosse pronunciada, porque também não teria a certeza sobre o que era isso acerca de  Marlon.

Além disso, se pressionasse o NVDA + f3 rapidamente, ouviria Marlon, Marlon, Marlon, Marlon ... o que não é produtivo porque sabe que está a procurar por Marlon.

#### Como funciona

Basta instalar o complemento.

Após a instalação, a linha corrente do dtermo de pesquisa é lida e o cursor é colocado sobre ele.

No exemplo acima, na primeira vez que realizou a pesquisa, ouviria
"Excluir comentários de Marlon"

Se mantivesse pressionado NVDA + f3, ouviria
"responder directamente a Marlon"
"Indicar Marlon como spammer"
"Marcar Marlon em uma resposta"

Além disso, se pressionasse o NVDA + f3 rapidamente, ouviria o início de cada linha, permitindo-lhe pressionar rapidamente enter na linha iniciada com Marcar,  porque sabe que o termo "Marlon" está presente numa última posição nessa mesma linha.

# ajudando a traduzir ou desenvolver o extra

Se quiser ajudar a traduzir ou desenvolver o extra, aceda o [repositório do projeto](https://github.com/marlon-sousa/EnhancedFindDialog) e busque pelo arquivo contrib.md no diretório de documentação equivalente ao seu idioma.

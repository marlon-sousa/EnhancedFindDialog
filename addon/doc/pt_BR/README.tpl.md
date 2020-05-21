# EnhancedFindDialog para NVDA ${addon_version}
Complemento que melhora o diálogo de busca:

* histórico de busca
* pesquisa circular, configurada por perfil
* distinção entre maiúsculas e minúsculas, configurada por perfil
* informações contextuais na busca

## Download
Baixe o [Complemento para o Diálogo de Busca Estendido ${addon_version}](https://github.com/marlon-sousa/EnhancedFindDialog/releases/download/${addon_version}/EnhancedFindDialog-${addon_version}.nvda-addon)

## Recursos

### Histórico de busca

Em muitos sites e aplicativos, a maneira mais rápida de acessar locais específicos é usando o
comando de busca, geralmente vinculado às teclas ctrl + nvda + f.

O diálogo de busca nos permite digitar um texto e sermos colocados na próxima ocorrência desse texto, se ele existir.

Frequentemente, você estará visitando os mesmos sites várias vezes durante a mesma sessão do NVDA. Em muitos desses sites, você precisará pesquisar
pelos mesmos termos, especialmente se essa for a única maneira de acessar rapidamente um link ou seção desse site.

Esse é especialmente o caso de pessoas que programam diariamente com sistemas baseados na Web como parte de seu trabalho.

No entanto, o NVDA não mantém os termos que você pesquisou
anteriormente em uma lista. Isso diminui sua produtividade, porque, a menos que você esteja procurando exatamente
o mesmo termo da sua última pesquisa, será preciso digitá-lo novamente.

Esse complemento mantém um histórico de pesquisa que vale enquanto o NVDA estiver em execução. Assim, quando ele estiver ativo, basta pressionar as setas para baixo
e para cima para ver o histórico dos termos anteriormente pesquisados e
pressionar enter no termo desejado para efetuar uma nova pesquisa.

Você pode, naturalmente, digitar novos termos no diálogo de pesquisa. Eles também serão adicionados à lista na próxima vez que você ativar a caixa de diálogo.

#### Como funciona?

Basta instalar o complemento. Quando ele for ativado, pressionar as setas para cima e para baixo no campo de edição
da caixa de diálogo de pesquisa permitirá
navegar pela lista de termos pesquisados anteriormente.

Você pode a qualquer momento digitar um novo termo, como de costume.

### Pesquisa circular

A pesquisa circular é um recurso que, se configurado, não considera a posição atual em que você está em um texto ao
realizar a busca.

Isso significa que, se você procurar algo que não está presente abaixo da sua posição atual, a pesquisa será realizada desde o
início para verificar se esse termo existe em algum lugar do texto inteiro.

Isso é muito útil para pessoas que trabalham com sistemas baseados na Web e precisam encontrar um determinado botão ou parte do texto, independentemente de onde estejam na página.

Essa opção é específica para cada perfil, o que significa que você pode ter um perfil onde
ela está ativa e outro onde não está.

#### Como funciona?

Basta instalar o complemento. Quando ativada, a caixa de diálogo Procurar oferecerá uma caixa de seleção chamada
pesquisa circular.

Se estiver marcada:

1. Se você procurar um termo e ele for encontrado abaixo da posição atual, você será colocado nele.
2. Se este termo não for encontrado abaixo da posição atual, ele será
pesquisado no início do texto.
3. Se o termo for encontrado, um bipe curto será produzido para que você saiba que o texto está acima da sua posição
atual e o cursor se moverá para essa posição.
4. Se esse termo não for encontrado, a mensagem de texto não encontrado será exibida.

Alterar essa caixa de seleção e realizar uma nova pesquisa salvará o novo estado
da caixa (marcado ou desmarcado) para o perfil atual. Cancelar a pesquisa não mudará seu estado no perfil
atual, mesmo se a caixa tiver sido alterada antes de cancelar a pesquisa.

### distinção entre maiúsculas e minúsculas

O NVDA já oferece a caixa de seleção de distinção entre maiúsculas e minúsculas. Esse complemento estende essa funcionalidade salvando o estado dessa caixa de seleção no perfil
atual, para que você possa ter perfis com essa opção configurados de maneiras
diferentes.

#### Como funciona?

Basta instalar o complemento. Alterar a caixa de seleção de distinção entre maiúsculas e minúsculas e executar uma pesquisa salvará o novo estado (marcado ou desmarcado)
da caixa para o perfil atual. Cancelar a pesquisa não mudará seu estado no
perfil atual, mesmo se você a tiver alterado antes de cancelar a pesquisa.

### informações contextuais na busca

A maneira como o NVDA se comporta quando um termo de pesquisa é encontrado é a seguinte: você é colocado na posição do termo pesquisado e a linha é lida a partir dele.

Isso sempre foi problemático quando você precisa pesquisar várias vezes (usando o NVDA + f3) por alguma coisa, porque a primeira coisa
que é lida é o próprio termo pesquisado, quando você o conhece, porque acabou de pesquisá-lo.

Esse complemento coloca o cursor na posição do termo, mas ao invés de ler
do termo em diante ele lê a linha completa, fornecendo o contexto completo de
onde ele foi encontrado.

Por exemplo, suponha que você esteja pesquisando "Marlon" porque sabe que existe um botão chamado
mencionar Marlon em algum lugar da página. Você não quer procurar por
mencionar, porque existem outros botões chamados "mencionar x y z" e deseja encontrar o botão Marlon de destino.

Aqui está o texto:

Excluir comentários de Marlon

responder diretamente a Marlon

Relatar Marlon como spammer

Mencionar Marlon em uma resposta

Se você pesquisasse Marlon antes desse bloco, ouviria
Marlon

Se você mantivesse pressionado NVDA + f3, ouviria

Marlon

Marlon como spammer

Marlon em uma resposta

Isso reduziria sua produtividade, porque primeiro você ouviria apenas marlon, sem saber nada sobre essa ocorrência.

Na próxima vez, você ouviria Marlon e teria que esperar que "como spammer" fosse falado, porque também não saberia o que há sobre Marlon neste texto.

Da mesma forma, da próxima vez você precisaria esperar "numa resposta" ser
lida, porque também não teria certeza sobre o que Marlon está se referindo
nessa linha.

Além disso, se você pressionasse NVDA + f3 rapidamente, ouviria Marlon, Marlon, Marlon, Marlon ... o que não é produtivo porque você sabe que está procurando por Marlon.

#### Como funciona

Basta instalar o complemento.

Após a instalação, a linha completa onde o termo de pesquisa for encontrado é lida e você é colocado nesse termo.

No exemplo acima, na primeira vez que você realizou a pesquisa, você ouviria

Excluir comentários de Marlon

Se você mantivesse pressionado NVDA + f3, ouviria

Responder diretamente a Marlon

Relatar Marlon como spammer

Mencionar Marlon em uma resposta

Além disso, se você pressionasse NVDA + f3 rapidamente, ouviria o início de cada linha, permitindo pressionar rapidamente enter na linha iniciada com mensionar, porque você sabe que
"Marlon" está presente mais à frente nessa linha.

# ajudando a traduzir ou desenvolver o complemento

Se quiser ajudar a traduzir ou desenvolver o complemento, acesse o [repositório do projeto](https://github.com/marlon-sousa/EnhancedFindDialog) e busque pelo arquivo contrib.md no diretório de documentação equivalente ao seu idioma.

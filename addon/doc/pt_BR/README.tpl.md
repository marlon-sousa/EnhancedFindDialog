# EnhancedFindDialog para NVDA ${addon_version}
Complemento que melhora o diálogo de busca:

* histórico de busca

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

## Contribuindo

### Gerando o complemento

Você vai precisar de:

* python 3.6 ou superior
* O pip deve estar configurado
* scons (pip install scons)
* markdown (pip install markdown)
* comando msgfmt. A maneira mais simples de obtê-lo é instalar o git e, na instalação, escolher a opção para tornar as ferramentas do bash disponíveis para o prompt de comandos

Uma vez que estes ítems estejam instalados, basta escrever scons na pasta raiz do projeto para gerar o complemento  

### Contribuindo traduções

#### Traduzindo o complemento

Assumindo-se que você já tenha o ambiente configurado para construir o complemento (veja item acima), para gerar um arquivo pot de tradução basta escrever scons pot na pasta raiz do projeto.

A partir daí, é possível contribuir os arquivos po de tradução para seu idioma.

Os idiomas atualmente já traduzidos podem ser encontrados na pasta addon/docs/locale.

#### Traduzindo documentação

As documentações de tradução devem ser geradas a partir de arquivos .tpl.md (não de arquivos .md).

Por isso, exceto pelo arquivo readme.md na raiz do projeto, você não encontrará outros arquivos .md versionados.

Os arquivos .tpl.md são arquivos markdown normais, exceto por um recurso a mais: se você usar ${[var]} em qualquer lugar do texto, [var] será substituído por uma variável com o mesmo nome ddefinida em buildVars.py.
Caso não haja uma variável com o mesmo nome, a substituição não acontece.

Isso é útil, por exemplo, para fazer com que a documentação reflita limks ou número de versão do complemento automaticamente, sem que precise ser reescrita.

Para traduzir a documentação, traduza o arquivo readme.tpl.md na raiz do projeto. O arquivo traduzido deve ser colocado na pasta addon/locale/[lang] e deve se chamar readme.tpl.md.

As variáveis ${[var]} não devem ser alteradas. Escreva scons na raiz do projeto para que a documentação HTML e markdown seja gerada.
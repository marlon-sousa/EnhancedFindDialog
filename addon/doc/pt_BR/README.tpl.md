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
o mesmo termo da sua última pesquisa, você deve digitá-lo novamente.

Esse complemento mantém um histórico de pesquisa que vale enquanto o NVDA estiver em execução. Assim, quando você o ativar, basta pressionar as setas para baixo
e para cima para ver o histórico dos termos anteriormente pesquisados e
pressionar enter no que você queira para efetuar uma nova pesquisa.

Você pode, naturalmente, digitar novos termos no diálogo de pesquisa. Eles também serão adicionados à lista na próxima vez que você ativar a caixa de diálogo.

#### Como funciona?

Basta instalar o complemento. Quando ele for ativado, pressionar as setas para cima e para baixo no campo de edição
da caixa de diálogo de pesquisa permitirá
navegar pela lista de termos pesquisados.

Você pode a qualquer momento digitar um novo termo, como de costume.

## Contribuindo

### construindo o complemento

Você precisa:

* Python 3.6 ou superior.
* pip deve estar configurado
* scons (pip install scons)
* markdown (pip install markdown)
* utilitário msgfmt. A forma mais fácil de obtê-lo é instalando o git bash
e escolher incluir bash tools at command prompt

Quando você tiver tudo instalado, digitando scons na raiz do projeto
deverá construir o complemento e gerar a documentação.

### traduções

#### traduzindo o complemento

Assumindo que você já tenha tudo configurado para construir o
complemento (ver tópico anterior) digitando scons pot deverá gerar um
arquivo pot na raiz do projeto. É então possível gerar e traduzir o
arquivo .po para seu idioma.
Os idiomas já traduzidos podem ser encontrados no diretório /addon/locale

#### traduzindo a documentação

As traduções da documentação são geradas a partir de arquivos .tpl.md (não
dos .md). É por isso que, exceto no arquivo readme.md na raiz do projeto, você não
encontrará outros arquivos .md.

Os arquivos .tpl.md são arquivos markdown normais com uma adição: se você usar $ {[var]} dentro
do texto, [var] será substituída por uma variável com o mesmo
nome definido em buildvars.py quando os arquivos md e .html correspondentes
forem gerados.

Se nenhuma variável com o nome existir, a substituição não ocorrerá.

Isso é útil, por exemplo, para gerar links e títulos com a versão atual do complemento sem precisar reescrever a documentação.

Para traduzir a documentação, crie um diretório para seu idioma na
pasta doc (se já não existir) e traduza o arquivo readme.tpl.md na raiz do projeto
ou atualize o já existente.

As variáveis ${[xxx]} não devem ser modificadas. Para gerar a
documentação, digite scons e o markdown com as variáveis substituídas e
o HTML serão gerados.

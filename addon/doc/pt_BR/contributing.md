# Contribuindo

## Gerando o complemento

Você vai precisar de:

* python 3.13.
* O pip deve estar configurado
* scons (pip install scons)
* markdown (pip install markdown)
* gettext, que fornece os utilitários `msgfmt` e `xgettext`. O `msgfmt` compila os arquivos de tradução a cada compilação, e o `xgettext` é usado pelo `scons pot` para gerar o modelo de tradução. No Windows, instale uma versão moderna a partir do [gettext-iconv-windows](https://github.com/mlocati/gettext-iconv-windows/releases) (ou use `scoop install gettext` / `choco install gettext`), e certifique-se de que o diretório `bin` dele venha antes de qualquer outro gettext no seu PATH. Não use o pacote gettext do GnuWin32: ele está congelado na versão 0.14.4 (2005) e é antigo demais para esta compilação (o `scons pot` falha na opção não suportada `--package-name`).

Uma vez que estes ítems estejam instalados, basta escrever scons na pasta raiz do projeto para gerar o complemento  

## Contribuindo traduções

### Traduzindo o complemento

Assumindo-se que você já tenha o ambiente configurado para construir o complemento (veja item acima), para gerar um arquivo pot de tradução basta escrever scons pot na pasta raiz do projeto.

A partir daí, é possível contribuir com os arquivos po de tradução para seu idioma.

Os idiomas atualmente já traduzidos podem ser encontrados na pasta addon/locale.

### Traduzindo documentação

As documentações de tradução devem ser geradas a partir de arquivos .tpl.md (não de arquivos .md).

Por isso, exceto pelo arquivo readme.md na raiz do projeto, você não encontrará outros arquivos .md versionados.

Os arquivos .tpl.md são arquivos markdown normais, exceto por um recurso a mais: se você usar ${[var]} em qualquer lugar do texto, [var] será substituído por uma variável com o mesmo nome ddefinida em buildVars.py.
Caso não haja uma variável com o mesmo nome, a substituição não acontece.

Isso é útil, por exemplo, para fazer com que a documentação reflita limks ou número de versão do complemento automaticamente, sem que precise ser reescrita.

Para traduzir a documentação, traduza o arquivo readme.tpl.md na raiz do projeto. O arquivo traduzido deve ser colocado na pasta addon/doc/[lang] e deve se chamar readme.tpl.md.

As variáveis ${[var]} não devem ser alteradas. Escreva scons na raiz do projeto para que a documentação HTML e markdown seja gerada.
# Contribuir

## Criar  o extra

Para  isso, vai precisar de:

* python 3.13.
* O pip deve estar configurado
* scons (pip install scons)
* markdown (pip install markdown)
* gettext, que fornece os utilitários `msgfmt` e `xgettext`. O `msgfmt` compila os ficheiros de tradução em cada compilação, e o `xgettext` é usado pelo `scons pot` para gerar o modelo de tradução. No Windows, instale uma versão moderna a partir do [gettext-iconv-windows](https://github.com/mlocati/gettext-iconv-windows/releases) (ou use `scoop install gettext` / `choco install gettext`), e certifique-se de que a pasta `bin` dele vem antes de qualquer outro gettext no seu PATH. Não use o pacote gettext do GnuWin32: está congelado na versão 0.14.4 (2005) e é demasiado antigo para esta compilação (o `scons pot` falha na opção não suportada `--package-name`).

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
# EnhancedFindDialog para NVDA ${addon_version}
Complemento para implementar algunas mejoras en el diálogo de búsqueda de NVDA:

* histórico de búsqueda
* continuidad de búsqueda, configurado por perfil
* sensible a las mayúsculas, configurado por perfil
* información contextual sobre las búsquedas

## Descargar
Descargar el complemento [Enhanced Find Dialog ${addon_version}](https://github.com/marlon-sousa/EnhancedFindDialog/releases/download/${addon_version}/EnhancedFindDialog-${addon_version}.nvda-addon)

## Características

### Histórico de búsqueda
En muchas páginas de Internet y otras aplicaciones, la forma más rápida de acceder a ciertos lugares específicos es usando la órden "Buscar", en general vinculado a las teclas "ctrl+nvda+f".

El diálogo de búsqueda nos permite escribir un texto y pulsando "Intro", se coloca en la siguiente ocurrencia de este texto si existe.

En muchos casos, visitarás, varias veces, los mismos lugares de una página incluso las mismas páginas durante la misma sesión de  NVDA. Por lo tanto, debe buscar los mismos términos, especialmente si esta es la única manera de acceder rápidamente a un enlace o sección de este sitio.

Esto es, en particular, el caso de las personas que trabajan, en su vida diaria, con sistemas basados ​​en la web.

Sin embargo, NVDA no mantiene un  histórico de los términos anteriormente buscados, lo que disminuye tu productividad porque, a menos que estés buscando exactamente el mismo término de tu última  búsqueda, deberás escribirlo nuevamente.

Este complemento mantiene un histórico de búsquedas, que permanece mientras se está ejecutando  NVDA. Por lo tanto, cuando se  pulsa las teclas para realizar la búsqueda, si ya has buscado un término o una expresión determinada, basta pulsar la flecha abajo o arriba y elige los términos anteriormente buscados, para realizar una nueva búsqueda y volver al lugar  deseado.

Por supuesto, siempre puedes escribir nuevos términos. En este caso, también se agregarán a la lista, la próxima vez que habilite el cuadro de diálogo de búsqueda.

#### ¿Como funciona?

Basta instalar el complemento. Cuando está habilitado, a través de las teclas "ctrl+nvda+f", Como generalmente lo haces para el diálogo de búsqueda de NVDA, pulsar las flechas arriba y abajo en el campo  de edición, permitiéndote navegar por la lista de términos y expresiones anteriormente buscados	.

Puedes en cualquier momento y siempre que lo necesites, escribir un nuevo término, como de costumbre.

### Continuidad de búsqueda

La continuidad de búsqueda es una característica  que, si está configurada, no considera la posición actual en la que está, en un texto, cuando se realiza búsquedas.

Esto significa que si busca algo que no está presente por debajo de su posición actual, la búsqueda se realizará desde el principio del texto para verificar que este término exista en algún lugar del documento.

Esto es especialmente importante para las personas que trabajan con sistemas basados ​​en la web y deben encontrar un determinado botón  o parte del texto, independientemente de dónde estén en la página.

Esta opción es específica para un perfil, lo que significa que puedes tener un perfil donde está activo y otro donde no lo está.

#### ¿Como funciona?

Basta instalar el complemento. Cuando esté habilitado, el cuadro de diálogo "Buscar" te proporcionará una casilla de verificación llamada "Continuidad de búsqueda".

Si está marcada:

1. Si se busca un término y se encuentra debajo de la posición actual, el cursor se colocará en este texto.
2. Si este término no se encuentra debajo de la posición actual, se buscará en la parte superior del texto.
3. Si se encuentra el término, se producirá un pitido corto para informarte que el texto encontrado está por encima de su posición actual y el cursor se coloca en esa posición.
4. Si no se encuentra este término, el mensaje de texto no encontrado será mostrado.

Cambiar esta casillas de verificación  y realizar una búsqueda guardará el nuevo estado (marcado o desmarcado) para el perfil activo. Cancelar la búsqueda no cambiará el estado  en el perfil activo, incluso si lo has cambiado antes de cancelar la búsqueda.

### Sensible a las mayúsculas

NVDA ya ofrece la casilla de verificación "Sensible a las mayúsculas" para permitir búsquedas considerando este caso. Este complemento extiende esta funcionalidad guardando el estado de esta casilla de verificación en el perfil activo, para que puedas tener perfiles configurados de manera diferente.

#### ¿Como funciona?

Basta instalar el complemento. Cambiar la casilla de verificación "Sensible a las mayúsculas" y realizar una búsqueda guardará el nuevo estado (marcado o desmarcado) para el perfil activo. Cancelar la búsqueda no cambiará el estado  en el perfil activo, incluso si lo has cambiado antes de cancelar la búsqueda.

### Información contextual sobre las búsquedas

Actualmente, sin este complemento, el modo como  NVDA se comporta, cuando un término de búsqueda es encontrado, es el siguiente: El cursor se coloca en la posición del término buscado  y apenas este término es pronunciado.

Esto se convierte en algo problemático cuando necesitas buscar varias veces para cualquier término (usando NVDA + f3) ¡Porque la primera cosa que se escucha es el propio término buscado, qué es redundante, porque acabas de hacer una búsqueda de ello!

Este complemento coloca el cursor en la posición del término, pero en lugar de leer el término en sí, lee la línea completa, proporcionando el contexto en el que se encontró este término.

Por ejemplo, supongamos que estás buscando "Marlon" porque sabes que hay un botón, en cualquier lugar de la página, llamado "Marcar Marlon". No quieres buscar el término  "marcar", porque hay otros botones llamados "marcar x y z" y deseas encontrar solo el botón  "Marcar Marlon".

Aquí está el texto:

Excluir comentarios de Marlon

responder directamente a Marlon

Indicar Marlon como spammer

Marcar Marlon en una respuesta

Si buscas "Marlon", antes de este bloque, escuchas
"comentarios de Marlon"

Si mantienes pulsado las teclas NVDA + f3, escuchas

"Marlon"

Marlon como spammer

Marlon en una respuesta

Esto reduciría tu productividad , porque, primero, escucharás apenas marlon, sin saber nada de esta ocurrencia.

La próxima vez, escucharás Marlon y tendría que esperar que "como spammer" fuera pronunciado, porque tampoco sabría qué hay sobre Marlon en este texto.

Del mismo modo, la próxima vez, tendrías que esperar a que el resto de la frase "en una respuesta" fuera pronunciada, porque también no tendrías la certeza sobre lo que era eso acerca de Marlon.

Además, si pulsas NVDA + f3 rápidamente, escucharás Marlon, Marlon, Marlon, Marlon... lo que no es productivo porque sabes que estás buscando Marlon.

#### ¿Como funciona?

Basta instalar el complemento.

Después de la instalación, la línea actual del término de búsqueda se lee y el cursor es colocado sobre él.

En el ejemplo anterior, la primera vez que se realizó la búsqueda, escuchabas

"Excluir comentarios de Marlon"

Si mantienes pulsado las teclas NVDA + f3, escuchas

"responder directamente a Marlon"

"Indicar Marlon como spammer"

"Marcar Marlon en una respuesta"

Además, si pulsas NVDA + f3 rápidamente, escucharás el comienzo de cada línea, lo que te permitirá  pulsar rápidamente "Intro" en la línea que comienza con Marcar, porque sabes que el término "Marlon" está presente en una última posición en esa misma línea.

# ayudando a traducir o desarrollar el complemento

Si deseas ayudar a traducir o desarrollar el complemento, por favor  acceda al [repositório del proyecto](https://github.com/marlon-sousa/EnhancedFindDialog) y buscar el archivo contributing.md en el directorio de documentación equivalente a tu idioma.

## Contribuidores

Agradecimientos especiales a


* Ângelo Miguel Abrantes - Traducción Portugués
* Rémy Ruiz - Traducción Español
* Rémy Ruiz - Traducción Francés
* Tarik Hadžirović - Traducción Croata
*  Thiago Seus - Traducción Portugués del Brasil
* Valentin Kupriyanov - Traducción Rusa
* Umut KORKMAZ - Traducción turco

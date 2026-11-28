# Preguntas frecuentes

> Esta traducción puede quedar desactualizada. La [FAQ original en inglés](https://github.com/ckryptickunal/OpenDesigner/blob/main/site/docs/faq.md) es la fuente canónica. Los enlaces llevan a la documentación original en inglés.

### ¿Qué es OpenDesigner?

Es un complemento gratuito y de código abierto para herramientas de IA como Claude, ChatGPT, Codex y Cursor. Te ayuda a crear un sistema de diseño: las reglas que definen el aspecto de tu aplicación, como colores, tamaños de texto, espacios, esquinas y botones. Lee tu proyecto, hace unas pocas preguntas sencillas, sugiere una respuesta y explica el motivo, comprueba el resultado y guarda las reglas como archivos en tu proyecto.

El código, las habilidades y los datos usan la licencia MIT; la investigación escrita y la documentación usan CC BY 4.0. Necesitas tu propia herramienta de IA, que puede tener un costo. Consulta la [introducción](https://opendesigner.dev/docs/introduction/).

### ¿No es simplemente un prompt?

En parte: las habilidades son instrucciones escritas que sigue tu IA. Un motor de Python hace los cálculos —desde escalas de color y tipografía hasta comprobaciones de contraste y todas las exportaciones— y las mismas respuestas producen los mismos archivos. También puedes ejecutar el motor sin IA. Consulta [Cómo funciona](https://opendesigner.dev/docs/how-it-works/).

### ¿Con qué herramientas de IA funciona?

Se distribuye para Claude Code, la aplicación de Claude, ChatGPT (como Project), Codex, Cursor, VS Code con Copilot, Gemini CLI y otros agentes que leen `.agents/skills/`. Aún falta grabar una prueba de ejecución en cada una. Consulta [Instalación](https://opendesigner.dev/docs/install/).

### ¿OpenDesigner es una habilidad de Claude?

Sí. En Claude Code, el plugin instala sus nueve habilidades; en la aplicación de Claude, las subes como un archivo ZIP de habilidades. Las mismas carpetas también funcionan en Codex, Cursor y otros agentes que leen habilidades. Consulta [Instalación](https://opendesigner.dev/docs/install/).

### ¿Cómo instalo OpenDesigner?

En Claude Code basta con dos comandos y una sesión nueva. La aplicación de Claude, ChatGPT, Codex, Cursor y los demás agentes también tienen un proceso breve. Después, abre tu proyecto y di: "Create a design system for this project." Consulta [Instalación](https://opendesigner.dev/docs/install/).

:::dev
```
/plugin marketplace add ckryptickunal/OpenDesigner
/plugin install opendesigner@opendesigner
```
:::

### ¿Cuánto cuesta?

Nada. OpenDesigner es gratuito y de código abierto; no necesitas crear una cuenta. El código, las habilidades y los datos usan la licencia MIT; la investigación escrita y la documentación usan CC BY 4.0. Necesitas tu propia herramienta de IA, que puede tener un costo. El motor también funciona sin IA. Consulta [Instalación](https://opendesigner.dev/docs/install/).

### ¿Cómo lo actualizo?

En Claude Code basta con un comando y una sesión nueva. En la aplicación de Claude, elimina la habilidad antigua y sube el ZIP más reciente. En Codex, Cursor y otros agentes, vuelve a ejecutar los comandos de copia. El [registro de cambios](https://opendesigner.dev/changelog/) explica qué cambió. Consulta [Actualizarlo](https://opendesigner.dev/docs/install/#update-it).

:::dev
```
claude plugin update opendesigner@opendesigner
```
:::

### ¿Cómo lo elimino o deshago lo que hizo?

Todo lo que escribe es un archivo normal en tu proyecto. Para deshacerlo, elimina `DESIGN.md`, `PRODUCT.md` y la carpeta `opendesigner/`. Si aceptaste la nota para sesiones futuras, elimina también su parte de `AGENTS.md` y la línea `@AGENTS.md` de `CLAUDE.md`. Después, desinstala el plugin o elimina la habilidad que subiste o copiaste. Consulta [Eliminarlo](https://opendesigner.dev/docs/install/#remove-it).

### ¿Qué pregunta durante la configuración?

Hace hasta cinco preguntas: qué estás creando, para quién, dónde se ejecutará, qué sensación debería transmitir y cuál es el color de tu marca o su logotipo. Cada pregunta incluye una respuesta sugerida y el motivo; también puedes decir "just pick". Además, pregunta una vez si puede guardar un registro privado de tus pasos. Consulta [Tu primer sistema de diseño](https://opendesigner.dev/docs/quickstart/).

### ¿Qué archivos crea OpenDesigner en mi proyecto?

Crea `DESIGN.md` y `PRODUCT.md` en la raíz, y una carpeta `opendesigner/` con tokens DTCG, exportaciones de código para tus plataformas, una página de resumen y el registro de decisiones. Consulta [Los archivos que escribe](https://opendesigner.dev/docs/files/).

{{figure:files-tree}}

### ¿Cómo funciona con Tailwind CSS?

Lee la configuración de Tailwind antes de preguntar nada. Si tus plataformas incluyen la web, cada compilación escribe un tema de Tailwind CSS v4, para que las clases de utilidad usen tus colores, espacios, radios y tipografía. Consulta [Exportar](https://opendesigner.dev/docs/export/).

### ¿Cómo usan `DESIGN.md` los agentes de programación con IA?

`DESIGN.md` contiene tus reglas de diseño en lenguaje sencillo, y los agentes de programación lo leen antes de tocar la interfaz. Antes de añadir una nota breve a `AGENTS.md`, OpenDesigner te pide permiso. Esa nota indica a los agentes que lean el documento, usen los tokens y ejecuten `engine.py review` al terminar. Consulta [Decisiones, DESIGN.md y la página de resumen](https://opendesigner.dev/docs/decisions/).

### ¿Cómo mantengo una interfaz coherente entre sesiones de programación con IA?

Haz que todas las sesiones lean las mismas reglas. OpenDesigner las escribe en tu proyecto: `DESIGN.md`, los tokens de diseño y, si das tu aprobación, una nota en `AGENTS.md` que `CLAUDE.md` importa y que pide al agente leer primero `DESIGN.md`. Al terminar una tarea, `engine.py review` enumera los colores y tamaños codificados directamente en el código, y las partes de `DESIGN.md` que quedaron desactualizadas. Consulta [Cómo funciona](https://opendesigner.dev/docs/how-it-works/).

### ¿Cómo encuentro espacios, colores y fuentes incoherentes en mi aplicación?

Una página muestra cómo se aplica tu sistema en el código: cada token y la frecuencia con la que se usa, y luego cada discrepancia entre el código y el sistema, con su archivo y línea. Esto incluye colores demasiado parecidos, espacios, tamaños de texto y esquinas fuera de escala, y valores escritos manualmente aunque exista un token. La revisión también indica cuándo las fuentes de `DESIGN.md` no aparecen en el código. Consulta [Empezar con una aplicación o marca existente](https://opendesigner.dev/docs/existing-product/).

:::dev
```
python3 skills/opendesigner/scripts/engine.py audit-page --open
```
:::

### ¿Puede reemplazar los colores y espacios codificados directamente por tokens de diseño?

Los encuentra y propone una corrección, pero no modifica el código por su cuenta. `engine.py review` enumera cada color, tamaño, radio, sombra y duración codificados directamente, y la página de auditoría ofrece hasta tres formas de resolver cada caso. Tu IA aplica el cambio después de que lo apruebes. Consulta [Para ingenieros](https://opendesigner.dev/docs/engineers/).

### ¿Puede mi chatbot responder con mis propios componentes en vez de texto?

Sí, con Smart UI, que viene con OpenDesigner y permanece desactivado hasta que lo pidas. Tu asistente responde con una parte de tu sistema, como una multa con un botón para pagar o el progreso de una aplicación. Cada respuesta se comprueba antes de mostrarse: el modelo no elige colores, tamaños ni enlaces, y nada se paga ni se reserva hasta que la persona pulsa el botón. Lee tu repositorio para determinar qué respuestas necesitan un componente. [Mira cómo construye una respuesta](https://opendesigner.dev/smart-ui/).

### ¿Qué es la interfaz generativa y cómo hago que coincida con mi sistema de diseño?

La interfaz generativa significa que un asistente de IA responde con una interfaz —por ejemplo, una tabla, un gráfico o un paso de reserva— en vez de limitarse al texto. Para que coincida con tu sistema de diseño, la interfaz debe proceder de tus propios componentes y tokens, no de código que el modelo escriba sobre la marcha. Smart UI prepara esas piezas de antemano a partir de tu biblioteca, las completa mediante código con tus datos y comprueba cada una antes de mostrarla. Consulta [Cómo funciona Smart UI](https://opendesigner.dev/docs/smart-ui/).

### ¿Cómo añado interfaz generativa a un chatbot que ya tengo?

Pídele a tu IA: "Add Smart UI to our assistant." Lee tu repositorio, propone qué respuestas necesitan un componente y tú las confirmas. Tu página muestra las respuestas con `<od-surface>`, un elemento HTML normal compatible con React, Vue, Svelte o HTML sin framework. Conservas tu propio modelo y tus agentes. [Añadir Smart UI a tu asistente](https://opendesigner.dev/docs/smart-ui-quickstart/).

### ¿El modelo escribe el código de la interfaz para cada respuesta?

No. Los componentes se preparan de antemano y se vinculan a los datos de tu aplicación. Para cada pregunta, un comparador rápido elige uno, el código lo completa cuando llegan los datos y el modelo solo redacta la frase. Si no hay un componente preparado que encaje, el modelo crea uno en un formato validado; se rechaza cualquier elemento que no siga el sistema. [Cómo una respuesta se convierte en interfaz](https://opendesigner.dev/docs/smart-ui/#how-an-answer-becomes-interface).

### ¿Envía mi código o mis datos a algún sitio?

El motor se ejecuta en tu computadora y no hace llamadas de red. Tu conversación se envía a tu proveedor de IA, como cualquier prompt. La habilidad de ilustración busca arte con licencias abiertas y sitios de fotos solo cuando la usas; los componentes de la biblioteca que incluyen una foto la cargan desde Unsplash. En la aplicación de Claude, los scripts se ejecutan en el entorno aislado de ejecución de código de Claude.

El registro privado de tus pasos está desactivado a menos que aceptes; permanece en tu proyecto. Los informes anónimos requieren un consentimiento aparte, y todavía no hay ningún servidor que los recopile. Consulta la [página de privacidad](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/PRIVACY.md).

### ¿Cuánto tarda?

El boceto requiere hasta cinco preguntas y está previsto que tarde unos 3 minutos, aunque nadie ha cronometrado todavía a personas reales. El motor tarda unos segundos. Después, profundizas solo donde quieras. Consulta [Niveles de detalle](https://opendesigner.dev/docs/zoom-levels/).

### ¿En qué se diferencia de un generador de temas para shadcn?

Si solo necesitas colores para shadcn/ui, un generador de temas como tweakcn es una buena opción. OpenDesigner empieza un paso antes: pregunta para quién es la aplicación, dónde se ejecuta y qué requisitos de accesibilidad tiene. Registra el motivo de cada decisión y escribe tokens DTCG independientes de las herramientas, además de variables CSS y un tema de Tailwind.

### ¿En qué se diferencia de las herramientas de IA de Figma?

Figma Make crea aplicaciones y prototipos mediante conversación, y un kit de Make empaqueta un sistema de diseño que ya tienes. OpenDesigner crea y documenta el propio sistema, explica el motivo de cada decisión y exporta variables de Figma. No dibuja en un lienzo. Consulta [Para diseñadores de producto](https://opendesigner.dev/docs/designers/).

### ¿En qué se diferencia de UI UX Pro Max?

UI UX Pro Max es una base de conocimiento de diseño de código abierto (MIT) para tu IA: recomienda un estilo, una paleta de colores, fuentes y patrones de página según el tipo de producto, ofrece pautas para muchas pilas tecnológicas y puede guardar el resultado como un archivo maestro Markdown. OpenDesigner crea el sistema a partir de tus propias respuestas y lo convierte en tokens DTCG y exportaciones de código, registra por qué se eligió cada valor y bloquea la compilación si falla el contraste o el tamaño de los objetivos táctiles. Elige UI UX Pro Max si buscas recomendaciones de estilo rápidas y amplias; elige OpenDesigner si quieres tokens que importe tu código y decisiones que tu equipo pueda revisar. Consulta [Cómo funciona](https://opendesigner.dev/docs/how-it-works/).

### ¿Reemplaza a los diseñadores?

No. Se ocupa del trabajo repetitivo del sistema: escalas, tokens, estados y contraste. Pide a una persona el logotipo, los iconos, las ilustraciones, las fotos, la tipografía y la voz de marca, y no puede saber si las personas usuarias entienden tu aplicación. Consulta [Recursos de marca](https://opendesigner.dev/docs/brand-assets/).

### ¿Mi aplicación tendrá el aspecto de cualquier otra creada con IA?

Es una preocupación razonable. OpenDesigner pregunta qué debería recordar la gente de tu producto, configura ocho parámetros a partir de tus respuestas y solicita tu propio logotipo, fuentes e ilustraciones en lugar de inventarlos. No copia otra marca. Si te gusta el aspecto de un sitio, puede crear un Taste Index; tú decides qué conservas y eres responsable de ello. Nunca se incluyen logotipos, nombres, imágenes ni textos.

Con franqueza, hay límites: en la prueba de estrés de octubre de 2026, agentes de IA crearon 46 piezas y 8 maquetas siguiendo el proceso. Una auditoría frente a productos publicados aprobó 28 de las 54, devolvió 20 para pulirlas y reconstruyó 6; gran parte del trabajo más llamativo se había creado fuera de los tokens. Los tokens dan coherencia y un contraste legible; para lograr un aspecto distintivo hace falta tu aporte.

La [galería](https://opendesigner.dev/showcase/) muestra un recuento distinto en la actualidad: desde esa auditoría, se reconstruyeron o se apartaron algunas piezas, y se añadieron pantallas de productos B2B y estudios de estilo.

### ¿Comprueba el contraste de color?

Sí. Comprueba cada pareja de colores de texto, bordes y anillos de foco que producen los tokens según WCAG 2.2 AA, en modo claro y oscuro y en todas las combinaciones de modos, incluido el texto al pasar el cursor y los rellenos al pulsar. Si falla, un error bloquea la compilación. Consulta los [requisitos mínimos de accesibilidad](https://opendesigner.dev/docs/accessibility/).

### ¿Hace que mi aplicación cumpla con WCAG?

Cada sistema incorpora contraste WCAG 2.2 AA, tamaños mínimos para objetivos táctiles, un anillo de foco y movimiento reducido; los errores bloquean la compilación. Eso es un mínimo: las comprobaciones automáticas solo detectan parte de los problemas de WCAG. Haz pruebas con personas reales, incluidas personas que usan tecnología de asistencia. Consulta los [requisitos mínimos de accesibilidad](https://opendesigner.dev/docs/accessibility/).

### Ya tenemos una aplicación o un sistema de diseño. ¿Nos sirve?

Sí. La habilidad de extracción mide tu CSS, archivos de tokens, variables de Figma o manual de marca y ofrece esos valores como respuestas sugeridas; después pregunta solo por lo que falta. No decide nada hasta que lo aceptas. Consulta [Empezar con una aplicación o marca existente](https://opendesigner.dev/docs/existing-product/).

### ¿Cómo funciona la gobernanza para un equipo de sistemas de diseño?

Todo es un archivo en tu repositorio, así que se aplica tu proceso habitual de revisión. Además, el registro de decisiones es acumulativo y explica los motivos; las decisiones bloqueadas y los estándares solo cambian cuando alguien lo pide explícitamente; y `engine.py review` encuentra valores codificados directamente y código que incumple un estándar. Los niveles de detalle más profundos preguntan quién puede cambiar el sistema y cómo se anuncian los cambios; nunca inventan las respuestas. Consulta [Para equipos empresariales de sistemas de diseño](https://opendesigner.dev/docs/enterprise/).

### ¿Cómo podría adoptarlo un equipo?

Ningún equipo lo ha probado en un piloto, así que todavía no hay una guía de implementación. Por ahora recibes `DESIGN.md` para diseñadores, ingenieros y agentes; una nota para `AGENTS.md` que pide a los agentes de programación leer primero el sistema; archivos de tokens que importan tus aplicaciones; y `engine.py review` para detectar desviaciones, aunque aún no se ha probado en una canalización de CI. Empieza con un producto y [cuéntanos](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose) qué necesita tu equipo.

### ¿Admite varias marcas o temas de marca blanca?

Todavía no. Cada sistema incluye modos claro y oscuro, tres densidades y movimiento reducido en un archivo de resolución. La entrevista puede registrar que habrá más marcas, pero el motor no crea modos separados para cada marca. No planifiques todavía una implementación multimarcas.

### ¿Por qué debería confiar en los valores predeterminados?

No tienes por qué confiar en ellos: puedes verificarlos. Se basan en más de 500 Decision Cards, cada una con fuentes registradas o marcada como inferencia. Una revisión volvió a comprobar 161 afirmaciones frente a fuentes vigentes y encontró cinco errores, que ya se corrigieron. Consulta el [mapa de investigación](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/RESEARCH.md).

### ¿En qué etapa está y cómo informo de un problema?

Está en una etapa inicial. La versión 0.3.1 salió el 11 de noviembre de 2026, seis días después de la primera versión etiquetada, y todavía no se han realizado pruebas de usuario observadas. Hasta ahora hay pruebas del motor, tres ejemplos completos, pruebas de usabilidad simuladas por evaluadores de IA y la prueba de estrés descrita arriba.

Para informar de un problema, cuéntale a tu IA qué salió mal. Guarda una nota en tu proyecto con un enlace de GitHub listo para enviar, o puedes [abrir un issue](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose) directamente. No se publica nada hasta que lo envíes.

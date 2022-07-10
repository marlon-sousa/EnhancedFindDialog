# Розширений діалог пошуку NVDA ${addon_version}
Розширений діалог пошуку NVDA реалізує покращення пошуку:

* історія пошуку
* циклічний пошук, що налаштовується для кожного профілю
* врахування регістру, що налаштовується для кожного профілю
* контекстна інформація пошукових запитів

## Завантажити
Завантажити [додаток Розширений діалог пошуку ${addon_version}](https://github.com/marlon-sousa/EnhancedFindDialog/releases/download/${addon_version}/EnhancedFindDialog-${addon_version}.nvda-addon)

## Особливості

### Історія пошуку
На багатьох веб-сайтах і веб-додатках найшвидший спосіб отримати доступ до певних місць — це скористатися командою пошуку, яка часто прив’язана до клавіш ctrl + nvda + f.

Діалог пошуку дає нам змогу ввести текст і перейти до наступного фрагмента цього тексту, якщо він існує.

У багатьох випадках ви відвідуєте ті самі веб-сайти кілька разів протягом одного сеансу NVDA. На багатьох із цих веб-сайтів вам доведеться шукати ті самі терміни, особливо якщо це єдиний спосіб швидко перейти за посиланням або розділом цього веб-сайту.
Особливо це стосується людей, які щодня працюють із веб-системами як частиною своєї роботи.

Однак NVDA не зберігає попередні запити, які ви шукали, у списку. Це сповільнює вашу продуктивність, оскільки, якщо ви не шукаєте той самий термін, що й у вашому останньому пошуку, вам доведеться вводити його знову.

Цей додаток зберігає історію пошуку, доки триває сеанс NVDA. Отже, під час активації пошуку вам потрібно просто натиснути стрілку вниз і вибрати попередні пошукові запити, щоб виконати новий пошук.

Звичайно, ви можете вводити нові запити. Їх також буде додано до списку наступного разу, коли ви активуєте діалог пошуку.

#### Як це працює?

Просто встановіть додаток. Коли його активовано, натискання стрілок вниз і вгору в полі редагування діалогу пошуку дозволить вам переміщатися по списку запитів, які шукалися раніше.

Ви можете будь-коли ввести новий запит, як зазвичай.

### Циклічний пошук

Циклічний пошук — це функція, яка, якщо її налаштовано, не враховує поточну позицію в тексті під час виконання пошуку.

Це означає, що коли ви шукаєте щось, чого немає нижче поточної позиції, пошук буде виконано з початку тексту, щоб перевірити, чи існує цей термін десь у всьому тексті.
Це особливо важливо для людей, які працюють із веб-системами й потребують пошуку певної кнопки чи фрагмента тексту незалежно від того, де вони знаходяться на сторінці.

Цей параметр залежить від профілю, тобто ви можете мати профіль, де він активний, і інший, де його немає.

#### Як це працює?

Просто встановіть додаток. Коли його активовано, у вікні пошуку знаходитиметься прапорець з назвою «Циклічний пошук».

Якщо позначено:

1. Якщо ви шукаєте певний запит і його знайдено нижче поточної позиції, курсор буде встановлено на цьому тексті.
2. Якщо цей запит не знайдено нижче поточної позиції, його пошук здійснюватиметься від початку тексту.
3. Якщо запит знайдено, пролунає короткий звуковий сигнал, який сповістить вас про те, що знайдений текст знаходиться вище поточної позиції, і курсор встановлено на  ньому.
4. Якщо цей запит взагалі не знайдено, то відображається повідомлення про те, що текст не знайдено.

Якщо змінити цей прапорець і виконати пошук, новий стан буде збережено (позначено, або не позначено) для активного профілю. Скасування пошуку не змінить його стану в активному профілі, навіть якщо ви змінили його перед скасуванням пошуку.

### Врахування регістру

NVDA вже пропонує прапорець врахування регістру, щоб дозволити пошук, який залежить від регістру. Цей додаток розширює цю функціональність, зберігаючи стан цього прапорця в активному профілі, так що ви можете мати профілі, налаштовані по-різному.

#### Як це працює?

Просто встановіть додаток. Зміна прапорця врахування регістру та виконання пошуку збережуть новий стан (позначено чи не позначено) для активного профілю. Скасування пошуку не змінить його стану в активному профілі, навіть якщо ви змінили його перед скасуванням пошуку.

### Контекстна інформація пошукових запитів

Коли знайдено пошуковий запит, NVDA поводиться наступним чином: курсор встановлюється в позицію знайденого запиту, і рядок читається починаючи від цієї позиції і до кінця рядка.

Це завжди було проблематично, коли вам доводилося шукати щось кілька разів (за допомогою NVDA + f3), тому що перше, що ви чуєте, це сам 
пошуковий запит, просто тому, що ви шукали цей запит.
Цей додаток встановлює курсор у позицію знайденого запиту, але замість читання від знайденого до кінця рядка, він читає увесь рядок, надаючи вам контекст цього запиту.

Наприклад, припустімо, що ви шукаєте "Марлон", оскільки знаєте, що десь існує кнопка під назвою "вибрати Марлона". Ви не хочете шукати "вибрати", оскільки є інші кнопки, які називаються «вибрати x y z", а ви хочете знайти кнопку "вибрати Марлона".

Ось текст:

Видалити Марлонові коментарі

Відповісти особисто марлонові

Повідомити, що Марлон спамер

Вибрати Марлона для відповіді

Якби ви почали шукати "Марлон" перед цим блоком, ви б почули:

Марлонові коментарі

Натискаючи далі NVDA + f3, ви би почули

Марлонові

Марлон спамер

Марлона для відповіді

Це знизило б вашу продуктивність, оскільки за першим разом ви б лише чули "Марлонові", нічого не знаючи про  контекст, у якому він згадується.

Наступного разу, ви б почули "Марлон" і довелося б чекати що буде промовлено "спамер", тому що ви не знаєте, про що йдеться в цьому тексті стосовно Марлона.

Так само і наступного разу, вам доведеться почекати, доки вимовиться фраза "для відповіді", оскільки ви також не будете впевнені, у якому контексті згадується про Марлона.

Окрім того, якщо ви будете швидко натискати NVDA + f3, ви почуєте Марлон, Марлон, Марлон, Марлон.., що не є продуктивним, оскільки ви знаєте, що шукаєте Марлон.

#### Як це працює

Просто встановіть додаток.

Після встановлення, поточний рядок, що містить запит, зачитується, і курсор встановлюється на позицію знайденого запиту.

У нашому прикладі вище, під час першого пошуку ви почуєте:

Видалити Марлонові коментарі

Якщо ви продовжите натискати NVDA + f3, ви почуєте:

Відповісти особисто марлонові

Повідомити, що Марлон спамер

Вибрати Марлона для відповіді

Окрім того, якщо ви  швидко натискатимете NVDA + f3, ви чутимете початок кожного рядка, що дозволить вам швидко натиснути enter у цільовому рядку, оскільки ви знаєте, що запит "Марлон" міститься на пізнішій позиції в тому самому рядку.

## Допомога та переклад

Якщо ви хочете внести свій внесок або перекласти цей додаток, перейдіть до [репозиторію проекту](https://github.com/marlon-sousa/EnhancedFindDialog) і знайдіть інструкції у файлі contributing.md у каталозі документації англійською мовою.

## Учасники

Особлива подяка


* Ângelo Miguel Abrantes - португальський переклад
* Rémy Ruiz - Французький переклад
* Rémy Ruiz - Іспанський переклад
* Tarik Hadžirović - Хорватський переклад
*  Thiago Seus - Переклад бразильською португальською
* Umut KORKMAZ - Турецький переклад
* Valentin Kupriyanov - Російський переклад
* Ivan Shtefuriak - Український переклад
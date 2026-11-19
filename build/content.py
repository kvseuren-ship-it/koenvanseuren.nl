# -*- coding: utf-8 -*-
# Alle inhoud van koenvanseuren.nl op één plek. Pas hier tekst aan en draai build.py opnieuw.

LANGS = ["nl", "en", "ru"]

UI = {
    "nl": {"over": "Over", "agenda": "Agenda", "werk": "Werk", "home": "home",
           "credits": "Credits", "speellijst": "Speellijst", "pers": "Pers",
           "terug": "← alle werk", "fotos": "Foto's", "rol": "Rol",
           "binnenkort": "Binnenkort", "recent": "Onlangs", "archief": "Eerder",
           "email": "E-mail", "tel": "Telefoon", "lang_name": "nederlands",
           "title_suffix": "theatermaker", "skip": "Naar inhoud",
           "meta_desc": "Koen van Seuren (1994) is regisseur en schrijver, artistiek leider van Antiklimax. Satirisch teksttoneel, radicale bewerkingen van repertoire.",
           "werk_intro": "Regie en tekst, tenzij anders vermeld. Nieuwste eerst.",
           "photo": "foto", "close": "sluiten", "kleur": "kleur"},
    "en": {"over": "About", "agenda": "Agenda", "werk": "Work", "home": "home",
           "credits": "Credits", "speellijst": "Performances", "pers": "Press",
           "terug": "← all work", "fotos": "Photos", "rol": "Role",
           "binnenkort": "Coming up", "recent": "Recently", "archief": "Earlier",
           "email": "Email", "tel": "Phone", "lang_name": "english",
           "title_suffix": "theatre maker", "skip": "Skip to content",
           "meta_desc": "Koen van Seuren (1994) is a Dutch theatre director and writer, artistic director of Antiklimax. Satirical text-based theatre, radical rewrites of the repertoire.",
           "werk_intro": "Direction and text unless stated otherwise. Newest first.",
           "photo": "photo", "close": "close", "kleur": "colour"},
    "ru": {"over": "Обо мне", "agenda": "Афиша", "werk": "Работы", "home": "главная",
           "credits": "Создатели", "speellijst": "Показы", "pers": "Пресса",
           "terug": "← все работы", "fotos": "Фото", "rol": "Роль",
           "binnenkort": "Скоро", "recent": "Недавно", "archief": "Ранее",
           "email": "Почта", "tel": "Телефон", "lang_name": "русский",
           "title_suffix": "театральный режиссёр", "skip": "К содержанию",
           "meta_desc": "Кун ван Сёрен (1994) — нидерландский театральный режиссёр и драматург, художественный руководитель компании Antiklimax.",
           "werk_intro": "Режиссура и текст, если не указано иное. Сначала новые.",
           "photo": "фото", "close": "закрыть", "kleur": "цвет"},
}

NAME = {"nl": "Koen van Seuren", "en": "Koen van Seuren", "ru": "Кун ван Сёрен"}

CONTACT = {
    "email": "koen@antiklimax.nl",
    "phone": "+31 6 43 40 57 07",
    "phone_href": "+31643405707",
    "instagram": "https://www.instagram.com/koenvanseuren/",
    "antiklimax": "https://antiklimax.nl",
}

PORTRAIT = {"img": "portret", "credit": "Het Zuidelijk Toneel"}

# ---------------------------------------------------------------- OVER
BIO = {
"nl": [
"<strong>Koen van Seuren</strong> (Almere, 1994) · regisseur en schrijver · regieopleiding Toneelacademie Maastricht (2020) · artistiek leider van <a href=\"https://antiklimax.nl\">Antiklimax</a>, samen met David Westera, met Grand Theatre Groningen als thuisbasis · maker bij Het Zuidelijk Toneel.",
],
"en": [
"<strong>Koen van Seuren</strong> (Almere, 1994) · director and writer · directing programme, Toneelacademie Maastricht (2020) · artistic director of <a href=\"https://antiklimax.nl\">Antiklimax</a> with David Westera, based at Grand Theatre Groningen · maker at Het Zuidelijk Toneel.",
],
"ru": [
"<strong>Кун ван Сёрен</strong> (Алмере, 1994) · режиссёр и драматург · режиссёрский факультет Театральной академии Маастрихта (2020) · художественный руководитель <a href=\"https://antiklimax.nl\">Antiklimax</a> вместе с Давидом Вестерой, базой служит Grand Theatre Groningen · автор в Het Zuidelijk Toneel.",
],
}

# Uitsluitend Koens eigen woorden, licht ingekort; 'we' soms 'ik'. Bronnen:
#  - projectplan VVV – Voor Volk en Vaderland (solo), Antiklimax 2026 (VVV)
#  - aanvraag We zijn niet alleen, 2026 (WZNA)
#  - interview 'Meet de Maker', Het Zuidelijk Toneel, 4 juli 2025 (HZT)
#  - 'Blijf vooral thuis', De Noorderlingen, november 2026 (NRD)
#  - Koens tekst op antiklimax.nl, pagina Personae (PER)
BIO_QUOTE = {
"nl": [
"Ik vertel geen verhalen om te bevestigen, maar om te bevragen.",  # VVV
"In het theater worden thema’s vaak psychologisch of poëtisch benaderd, maar zelden structureel en ideologisch. Mijn personages zijn geen mensen in de psychologische zin van het woord; ze zijn dragers van ideeën, belichaamde ideologieën. Een personage is nooit puur een individu, maar wordt geconstrueerd uit de omgeving waarin het zich begeeft.",  # VVV + HZT
"Nationalisme, chauvinisme en in uiterste gevallen fascisme hebben geen louter psychologische aanleiding, maar vinden hun oorsprong in de penibele materiële situatie van aanvankelijk doodnormale mensen. De complotdenker is geen gevaarlijke gek, maar een uiting van vals klassenbewustzijn; de kanarie in de kolenmijn van een samenleving die verhardt.",  # VVV + WZNA
"Onze verbeelding zit vast in de romantische orde. Romantiek maakt onze verlangens vermarktbaar – vrijheid is de aanschaf van een Range Rover, de ware liefde vind je door het juiste parfum te kopen – en tegelijkertijd blijft wat we werkelijk verlangen altijd onbereikbaar; waardoor we blijven consumeren, zonder dat de wereld om ons heen verandert of ons echt gelukkiger maakt.",  # VVV
"Ik word hoofdzakelijk geïnspireerd door repertoire van de westerse canon. Belangrijkste uitgangspunt is het fileren en filteren van de ideologie die achter het oorspronkelijke stuk verscholen ligt, en te kijken hoeveel van die ideeën nog terug te vinden zijn in de onze. Je bewijst een oude schrijver de grootste dienst door zijn tekst brutaal naar het heden te trekken.",  # PER + NRD
"Humor is voor mij het beste smeermiddel om ‘serieuze’ vragen te onderzoeken. De lach werkt als een breekijzer: je laat het publiek keihard lachen zodat hun verdediging zakt, en precies op dat moment kun je ze aan het denken zetten. Pas later, bij het weglopen of het napraten, moet het besef komen: wacht even, dit ging ergens over.",  # NRD + HZT
"Waar de realiteit tekortschiet en een collectief verhaal mist om die pijn te duiden, neemt de overlevingsdrang van de fantasie het over.",  # WZNA
],
"en": [
"I don't tell stories to confirm, but to question.",
"In theatre, themes are often approached psychologically or poetically, but rarely structurally and ideologically. My characters are not people in the psychological sense of the word; they are carriers of ideas, embodied ideologies. A character is never purely an individual, but is constructed from the environment it moves in.",
"Nationalism, chauvinism and, in extreme cases, fascism do not have merely psychological causes; they originate in the precarious material situation of initially perfectly ordinary people. The conspiracy theorist is not a dangerous lunatic but an expression of false class consciousness: the canary in the coal mine of a society that is hardening.",
"Our imagination is stuck in the romantic order. Romanticism makes our desires marketable – freedom is buying a Range Rover, true love is found by buying the right perfume – while what we really desire always remains out of reach; so we keep consuming, without the world around us changing or making us any happier.",
"I am mainly inspired by the repertoire of the Western canon. My starting point is to fillet and filter the ideology hidden behind the original play, and to see how much of it can still be found in ours. You do an old writer the greatest service by dragging his text brazenly into the present.",
"For me, humour is the best lubricant for examining ‘serious’ questions. Laughter works like a crowbar: you make the audience laugh out loud so their defences drop, and at exactly that moment you can make them think. Only later, walking out or talking it over, should the realisation come: hang on, this was about something.",
"Where reality falls short and a collective story is missing to make sense of that pain, the survival instinct of fantasy takes over.",
],
"ru": [
"Я рассказываю истории не чтобы подтверждать, а чтобы ставить под вопрос.",
"В театре темы часто решаются психологически или поэтически, но редко структурно и идеологически. Мои персонажи — не люди в психологическом смысле слова; они носители идей, воплощённые идеологии. Персонаж никогда не бывает просто индивидом — его конструирует среда, в которой он существует.",
"У национализма, шовинизма и в крайних случаях фашизма нет чисто психологических причин: они коренятся в бедственном материальном положении поначалу совершенно обычных людей. Конспиролог — не опасный безумец, а выражение ложного классового сознания: канарейка в угольной шахте ожесточающегося общества.",
"Наше воображение застряло в романтическом порядке. Романтизм делает наши желания товаром — свобода есть покупка Range Rover, настоящая любовь находится с правильными духами, — а то, чего мы действительно хотим, остаётся недостижимым; и мы продолжаем потреблять, а мир вокруг не меняется и счастливее нас не делает.",
"Прежде всего меня вдохновляет репертуар западного канона. Главное — вскрыть и процедить идеологию, спрятанную за оригинальной пьесой, и посмотреть, сколько её ещё осталось в нашей. Лучшая услуга старому автору — дерзко перетащить его текст в настоящее.",
"Юмор для меня — лучшая смазка, чтобы исследовать «серьёзные» вопросы. Смех работает как лом: зрители хохочут, их защита падает, и именно в этот момент их можно заставить думать. Лишь потом, по дороге домой или в разговоре, приходит понимание: постойте, это было о чём-то.",
"Там, где реальности не хватает и нет коллективного рассказа, чтобы осмыслить эту боль, за дело берётся инстинкт выживания — фантазия.",
],
}

OVER_IMG = {"img": "makers", "alt": "Koen van Seuren en David Westera", "credit": "De Noorderlingen"}

ALSO = {
"nl": "Koen woont en werkt sinds 2020 in Rotterdam. Hij was regieassistent van Sarah Moeremans bij Het Zuidelijk Toneel en Theater Oostpool, onder meer bij <em>We Are The World, We Are The Brabant</em>, en regisseerde meermaals de tweejaarlijkse Bosch Parade in ’s-Hertogenbosch.",
"en": "Koen has lived and worked in Rotterdam since 2020. He was assistant director to Sarah Moeremans at Het Zuidelijk Toneel and Theater Oostpool, including <em>We Are The World, We Are The Brabant</em>, and has directed the biennial Bosch Parade in ’s-Hertogenbosch several times.",
"ru": "С 2020 года Кун живёт и работает в Роттердаме. Он был ассистентом режиссёра Сары Мурманс в Het Zuidelijk Toneel и Theater Oostpool, в том числе в спектакле <em>We Are The World, We Are The Brabant</em>, и не раз ставил проходящий раз в два года Bosch Parade в Хертогенбосе.",
}

# ---------------------------------------------------------------- WERK
# role: korte rol-aanduiding per taal. imgs: bestandsnamen in build/img_src (zonder extensie volgorde = volgorde op pagina)
WORK = [
{
 "slug": "vvv-voor-volk-en-vaderland", "year": "2027", "title": "VVV – Voor Volk en Vaderland",
 "maker": {"nl": "Antiklimax / Grand Theatre Groningen", "en": "Antiklimax / Grand Theatre Groningen", "ru": "Antiklimax / Grand Theatre Groningen"},
 "role": {"nl": "concept & tekst (Antiklimax), regie", "en": "concept & text (Antiklimax), direction", "ru": "концепция и текст (Antiklimax), режиссура"},
 "status": {"nl": "in ontwikkeling · seizoen 2027–2028", "en": "in development · season 2027–2028", "ru": "в работе · сезон 2027–2028"},
 "text": {
  "nl": ["Het sluitstuk van het romantiek-drieluik van Antiklimax, over de meest omstreden erfenis van de romantiek: het nationalisme.",
         "Welkom in Steggelen. Vroeger stopte hier elk halfuur een bus; nu wacht het VVV-kantoortje met smart op toeristen die nooit komen. Als het dorp dreigt op te gaan in een gemeentefusie, groeit het verzet uit tot een volksmythe van heroïsche proporties. Een bombastische tragikomedie over hunkering naar gemeenschap: als het niet de grond is waarop we zijn geboren, wat hebben we dan écht gemeen?"],
  "en": ["The final part of Antiklimax's trilogy on romanticism, about its most contested legacy: nationalism.",
         "Welcome to Steggelen. A bus used to stop here every half hour; now the little tourist office waits in vain for visitors who never come. When a municipal merger threatens to erase the village, resistance swells into a folk myth of heroic proportions. A bombastic tragicomedy about the longing for community: if it isn't the soil we were born on, what do we really have in common?"],
  "ru": ["Финальная часть трилогии Antiklimax о романтизме — о самом спорном его наследии: национализме.",
         "Добро пожаловать в Стеггелен. Когда-то здесь каждые полчаса останавливался автобус, а теперь крошечное туристическое бюро тщетно ждёт гостей. Когда деревне грозит исчезновение из-за слияния муниципалитетов, сопротивление разрастается в народный миф героических масштабов. Бомбастическая трагикомедия о тоске по общности: если не земля, на которой мы родились, — что же у нас на самом деле общего?"]},
 "credits": [["concept & tekst", "Antiklimax"], ["regie", "Koen van Seuren"], ["coproductie", "Grand Theatre Groningen"]],
 "quotes": [], "dates": [], "imgs": ["vvv-1"], "photo": "Antiklimax", "upcoming": True,
},
{
 "slug": "de-zelf-moordenaar", "year": "2026", "title": "De Zelf-moordenaar",
 "maker": {"nl": "Antiklimax i.s.m. De Noorderlingen", "en": "Antiklimax with De Noorderlingen", "ru": "Antiklimax и De Noorderlingen"},
 "role": {"nl": "tekst (Antiklimax)", "en": "text (Antiklimax)", "ru": "текст (Antiklimax)"},
 "text": {
  "nl": ["Speciaal voor de productiegroep van vooropleiding De Noorderlingen schreef Antiklimax een totaal geschifte herinterpretatie van <em>De Zelfmoordenaar</em>, de ooit verboden Sovjetsatire van Nikolaj Erdman.",
         "Tien stuurloze jongvolwassenen, vijf overbezorgde ouders, één glittergordijn en eindeloos veel meningen over hoe je moet leven en waarom je zou sterven. Een satirische komedie (12+) over de dood, het leven en alles daartussen."],
  "en": ["For the production group of the Groningen pre-training programme De Noorderlingen, Antiklimax wrote a thoroughly unhinged rewrite of <em>The Suicide</em>, Nikolai Erdman's once-banned Soviet satire.",
         "Ten rudderless young adults, five overprotective parents, one glitter curtain and endless opinions on how to live and why you might die. A satirical comedy (12+) about death, life and everything in between."],
  "ru": ["Для производственной группы подготовительной школы De Noorderlingen Antiklimax написал совершенно безумную переработку «Самоубийцы» — когда-то запрещённой советской сатиры Николая Эрдмана.",
         "Десять потерянных молодых людей, пятеро чересчур заботливых родителей, один блестящий занавес и бесконечные мнения о том, как надо жить и зачем умирать. Сатирическая комедия (12+) о смерти, жизни и обо всём, что между ними."]},
 "credits": [["concept & tekst", "Antiklimax"], ["regie", "Lies van de Wiel"],
             ["spel", "Mees Alberts, Jip Kluwer, Ido Kootstra, Maaike Kroneman, Misha Leigh-Valles, Joan Leunge, Lente Mintjes, Oskar Moorlag, Sven Mulder, Daan Wieringa"],
             ["kostuums", "Freja Roelofs, Demi Dijstelberge, Jonna Mulder"], ["vormgeving", "André Kok"], ["techniek", "Herman van Keulen"], ["productie", "Jente Rikken"],
             ["naar", "De Zelfmoordenaar van Nikolaj Erdman"]],
 "quotes": [], "dates": ["13–15/11/2026 · Jonge Harten Festival, Groningen"], "imgs": ["zelfmoordenaar-2", "zelfmoordenaar-1"], "poster": "poster-zelfmoordenaar", "photo": "De Noorderlingen, Jonge Harten",
},
{
 "slug": "we-zijn-niet-alleen", "year": "2026", "title": "We zijn niet alleen",
 "maker": {"nl": "Koen van Seuren & Luca Bötzel · De Parade", "en": "Koen van Seuren & Luca Bötzel · De Parade", "ru": "Кун ван Сёрен и Лука Бётцель · De Parade"},
 "role": {"nl": "tekst & regie", "en": "text & direction", "ru": "текст и режиссура"},
 "text": {
  "nl": ["Een razende punkmonoloog over complotdenkers. Ze duiken op bij familiefeesten, je ontmoet ze bij de bushalte of ze serveren je tafel in een restaurant. De een denkt dat de aarde plat is, de ander dat een bende aliens de wereld bestuurt.",
         "Luca Bötzel brengt het getuigenis van een man die zeker weet dat ze er zijn. Gaandeweg blijkt de buitenaardse waarheid steeds dichter bij huis te liggen: bij verlies, ontheemding en klasse. Een blik in het hoofd van de complotdenker én onder de motorkap van onze samenleving.",
         "Gespeeld op theaterfestival De Parade in Den Haag, Amsterdam en Utrecht (zomer 2026), vanaf Den Haag elke avond uitverkocht. Besproken door Han van Wieringen in <em>De Groene Amsterdammer</em>."],
  "en": ["A raging punk monologue about conspiracy thinkers. They turn up at family parties, at the bus stop, or they wait your table in a restaurant. One believes the earth is flat, another that a gang of aliens runs the world.",
         "Luca Bötzel delivers the testimony of a man who knows for certain that they are out there. Bit by bit the extraterrestrial truth turns out to lie much closer to home: in loss, displacement and class. A look inside the conspiracy thinker's head, and under the bonnet of our society.",
         "Played at the touring theatre festival De Parade in The Hague, Amsterdam and Utrecht (summer 2026), sold out every night from The Hague onwards. Reviewed by Han van Wieringen in <em>De Groene Amsterdammer</em>."],
  "ru": ["Неистовый панк-монолог о конспирологах. Они появляются на семейных праздниках, на автобусной остановке, обслуживают ваш столик в ресторане. Один уверен, что Земля плоская, другой — что миром правит банда пришельцев.",
         "Лука Бётцель произносит свидетельство человека, который точно знает: они здесь. Постепенно оказывается, что инопланетная правда лежит гораздо ближе — в утрате, бездомности и классе. Взгляд в голову конспиролога и под капот нашего общества.",
         "Спектакль шёл на передвижном театральном фестивале De Parade в Гааге, Амстердаме и Утрехте (лето 2026), начиная с Гааги — с аншлагами каждый вечер. Рецензия Хана ван Виринге в <em>De Groene Amsterdammer</em>."]},
 "credits": [["spel", "Luca Bötzel"], ["tekst & regie", "Koen van Seuren"], ["licht", "Wout Panis"], ["dramaturgie", "Luna Joosten"], ["artistieke begeleiding", "Ellen Goemans"], ["foto's", "Niels “Knelis” Meijer"]],
 "quotes": [],
 "dates": ["juli 2026 · De Parade, Den Haag", "juli 2026 · De Parade, Amsterdam", "14–18/08/2026 · De Parade, Utrecht"],
 "imgs": ["wzna-1", "wzna-2", "wzna-3", "wzna-4", "wzna-5"], "photo": "Niels “Knelis” Meijer",
},
{
 "slug": "bosch-parade-2026", "year": "2026", "title": "Bosch Parade 2026",
 "maker": {"nl": "Bosch Parade, ’s-Hertogenbosch", "en": "Bosch Parade, ’s-Hertogenbosch", "ru": "Bosch Parade, Хертогенбос"},
 "role": {"nl": "regie", "en": "direction", "ru": "режиссура"},
 "text": {
  "nl": ["De elfde editie van de tweejaarlijkse varende parade op de Dommel in het hart van ’s-Hertogenbosch, in de geest van Jheronimus Bosch. Onder het thema <em>Mankement als Motor</em> maakten kunstenaars samen met communities uit de stad varende kunstwerken over gebreken, haperingen en wat daar toch uit voortkomt.",
         "Als regisseur verbond Koen de afzonderlijke werken tot één voorstelling op het water: „We definiëren wat we vertellen, ordenen dáárop en bouwen zichtbaar dramaturgisch cement dat makers en publiek door één gezamenlijk verhaal leidt, zonder de autonomie van de werken te verstikken.”",
         "Ruim 56.000 bezoekers zagen de parade; nog eens bijna 25.000 bezochten de Tuin der Lusten op de Citadel."],
  "en": ["The eleventh edition of the biennial floating parade on the river Dommel in the heart of ’s-Hertogenbosch, in the spirit of Hieronymus Bosch. Under the theme <em>Powered by Defect</em>, artists worked with communities from the city on floating artworks about flaws, breakdowns and what grows out of them.",
         "As director, Koen tied the separate works into one performance on the water: “We define what we are telling, order everything accordingly and build visible dramaturgical cement that leads makers and audience through one shared story, without smothering the autonomy of the works.”",
         "More than 56,000 people watched the parade; almost 25,000 more visited the Garden of Earthly Delights on the Citadel."],
  "ru": ["Одиннадцатый выпуск проходящего раз в два года плавучего парада на реке Доммел в центре Хертогенбоса, в духе Иеронима Босха. На тему <em>«Изъян как мотор»</em> художники вместе с городскими сообществами создали плавучие произведения об изъянах, сбоях и о том, что из них вырастает.",
         "Как режиссёр Кун связал отдельные работы в один спектакль на воде: «Мы определяем, что рассказываем, выстраиваем всё вокруг этого и создаём видимый драматургический цемент, который ведёт создателей и публику через одну общую историю, не душа автономию работ».",
         "Парад увидели более 56 000 зрителей; ещё почти 25 000 посетили «Сад земных наслаждений» в Цитадели."]},
 "credits": [["regie", "Koen van Seuren"], ["curator", "David Bade"], ["muziek", "Nicoline Soeter"], ["libretto", "Joachim Robbrecht"], ["artistiek leider", "Erik de Jong"]],
 "quotes": [],
 "dates": ["18–21/06/2026 · Dommel, ’s-Hertogenbosch", "20/05–21/06/2026 · Tuin der Lusten, Citadel"],
 "imgs": ["bp26-2", "bp26-1", "bp26-3", "bp26-4", "bp26-5", "bp26-6", "bp26-7", "bp26-8", "bp26-9", "bp26-10", "bp26-11", "bp26-12"], "photo": "Bosch Parade, Willeke Machiels",
},
{
 "slug": "herzschmerz", "year": "2026", "title": "Herzschmerz",
 "maker": {"nl": "Antiklimax / Grand Theatre Groningen", "en": "Antiklimax / Grand Theatre Groningen", "ru": "Antiklimax / Grand Theatre Groningen"},
 "role": {"nl": "concept & tekst (Antiklimax), regie", "en": "concept & text (Antiklimax), direction", "ru": "концепция и текст (Antiklimax), режиссура"},
 "text": {
  "nl": ["A lovestory to end all lovestories. Antiklimax maakt het uit met de romantische liefde, in een voorstelling vol hartstocht en cris de cœur. Naar Goethes <em>Het lijden van de jonge Werther</em>, Bertolucci’s <em>The Dreamers</em>, tal van andere liefdesverhalen. En <em>Scarface</em>.",
         "Theatermaker Elias probeert zijn uit elkaar vallende voorstelling, en zijn leven, te redden. Hij vraagt zijn oude vriendin Lucinde auditie te doen voor de rol van Lotte. Wat begint als een auditie, wordt een romantische bermudadriehoek, terwijl buiten de wereld in de fik staat. Is de liefde hun ontsnapping uit de werkelijkheid? Of redt de werkelijkheid hen juist van de liefde?"],
  "en": ["A love story to end all love stories. Antiklimax breaks up with romantic love in a show full of passion and cris de cœur, after Goethe's <em>The Sorrows of Young Werther</em>, Bertolucci's <em>The Dreamers</em>, countless other love stories. And <em>Scarface</em>.",
         "Theatre maker Elias tries to save his collapsing production, and his life. He asks his old friend Lucinde to audition for the part of Lotte. What starts as an audition turns into a romantic Bermuda triangle, while outside the world is on fire. Is love their escape from reality, or will reality save them from love?"],
  "ru": ["История любви, которая покончит со всеми историями любви. Antiklimax расстаётся с романтической любовью в спектакле, полном страсти и криков души, — по «Страданиям юного Вертера» Гёте, «Мечтателям» Бертолуччи, множеству других любовных историй. И «Лицу со шрамом».",
         "Театральный режиссёр Элиас пытается спасти разваливающийся спектакль — и собственную жизнь. Он просит старую подругу Люсинду пройти пробы на роль Лотты. То, что начинается как прослушивание, превращается в романтический бермудский треугольник, пока снаружи горит мир. Любовь — это их бегство от реальности? Или реальность спасёт их от любви?"]},
 "credits": [["concept & tekst", "Antiklimax"], ["regie", "Koen van Seuren"], ["spel", "David Westera, Mathieu Wijdeven, Pleun de Roode"], ["scenografie & kostuums", "Caz Egelie"], ["lichtontwerp", "Bogi Bakker"], ["dramaturgie", "Luna Joosten"], ["productieleiding", "Annemarie Venema"], ["coproductie", "Grand Theatre Groningen"], ["foto's", "Niels “Knelis” Meijer"]],
 "quotes": [["Een over-de-top komedie met diep tragische elementen.", "Kester Freriks, Theaterkrant"], ["Echt ingenieus gemaakt.", "Leonie Clement, Festival Cement"]],
 "dates": ["20/02/2026 · première, Grand Theatre Groningen", "tournee feb–apr 2026 o.a. De Nieuwe Vorst Tilburg, Schuur Haarlem, Theater Kikker Utrecht, Zaal 3 Den Haag, De Harmonie Leeuwarden, Theater Bellevue Amsterdam, Theater Walhalla Rotterdam, De Lieve Vrouw Amersfoort, Theater aan de Rijn Arnhem"],
 "imgs": ["herzschmerz-1", "herzschmerz-11", "herzschmerz-7", "herzschmerz-2", "herzschmerz-6", "herzschmerz-3", "herzschmerz-8", "herzschmerz-4", "herzschmerz-5", "herzschmerz-12"], "poster": "poster-herzschmerz", "photo": "Niels “Knelis” Meijer",
},
{
 "slug": "revenge-of-the-extras", "poster": "poster-revenge", "year": "2025", "title": "Revenge of the Extras",
 "maker": {"nl": "Het Zuidelijk Toneel · De Parade", "en": "Het Zuidelijk Toneel · De Parade", "ru": "Het Zuidelijk Toneel · De Parade"},
 "role": {"nl": "tekst & regie", "en": "text & direction", "ru": "текст и режиссура"},
 "text": {
  "nl": ["Een sci-fi satire over wie nooit bovenaan de callsheet staat. Op de set van een sciencefictionfilm eisen twee foeterende figuranten het hoofdpodium op, niet om moreel eerherstel te krijgen, maar om meegezogen te worden in een absurd spektakel waar zelfs de revolutie een performance is geworden. Met flitsende laserstralen en druipend alienbloed.",
         "De Short Summer Show van Het Zuidelijk Toneel, gespeeld op theaterfestival De Parade in Rotterdam, Den Haag, Amsterdam en Utrecht."],
  "en": ["A sci-fi satire about those who never make the top of the call sheet. On the set of a science-fiction film, two grumbling extras seize the main stage, not to restore their moral standing but to get sucked into an absurd spectacle in which even the revolution has become a performance. With flashing lasers and dripping alien blood.",
         "Het Zuidelijk Toneel's Short Summer Show, played at the touring theatre festival De Parade in Rotterdam, The Hague, Amsterdam and Utrecht."],
  "ru": ["Научно-фантастическая сатира о тех, кто никогда не оказывается в начале вызывного листа. На съёмках фантастического фильма двое ворчливых статистов захватывают главную сцену — не ради морального реванша, а чтобы их затянуло в абсурдное зрелище, где даже революция стала перформансом. С мигающими лазерами и капающей кровью пришельцев.",
         "Летний спектакль Het Zuidelijk Toneel, шедший на фестивале De Parade в Роттердаме, Гааге, Амстердаме и Утрехте."]},
 "credits": [["tekst & regie", "Koen van Seuren"], ["spel", "Emma Vermeulen, Noah de Nooij, Teun Donders"], ["muziek", "Ton van der Meer"], ["kostuums", "Ilse Vermeulen"], ["tekstadvies", "David Westera"], ["dramaturgisch advies", "Joachim Robbrecht"], ["productie", "Het Zuidelijk Toneel"]],
 "quotes": [["Een vrolijke verpakking met hoge amusementswaarde.", "de Volkskrant"], ["Een echte Parade-voorstelling met actie, humor en visuele effecten.", "NRC"], ["Een dramaturgisch uitbundig, kort toneelstuk.", "Kester Freriks, Theaterkrant"]],
 "dates": ["20/06/2025 · première, De Parade Rotterdam", "zomer 2025 · De Parade Den Haag, Amsterdam, Utrecht"],
 "imgs": ["revenge-1", "revenge-2", "revenge-3"], "photo": "Het Zuidelijk Toneel",
},
{
 "slug": "we-are-the-world-we-are-the-brabant", "poster": "poster-watw", "year": "2025", "title": "We Are The World, We Are The Brabant",
 "maker": {"nl": "Het Zuidelijk Toneel / Sarah Moeremans", "en": "Het Zuidelijk Toneel / Sarah Moeremans", "ru": "Het Zuidelijk Toneel / Sarah Moeremans"},
 "role": {"nl": "regieassistent", "en": "assistant director", "ru": "ассистент режиссёра"},
 "text": {
  "nl": ["Een inwijdingsritueel met Brabantse amateurspelers. Wat is een Brabander, en wanneer ben je deel van Brabant? Het ensemble van Het Zuidelijk Toneel en lokale spelers uit elke speelstad maken van de avond een rood-wit-geblokt Brabants feest, met Schrobbelèr en worstenbrood op het podium."],
  "en": ["An initiation ritual with amateur performers from Brabant. What makes someone a Brabander, and when do you belong? The Het Zuidelijk Toneel ensemble and local performers from each tour city turn the evening into a red-and-white-chequered Brabant party, with Schrobbelèr and sausage rolls on stage."],
  "ru": ["Обряд посвящения с актёрами-любителями из Брабанта. Кто такой брабантец и когда ты становишься частью Брабанта? Ансамбль Het Zuidelijk Toneel и местные исполнители из каждого города гастролей превращают вечер в красно-белый клетчатый брабантский праздник — с ликёром Schrobbelèr и колбасными булочками прямо на сцене."]},
 "credits": [["regie", "Sarah Moeremans"], ["spel", "Alicia Boedhoe, Gillis Biesheuvel, Julia Ghysels, Joep van der Geest, Keja Klaasje Kwestro, Louis van der Waal en 32 Brabantse spelers"], ["kostuums", "Daphne de Winkel"], ["muziek", "Timo Merkies"], ["regieassistent", "Koen van Seuren"], ["productie", "Het Zuidelijk Toneel"], ["foto's", "Sofie Knijff"]],
 "quotes": [],
 "dates": ["31/01/2025 · première", "tournee tot 16/03/2025 · Tilburg, ’s-Hertogenbosch, Helmond, Etten-Leur, Roosendaal, Eindhoven"],
 "imgs": [], "photo": "Sofie Knijff",
},
{
 "slug": "bosch-parade-2024", "year": "2024", "title": "Bosch Parade 2024",
 "maker": {"nl": "Bosch Parade, ’s-Hertogenbosch · Het Zuidelijk Toneel", "en": "Bosch Parade, ’s-Hertogenbosch · Het Zuidelijk Toneel", "ru": "Bosch Parade, Хертогенбос · Het Zuidelijk Toneel"},
 "role": {"nl": "eindregie, met Sarah Moeremans", "en": "final direction, with Sarah Moeremans", "ru": "режиссура, вместе с Сарой Мурманс"},
 "text": {
  "nl": ["De tiende editie van de varende parade op de Dommel, met als thema <em>Hedendaagse Demonen</em>: algoritmes en data, newsfeeds en social media, hackers en trackers, influencers en instaposts als de plagen van een moderne apocalyps, in een stoet nieuwe kunstwerken in de geest van Jheronimus Bosch.",
         "Koen had de eindregie, onder de vlag van Het Zuidelijk Toneel en in co-regie met Sarah Moeremans."],
  "en": ["The tenth edition of the floating parade on the Dommel, themed <em>Contemporary Demons</em>: algorithms and data, newsfeeds and social media, hackers and trackers, influencers and Instagram posts as the plagues of a modern apocalypse, in a procession of new artworks in the spirit of Hieronymus Bosch.",
         "Koen was in charge of the final direction, under the banner of Het Zuidelijk Toneel and co-directing with Sarah Moeremans."],
  "ru": ["Десятый выпуск плавучего парада на Доммеле на тему <em>«Современные демоны»</em>: алгоритмы и данные, ленты новостей и соцсети, хакеры и трекеры, инфлюенсеры и посты как казни современного апокалипсиса — в шествии новых работ в духе Иеронима Босха.",
         "Кун отвечал за итоговую режиссуру под эгидой Het Zuidelijk Toneel, вместе с Сарой Мурманс."]},
 "credits": [["eindregie", "Koen van Seuren"], ["co-regie", "Sarah Moeremans"], ["libretto", "Joachim Robbrecht"], ["artistiek leider", "Miesjel van Gerwen"]],
 "quotes": [],
 "dates": ["20–23/06/2024 · Dommel, ’s-Hertogenbosch"],
 "imgs": ["bp24-1"], "photo": "Willeke Machiels",
},
{
 "slug": "as-the-world-hurts", "year": "2024", "title": "As The World Hurts",
 "maker": {"nl": "Antiklimax / Grand Theatre Groningen", "en": "Antiklimax / Grand Theatre Groningen", "ru": "Antiklimax / Grand Theatre Groningen"},
 "role": {"nl": "concept & tekst (Antiklimax), regie", "en": "concept & text (Antiklimax), direction", "ru": "концепция и текст (Antiklimax), режиссура"},
 "text": {
  "nl": ["Een romantische <em>Into the Wild</em> over mens en natuur, het eerste deel van het romantiek-drieluik van Antiklimax.",
         "Een romantisch aangelegde maar wanhopige jongen neemt het besluit van zijn leven: hij offert zijn culturele luxeleventje op en trekt het bos in. Vrij van wetten, verplichtingen en etiquette hoopt hij dichter bij zijn ware natuur te komen. Maar is er voor de mens nog wel plaats in de natuur? Een romantische safari vol taalvondsten, levensvraagstukken, fantasie en muziek."],
  "en": ["A romantic <em>Into the Wild</em> about people and nature, the first part of Antiklimax's trilogy on romanticism.",
         "A romantically inclined but desperate young man makes the decision of his life: he sacrifices his cosy cultured existence and heads into the woods. Free of laws, duties and etiquette, he hopes to get closer to his true nature. But is there still room for humans in nature? A romantic safari full of wordplay, existential questions, fantasy and music."],
  "ru": ["Романтический «В диких условиях» о человеке и природе — первая часть трилогии Antiklimax о романтизме.",
         "Романтичный, но отчаявшийся юноша принимает главное решение своей жизни: он жертвует уютной культурной жизнью и уходит в лес. Свободный от законов, обязательств и этикета, он надеется приблизиться к своей истинной природе. Но осталось ли в природе место для человека? Романтическое сафари, полное словесных находок, жизненных вопросов, фантазии и музыки."]},
 "credits": [["concept & tekst", "Antiklimax"], ["regie", "Koen van Seuren"], ["spel", "David Westera, Hélène Vrijdag, Emma Vermeulen"], ["scenografie & kostuums", "Caz Egelie"], ["muziek", "Aart Strootman"], ["dramaturgie", "Judith Blankenberg"], ["lichtontwerp", "Bogi Bakker"], ["tekstcoach", "Joachim Robbrecht"], ["coproductie", "Grand Theatre Groningen"], ["foto's", "Niels “Knelis” Meijer"]],
 "quotes": [["Een verrukkelijk, lichtvoetig theatersprookje.", "Peter van Strien, Dagblad van het Noorden ★★★★"]],
 "dates": ["04/05/2024 · première, Grand Theatre Groningen", "tournee 2024–2025 o.a. Theater Bellevue Amsterdam, Theater Kikker Utrecht, Theater Walhalla Rotterdam, Schuur Haarlem, Zaal 3 Den Haag, Verkadefabriek Den Bosch"],
 "imgs": ["atwh-1", "atwh-11", "atwh-4", "atwh-12", "atwh-5", "atwh-2", "atwh-6", "atwh-7", "atwh-8", "atwh-10", "atwh-3"], "poster": "poster-atwh", "photo": "Niels “Knelis” Meijer",
},
{
 "slug": "funf-sechs-alles-flex", "poster": "poster-funf", "year": "2023", "title": "Fünf, sechs, alles Flex",
 "maker": {"nl": "Het Zuidelijk Toneel / Club Gewalt", "en": "Het Zuidelijk Toneel / Club Gewalt", "ru": "Het Zuidelijk Toneel / Club Gewalt"},
 "role": {"nl": "regie, met Sarah Moeremans", "en": "co-direction with Sarah Moeremans", "ru": "сорежиссура с Сарой Мурманс"},
 "text": {
  "nl": ["Een muzikale komedie naar <em>Frühere Verhältnisse</em> van de Oostenrijkse komedieschrijver Johann Nestroy. Vastgoedondernemer Scheitermann en professorsdochter Josephine zoeken allebei een nieuwe persoonlijke assistent voor hun losse handjes en wisselende buien. Een overdaad aan taal, muziek en autotune over de valse, ongelijke wereld van rijkdom en schijn."],
  "en": ["A musical comedy after <em>Frühere Verhältnisse</em> by the Austrian comic playwright Johann Nestroy. Property tycoon Scheitermann and professor's daughter Josephine are both looking for a new personal assistant to put up with their wandering hands and changing moods. A delightful overdose of language, music and autotune about the false, unequal world of wealth and pretence."],
  "ru": ["Музыкальная комедия по пьесе австрийского комедиографа Иоганна Нестроя «Былые отношения». Девелопер Шайтерман и профессорская дочка Жозефина ищут нового личного ассистента, готового терпеть их распущенные руки и перепады настроения. Изобилие текста, музыки и автотюна о фальшивом, неравном мире богатства и видимости."]},
 "credits": [["regie", "Sarah Moeremans, Koen van Seuren"], ["tekstbewerking", "Sarah Moeremans, Gillis Biesheuvel, Joep van der Geest"], ["productie", "Het Zuidelijk Toneel, Club Gewalt"]],
 "quotes": [], "dates": ["23/06/2023 · première"], "imgs": [], "photo": "",
},
{
 "slug": "hamlet-versus-don-quixote", "year": "2023", "title": "Hamlet versus Don Quixote",
 "maker": {"nl": "Antiklimax / Grand Theatre Groningen", "en": "Antiklimax / Grand Theatre Groningen", "ru": "Antiklimax / Grand Theatre Groningen"},
 "role": {"nl": "tekst & regie", "en": "text & direction", "ru": "текст и режиссура"},
 "text": {
  "nl": ["Een duel tussen twee (anti)helden. We twijfelen aan de wereld, aan onszelf, aan goed en kwaad, en ondertussen branden de bossen, stijgt de zeespiegel en groeit de ongelijkheid. Om wat voor helden vraagt deze tijd?",
         "Evalinde Lammers en David Westera zoeken de Hamlet en de Don Quixote in zichzelf: tussen hoofd en hart, tussen egoïsme en idealisme. To Hamlet or to Don Quixote, that’s the question."],
  "en": ["A duel between two (anti)heroes. We doubt the world, ourselves, good and evil, while forests burn, sea levels rise and inequality grows. What kind of heroes does this age need?",
         "Evalinde Lammers and David Westera search for the Hamlet and the Don Quixote in themselves: between head and heart, between egoism and idealism. To Hamlet or to Don Quixote, that is the question."],
  "ru": ["Дуэль двух (анти)героев. Мы сомневаемся в мире, в себе, в добре и зле, а тем временем горят леса, поднимается уровень моря и растёт неравенство. Каких героев требует наше время?",
         "Эвалинде Ламмерс и Давид Вестера ищут Гамлета и Дон Кихота в себе — между головой и сердцем, между эгоизмом и идеализмом. Гамлетить или донкихотствовать — вот в чём вопрос."]},
 "credits": [["concept", "Antiklimax"], ["regie & tekst", "Koen van Seuren"], ["spel & tekst", "David Westera, Evalinde Lammers"], ["dramaturgie", "Judith Blankenberg"], ["vormgeving", "Caz Egelie"], ["lichtontwerp", "Bogi Bakker"], ["coproductie", "Grand Theatre Groningen"], ["foto's", "Niels “Knelis” Meijer"]],
 "quotes": [["Een cadeautje vol energie en curieuze gebeurtenissen.", "Ingrid de Vries, Theater050"]],
 "dates": ["24/02/2023 · première, Grand Theatre Groningen", "tournee 2023 o.a. Festival Cement Den Bosch, Het Nationale Theater Den Haag, Theater Kikker Utrecht, Theater Walhalla Rotterdam, De Sloot Amsterdam"],
 "imgs": ["hamlet-1", "hamlet-2", "hamlet-6", "hamlet-3", "hamlet-7", "hamlet-4"], "poster": "poster-hamlet", "photo": "Niels “Knelis” Meijer",
},
{
 "slug": "peer-gynt", "year": "2022", "title": "Peer Gynt (speelt David Westera)",
 "maker": {"nl": "Antiklimax / Grand Theatre Groningen", "en": "Antiklimax / Grand Theatre Groningen", "ru": "Antiklimax / Grand Theatre Groningen"},
 "role": {"nl": "concept & tekst (met David Westera), regie", "en": "concept & text (with David Westera), direction", "ru": "концепция и текст (с Давидом Вестерой), режиссура"},
 "text": {
  "nl": ["Een krachttoer vol leugens en grootheidswaan. Antiklimax herschreef Ibsens monumentale stuk, dat meer dan zestig personages telt, tot een monoloog voor één eenzame leugenaar: een twintiger op zoek naar zijn titelrol op het wereldtoneel. Wie ben je echt, als je liegt?",
         "Ontstaan als afstudeervoorstelling aan de Toneelacademie Maastricht (2020); in 2022 in een nieuwe versie in première bij Grand Theatre Groningen."],
  "en": ["A tour de force of lies and megalomania. Antiklimax rewrote Ibsen's monumental play, with its more than sixty characters, into a monologue for one lonely liar: a twenty-something searching for his title role on the world stage. Who are you really, when you lie?",
         "First made as a graduation production at the Toneelacademie Maastricht (2020); a new version premiered at Grand Theatre Groningen in 2022."],
  "ru": ["Феерия лжи и мании величия. Antiklimax переписал монументальную пьесу Ибсена, в которой более шестидесяти персонажей, в монолог для одного одинокого лжеца — двадцатилетнего парня в поисках своей главной роли на мировой сцене. Кто ты на самом деле, когда лжёшь?",
         "Спектакль родился как дипломная работа в Театральной академии Маастрихта (2020); в 2022 году новая версия вышла в Grand Theatre Groningen."]},
 "credits": [["concept & tekst", "Antiklimax"], ["spel", "David Westera"], ["regie", "Koen van Seuren"], ["dramaturgie", "Judith Blankenberg"], ["lichtontwerp (2020)", "Bogi Bakker"], ["coproductie", "Grand Theatre Groningen"], ["foto's", "Niels “Knelis” Meijer"]],
 "quotes": [["Een spannende monoloog, virtuoos gespeeld ook.", "Moos van den Broek, Theaterkrant (keuze van de criticus)"], ["Met een ongelofelijke levenslust, bravoure, fantasie, welbespraaktheid en vooral talent.", "Dio van Velden, Theater050"]],
 "dates": ["04/06/2022 · première, Grand Theatre Groningen", "tournee 2022–2024 o.a. Het Nationale Theater Den Haag, Theater Kikker Utrecht, Theater Walhalla Rotterdam, De Lawei Drachten, Stormram-tournee Groningen/Friesland/Drenthe"],
 "imgs": ["peergynt-1", "peergynt-2", "peergynt-7", "peergynt-3", "peergynt-4", "peergynt-6"], "poster": "poster-peergynt", "photo": "Niels “Knelis” Meijer",
},
{
 "slug": "on-hold", "year": "2022", "title": "On Hold",
 "maker": {"nl": "Finn Borath / Likeminds", "en": "Finn Borath / Likeminds", "ru": "Финн Борат / Likeminds"},
 "role": {"nl": "eindregie", "en": "final direction", "ru": "режиссура"},
 "text": {
  "nl": ["Een beeldende performance van Finn Borath over verveling, nutteloosheid en bullshitjobs: een man gevangen in een kantoorbaan die enkel nog bestaat uit het lezen, bestempelen en sorteren van documenten waar vervolgens niets mee gebeurt. Te zien in <em>Likeminds bedankt!</em>, Amsterdam-Noord."],
  "en": ["A visual performance by Finn Borath about boredom, futility and bullshit jobs: a man trapped in an office job that consists only of reading, stamping and sorting documents that nothing is ever done with. Shown at <em>Likeminds bedankt!</em>, Amsterdam-Noord."],
  "ru": ["Визуальный перформанс Финна Бората о скуке, бессмысленности и «бредовой работе»: человек заперт в офисе, где он лишь читает, штампует и сортирует бумаги, с которыми потом ничего не происходит. Показан в программе <em>Likeminds bedankt!</em> в Амстердаме-Норд."]},
 "credits": [["concept & uitvoering", "Finn Borath"], ["decor", "Yoeri Taken"], ["eindregie", "Koen van Seuren"], ["productie", "Likeminds"]],
 "quotes": [], "dates": ["07/04/2022 · Likeminds, Amsterdam"], "imgs": [], "photo": "",
},
{
 "slug": "de-rattenvanger", "year": "2020", "title": "De Rattenvanger – What’s in a fairytale?",
 "maker": {"nl": "Theater Oostpool", "en": "Theater Oostpool", "ru": "Theater Oostpool"},
 "role": {"nl": "regie, met Sarah Moeremans", "en": "co-direction with Sarah Moeremans", "ru": "сорежиссура с Сарой Мурманс"},
 "text": {
  "nl": ["Een nieuw deel in Sarah Moeremans’ sprookjesreeks <em>What’s in a fairytale?</em> bij Theater Oostpool, naar de rattenvanger van Hamelen."],
  "en": ["A new instalment of Sarah Moeremans's fairy-tale series <em>What’s in a fairytale?</em> at Theater Oostpool, after the Pied Piper of Hamelin."],
  "ru": ["Новая часть сказочной серии Сары Мурманс <em>What’s in a fairytale?</em> в Theater Oostpool — по легенде о гамельнском крысолове."]},
 "credits": [["regie", "Sarah Moeremans, Koen van Seuren"], ["productie", "Theater Oostpool"]],
 "quotes": [], "dates": ["08/02/2020 · première"], "imgs": [], "photo": "",
},
]

# Labels van credits vertalen (nl is de sleutel)
CREDIT_LABELS = {
 "en": {"concept & tekst": "concept & text", "regie": "direction", "spel": "performers", "kostuums": "costumes", "vormgeving": "design",
        "techniek": "technical", "productie": "production", "naar": "after", "tekst & regie": "text & direction", "licht": "lighting",
        "dramaturgie": "dramaturgy", "artistieke begeleiding": "artistic guidance", "foto's": "photography", "scenografie & kostuums": "set & costumes",
        "lichtontwerp": "lighting design", "productieleiding": "production manager", "coproductie": "co-production", "muziek": "music",
        "tekstadvies": "text advice", "dramaturgisch advies": "dramaturgical advice", "tekstcoach": "text coach", "tekstbewerking": "adaptation",
        "concept": "concept", "regie & tekst": "direction & text", "spel & tekst": "performers & text", "lichtontwerp (2020)": "lighting design (2020)",
        "concept & uitvoering": "concept & performance", "decor": "set", "eindregie": "final direction", "co-regie": "co-direction", "curator": "curator", "libretto": "libretto", "artistiek leider": "artistic director", "regieassistent": "assistant director"},
 "ru": {"concept & tekst": "концепция и текст", "regie": "режиссура", "spel": "в ролях", "kostuums": "костюмы", "vormgeving": "оформление",
        "techniek": "техника", "productie": "продюсирование", "naar": "по мотивам", "tekst & regie": "текст и режиссура", "licht": "свет",
        "dramaturgie": "драматургия", "artistieke begeleiding": "художественный куратор", "foto's": "фото", "scenografie & kostuums": "сценография и костюмы",
        "lichtontwerp": "художник по свету", "productieleiding": "руководитель производства", "coproductie": "копродукция", "muziek": "музыка",
        "tekstadvies": "консультант по тексту", "dramaturgisch advies": "драматургический консультант", "tekstcoach": "педагог по тексту",
        "tekstbewerking": "адаптация текста", "concept": "концепция", "regie & tekst": "режиссура и текст", "spel & tekst": "в ролях и текст",
        "lichtontwerp (2020)": "художник по свету (2020)", "concept & uitvoering": "концепция и исполнение", "decor": "декорации", "eindregie": "режиссура", "co-regie": "сорежиссура", "curator": "куратор", "libretto": "либретто", "artistiek leider": "художественный руководитель", "regieassistent": "ассистент режиссёра"},
}

# Agenda-teksten
AGENDA_NOTE = {
 "nl": "Speeldata van Antiklimax staan ook op <a href=\"https://antiklimax.nl\">antiklimax.nl</a>.",
 "en": "Antiklimax performance dates are also listed at <a href=\"https://antiklimax.nl\">antiklimax.nl</a>.",
 "ru": "Расписание Antiklimax также на сайте <a href=\"https://antiklimax.nl\">antiklimax.nl</a>.",
}

# Wat op de homepage als beeld rouleert (volgorde)
HERO = "wzna-2"  # Luca bij de draaimolen, We zijn niet alleen
HERO_CAPTION = {"nl": "Luca Bötzel in <em>We zijn niet alleen</em>, De Parade 2026 · foto Niels “Knelis” Meijer",
                "en": "Luca Bötzel in <em>We zijn niet alleen</em>, De Parade 2026 · photo Niels “Knelis” Meijer",
                "ru": "Лука Бётцель в спектакле <em>We zijn niet alleen</em>, De Parade 2026 · фото Нильс «Кнелис» Мейер"}

# Beeldenrij op de homepage (link naar productie)
MOSAIC = [("poster-herzschmerz","herzschmerz"),("wzna-3","we-zijn-niet-alleen"),("atwh-4","as-the-world-hurts"),("poster-zelfmoordenaar","de-zelf-moordenaar"),
          ("hamlet-7","hamlet-versus-don-quixote"),("revenge-2","revenge-of-the-extras"),("poster-peergynt","peer-gynt"),("herzschmerz-7","herzschmerz"),
          ("poster-atwh","as-the-world-hurts"),("zelfmoordenaar-2","de-zelf-moordenaar"),("poster-hamlet","hamlet-versus-don-quixote"),("atwh-6","as-the-world-hurts")]

# Openingszin op home (Koen, HZT 2025)
HOME_LEAD = {
"nl": "In het toneelstuk dat het leven heet, speelt 99,9 procent van de mensen een bijrol. En toch dromen we er allemaal van de hoofdrol te spelen.",
"en": "In the play called life, 99.9 per cent of people have a supporting role. And yet we all dream of playing the lead.",
"ru": "В пьесе под названием «жизнь» 99,9 процента людей играют второстепенные роли. И всё же все мы мечтаем о главной.",
}

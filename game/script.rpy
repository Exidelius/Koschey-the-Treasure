﻿
# Определение изменений воспроизведения
define menu = nvl_menu

# Определение персонажей игры.
define mc = Character('Василиса', color='#20DAA4', kind=nvl, what_prefix = '{cps=100}')
define koschey = Character('Кощей Бессмертный', color='#ED8F33', kind=nvl, what_prefix = '{cps=100}')
define yaga = Character('Баба Яга', color='#672529', kind=nvl, what_prefix = '{cps=30}')
define likho = Character('Лихо Лесное', color='#5F990C', kind=nvl, what_prefix = '{cps=200}')
define snake = Character('Заколдованная', color='#9466BF', kind=nvl, what_prefix = '{cps=50}')
define narrator = nvl_narrator


init:
    $ relation_current = 0
    $ relation_max = 100
    $ first_choice = None
    $ diastyle = 2


label transition(text, time=4.0):
    scene black with dissolve

    show text text

    pause time

    scene black with dissolve  

    return


label start:
    call transition('Работа не волк. Работа - это ворк, а волк - это ходить.')
    call transition('"НАЗВАНИЕ НОВЕЛЛЫ"', time=6.0)

    # TODO убрать переходы между актами
    # TODO указать нужную скорость отображения текста
    # TODO добавить описание "Разработано в рамках джема..." на начальный экран

    'В некотором царстве, в некотором государстве жила-была царевна, и имя ей было Василиса.'

    'Была она - умом одаренная, невиданной красоты да силы неслыханной.'

    'Правила она год, другой, и все лета царствования своего искала себе мужа, - по силе равного да богатством не обделенного.'

    'Приходили к ней богатыри ладные, царевичи славные, но никто Василисе не приглянулся.'

    'Надоело ей ждать, когда счастье её найдет, и отправилась она сама, да не куда-то, а на поиски Кощея Бессмертного.'

    'Слыхала она, что богатства у него немерено, сил невиданно, да жизнь надежно спрятана.'

    scene forest with dissolve

    'Находясь в лесной глуши, царевна направляется к той единственной, кто может помочь ей добраться в царство Кощея.'

    'День за днём, год за годом, оберегает она путь к царству мертвому, провожает души, да не позволяет живым перейти в мир иной.'

    'Путь к дому Бабы Яги темен и извилист, идет он через зыбкие топи, да густую чащу, полную кустов терновника. 
    Но не тронута кожа Василисы иглами острыми, не сыры ноги её от воды мёртвой, словно и не шла она три ночи к дому ведьмы.'

    'И вот стоит царевна перед домом Яги, да держит в руках букет из полыни и чертополоха, и хоть неспокойна душа её, знает, - другого пути к Кощею нет.'

    mc 'Долгий путь, Яга, я проделала, шла к тебе три дня и три ночи, черной птицей обернулась, черным вороном, не видел меня ни зверь твой, да не ты сама, ведьма окаянная. Так повернись изба, ко мне передом, к лесу - задом!'

    'Повязала Василиса букет на пояс около верного меча своего, сняла сапоги, и босыми ногами обошла дом Яги три раза. 
    Глаза в пол не опускала, смотрела на лесную чащу, да чувствовала, как ледяная трава и корни, словно ловкие пальцы, пытаются ухватить её за ноги.'

    # TODO K4-K5

    'Стоит царевна перед порогом избы, и слышит, как идет хозяйка дома, разной поступью идёт, - одна нога ступает мягко, словно кошка крадется, а вторая, - со звоном, да холодным таким, как звон множества колокольчиков.'

    'Слышит девушка - двери Яга отпирает, и думается ей, вот увидит она сейчас ту, о которой с детства говорили - “стара и страшна, поганая баба, костяной ногой в том мире стоит, детей в полдень крадет, и в лютый мороз губит”.'

    'Но стоит перед царевной не костлявая старуха, а женщина, чьей красоты мир не видел, - красивее всех царевн.' 
    
    'Волосы черные как ночь, волнами ниспадают до самой земли, и только то тут, то там, - серебряные змейки вьются в них. Кожа её солнцем поцелована, глаза - зеленый малахит, а губы красны словно кровь.'

    yaga 'Чего тебе надобно, негодница? Смотри, выйду к тебе, царевна, костяной ногой, обратно не вернешься, так и останешься со мной.'

    mc 'Доброго вечера, Яга, пришла я к тебе из своего царства, по болотам зыбким шла, по тропам неведомым, да ради знания о том, как пройти в царство Кощеево.'

    # TODO

    mc 'Сильна я и умна, Яга, да нет в царстве моём дружины крепкой, казны полной, и главное - душа моя одинока.' 
    
    mc 'Не нашлось еще богатыря, что был бы равен мне и умом, и силой. Кощей только остался - последняя надежда моя. Коль приглянусь я ему, будет правление наше складным и ладным. 
'
    yaga 'А коль не приглянешься? Что тогда?'

    'Стоит Яга за порогом, да хитро на Василису смотрит, с ехидством, словно знает то, что сама царевна не знает'
    
    'И отвечает ей царевна, и холодно так отвечает, а в глазах её огонь блещет.'

    mc 'Коль не приглянусь? Не сносить ему головы, да лишится он всех своих сокровищ. Одна править стану'

    yaga 'Хочешь сказать, что ты, Василиса, сможешь Кощея одолеть?'

    yaga 'Ну так заходи в избу, уж больно любопытно мне, осмелишься ли ты Кощея с трона сместить, аль может и полюбит он тебя.'

    'И ступила Яга за порог живой ногой, приглашая царевну в избу. Теплом печи повеяло, травами лесными, с лугов собранных.'

    'Заходит царевна в избу, через сени проходит, да без стеснения осматривается.' 
    
    'Светло в избе, по центру печь расположена - украшена она узорами и письменами, а над нею полог кружевной висит.' 
    
    'Дивится царица - травы невиданные, в пучки собранные, под самым потолком развешаны, а по стенам избы то тут, то там, черепа зверей висят, да глазницы их искрами света мерцают.'

    yaga 'Раз пришла ты ко мне, то, верно, знаешь, что от тебя попрошу я? Да вот только кажется мне, что просить тебя воды натаскать, да всякое на веретёнце по ниточке напрядсти, толку нет.'

    yaga 'Ты ответь-ка мне, Василиса, тот перстень, что ты на руке левой носишь, отдашь ли его? Помнится мне, что перстень то этот не простой - путь домой он укажет, да ложь чужую покажет.'

    yaga 'Вот если готова ты с ним расстаться, то помогу тебе дорогу найти в Кощеево царство.'

    'Услышала Василиса просьбу Яги, да побледнела, и не от того, что перстень волшебный был,' 
    
    'а потому что единственной вещью он остался в память о сестре её, Марье, что была отдана в жены змею. И ведь знала же Яга об этом, и всё равно в дар перстень запросила.'

    'И так на Ягу глянула царевна, с обидою страшною, да сняла с руки перстень. Был подарен он Марье отцом с матерью в день её свадьбы, прежде чем забрал сестру змей из отчего дома.'

    'Год спустя Василиса и получила этот перстень, в напоминание о жизни сестры,  короткой, да славной.'

    mc 'Уколоть меня решила, Яга? Но так и быть, забирай.'

    yaga 'Больно легко ты с ним расстаешься, Василиса, не горюешь по сестре, аль не печалишься о том, что убила змея? Ведь не повинен он был в смерти сестры твоей.'

    yaga 'Если ты вернуть её намерена, то знай, что провожала я Марью в царство Кощеева, но обратно она не воротится. Да и нет её там уже давно, душа её светлее других была. Не с Кощеем она больше.'

    'Но не за сестрой отправляется царевна, а за богатствами, да судьбу испытать.' 
    
    'Помнила она, как сладко жили Змей и Марья, и без зависти была счастлива за них, да мечтала, что однажды и ей, с её холодным сердцем, тяжелой рукой да острым умом, найдется суженный.'

    mc 'Змей по своей вине мертв, - не уберег сестру мою, ту, которую так любил, которой о верности клялся. Милосердно с ним я поступила, а иначе бы сидеть ему в темнице до скончания времен.'

    mc 'А что не вернуть мне её, - сама знаю. Не за этим я прошу тебя о помощи.'

    yaga 'Много девок к Кощею просятся, да никто еще не возвращался, всех он в ящерок да птичек превращает. Но верится мне, но коль даже если не полюбит он тебя, иль сокровища ты его не получишь, встретимся мы вновь.'

    yaga 'И коль вернешься ко мне, есть одно предложение к тебе, царевна.'

    'И наклонилась она к царевне, да прошептала ей на ухо заветное предложение.'

    'В ответ кивнула девушка, давая свое безмолвное согласие.'

    yaga 'А теперь не стой столбом, Василиса - владычица царства вороньевых да змеиных, встань у печи, да слушай внимательно.'

    yaga 'Покуда жива ты, не могу я просто так пустить тебя в царство Кощея, должна ты сама открыть себе путь.'

    yaga 'Не вернуться тебе в мир живых, коль не готова ты пожертвовать миру мертвых себя. Всё, что угодно отдай, но с условием одним - ту часть твою, что едина с тобою.'

    'И топнула Яга ногой костлявой, да зазвенели колокольчики, что украшали ту самую ногу. Вспыхнул огонь в печи, ухнула птица где-то в лесной глуши, еще ярче загорелись искры в глазницах черепов зверей, да так ярко, словно полдень летний в самом разгаре.'

    'И выполнила царевна условие Яги, да опустила левую руку по запястье в печь, - не был огонь в печи горячим вовсе, а был холодным, как лёд.
    Видит Василиса, что не пламя это, а ручища, что тянутся к ней, да так много их, что и не видно, откуда они поднимаются.'
    
    'Вытащила Василиса руку, да глядит, что точь в точь она костяная, прям как нога у Яги, но присмотрелась царевна - и не костяная вовсе, а серебром блестит, словно изготовлена самым лучшим кузнецом.'

    'Боялась ею пошевелить Василиса, но одолело царевну любопытство. Повела она рукою и поняла, что та словно легче стала, и пальцы двигаются плавно так, как колосья на ветру колышутся.'

    yaga 'Вот теперь любая дверь тебе открыта в царство Кощея, Василиса.' 
    
    yaga 'Но знай одно, - проведешь с собой хоть одно живое существо, найду тебя, царевна, изрублю на мелкие куски, да скормлю зверям, а душу твою скитаться отправлю.'
    
    yaga 'Будешь путников несчастных пугать да покоя не найдешь.'

    mc 'Не нарушу указ твой, Яга, а ежели прокрадётся за мной зверь или человек, будь по твоему.'

    mc 'А на этом ли всё, Яга, - перстень, да рука моя? А как же напоить, да накормить, в бани попарить, и спать уложить?'

    'Улыбается царевна, больно быстро Яга её просьбу выполнила, да слишком просто всё. Хоть перстень и дорог ей, но память о сестре она в душе хранит. И не пугают испытания её перед целями, которые она выбрала.'


    'Смеётся в ответ Яга, знает, что каким бы не был исход путешествия царевны, он всё равно повесит её, и сложит она о ней новый сказ, и будет рассказывать добрым молодцам да красным девицам.'

    'О сокровищах неслыханных ли будет рассказ, аль о любви единственной, о смерти, или о жизни, - все зависит только от царевны.'

    yaga 'Василиса, душа твоя холодна, как и разум, и хоть жаждешь ты любви, желанию этому не затмить ум твой, не собьешься ты с пути, даже если зверь невиданный попытается сбить тебя с него.'

    'Слушает Василиса Ягу, да знает, что не путь к Кощею главное испытание, ни лес темный, ни зверь хищный, а сам владыка душ и сокровищ.'

    yaga 'А теперь ступай, больше нет у тебя забот в доме моём. Но пред тем как отправиться в путь, ответь мне на вопрос один.'

    mc 'Да что ж не ответить? Что знать ты хочешь, Яга?'

    mc 'Что на самом деле таится в игле Кощеевой? И хоть нет тут ответа верного, что тебе говорит душа твоя, Василиса?'

    menu:
        '1. Слыхала я, что не жизнь его там спрятана, а память о жизни прошлой, о любви ненайденной, да о судьбах погубленных. Говорят, что не помнит Кощей, что по силе не уступал он богам всевластным, но за лукавство и вероломный характер его был он сослан в царство подземное. С того дня лишь сокровища непомерные - его радость.':
            $ first_choice = 1

            mc '1. Слыхала я, что не жизнь его там спрятана, а память о жизни прошлой, о любви ненайденной, да о судьбах погубленных. Говорят, что не помнит Кощей, что по силе не уступал он богам всевластным, но за лукавство и вероломный характер его был он сослан в царство подземное. С того дня лишь сокровища непомерные - его радость.'


        '2. Правду говорят, что в игле жизнь Кощеева, да сломав её - не убить владыку царства мёртвого. Вышита иглой этой судьба его, но сломав её, не соткать судьбы новой.':
            $ first_choice = 2

            mc '2. Правду говорят, что в игле жизнь Кощеева, да сломав её - не убить владыку царства мёртвого. Вышита иглой этой судьба его, но сломав её, не соткать судьбы новой.'

        '3. Ходит среди народа молва, что не только жизнь спрятана в игле Кощея, от того так хитроумно запрятана она. Говорят, что игла укажет путь к настоящему его сокровищу.':
            $ first_choice = 3

            mc '3. Ходит среди народа молва, что не только жизнь спрятана в игле Кощея, от того так хитроумно запрятана она. Говорят, что игла укажет путь к настоящему его сокровищу.'

    yaga 'Есть правда в ответе твоем, царевна. А теперь отправляйся в путь. Воротишься ты или нет - покажет только время.'

    mc 'Прощай, Яга, и знай, ежели вернусь, то выполню наше соглашение.'

    'Вышла Василиса в сени, прошла снова чрез травы душистые, отворила дверь избы левой рукой да шагнула за порог.'

    jump act_2_the_path


label act_2_the_path:
    call transition('АКТ 2 - "Путь"')

    scene forest with dissolve

    'Вышла царевна, из избы Яги, спустилась по ступеням обратно на поляну, да подняла сапоги свои у дома оставленные, узором вышитые. Надела Василиса их и пошла куда ей сердце велит.'

    'Ни длинен, ни короток путь царевны был, да всё слышит она, как кто-то с ветки на ветку перелетает, да следит за ней.'

    'И обернулась дева черным вороном, взлетела к ветвям, около которых шум слышался. Схватила она птицу, аль зверя, да устремилась к земле.'

    'Ударились они оземь, обратно Василиса облик человеческий приняла, да прижала сапогом гостя непрошенного.'

    'Глядит Василиса, а это филин желтоглазый.'

    mc 'Слышу я, что следишь за мной с первых шагов по лесу мёртвому. Кто послал? Яга мне ль не доверяет, или страж Кощеев ты?'

    'Вырывается филин лесной, крыльями бьёт, да все тщетно, крепко прижала Василиса его к земле.'

    'Да не долго сопротивлялся филин, - знает он, что ежели вырвется, не ускользнуть ему от зоркого взгляда царевны.'

    'Обернулся филин, - и предстал перед Василисой юношей чернобровым, златоглазым, всем складен и ладен он, да видит царевна, обмануть пытается её, под лик человеческий маскируется.'

    'Взмахнула царевна левой рукой пред молодцем, - чары его развеяла.'

    'А лихо то непростое, краше остальных. Лишь хвост как у черта выдаёт его, да когти на руках звериные.'

    'И закричало лихо, голосом нечеловеческим, завыло жалобно так, и говорит царевне.'

    likho 'НЕ ЛИХО! НЕ ЛИХО! ЧЁРТ Я! ВЕДЬМА ТЫ БЕЗСОРОМНАЯ!'

    likho 'ПОГЛЯДИ НА МЕНЯ, НА ХВОСТ МОЙ, ДА КОГТИ ОСТРЫЕ!'

    'Стоит Василиса, на лихо глядит, да весело ей от того, что решил он, будто обмануть её может.'




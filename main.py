import telebot
from telebot import types
bot = telebot.TeleBot('5744057090:AAHfZvmwBQuJite_9li6ugzRxQnn3UPeu_Y')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Демалудын түрлері")
    item2 = types.KeyboardButton("Қызықты жерлер")
    item4 = types.KeyboardButton('Отели')
    item5 = types.KeyboardButton('Мейрамханалар')
    markup.add(item1, item2, item4, item5)
    photo = open('romero.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, f"Армысын, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>\nАстана туризм ботына қош келдініз!!", parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
        if message.text == 'Қызықты жерлер':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            mark = types.InlineKeyboardMarkup()
            back = types.KeyboardButton('Бастапқы мәзірге қайту')
            next = types.KeyboardButton('жалғастыру')
            markup.add(back, next)
            mark.add(types.InlineKeyboardButton("EXPO туралы нақты ақпарат", url="https://astana.citypass.kz/"))
            photo = open('expo.jpg', 'rb')
            bot.send_message(message.chat.id, "EXPO 2017")
            bot.send_photo(message.chat.id, photo, "Это Expo 2017, есть развлечения для детей, и можно погулять"
                                                   "Там не только для развлечений, и для экскурсий где "
                                                   "приходят люди из рахных стран чтобы посмотреть на технологии мира",
                           reply_markup=mark)
            bot.send_message(message.chat.id, "не шештіңіз?", reply_markup=markup)

        if message.text == 'жалғастыру':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            maup = types.InlineKeyboardMarkup()
            back = types.KeyboardButton('Бастапқы мәзірге қайту')
            xent = types.KeyboardButton('жалғастыруу')
            maup.add(types.InlineKeyboardButton("Нақты ақпарат осында",url="https://ru.wikipedia.org/wiki/%D0%91%D0%B0%D0%B9%D1%82%D0%B5%D1%80%D0%B5%D0%BA_(%D0%BC%D0%BE%D0%BD%D1%83%D0%BC%D0%B5%D0%BD%D1%82)"))
            iterek = open('iterek.jpg', 'rb')
            markup.add(back, xent)
            bot.send_message(message.chat.id, "Бәйтерек")
            bot.send_photo(message.chat.id, iterek, "Бәйтерек — Қазақстан астанасындағы монумент және бақылау мұнарасы",
                           reply_markup=maup)
            bot.send_message(message.chat.id, "не шештіңіз?", reply_markup=markup)

        if message.text == 'жалғастыруу':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ramm = types.InlineKeyboardMarkup()
            back = types.KeyboardButton('Бастапқы мәзірге қайту')
            next = types.KeyboardButton('жалғастыру_3')
            ramm.add(types.InlineKeyboardButton("Подробнее", url="https://e-history.kz/ru/news/show/4745"))
            museum = open('musek.jpg', 'rb')
            bot.send_message(message.chat.id, "Қазақстан Республикасынын ұлттық музейі")
            bot.send_photo(message.chat.id, museum , "\nМузей еліміздің Бас алаңы – Тәуелсіздік алаңында орналасқан. "
                                                     "1998 жылы халық бірлігі және ұлттық тарихы жылын өткізу бойынша "
                                                     "комиссияның кеңейтілген отырысында ҚР Тұңғыш президенті "
                                                     "Елбасы Нұрсұлтан Назарбаевтың елордада әлемнің түкпірінен "
                                                     "келген қонақтарға  қазақ халқының ежелгі дәуірден  бастап қазіргі "
                                                     "уақыта дейінгі бай тарихы таныстырылатын Ұлттық музей құру идеясы "
                                                     "туралы айтылған болатын. Музейдің құрылысы 2010 жылы басталып 2013 жылы аяқталды. ", reply_markup=ramm)
            markup.add(back, next)
            bot.send_message(message.chat.id, "что вы решили", reply_markup=markup)

        if message.text == 'жалғастыру_3':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ramm = types.InlineKeyboardMarkup()
            back = types.KeyboardButton('Бастапқы мәзірге қайту')
            next = types.KeyboardButton('Келесі')
            ramm.add(types.InlineKeyboardButton("Подробнее", url="https://e-history.kz/ru/news/show/4745"))
            museum = open('aljir.jpg', 'rb')
            bot.send_message(message.chat.id, "АЛЖИР мұражай-мемориалдық кешені")
            bot.send_photo(message.chat.id, museum, "Дәл осы жерде Отан сатқындар әйелдерінің әйгілі Ақмола лагері – <<АЛЖИР>> болды,\nонда әр жылдары 18 мыңнан астам\nәйел ұсталды. Кінәсі тек тұтқындалған, атылған халық\nжауларының әйелдері болған әйелдер.", reply_markup=ramm)
            markup.add(back, next)
            bot.send_message(message.chat.id, "жалғастырасын ба?", reply_markup=markup)

        if message.text == 'Келесі':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ramm = types.InlineKeyboardMarkup()
            back = types.KeyboardButton('Бастапқы мәзірге қайту')
            ramm.add(types.InlineKeyboardButton("Подробнее", url="https://e-history.kz/ru/news/show/4745"))
            museum = open('batyr.jpg', 'rb')
            bot.send_message(message.chat.id, "Кабанбай батыр кесенесі")
            bot.send_photo(message.chat.id, museum, 'Қабанбай батыр-XVIII ғасырда жоңғар жаулап алушыларына\nқарсы соғысқан атақты қолбасшы. Халық жауынгердің күшті\nболғаны соншалық, ол жылқыны иығына көтере алатынын\nайтты. Қару оның астында болды болу-салмағы 60-70 кг\nболатын толық металл алтыбұрышты найза, ол жаудың\nқалқанын да, өзін де тесіп өтті.  Батырдың шын аты-Ерасыл.\nОл Қабанбай есімін 1717 жылы Аягөз өзенінде болған\nшайқаста алған және ол-үздіксіз жауды алаңдататын дегенді білдіреді.', reply_markup=ramm)
            markup.add(back)
            bot.send_message(message.chat.id, "экскурсия аяқталды", reply_markup=markup)


        if message.text == 'Демалудын түрлері':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.InlineKeyboardMarkup(row_width=2)
            btn1 = types.InlineKeyboardButton('Караокие', callback_data='Caraoke')
            btn2 = types.InlineKeyboardButton('Серуендеу', callback_data='walk')
            btn3 = types.InlineKeyboardButton('ашық аспандағы кинотеатр', callback_data='Kino')
            ket = types.InlineKeyboardButton('Бастапқы мәзірге қайту')
            btn.add(btn1,btn2,btn3)
            markup.add(ket)
            bot.send_message(message.chat.id, "сіз демалудын қандай түрің тандайсыз??", reply_markup=btn)
            bot.send_message(message.chat.id, "немесе артқа барайық егер қаласаныз?", reply_markup=markup)

        if message.text == 'Бастапқы мәзірге қайту':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Демалудын түрлері")
            item2 = types.KeyboardButton("Қызықты жерлер")
            item3 = types.KeyboardButton('Отели')
            item4 = types.KeyboardButton('Мейрамханалар')
            markup.add(item1, item2, item3, item4)
            photo = open('romero.jpg', 'rb')
            bot.send_photo(message.chat.id, photo,
                           f"Армысын, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>\nАстана туризм ботына қош келдініз!!",
                           parse_mode='html', reply_markup=markup)


        if message.text == 'Отели':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.InlineKeyboardMarkup()
            btn2 = types.InlineKeyboardMarkup()
            btn3 = types.InlineKeyboardMarkup()
            btn4 = types.InlineKeyboardMarkup()
            ket = types.InlineKeyboardButton('Бастапқы мәзірге қайту ')
            btn1.add(types.InlineKeyboardButton("The Ritz-Carlton, Astana", url="https://www.ritzcarlton.com/ru/hotels/kazakhstan/astana#HOTEL"))
            btn2.add(types.InlineKeyboardButton("Hilton Hotel", url="https://www.hilton.ru/hotels/hilton-astana/#overview"))
            btn3.add(types.InlineKeyboardButton("The St. Regis Astana", url="https://e-history.kz/ru/news/show/4745"))
            btn4.add(types.InlineKeyboardButton("Отель Jt-Жумбактас", url="https://e-history.kz/ru/news/show/4745"))
            markup.add(ket)
            rc = open('RC_Astana.jpg', 'rb')
            hilton = open('Hilton.jpg', 'rb')
            jumba = open('jumba.jpg', 'rb')
            regis = open('regis.jpg', 'rb')

            bot.send_message(message.chat.id, "сізге назарынызға топ 4-отельдер көрсетілген", reply_markup=markup)
            bot.send_message(message.chat.id, "The Ritz-Carlton Astana")
            bot.send_photo(message.chat.id, rc, "The Ritz-Carlton Astana — Қазақстан астанасындағы алғашқы люкс қонақ үй. Мүмкін, Talan Towers кешенінде орналасқан қаланың ең буржуазиялық қонақ үйі.", reply_markup=btn1)

            bot.send_message(message.chat.id, "Hilton")
            bot.send_photo(message.chat.id, hilton, 'Hilton қонақ үй желісінде бүкіл әлем бойынша 4200-ден астам қонақүй бар. Қазақ Hilton Hotel"тамыр жайды" ', reply_markup=btn2)

            bot.send_message(message.chat.id, "Jumbaktas")
            bot.send_photo(message.chat.id, jumba, 'Сол жағалаудың қақ ортасында орналасқан Жұмбақтас\nқонақ үйі ең ірі сауда орталықтарынан, туристік\nорындардан, министрліктерден және банктерден жаяу\nқашықтықта орналасқан. Қаланың фонында ерекше\nсәулетімен ерекшеленетін қонақ үйдің сыртқы түрі\nерекше. Шексіз дала мен таулар өздерінің әсемдігімен,\nтуған жерлерімен кешеннің жанрлық безендірілуі мен\nөзіндік ерекшелігін анықтады. Холлдың ұлылығы\nшаңырақтың бейнесін – ортақ үйдің және барлық\nхалықтар үшін біртұтас Отанның символын көрсетеді.\nКөкпек шөптері, таза көлдер, мерекелік киіз үйлердің ақ\nкүмбездері, өрілген күміс әшекейлері бар қазақ сұлулары\nөсетін қауырсынды Дала кеңістігінің түрлі – түсті түстерін\nқонақүйдің кең дәліздерінде ұсынылған фотокартиналардан көруге болады. ', reply_markup=btn3)

            bot.send_message(message.chat.id, "The St. Regis Astana ")
            bot.send_photo(message.chat.id, regis,
                           'The St. Regis Astana елорданың өте әсем жерінде —\nЕсіл өзенінің бейбіт оң жағалауы мен қаланың қазіргі\nіскерлік бөлігінің түйіскен жерінде, орталық саябақта орналасқан',
                           reply_markup=btn4)
            bot.send_message(message.chat.id, "бастапқы мәзірге оралайық", reply_markup=markup)

        if message.text == 'Мейрамханалар':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.InlineKeyboardMarkup(row_width=2)
            btn1 = types.InlineKeyboardButton('қытайлық', callback_data='Asian')
            btn2 = types.InlineKeyboardButton('Европалық', callback_data='Eur')
            btn3 = types.InlineKeyboardButton('Ұлттық', callback_data='nati')
            ket = types.InlineKeyboardButton('Бастапқы мәзірге қайту ')
            markup.add(ket)
            btn.add(btn1,btn2,btn3)
            bot.send_message(message.chat.id, "қандай ұлттың мейрамханасын тандайсындар?", reply_markup=btn)
            bot.send_message(message.chat.id, "немесе қайтадан бас мәзірге оралайық", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'Kino':
            btn1 = types.InlineKeyboardMarkup()
            btn2 = types.InlineKeyboardMarkup()
            btn3 = types.InlineKeyboardMarkup()
            btn4 = types.InlineKeyboardMarkup()
            btn5 = types.InlineKeyboardMarkup()

            btn1.add(types.InlineKeyboardButton("Kinotün", url="https://www.instagram.com/kino.tun/"))
            btn2.add(types.InlineKeyboardButton("Sunset Insta", url="https://www.instagram.com/p/CeG2dulMIif/"))
            btn3.add(types.InlineKeyboardButton('Central Park Cinema', url='https://www.instagram.com/centralpark_cinema/'))
            btn4.add(types.InlineKeyboardButton('Cinema Park', url='https://www.instagram.com/cinemapark_astana'))
            btn5.add(types.InlineKeyboardButton('Уличный кинотеатр Abu Dhabi Plaza', url='https://www.instagram.com/abudhabiplaza.official/'))

            abu = open('kino/abu.jpg', 'rb')
            central = open('kino/central.jpg', 'rb')
            tun = open('kino/tun.jpg', 'rb')
            sun = open('kino/sun.jpg', 'rb')
            cinema = open('kino/cinema.jpg', 'rb')




            bot.send_message(call.message.chat.id, 'Сіз жұлдызды аспан астындағы көрпеге оралып, сүйікті фильміңізді '
                                                   'көресіз. Егер осы фразадан кейін ол бір жерде болса, міне, '
                                                   'елордадағы бес көше кинотеатрының таңдауы.')
            bot.send_message(call.message.chat.id, 'Abu Dhabi Plaza көше кинотеатры')
            bot.send_photo(call.message.chat.id, abu, 'Жазда Abu Dhabi Plaza - да ашық аспан астындағы кинотеатр жұмыс істейді. \nСОО-да төленген 5000 теңгелік чек үшін Сіз сөмке креслосын аласыз және арнайы аймаққа - төбеге, ұқыпты кесілген көгалдарға барасыз және экранның алдында орналасасыз. \nЧексіз сіз азық-түлік кортынан немесе дүкеннен көруге қосыла \nаласыз. 5 жасқа дейінгі балаларға кіру тегін.', reply_markup=btn5)

            bot.send_message(call.message.chat.id, 'Central Park Cinema')
            bot.send_photo(call.message.chat.id, central, 'Ағаштардың арасында орталық саябақтың қақ ортасында '
                                                          'Central Park Cinema көше кинотеатры орналасқан. '
                                                          'Ұйымдастырушылардың айтуынша, сізді масалар шағып алады '
                                                          'деп алаңдамайсыз — мұнда олар уланып, спреймен қамтамасыз '
                                                          'етілген. Азық-түлікті өзіңізбен бірге алып келуге немесе '
                                                          'жергілікті көше кафелерінен сатып алуға болады. '
                                                          'Сондай-ақ, әкімшілік османдықтар мен көрпелерді ұсынады', reply_markup=btn3)

            bot.send_message(call.message.chat.id, 'Cinema park')
            bot.send_photo(call.message.chat.id, cinema, ' Астанадағы алғашқы көше кинотеатры. Ашық аспан астындағы Кинотеатр Жетісу саябағында орналасқан.\n Мұнда күн сайын сағат 21.00 және 23.00-де екі сеанс өтеді. Кинотеатр 20 орынға арналған. \nЖұмсақ пуфтар, сапалы дыбыс және саябақтың жағымды атмосферасы сүйікті фильмдеріңізді көру үшін сиқырлы атмосфера жасайды. Салқын ауа-райында сізге жылы көрпе мен шай ұсынылады.', reply_markup=btn4)

            bot.send_message(call.message.chat.id, 'Kinotün')
            bot.send_photo(call.message.chat.id, tun, 'Kinotün Астананың ең жасыл саябақтарының бірі-Жерұйықта ашық ауада орналасқан.\nМұнда сізде биік шыршалар мен қайыңдар арасында таза ауа алуға және жақсы фильмді тамашалауға тамаша мүмкіндік бар. Фильм репертуары үш тілде ойналады. Киноның әр түрлі жанрлары бар.', reply_markup=btn1)


            bot.send_message(call.message.chat.id, 'Sunset Cinema')
            bot.send_photo(call.message.chat.id, sun, 'Sunset Cinema жазғы ашық кинотеатры қалалық пикник стилінде өткізілетіндігімен ерекше. '
                                                      'Аймақтың өзі әдемі безендірілген және жақсы демалу үшін де, '
                                                      'іс-шаралар, шеберханалар мен фотосессиялар үшін де қолайлы.', reply_markup=btn2)

        if call.data == 'walk':
            btn1 = types.InlineKeyboardMarkup()
            btn2 = types.InlineKeyboardMarkup()
            btn3 = types.InlineKeyboardMarkup()
            btn4 = types.InlineKeyboardMarkup()
            btn5 = types.InlineKeyboardMarkup()
            btn1.add(types.InlineKeyboardButton("Подробнее",
                                                url="https://astana.citypass.kz/ru/2021/08/09/most-atyrau-kopiri/"))

            btn2.add(types.InlineKeyboardButton("Подробнее", url="https://sxodim.com/astana/place/botanicheskij-sad"))

            btn3.add(types.InlineKeyboardButton("Подробнее", url="https://sxodim.com/astana/article/obzor-park-zhetysu"))

            btn4.add(types.InlineKeyboardButton("Подробнее", url="https://sxodim.com/astana/place/triatlon-park"))

            btn5.add(types.InlineKeyboardButton("Подробнее", url="https://sxodim.com/astana/place/botanicheskij-sad"))
            bridge = open('bridge.jpg', 'rb')
            botan = open('botan.jpg', 'rb')
            zheti = open('Gate_.jpg', 'rb')
            tri = open('tri.jpg', 'rb')
            nabka = open('nabka.jpg', 'rb')
            bot.send_message(call.message.chat.id, "мында топ 5 серуендеп қайтуға арналған жерлер берілген")
            bot.send_message(call.message.chat.id, "Атырау көпірі")
            bot.send_photo(call.message.chat.id, bridge, "2018 жылдың 1 шілдесінде Астанада жаңа жаяу жүргіншілер "
                                                         "көпірінің ашылуы өтті. Жаңа көпір Атырау облысы әкімдігінің "
                                                         "Елорданың 20 жылдық мерейтойына арналған сыйы болып табылады. "
                                                         "Көпірдің сырты Атырау облысының символы болып табылатын балық "
                                                         "таразысына ұқсайды, көпірдің сәндік құрылымы 2450 алюминий "
                                                         "жапырақшасынан тұрады, олардың әрқайсысы ерекше пішінге ие. "
                                                         "Сіз іштен өтіп бара жатқанда, сіз өзіңізді үлкен балықтың "
                                                         "ішінде жүргендей сезінесіз.",reply_markup=btn1)

            bot.send_message(call.message.chat.id, "Ботаникалық саябақ")
            bot.send_photo(call.message.chat.id, botan, '', reply_markup=btn2)

            bot.send_message(call.message.chat.id, "Жетісу саябағы")
            bot.send_photo(call.message.chat.id, zheti, 'Бұрынғы Арай саябағы 2018 жылы қайта құрылды. Саябақ оңтүстіктен '
                                                        'Сарайшық көшесімен, шығыстан Есіл өзенімен, батыстан және '
                                                        'солтүстіктен Шұбар шағынауданымен шектеседі. "Жетісу" саябағы-'
                                                        'Спорт және белсенді демалыс әуесқойлары үшін жұмақ. '
                                                        'Онда әртүрлі спорт алаңдары, соның ішінде скейтборд '
                                                        'пандустары және 1200 метрлік велосипед жолы бар. '
                                                        'Саябақтың орталық аллеясында Алматыдағыдай көптеген '
                                                        'субұрқақтар мен арқалары үлкен орындықтарды көруге болады.', reply_markup=btn3)

            bot.send_message(call.message.chat.id, "Triatlon саябағы")
            bot.send_photo(call.message.chat.id, tri, 'Саябақ қатысушыларды триатлон жарыстарына дайындау үшін салынған, '
                                                      'сондықтан мұнда спортпен шұғылдануға барлық жағдай жасалған. '
                                                      'Саябақтың аумағында арнайы жабыны бар үш футбол алаңы бар. '
                                                      'Саябақта спортпен шұғылданып қана қоймай, сонымен қатар жақсы '
                                                      'уақыт өткізуге болады: әдемі орындықтар, тығыз отырғызылған '
                                                      'ағаштар, көне шамдар — демалу үшін жағымды атмосфера жасайды.',
                                                       reply_markup=btn4)

            bot.send_message(call.message.chat.id, "Набережка")
            bot.send_photo(call.message.chat.id, nabka, 'Көбінесе жас түлектер күннің батуын осында қарсы алады. '
                                                        'Кешкі жағалау әсіресе балғын және әдемі.', reply_markup=btn5)

        if call.data == 'Caraoke':
            btn1 = types.InlineKeyboardMarkup()
            btn2 = types.InlineKeyboardMarkup()
            btn3 = types.InlineKeyboardMarkup()
            btn4 = types.InlineKeyboardMarkup()
            btn5 = types.InlineKeyboardMarkup()

            btn1.add(types.InlineKeyboardButton("Подробнее", url="https://www.instagram.com/millionaire.astana/"))

            btn2.add(types.InlineKeyboardButton("Подробнее", url="https://www.instagram.com/baobao.nur/?hl=ru"))

            btn3.add(types.InlineKeyboardButton("Maestro", url="https://www.instagram.com/maestro.karaoke.bar/"))

            btn4.add(types.InlineKeyboardButton("Brio", url="https://instagram.com/brio_karaoke"))

            btn5.add(types.InlineKeyboardButton("Подробнее", url="https://instagram.com/tofu_astana?igshid=snzx26icwzxo"))

            bao = open('caraoke/bao.jpg', 'rb')
            brio = open('caraoke/brio.jpg', 'rb')
            maestro = open('caraoke/maestro.jpg', 'rb')
            milion = open('caraoke/milion.jpg', 'rb')
            tosu = open('caraoke/tosu.jpg', 'rb')

            bot.send_message(call.message.chat.id, 'Астында астанадағы өте танымал караокелердің бірі көрсетілген')
            bot.send_message(call.message.chat.id, 'Караоке-клуб Brio')
            bot.send_photo(call.message.chat.id, brio, '"Brio" Караоке клубы-Астананың орталығындағы түнгі караоке клубы. '
                                                       'Кәсіби дыбыс инженерлері қонақтарға ұмытылмас сезім қалыптастыруға '
                                                       'көмектеседі.Караоке клубының айырмашылығы-бұл танымал хиттердің '
                                                       'таңдауымен, арнайы жеңіл музыкамен және түтінді толықтырумен би '
                                                       'үзілісін қамтамасыз ететін кешке арналған бағдарлама. Толығырақ '
                                                       'төменде Instagram сілтемесінен біле аласыз', reply_markup=btn4)

            bot.send_message(call.message.chat.id, 'Караоке-бар Maestro')
            bot.send_photo(call.message.chat.id, maestro, 'Караоке Астананың сол жағалауында орналасқан. '
                                                          'Мұнда 90 орындық жалпы зал бар. Әр жұма және сенбі сайын '
                                                          'Maestro караокесінде әнді вокалды-аспаптық ансамбльмен '
                                                          'сүйемелдеумен орындауға болады', reply_markup=btn3)

            bot.send_message(call.message.chat.id, 'Tofu')
            bot.send_photo(call.message.chat.id, tosu, 'Tofu Астана бірнеше бағытты біріктіреді. Мейрамхана: күндізгі '
                                                       'уақытта отбасылық және іскерлік түскі ас, бір шыны кофе '
                                                       'үзілістері және достарыңызбен тыныш түскі ас үшін. '
                                                       'Караоке: біздің қонақтарымыз үшін сыйымдылығы 15 '
                                                       'адамға дейін екі VIP караоке бөлмесі жабдықталған.' , reply_markup=btn5)

            bot.send_message(call.message.chat.id, 'Bao bao')
            bot.send_photo(call.message.chat.id, bao, 'Мейрамхана бар паназиялық тағамдар 16 адамға арналған караоке бар зал', reply_markup=btn2)

            bot.send_message(call.message.chat.id, 'milioner')
            bot.send_photo(call.message.chat.id, milion, 'Ең ауқымды караоке-клуб Астана қаласы. Бізде музыкамен\nөмір сүретін және вокалдық қабілеттерін көрсетуге дайын\nбарлық шығармашылық адамдарды біріктіретін үлкен\nмузыкалық кеңістік бар.  "MILLIONAIRE" өзінің талапшыл\nқонақтарына элиталық және бірегей VIP-залдарды ұсынады!\nБірегейлігі - олардың әрқайсысында танымал брендтердің\nерекше стилі және кез-келген адам сезіне алмайтын керемет\nатмосфера бар! Залдың барлық бөлшектеріндегі сән-салтанат.', reply_markup=btn1)



        if call.data == 'nati':
            mark = types.InlineKeyboardMarkup()
            maup = types.InlineKeyboardMarkup()
            ramm = types.InlineKeyboardMarkup()
            mark.add(types.InlineKeyboardButton("Нақытырақ instagram парақшысанан көре аласындар", url="https://www.instagram.com/satgrouprest/"))
            maup.add(types.InlineKeyboardButton("Нақтырақ instagram парақшысанан көре аласындар", url="https://astana.restolife.kz/banketnyi-zal/a-tilek/"))
            ramm.add(types.InlineKeyboardButton("Нақтырақ instagram парақшысанан көре аласындар", url="https://instagram.com/astau_restaurant/"))

            astau = open('kitchen/Astau.jpg', 'rb')
            arnau = open('kitchen/arnau.jpg', 'rb')
            akti = open('kitchen/aktilek.jpg', 'rb')

            bot.send_message(call.message.chat.id, 'мында топ 3 қазақтардын ұлттық ресторандары берілген')
            bot.send_message(call.message.chat.id, 'Astau restoraunt')
            bot.send_photo(call.message.chat.id, astau, ' 90 орындық жалпы зал, 7 адамға арналған VIP-кабина, 10-20 адамға арналған vip-аймақ бар. Жайлы қазақ ортасы, тамаша орналасуы. Акциялар жиі өткізіледі, мысалы -20% ас үйдің барлық мәзірінде ', reply_markup=mark)
            bot.send_message(call.message.chat.id, 'Arnau restoraunt')
            bot.send_photo(call.message.chat.id, arnau, 'Мейрамхананың аспаздық тұжырымдамасы-жоғары Қазақ ұлттық тағамдары, '
                                                        'талғампаз және үйдегідей дәмді. Ұлттық нақыштағы сәнді '
                                                        'интерьер өзінің жайлылығымен және әсемдігімен баурап алады, '
                                                        'ал қазақ халық аспаптарының әсем дыбысымен жанды музыка ерекше '
                                                        'көңіл-күй сыйлайды.  ', reply_markup=maup)

            bot.send_message(call.message.chat.id, 'Ak-tilek restoraunt')
            bot.send_photo(call.message.chat.id, akti, 'Ас үйде ұлттық тағам тұжырымдамасы бар. Еуропалық тағамдар да бар. '
                                                       'Балалар мәзірі бар. Банкет залы 250 адамға дейін сыяды.', reply_markup=ramm)

        if call.data == 'Asian':
            mark = types.InlineKeyboardMarkup()
            maup = types.InlineKeyboardMarkup()
            ramm = types.InlineKeyboardMarkup()

            mark.add(types.InlineKeyboardButton("инстаграмм парақшасынан өтіп көре аласындар", url="https://instagram.com/qingdao.astana/"))
            maup.add(types.InlineKeyboardButton("Озывты instagram парақшысанда қалдыра аласыздар",
                                                url="https://instagram.com/soluxe_hotel_astana/"))
            ramm.add(types.InlineKeyboardButton("Нақтырақ instagram парақшысанан көре аласындар",
                                                url="https://instagram.com/astau_restaurant/"))

            qing = open('kitchen/qingdao.jpg', 'rb')
            gw = open('kitchen/wg.jpg', 'rb')
            ct = open('kitchen/chtown.jpg', 'rb')
            bot.send_message(call.message.chat.id, 'мында топ 3 қытайдын ұлттық ресторандары берілген')
            bot.send_message(call.message.chat.id, 'qindao')
            bot.send_photo(call.message.chat.id, qing, "Шынайы қытай тағамдары, Қытайдан келген аспаз.\nЫдыс-аяқтар ащы, жартылай өткір және өте ащы болып бөлінеді.\nҚызықты тағамдарға назар аударыңыз - шелпек қосылған Гунбао сиыр еті ", reply_markup=mark)
            bot.send_message(call.message.chat.id, "Great Wall")
            bot.send_photo(call.message.chat.id, gw, "Орташа чек - 10.000 теңгеден бастап. Мейрамхананың\nөзінде шынайы атмосфера бар, кейде спектакльдер\nөткізіледі-мысалы, Аспан асты елінің халық билері.\nМұнда сіз нағыз шай рәсіміне қатыса аласыз\n", reply_markup=maup)
            bot.send_message(call.message.chat.id, "LАПША Chinatown")
            bot.send_photo(call.message.chat.id, ct, "қуырылған кальмар күрішін немесе БОК Чай мұхиттық\nсұлтанды қолданып көріңіз. Егер сіз үлкен бөлікті\nалғыңыз келсе, мәзірден сучуан үйрегін іздеңіз\nВегетариандық тағамдар бар..", reply_markup=ramm)

        if call.data == 'Eur':
            mark = types.InlineKeyboardMarkup()
            maup = types.InlineKeyboardMarkup()
            ramm = types.InlineKeyboardMarkup()
            mar = types.InlineKeyboardMarkup()
            kar = types.InlineKeyboardMarkup()

            mark.add(types.InlineKeyboardButton("инстаграмм парақшасынан өтіп көре аласындар",
                                                url="https://www.instagram.com/restoran_augustin/"))
            maup.add(types.InlineKeyboardButton("Озывты instagram парақшысанда қалдыра аласыздар",
                                                url="https://www.instagram.com/cabernet_restaurant/"))
            ramm.add(types.InlineKeyboardButton("Нақтырақ instagram парақшысанан көре аласындар",
                                                url="https://instagram.com/bootlegger_ast/"))
            mar.add(types.InlineKeyboardButton("Нақтырақ instagram парақшысанан көре аласындар",
                                                url="https://astana.restolife.kz/restoran/the-continental/instagram/"))
            kar.add(types.InlineKeyboardButton("Нақтырақ instagram парақшысанан көре аласындар",
                                                url="https://www.instagram.com/zina_restaurant/"))

            augost = open('kitchen/augost.jpg', 'rb')
            conti = open('kitchen/conti.jpg', 'rb')
            echo = open('kitchen/caber.jpg', 'rb')
            zina = open('kitchen/zina.jpg', 'rb')
            boot = open('kitchen/boot.jpg', 'rb')

            bot.send_message(call.message.chat.id, 'астында Астанадағы топ 5 Европейлық мейрамханалар берілген')
            bot.send_message(call.message.chat.id, 'Augostin')
            bot.send_photo(call.message.chat.id, augost, 'Августин-ескі Еуропаның ең жақсы дәстүрлерінде жасалған\nмейрамхана. Ол ескі классикалық интерьермен және\nфранцуз аспазшысы Жан-Филипп Гоместің көптеген\nтағамдары мен тағамдарымен, сондай-ақ сыраның әсерлі\nассортиментімен ерекшеленеді. Біз "Августинді" үлкен, тату\nкомпания үшін тамаша демалыс орны ретінде ұсынамыз.', reply_markup=mark)

            bot.send_message(call.message.chat.id, 'Continental')
            bot.send_photo(call.message.chat.id, conti, 'The Continental-да сіз еуропалық тағамдарға тапсырыс бере\nаласыз, әсіресе мұнда стейктерді сынап көру ұсынылады!\nБар мәзірінде коктейльдер мен алкогольдік сусындардың\n үлкен таңдауы бар, олардың арасында Сіз премиум алкогольді таба аласыз. Мұнда үнемі оқиғалар өткізіліп тұрады, олардың арасында стенд-ап қойылымдары және тірі топтардың тірі қойылымдары бар.',  reply_markup=mar)

            bot.send_message(call.message.chat.id, 'Cabernet Club')
            bot.send_photo(call.message.chat.id, echo, 'Мәзірде еуропалық тағамдар мен шараптардың үлкен ассортименті '
                                                       'бар. Таңдалған шарап сортында сіз устрица, грильдегі дорадо, '
                                                       'барбекю қабырғалары және басқа да тартымды тағамдар түріндегі '
                                                       'лайықты компанияны таба аласыз.', reply_markup=maup)

            bot.send_message(call.message.chat.id, 'Bootlegger')
            bot.send_photo(call.message.chat.id, boot, 'Мекеменің мәзірінде еуропалық тағамдар бар.Залда\nжұма күндері жанды музыка ойналады. Жабық\nМерекелер үшін Vip зал бар. Мейрамхананың\nинтерьері ағылшын стилінде жасалған.', reply_markup=ramm)

            bot.send_message(call.message.chat.id, 'Zina')
            bot.send_photo(call.message.chat.id, zina, 'Мейрамханада тағамдар тірі отта және пештегі емен бөренелерінде дайындалады. Сіз сондай-ақ вегетариандық тағамдарды, арнайы шайларды және таңғы астың үлкен таңдауын таба аласыз. Толығырақ сипаттаманың астындағы сілтемеде танысуға болады', reply_markup=kar)

bot.polling(none_stop=True, interval=0)

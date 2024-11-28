from aiogram import Bot, Dispatcher, executor, types
import settings

bot = Bot(settings.APY_KEY)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет, в этом боте представлены интересные, простые рецепты очень вкусных блюд. Чтобы вывести список рецептов нажмите сюда -> /rez.')

@dp.message_handler(commands=['rez'])
async def call(message: types.Message):
    markup = create_markup()
    but = types.InlineKeyboardMarkup()
    but.add(types.InlineKeyboardButton('>>',url='https://www.russianfood.com/recipes/bytype/?fid=791#rcp_list'))
    await message.answer('Ещё больше интересных рецептов, очень вкусных блюд, здесь!', reply_markup=but)
    await message.answer('Выберите рецепт (название блюда указана на самой кнопке):',  reply_markup=markup)



def create_markup(show_back_button=False):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Домашние сырные палочки', callback_data='get_text_1'))
    markup.add(types.InlineKeyboardButton('Пицца на сковороде', callback_data='get_text_2'))
    markup.add(types.InlineKeyboardButton('Хоткейки', callback_data='get_text_3'))
    markup.add(types.InlineKeyboardButton('Ленивый хачапури на сковороде', callback_data='get_text_4'))
    markup.add(types.InlineKeyboardButton('Корн-доги',  callback_data='get_text_5'))
    markup.add(types.InlineKeyboardButton('Рулет "Баунти"',  callback_data='get_text_6'))
    markup.add(types.InlineKeyboardButton('Чипсы в микроволновке',  callback_data='get_text_7'))
    markup.add(types.InlineKeyboardButton('Закусочные слойки с сыром и ветчиной',  callback_data='get_text_8'))
    markup.add(types.InlineKeyboardButton('Шаурма в домашних условиях',  callback_data='get_text_9'))
    markup.add(types.InlineKeyboardButton('Чебуреки из слоёного теста',  callback_data='get_text_10'))
    if show_back_button:
        markup.add(types.InlineKeyboardButton('<<', callback_data='back'))
    return markup

@dp.callback_query_handler(text='get_text_1')
async def send_txt_1(callback_query: types.CallbackQuery):
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('Вернуться к рецептам', callback_data='back'))
        await callback_query.answer()
        photo_url1 = 'https://img1.russianfood.com/dycontent/images_upl/248/sm_247393.jpg'
        text1 = ('Продукты: \n Сыр твердый - 300 г \n Яйцо - 1 шт. \n Мука - 30 г (1 ст. ложка с горкой) \n Масло растительное - 70 мл \n \n Поэтапно процессы готовки: \n \n 1.Приготовим продукты для сырных палочек. \n \n  2.Сыр натереть на мелкой терке, добавить муку, яйцо. \n Перемешать. \n Сформировать сырные палочки. \n \n 3.Обжарить их в растительном масле до золотистого цвета. \n \n Сырные палочки готовы! \n Приятного аппетита! ')
        await bot.send_photo(chat_id=callback_query.from_user.id, photo = photo_url1, caption=text1, reply_markup=markup1)
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)


@dp.callback_query_handler(text='get_text_2')
async def send_txt_1(callback_query: types.CallbackQuery):
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('Вернуться к рецептам', callback_data='back'))
        await callback_query.answer()
        photo_url2 = 'https://img1.russianfood.com/dycontent/images_upl/175/sm_174367.jpg'
        text2 = 'Продукты: \n Яйца - 3 шт. \n Майонез - 5 ст. л. \n Мука - 5 ст. л. \n Соль - по вкусу \n Колбаса \n Сыр \n Помидор\n Огурцы соленые \n Лук репчатый \n Чеснок \n Кетчуп \n \n 1. Чтобы приготовить жидкое тесто для пиццы, хорошо перемешайте с помощью венчика яйца, майонез, муку и немного соли. \n \n 2.Вылейте тесто в сковороду (с антипригарным покрытием), в которой будет готовиться пицца. \n Кетчуп аккуратно распределите его по поверхности теста. \n \n 3.Овощи и колбасу нарежьте небольшими кусочками или \n кружочками (кому как нравится) и в произвольном порядке разложите на тесто. \n \n 4.Сверху, не скупясь, \n присыпьте все тертым сыром. \n \n 5.Поставьте сковороду с "ленивой" пиццей на медленный огонь и накройте крышкой. \n Выпекается пицца на сковороде примерно 10 минут (проверяйте готовность теста) \n \n Вкусная и ароматная, домашняя пицца на сковороде готова! \n Приятного аппетита!'
        await bot.send_photo(chat_id=callback_query.from_user.id, photo = photo_url2, caption=text2, reply_markup=markup1)
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)

@dp.callback_query_handler(text='get_text_3')
async def send_txt_1(callback_query: types.CallbackQuery):
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('Вернуться к рецептам', callback_data='back'))
        await callback_query.answer()
        photo_url3 = 'https://img1.russianfood.com/dycontent/images_upl/413/sm_412021.jpg'
        text3 = 'Продукты: \n Молоко - 200 мл \n Яйца - 2 шт. \n Сахар - 80 г \n Сахар - 80 г \n Разрыхлитель - 7 г \n Ванилин - 1 щепотка \n или ванильный сахар - 1-2 ч. ложки \n \n 1.Подготовить продукты по списку. \n \n 2.В глубокой миске соединить яйца, сахар и ванилин (или ванильный сахар). \n \n 3.Хорошо взбить венчиком или миксером до образования лёгкой пены. \n \n 4.Влить молоко и перемешать. \n \n 5.Всеять через мелкое сито муку и разрыхлитель. \n \n 6.Хорошо перемешать до однородности. \n Тесто должно получиться довольно густым и стекать с ложки или венчика толстой струйкой. \n \n 7.Сухую сковороду с антипригарным покрытием хорошо разогреть на среднем огне. \n Налить в сковороду примерно 2 ст. ложки теста, формируя круглый блинчик.'
        text_3 = '\n \n 8.Жарить хоткейк на среднем огне сперва с одной стороны 2-3 минуты, пока сверху он не станет матовым и на поверхности не появятся пузырьки. \n Затем перевернуть хоткейк и жарить ещё примерно 1-2 минуты (можно накрыть сковороду крышкой). \n Таким же образом пожарить все остальные хоткейки. \n \n Готовые хоткейки сложить стопочкой и подавать к столу, по желанию дополнив сметаной, \n мёдом, любыми сиропами или соусами на свой вкус. \n Приятного аппетита!'
        await bot.send_photo(chat_id=callback_query.from_user.id, photo = photo_url3, caption=text3)
        await bot.send_message(chat_id=callback_query.from_user.id, text=text_3, reply_markup=markup1)

@dp.callback_query_handler(text='get_text_4')
async def send_txt_1(callback_query: types.CallbackQuery):
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('Вернуться к рецептам', callback_data='back'))
        await callback_query.answer()
        photo_url4 = 'https://img1.russianfood.com/dycontent/images_upl/453/sm_452300.jpg'
        text4 = 'Продукты: \n Сыр сулугуни (или другой) – 150-250 г (чем больше сыра, тем вкуснее) \n Мука – 120-130 г (1 стакан объёмом 200 мл) \n Молоко – 200 мл (1 стакан) \n Яйцо – 1 шт. \n Сахар – 0,5 ч. ложки \n Соль – по вкусу (в зависимости от солености сыра) \n Разрыхлитель – 0,5 ч. ложки \n Масло сливочное (по желанию) – маленький кусочек \n \n 1.В миске смешать яйцо, соль, сахар, молоко, муку и разрыхлитель. Перемешать венчиком. \n \n 2.Туда же натереть на средней тёрке сыр сулугуни (можно использовать любой другой сыр, который хорошо плавится). \n \n 3.Сковороду (у меня диаметром 26 см) хорошо разогреть, смазать тонким слоем растительного масла. \n Вылить в сковороду тесто. \n \n 4.Жарить сырную лепёшку под закрытой крышкой на маленьком огне 7-8 минут, пока тесто сверху не схватится \n \n 5.Аккуратно перевернуть лепёшку и жарить с другой стороны 2-3 минуты, до румяности. \n \n 6.Ещё горячую сырную лепёшку можно смазать сливочным маслом. \n \n Приятного аппетита!'
        await bot.send_photo(chat_id=callback_query.from_user.id, photo = photo_url4, caption=text4, reply_markup=markup1)
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)

@dp.callback_query_handler(text='get_text_5')
async def send_txt_1(callback_query: types.CallbackQuery):
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('Вернуться к рецептам', callback_data='back'))
        await callback_query.answer()
        photo_url5 = 'https://img1.russianfood.com/dycontent/images_upl/266/sm_265013.jpg'
        text5 = 'Продукты: \n Сосиски - 350 г \n Яйцо - 1 шт. \n Мука пшеничная - 100 г \n Мука кукурузная - 100 г \n Разрыхлитель - 1/2 ч. л. \n Молоко - 50-70 мл (смотрите по консистенции теста) \n Соль - 1/3 ч. л. \n Сахар - 1/2 ч. л. с горкой \n Масло растительное - для фритюра \n \n 1.Чтобы приготовить корн-доги, подготовить продукты. \n Для рецепта берите свои любимые вкусные сосиски. \n Если дома не нашли кукурузную муку, ее можно заменить пшеничной и сделать кляр только из пшеничной муки, будет тоже очень вкусно. \n \n 2.Смешиваем сухие ингредиенты в емкости с высокими стенками, чтобы в дальнейшем было легко окунать сосиски.'
        text_5 = '\n \n 3.Добавляем яйцо, перемешиваем, вливаем молоко до получения очень густого теста. \n \n 4. Сосиски предварительно обваливаем в муке. \n \n 5.Прокалываем каждую сосиску шпажкой и окунаем в тесто полностью, \n чтобы верхняя часть шпажки тоже покрылась тестом. \n \n 6.Разогреваем фритюр до 150-170 градусов, обжариваем сосиски в тесте, \n вращая шпажки, чтобы корн-доги равномерно зарумянились \n \n Подаем с любимыми соусами и наслаждаемся!'
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_url5, caption=text5)
        await bot.send_message(chat_id=callback_query.from_user.id, text=text_5, reply_markup=markup1)
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)

@dp.callback_query_handler(text='get_text_6')
async def send_txt_1(callback_query: types.CallbackQuery):
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('Вернуться к рецептам', callback_data='back'))
        await callback_query.answer()
        photo_url6 = 'https://img1.russianfood.com/dycontent/images_upl/675/sm_674036.jpg'
        text6 = 'Продукты: \n Печенье песочное – 300 г \n Масло сливочное (размягчённое) – 200 г \n Сахарная пудра – 100 г \n  Какао-порошок – 25 г (3 ст. ложки) \n Сахар – 60 г \n Кокосовая стружка – 40 г \n Вода (кипяток) – 50 мл \n \n 1.Подготавливаем продукты. \n Сливочное масло предварительно достаём из холодильника, оно должно размягчиться. \n \n 2.В небольшую мисочку всыпаем сахар, заливаем кипятком. Перемешиваем до тех пор, пока сахар не растворится. Остужаем получившийся сироп. \n \n 3.Печенье натираем на мелкой тёрке \n \n 4.В миску с крошкой печенья добавляем какао-порошок. Перемешиваем \n \n 5.К смеси печенья и какао-порошка добавляем остывший сироп. '
        text_6 = '\n \n 6.Добавляем 100 г размягчённого сливочного масла. \n \n 7.Замешиваем мягкое гладкое "тесто". \n \n 8.Оставшееся размягчённое сливочное масло соединяем в отдельной миске с кокосовой стружкой и сахарной пудрой \n \n 9.Перемешиваем миксером масляно-кокосовую начинку до однородности и гладкости. \n \n 10.Рабочую поверхность застилаем пищевой плёнкой. Выкладываем шоколадное "тесто" на плёнку и раскатываем в прямоугольный пласт (23х32 см) толщиной примерно 0,3-0,4 см. \n \n 11.По всей поверхности теста равномерно распределяем масляно-кокосовую начинку. \n \n 12.Аккуратно сворачиваем плотный рулет, помогая себе плёнкой. \n \n 13.Свёрнутый рулет заворачиваем в пищевую плёнку и отправляем в холодильник примерно на 40-60 минут. \n \n 14.Затем извлекаем рулет из холодильника, освобождаем от плёнки и острым ножом нарезаем небольшими порционными кусочками. \n \n 15.Выкладываем кусочки рулета на тарелку и подаём к столу. \n \n Приятного аппетита!'
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_url6, caption=text6)
        await bot.send_message(chat_id=callback_query.from_user.id, text=text_6, reply_markup=markup1)
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)

@dp.callback_query_handler(text='get_text_7')
async def send_txt_1(callback_query: types.CallbackQuery):
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('Вернуться к рецептам', callback_data='back'))
        await callback_query.answer()
        photo_url7 = 'https://img1.russianfood.com/dycontent/images_upl/264/sm_263208.jpg'
        text7 = 'Продукты: \n Картофель – 2 шт. \n Паприка сладкая молотая - по вкусу \n Соль - по вкусу \n \n 1.Картофель нарезаем тонкими ломтиками. Я буду использовать для этого овощерезку. Вы можете делать это чем угодно, даже ножом. \n \n 2.Промываем ломтики картошки в воде, чтобы избавить её от лишнего крахмала. \n \n 3.При помощи бумажного полотенца избавляем картофель от лишней влаги. \n \n 4.На тарелку кладем сухое бумажное полотенце и выкладываем на него ломтики картошки так, чтобы они не касались друг друга. Добавляем соль и сладкую паприку (или другие специи, на Ваш вкус). \n \n 5.Отправляем тарелку с картошкой в микроволновку на 2 минуты при мощности 800 ватт.Через 2 минуты переворачиваем картофельные чипсы на другую сторону и снова помещаем их на 2 минуты в микроволновую печь. \n \n Домашние чипсы в микроволновке готовы. \n Приятного аппетита!'
        await bot.send_photo(chat_id=callback_query.from_user.id, photo = photo_url7, caption=text7, reply_markup=markup1)
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)

@dp.callback_query_handler(text='get_text_8')
async def send_txt_1(callback_query: types.CallbackQuery):
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('Вернуться к рецептам', callback_data='back'))
        await callback_query.answer()
        photo_url8 = 'https://img1.russianfood.com/dycontent/images_upl/717/sm_716868.jpg'
        text8 = 'Продукты: \n Тесто слоёное - 330 г \n Сыр твёрдый - 100 г (8 ломтиков) \n Ветчина - 100 г (8 ломтиков) \n Яйцо - 1 шт. \n Кунжут чёрный (семена) - 10 г \n \n 1.Подготовьте продукты. Слоёное тесто предварительно разморозьте.Ветчину и твёрдый сыр лучше брать уже нарезанные слайсами.Кунжут можно заменить семенами тмина или семечками.Включите духовку разогреваться до 180 градусов. \n \n 2.Слоёное тесто разложите на пергаменте. \n \n 3.На одну половину теста выложите тонко нарезанные ломтики сыра. \n \n 4. На сыр выложите тонко нарезанную ветчину. \n \n 5.Накройте сыр и ветчину второй половиной теста. '
        text_8 = '\n \n Острым ножом или круглым ножом для пиццы разрежьте получившийся прямоугольник на 4 полоски, равные по ширине. \n \n 6.Затем каждую полоску разрежьте на 4-5 частей. Получаются квадраты со стороной около 3-4 см. \n \n 7.Яйцо вбейте в глубокую тарелку. Вилкой перемешайте белок и желток. \n \n 8.Кисточкой смажьте поверхность теста взбитым яйцом - это придаст готовым слойкам аппетитный блеск. \n \n 9.Сверху слоёные квадратики присыпьте семенами кунжута. \n \n 10.Переложите тесто вместе с пергаментом в форму для выпечки или на противень. \n \n 11.Выпекайте закусочные слойки в разогретой до 180 градусов духовке 25-30 минут, до румяности (зависит от особенностей вашей духовки). \n \n 12.Аккуратно отделите горячие закусочные слойки с сыром и ветчиной одну от другой и выложите на тарелку. \n \n Такая закуска идеальна на фуршетный стол, в качестве перекуса на природу или в школу. \n Приятного аппетита!'
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_url8, caption=text8)
        await bot.send_message(chat_id=callback_query.from_user.id, text=text_8, reply_markup=markup1)
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)

@dp.callback_query_handler(text='get_text_9')
async def send_txt_1(callback_query: types.CallbackQuery):
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('Вернуться к рецептам', callback_data='back'))
        await callback_query.answer()
        photo_url9 = 'https://img1.russianfood.com/dycontent/images_upl/151/sm_150561.jpg'
        text9 = 'Продукты: \n Лаваш тонкий - 4 шт. \n Филе куриное - 2 шт. \n Картофель - 4 шт. \n Морковка корейская - 100 г. \n Сыр твёрдый - 150 г. \n Соль - 1,5 г \n Специи - по вкусу \n Масло растительное - 50 г. \n Кетчуп - 1 ст.л. \n Майонез - 1 ст.л. \n Соус соевый - 5 г. \n Чеснок - 1 зубчик \n \n 1.Чтобы куриное филе было максимально сочным, нарезаем его на крупные слайсы под углом 45 градусов. Если нарезать его мелкими кусочками, то при обжаривании филе может стать сухим и невкусным. \n \n 2.Отправляем филе в миску, добавляем специи и соль. Чтобы специи хорошо распределились вливаем растительное масло. Перемешиваем руками. \n \n 3.Куриное филе обжариваем на растительном масле до готовности, но стараемся не пересушить. Чтобы проверить готовность мяса, нужно проткнуть его ножом. \n Если выделяется прозрачный сок - куриное филе готово! \n \n 4.Пока жарится филе, картофель очищаем от кожуры, нарезаем брусочками и выкладываем на сковороду с растительным маслом. \n \n 5.Обжариваем картофель до золотистой корочки. '
        text_9 = '\n \n 6.Приступаем к приготовлению соуса. В миске соединяем кетчуп и майонез в равных количествах, добавляем соевый соус и чеснок, выдавленный через пресс. \n \n 7.Перемешиваем ложкой. Соус для куриной шаурмы готов. \n \n 8.Сыр натираем на крупной тёрке. \n \n 9.Готовое куриное филе нарезаем произвольным образом. \n \n 10.Разворачиваем лаваш. В центр выкладываем картофель и куриное филе. Поливаем соусом. \n \n 11.Сверху посыпаем морковкой и тёртым сыром, снова поливаем соусом. \n \n 12.Подворачивая края к середине, заворачиваем начинку в лаваш. \n \n Домашняя шаурма с курицей готова. Запекаем шаурму в духовке, на гриле или воспользуемся вафельницей, как в нашем случае.'
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_url9, caption=text9)
        await bot.send_message(chat_id=callback_query.from_user.id, text=text_9, reply_markup=markup1)
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)

@dp.callback_query_handler(text='get_text_10')
async def send_txt_1(callback_query: types.CallbackQuery):
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('Вернуться к рецептам', callback_data='back'))
        await callback_query.answer()
        photo_url10 = 'https://img1.russianfood.com/dycontent/images_upl/722/sm_721126.jpg'
        text10 = 'Продукты: \n Тесто слоёное дрожжевое - 450 г \n Фарш мясной (у меня свинина + куриное филе) - 330 г \n Лук репчатый - 100 г \n Лук зелёный - 20 г \n Вода (в фарш) - 50 мл \n Соль - по вкусу \n Перец чёрный молотый - по вкусу \n Мука (для работы с тестом) - 25 г \n Масло растительное рафинированное - 100 мл\n\n1.Подготавливаем необходимые продукты.Тесто предварительно вынимаем из морозильной камеры.\n\n2.Репчатый лук очищаем и нарезаем маленькими кубиками.Зелёный лук мелко нарезаем.\n\n3.В фарш добавляем репчатый и зелёный лук. соль и молотый перец.\n\n4.Перемешиваем до однородности.\n\n5.Затем вливаем воду. Перемешиваем. Воды может понадобиться чуть больше или меньше, в зависимости от влажности фарша. Фарш должен получиться сочным, но хорошо держать форму.Фарш в миске накрываем и помещаем в холодильник на 15-20 минут.'
        text__10 = '\n\n6.Оттаявшее тесто выкладываем на присыпанную мукой поверхность. У меня два листа слоеного теста размером 10х29 см.\n\n7.Раскатываем лист теста в тонкий пласт, толщиной около 2 мм. У меня получились размеры пласта - 25х51 см.\n\n8.Затем разрезаем раскатанный пласт теста на 3 одинаковых части. Размер каждой части - 17х25 см. \n\n9.Каждую часть теста складываем пополам.\n\n10.Накладываем все три заготовки одна на другую.\n\n11.И ножом (можно накрыть тарелкой) обрезаем два угла со стороны, противоположной сгибу.\n\n12.Получаются вот такие полукруглые заготовки.'
        text_10 = '\n\n13.Из одного листа получилось 3 штуки.\n\n14.Точно так же формируем ещё 3 заготовки из второго листа теста. Всего получилось 6 заготовок. При таком способе формирования чебуреков тесто расходуется очень экономно, лишнего теста.\n\n15.Раскрываем получившуюся заготовку и на одну половинку теста выкладываем 1/6 часть фарша. Края теста (где нет фарша) слегка смачиваем водой.\n\n16.Хорошо слепляем края теста, формируем чебурек.\n\n17.Края можно обрезать фигурным ножом для чебуреков или запечатать вилкой.\n\n18.В сковороде хорошо разогреваем большое количество растительного масла. Выкладываем чебуреки на сковороду.\n\n19.Обжариваем чебуреки на среднем огне примерно по 4-5 минут с каждой стороны, до золотистого цвета.\n\n20.Готовые чебуреки сперва выкладываем на бумажное полотенце, чтобы впиталось лишнее масло.\n\nПриятного аппетита!'
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_url10, caption=text10)
        await bot.send_message(chat_id=callback_query.from_user.id, text=text__10)
        await bot.send_message(chat_id=callback_query.from_user.id, text=text_10, reply_markup=markup1)
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)

@dp.callback_query_handler(text='back')
async def back(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await bot.send_message(callback_query.from_user.id, 'Другие рецепты:', reply_markup=create_markup())
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)



if __name__ == '__main__':
    executor.start_polling(dp)

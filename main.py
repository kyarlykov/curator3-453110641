import telebot

bot = telebot.TeleBot('7764614646:AAFunoZPqtMHORFW8ryD0iEJQEh-4waxNzw')


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id,
                     '*Приветствую тебя в чат-боте Славных!*\n\n'
                     'Чтобы узнать, какие команды можно использовать, напиши _/help_',
                     parse_mode='Markdown')


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id,
                     '*Команды для использования:*\n\n'
                     '_/homegroup_ - запись на домашнюю группу\n'
                     '_/faq_ - информация о нас и о христианском движении\n',
                     parse_mode='Markdown')


@bot.message_handler(commands=['faq'])
def faq_command(message):
    bot.send_message(message.chat.id,
                     'Молодёжное служение Церкви Славы Божьей - это место, где ты можешь:\n\n'
                     '- получить ответы на те вопросы, которые беспокоят тебя;\n'
                     '- научиться слушать Бога и следовать за Ним;\n'
                     '- принять Его любовь и милость в свою жизнь;\n'
                     '- научиться пророчествовать, исцелять и помогать людям;\n'
                     '- поучаствовать в интересных мероприятиях, семинарах и тренингах;\n'
                     '- общаться с единомышленниками и наставниками.\n\n'
                     'Чтобы узнать о нас побольше,'
                     'переходи в [сообщество ВКонтакте](https://vk.com/gloriousglory)'
                     ' или [группу Телеграмм](https://t.me/slavnyye)',
                     parse_mode='Markdown')


@bot.message_handler(commands=['homegroup'])  # команда хоумгруп
def homegroup_command(message):
    bot.send_message(message.chat.id,
                     'Чтобы записаться на домашку, выбери служителя:\n\n'
                     '_Артем Рихтер_\n'
                     '_Дмитрий Колбасов_\n' 
                     '_Илья Макаров_',
                     parse_mode='Markdown')


@bot.message_handler(content_types=['text'])
def check(message):
    answer = message.text.lower()
    if answer.lower() == 'артем рихтер':
        bot.reply_to(message,
                     'Домашняя группа Артема Рихтера проводится на м.Окская по средам в 19:00\n'
                     'тел. +7 999 999 99 99',
                     parse_mode='Markdown')
    elif answer.lower() == 'дмитрий колбасов':
        bot.reply_to(message,
                     'Домашняя группа Дмитрия Колбасова проводится на м.Лефортово по средам в 19:00\n'
                     'тел. +7 888 888 88 88',
                     parse_mode='Markdown')
    elif answer.lower() == 'илья макаров':
        bot.reply_to(message,
                     'Домашняя группа Ильи Макарова проводится на м.Кантемироваская по четвергам в 19:00\n'
                     'тел. +7 777 777 77 77',
                     parse_mode='Markdown')
    else:
        bot.reply_to(message,
                     'Пожалуйста, напишите верно имя и фамилию выбранного вами служителя',
                     parse_mode='Markdown')


bot.infinity_polling(none_stop=True)

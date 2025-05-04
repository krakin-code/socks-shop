import telebot
from telebot import types


# === ВСТАВЬ СВОЙ ТОКЕН БОТА ===
TOKEN = '7614790990:AAENb71fHOGtlNxiLoiBaplKN0mBy5kCPwc'

bot = telebot.TeleBot(TOKEN)

# === Главное меню ===
def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🧦 Продукция")
    btn2 = types.KeyboardButton("🚚 Доставка")
    btn3 = types.KeyboardButton("🔔 Подписка")
    btn4 = types.KeyboardButton("ℹ️ Информация о магазине")
    btn5 = types.KeyboardButton("📝 Отзывы")
    markup.add(btn1, btn2)
    markup.add(btn3)
    markup.add(btn4, btn5)
    bot.send_message(message.chat.id, "Добро пожаловать в магазин носков! Выберите раздел:", reply_markup=markup)

# === Стартовое сообщение ===
@bot.message_handler(commands=['start'])
def start(message):
    main_menu(message)

# === Обработка сообщений ===
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "🧦 Продукция":
        send_products(message)
    elif message.text == "🚚 Доставка":
        send_delivery_info(message)
    elif message.text == "🔔 Подписка":
        send_subscription_info(message)
    elif message.text == "ℹ️ Информация о магазине":
        send_shop_info(message)
    elif message.text == "📝 Отзывы":
        send_reviews(message)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите пункт из меню.")

# === Раздел "Продукция" ===
def send_products(message):
    bot.send_message(message.chat.id, "Вот наша продукция! https://t.me/tesrttiks_bot/socks_shop")
    # === ЗДЕСЬ ВСТАВЬ ССЫЛКУ НА МИНИ-ПРИЛОЖЕНИЕ И КАРТИНКИ НОСКОВ ===

    # Пример отправки фото носков
    photos = [
        'URL_КАРТИНКИ_НОСКОВ_1',  # ВСТАВЬ ССЫЛКУ НА ИЗОБРАЖЕНИЕ 1
        'URL_КАРТИНКИ_НОСКОВ_2',  # ВСТАВЬ ССЫЛКУ НА ИЗОБРАЖЕНИЕ 2
        'URL_КАРТИНКИ_НОСКОВ_3'   # ВСТАВЬ ССЫЛКУ НА ИЗОБРАЖЕНИЕ 3
    ]

    for photo_url in photos:
        bot.send_photo(message.chat.id, photo_url)

    # Кнопка с ссылкой на ваш Telegram аккаунт
    markup = types.InlineKeyboardMarkup()
    # === ВСТАВЬ ССЫЛКУ НА СВОЙ ТЕЛЕГРАМ АККАУНТ ===
    account_link = types.InlineKeyboardButton("Связаться с нами", url="https://t.me/YOUR_TELEGRAM_USERNAME")
    markup.add(account_link)

    bot.send_message(message.chat.id, "Если хотите заказать или задать вопрос — пишите нам!", reply_markup=markup)

# === Раздел "Доставка" ===
def send_delivery_info(message):
    # === ВСТАВЬ УСЛОВИЯ ДОСТАВКИ И ТАРИФЫ ===
    delivery_text = "Условия доставки:\n\n- По городу — 300 руб.\n- По России — 500 руб.\n- Бесплатная доставка при заказе от 3000 руб.\n\nОтправляем в течение 2 рабочих дней."
    bot.send_message(message.chat.id, delivery_text)

# === Раздел "Подписка" ===
def send_subscription_info(message):
    # === ВСТАВЬ ИНФОРМАЦИЮ О ПОДПИСКЕ ===
    subscription_text = "Оформите подписку и получайте новые коллекции носков каждый месяц!\n\n- 1 пара в месяц — 800 руб.\n- 2 пары в месяц — 1500 руб.\n\nДля оформления подписки — напишите нам."
    bot.send_message(message.chat.id, subscription_text)

# === Раздел "Информация о магазине" ===
def send_shop_info(message):
    # === ВСТАВЬ ИНФОРМАЦИЮ О МАГАЗИНЕ ===
    info_text = "Магазин носков \"SockShop\" открыт с 2020 года.\n\nАдрес: г. Москва, ул. Примерная, 1.\n\nПриходите к нам или заказывайте онлайн!"

    # Кнопка с местом на карте
    markup = types.InlineKeyboardMarkup()
    # === ВСТАВЬ ССЫЛКУ НА ЛОКАЦИЮ В GOOGLE КАРТАХ ===
    map_link = types.InlineKeyboardButton("Посмотреть на карте", url="https://goo.gl/maps/YOUR_SHOP_MAP_LINK")
    markup.add(map_link)

    bot.send_message(message.chat.id, info_text, reply_markup=markup)

# === Раздел "Отзывы" ===
def send_reviews(message):
    # === ВСТАВЬ ССЫЛКУ НА КАНАЛ С ОТЗЫВАМИ ===
    review_link = "https://t.me/YOUR_REVIEW_CHANNEL"
    bot.send_message(message.chat.id, f"Читать отзывы о нас можно здесь: {review_link}")

# === Запуск бота ===
bot.polling(none_stop=True)
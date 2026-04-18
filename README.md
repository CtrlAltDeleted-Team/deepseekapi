# deepseekapi
Бесплатная Python-библиотека для взаимодействия с DeepSeek AI через эмуляцию браузера. Работает без официального API-ключа, используя твой userToken из веб-версии чата.
Возможности
Отправка сообщений в DeepSeek Chat

Поддержка Deep Think (R1) — режим глубокого размышления

Поддержка Web Search — поиск в интернете

Автоматическое восстановление при ошибках (stale element, таймауты)

Очистка эмодзи — автоматически убирает символы, ломающие ChromeDriver

Управление историей — создание новых чатов

Установка
git clone https://github.com/CtrlAltDeleted-Team/deepseekapi.git
cd deepseekapi
pip install -r requirements.txt

Зависимости
undetected-chromedriver — обход защиты Cloudflare

selenium — управление браузером

psutil — управление процессами

Получение токена
Зайди на chat.deepseek.com и войди в аккаунт

Открой DevTools (F12) → вкладка Application (или Хранилище)

В левом меню выбери Local Storage → https://chat.deepseek.com

Найди ключ userToken и скопируй его значение (value)

Быстрый старт
from deep_api import dpsk

Инициализация с твоим токеном
chat = dpsk("ТВОЙ_USER_TOKEN_ЗДЕСЬ")

Простой запрос
response = chat.chat("Привет, как дела?")
print(response)

С режимом Deep Think (R1)
response = chat.chat("Реши сложную задачу по математике", think=True)

С поиском в интернете
response = chat.chat("Какая погода в Москве?", search=True)

Очистка истории (новый чат)
chat.del_history()

Не забудь закрыть браузер
chat.driver.quit()

}Класс dpsk
dpsk(userToken, prompt=None, headless=True)

Параметр	Тип	Описание
userToken	str	Твой токен из LocalStorage
prompt	str	Системный промпт (отправляется при создании чата)
headless	bool	True — скрытый режим, False — видимое окно
Метод chat()
chat(text, think=False, search=False)

Параметр	Тип	Описание
text	str	Текст сообщения
think	bool	Включить режим Deep Think (R1)
search	bool	Включить поиск в интернете
Метод del_history()
del_history(prompt=None)

Создаёт новый чат. Если передан prompt, отправляет его первым сообщением.

Важные замечания
Chrome обязателен — библиотека использует undetected-chromedriver

Токен может протухнуть — если авторизация слетела, получи новый токен

Эмодзи автоматически вырезаются — ChromeDriver не поддерживает символы вне BMP

Не для продакшена — библиотека создана для личного использования и тестирования

Известные проблемы и решения
Ошибка	Причина	Решение
ModuleNotFoundError: No module named 'deep_api'	Файл не в той папке	Положи deep_api.py рядом со своим скриптом
UserTokenError: invalid userToken	Токен неверный или истёк	Получи новый токен
ChromeDriver only supports characters in the BMP	В тексте есть эмодзи	Библиотека чистит автоматически
StaleElementReferenceException	Страница обновилась во время поиска	Библиотека автоматически повторяет запрос

# deepseekapi-RU
Бесплатная Python-библиотека для взаимодействия с DeepSeek AI через эмуляцию браузера. Работает без официального API-ключа, используя твой userToken из веб-версии чата.
Возможности
Отправка сообщений в DeepSeek Chat

Поддержка Deep Think (R1) — режим глубокого размышления

Поддержка Web Search — поиск в интернете

Автоматическое восстановление при ошибках (stale element, таймауты)

Очистка эмодзи — автоматически убирает символы, ломающие ChromeDriver

Управление историей — создание новых чатов

-------------------------------

Установка

1.

git clone https://github.com/CtrlAltDeleted-Team/deepseekapi.git

2.

cd deepseekapi

3.

pip install -r requirements.txt

-------------------------------

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

## Известные проблемы и решения

**ModuleNotFoundError: No module named 'deep_api'**
Причина: Файл не в той папке.
Решение: Положи deep_api.py рядом со своим скриптом.

**UserTokenError: invalid userToken**
Причина: Токен неверный или истёк.
Решение: Получи новый токен в LocalStorage на сайте DeepSeek.

**ChromeDriver only supports characters in the BMP**
Причина: В тексте есть эмодзи или специальные символы.
Решение: Библиотека чистит такие символы автоматически, ничего делать не нужно.

**StaleElementReferenceException**
Причина: Страница обновилась во время поиска элемента.
Решение: Библиотека автоматически повторяет запрос до 3 раз.

**TimeoutException / Ответ не получен**
Причина: DeepSeek долго думает или проблемы с интернетом.
Решение: Библиотека автоматически обновляет страницу и пробует снова.

**Браузер не закрывается после завершения программы**
Причина: Программа завершилась с ошибкой до вызова driver.quit().
Решение: Используй конструкцию try/finally или закрой процессы вручную через диспетчер задач.

# deepseekapi-EN
Free Python library for interacting with DeepSeek AI through browser emulation. Works without an official API key, using your userToken from the web version of the chat.

Features
Send messages to DeepSeek Chat

Deep Think (R1) support — deep reasoning mode

Web Search support — internet search capability

Automatic error recovery (stale element, timeouts)

Emoji cleaning — automatically removes characters that break ChromeDriver

History management — create new chats


-------------------------------

Installation

1.

git clone https://github.com/CtrlAltDeleted-Team/deepseekapi.git

2.

cd deepseekapi

3.

pip install -r requirements.txt

-------------------------------

selenium — browser automation

psutil — process management

Getting Your Token
Go to chat.deepseek.com and log in to your account

Open DevTools (F12) → Application tab (or Storage)

In the left menu, select Local Storage → https://chat.deepseek.com

Find the key userToken and copy its value

Quick Start
python
from deep_api import dpsk

# Initialize with your token
chat = dpsk("YOUR_USER_TOKEN_HERE")

# Simple request
response = chat.chat("Hello, how are you?")
print(response)

# With Deep Think (R1) mode
response = chat.chat("Solve a complex math problem", think=True)

# With web search
response = chat.chat("What's the weather in London?", search=True)

# Clear history (new chat)
chat.del_history()

# Don't forget to close the browser
chat.driver.quit()
Documentation
dpsk Class
text
dpsk(userToken, prompt=None, headless=True)
Parameter	Type	Description
userToken	str	Your token from LocalStorage
prompt	str	System prompt (sent when creating a chat)
headless	bool	True — hidden mode, False — visible window
chat() Method
text
chat(text, think=False, search=False)
Parameter	Type	Description
text	str	Message text
think	bool	Enable Deep Think (R1) mode
search	bool	Enable web search
del_history() Method
text
del_history(prompt=None)
Creates a new chat. If prompt is provided, sends it as the first message.

Important Notes
Chrome is required — the library uses undetected-chromedriver

Token may expire — if authorization fails, get a new token

Emojis are automatically stripped — ChromeDriver doesn't support characters outside BMP

Not for production — this library is designed for personal use and testing

Known Issues and Solutions
ModuleNotFoundError: No module named 'deep_api'
Cause: The file is not in the right folder.
Solution: Place deep_api.py next to your script.

UserTokenError: invalid userToken
Cause: The token is invalid or expired.
Solution: Get a new token from LocalStorage on the DeepSeek website.

ChromeDriver only supports characters in the BMP
Cause: The text contains emojis or special characters.
Solution: The library automatically strips these characters, no action needed.

StaleElementReferenceException
Cause: The page refreshed while searching for an element.
Solution: The library automatically retries the request up to 3 times.

TimeoutException / No response received
Cause: DeepSeek is taking too long to respond or internet issues.
Solution: The library automatically refreshes the page and tries again.

Browser doesn't close after program finishes
Cause: The program terminated with an error before calling driver.quit().
Solution: Use a try/finally block or manually close processes via Task Manager.

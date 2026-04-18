from deep_api import dpsk

TOKEN = "ТВОЙ_USER_TOKEN"

chat = dpsk(TOKEN, headless=False)

try:
    print("DeepSeek:", chat.chat("Привет! Расскажи о себе."))
    chat.del_history()
    print("DeepSeek (R1):", chat.chat("Сколько будет 2+2*2?", think=True))
finally:
    chat.driver.quit()
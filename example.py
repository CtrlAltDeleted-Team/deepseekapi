from deep_api import dpsk

TOKEN = ""

chat = dpsk(TOKEN, headless=False)

try:
    print("DeepSeek:", chat.chat("Привет"))
    chat.del_history()
    print("DeepSeek (R1):", chat.chat("Сколько будет 2+2*2?", think=True))
finally:
    chat.driver.quit()

"""
          ░░░░▒▓▓▓▓▓▓▓▓▓▓▒░░░░░         
       ░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░       
      ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░     
    ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░   
 ░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░   
 ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░ 
░░▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░▒▓▓▓▓▒░▓▓▓▓▓▓▓▓▓▓▓░░
░▓▓▓▓▓▓▒░░░░░      ░▓▓▓▓▓▒ ░░▒▓▓▒▒░░▓▓▓░
░▓▓▓▓▓░░░░          ░░▒▓▓▓░░ ░░░  ░▒▓▓▓▒
▒▓▓▓▓░░░░             ░░▒▓▓░░░ ░░░▓▓▓▓▓▓
▓▓▓▓░░░▒▒▒░░░░      ░░░░░░▒▒░░░▓▓▓▓▓▓▓▓▓
▓▓▓▓░░▒▓▓▓▓▓▓▓░░    ░░▓▒░░░ ░░░▓▓▓▓▓▓▓▓▓
▒▓▓▓░░░▓▓▓▓▓▓▓▓▓░░  ░░▒▓▓░  ░░▒▓▓▓▓▓▓▓▓▓
▒▓▓▓▒░░▒▓▓▓▓▓▓▓▓▓▒░░░ ░░░░  ░░▓▓▓▓▓▓▓▓▓▒
░▓▓▓▓░░░▒▓▓▓▓▓▓▓▓▓▓░░      ░░▓▓▓▓▓▓▓▓▓▓░
░░▓▓▓▓░░░░▓▓▓▓░░▒▓▓▓░░░  ░░▒▓▓▓▓▓▓▓▓▓▓░░
░░░▓▓▓▓▒░░░░▒▓▓░░░░▓▓▓░░ ░░░▒▓▓▓▓▓▓▓▓░░░
  ░░▓▓▓▓▓▒░░░░░░    ░░░▒▒░░░░▓▓▓▓▓▓▓░░░ 
   ░░▒▓▓▓▓▓▓▓▒░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░  
     ░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░   
        ░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░      
          ░░░░▒▓▓▓▓▓▓▓▓▓▓▒░░░░░░         """
print("""
░█▀▀▄ ░█▀▀▀ ░█▀▀▀ ░█▀▀█ ── ─█▀▀█ ░█▀▀█ ▀█▀ 
░█─░█ ░█▀▀▀ ░█▀▀▀ ░█▄▄█ ▀▀ ░█▄▄█ ░█▄▄█ ░█─ 
░█▄▄▀ ░█▄▄▄ ░█▄▄▄ ░█─── ── ░█─░█ ░█─── ▄█▄
    the free api library of deepseek fixed for the new version of the site
            create by b1tOne
            fixed by CADTeam
    github: https://github.com/CtrlAltDeleted-Team
    github: https://github.com/b1t0nese""")

from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import psutil
import json
import time
import re

def close_processes(process_names):
    for proc in psutil.process_iter():
        for name in process_names:
            if name.lower() in proc.name().lower():
                proc.kill()
                print(f"Process {proc.pid} ({proc.name()}) has been terminated.")

def close_chromedrivers():
    process_names = ["chrome.exe", "chromedriver.exe"]
    close_processes(process_names)

class UserTokenError(Exception):
    def __init__(self, message="Invalid userToken", code=400):
        self.code = code
        super().__init__(f"{message} (code: {code})")

class dpsk:
    def __init__(self, userToken, prompt=None, headless=True):
        print("Chrome initialization...")
        self.driver = Chrome(headless=headless)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
            """
        })
        
        self.count_msgs = 0
        self.prompt = prompt
        
        print("Starting DeepSeek...")
        self.driver.get("https://chat.deepseek.com")
        time.sleep(3)
        
        # Устанавливаем токен в localStorage
        local_storage = self.driver.execute_script("return window.localStorage;")
        local_storage['userToken'] = json.dumps({"value": userToken, "__version": "0"})
        self.driver.execute_script("window.localStorage.clear();")
        for key, value in local_storage.items():
            self.driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")
        
        self.driver.get("https://chat.deepseek.com")
        time.sleep(3)
        
        if "sign_in" in self.driver.current_url:
            self.driver.quit()
            raise UserTokenError("invalid userToken")
        
        print("DeepSeek started!\n")
        
        if prompt or self.prompt:
            print("Sending prompt to DeepSeek...")
            if prompt:
                self.prompt = prompt
            self.chat(self.prompt)
            print("Complete!\n")

    def _clean_text(self, text):
        """Очищает текст от эмодзи и не-BMP символов"""
        if not text:
            return "..."
        
        clean = re.sub(r'[^\u0000-\uFFFF]', '', text)
        
        if not clean.strip():
            clean = text.encode('ascii', 'ignore').decode('ascii')
        
        if not clean.strip():
            clean = "..."
            
        return clean

    def _find_input_box(self):
        """Находит поле ввода, используя точные селекторы с сайта"""
        selectors = [
            "textarea[placeholder='Message DeepSeek']",
            "textarea._27c9245",
            "textarea.d96f2d2a",
            "textarea",
        ]
        
        for selector in selectors:
            try:
                element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                )
                if element.is_displayed():
                    return element
            except:
                continue
        return None

    def _get_last_message(self):
        """Получает последнее сообщение от DeepSeek"""
        try:
            messages = self.driver.find_elements(By.CSS_SELECTOR, "div.ds-markdown")
            if messages and len(messages) > self.count_msgs:
                return messages[-1].text
        except:
            pass
        return None

    def _wait_for_response(self, timeout=60):
        """Ждёт появления ответа с обработкой StaleElementReferenceException"""
        start_time = time.time()
        last_text = ""
        stable_count = 0
        
        while time.time() - start_time < timeout:
            try:
                current_text = self._get_last_message()
                
                if current_text:
                    if current_text == last_text:
                        stable_count += 1
                        if stable_count >= 5:
                            return current_text
                    else:
                        stable_count = 0
                        last_text = current_text
            except StaleElementReferenceException:
                # Если элемент устарел, просто ждем дальше
                pass
            except Exception as e:
                print(f"Debug: Exception in _wait_for_response: {e}")
                pass
            
            time.sleep(1)
        
        return last_text if last_text else None

    def chat(self, text, think=False, search=False, retry_count=0):
        """Отправляет сообщение и возвращает ответ"""
        if retry_count >= 3:
            raise Exception(" Не удалось отправить сообщение после 3 попыток.")
            
        # Очищаем текст от эмодзи
        clean_text = self._clean_text(text)
        
        # Нажимаем на кнопки think/search если нужно
        if think or search:
            try:
                buttons = self.driver.find_elements(By.CSS_SELECTOR, "button")
                for btn in buttons:
                    try:
                        btn_text = btn.text.lower()
                        if think and "think" in btn_text:
                            btn.click()
                            time.sleep(0.3)
                        if search and "search" in btn_text:
                            btn.click()
                            time.sleep(0.3)
                    except StaleElementReferenceException:
                        continue
                    except:
                        continue
            except:
                pass
        
        # ЗАНОВО ищем поле ввода
        chat_input = self._find_input_box()
        if not chat_input:
            print(" Поле ввода не найдено. Обновляю страницу...")
            self.driver.refresh()
            time.sleep(3)
            return self.chat(text, think, search, retry_count + 1)
        
        # Очищаем поле и вводим текст с обработкой StaleElementReferenceException
        try:
            chat_input.clear()
        except StaleElementReferenceException:
            return self.chat(text, think, search, retry_count + 1)
        except:
            pass
        
        try:
            chat_input.send_keys(clean_text)
            time.sleep(0.5)
        except StaleElementReferenceException:
            return self.chat(text, think, search, retry_count + 1)
        except Exception as e:
            print(f" Ошибка при вводе текста: {e}")
            return self.chat(text, think, search, retry_count + 1)
        
        # ЗАНОВО ищем кнопку отправки и нажимаем
        try:
            send_button = None
            buttons = self.driver.find_elements(By.CSS_SELECTOR, "button.ds-icon-button")
            for btn in buttons:
                try:
                    if btn.is_displayed() and btn.is_enabled():
                        svg = btn.find_elements(By.CSS_SELECTOR, "svg")
                        if svg:
                            send_button = btn
                            break
                except StaleElementReferenceException:
                    continue
                except:
                    continue
            
            if send_button:
                send_button.click()
            else:
                chat_input.send_keys(Keys.ENTER)
        except StaleElementReferenceException:
            return self.chat(text, think, search, retry_count + 1)
        except Exception as e:
            print(f" Ошибка при отправке: {e}")
            return self.chat(text, think, search, retry_count + 1)
        
        # Ждём ответ
        response = self._wait_for_response()
        
        if response:
            self.count_msgs += 1
        else:
            print("Ответ не получен, пробую снова...")
            self.driver.refresh()
            time.sleep(3)
            return self.chat(text, think, search, retry_count + 1)
        
        # Выключаем think/search обратно
        if think or search:
            try:
                buttons = self.driver.find_elements(By.CSS_SELECTOR, "button")
                for btn in buttons:
                    try:
                        btn_text = btn.text.lower()
                        if think and "think" in btn_text:
                            btn.click()
                        if search and "search" in btn_text:
                            btn.click()
                    except StaleElementReferenceException:
                        continue
                    except:
                        continue
            except:
                pass
        
        return response

    def del_history(self, prompt=None):
        """Создаёт новый чат"""
        self.count_msgs = 0
        self.driver.get("https://chat.deepseek.com")
        time.sleep(3)
        
        if "sign_in" in self.driver.current_url:
            self.driver.quit()
            raise UserTokenError("invalid userToken")
        
        if prompt or self.prompt:
            if prompt:
                self.prompt = prompt
            self.chat(self.prompt)

# Пример использования
if __name__ == "__main__":
    userToken = "your userToken"
    chat = dpsk(userToken)
    
    try:
        while True:
            inpt = input("Message DeepSeek: ")
            if inpt == "exit":
                chat.driver.quit()
                break
            
            print("DeepSeek:", chat.chat(inpt) + "\n")
    
    except KeyboardInterrupt:
        chat.driver.quit()
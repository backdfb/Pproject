from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

# Chrome 드라이버 경로 설정
driver_path = 'C:\\chromedriver-win64\\chromedriver.exe'
service = Service(driver_path)

# Chrome 옵션 설정
options = Options()
options.add_argument(r"user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data\Default")  # Chrome 프로필 경로
options.add_argument("--start-maximized")  # 브라우저 최대화

# 웹 드라이버 초기화
driver = webdriver.Chrome(service=service, options=options)

url = 'https://yozm.wishket.com/magazine/detail'
driver.get(url)

# 페이지 로딩 대기
time.sleep(5)
try:
    # 클립 버튼이 나타날 때까지 최대 10초 대기
    clip_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-btn"]'))
    )
    clip_button.click()
    print("클립 완료!")

    # Obsidian Web Clipper 단축키 입력 (예: Ctrl + Shift + K)
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.CONTROL + Keys.SHIFT + 'k')  # 단축키 조합

    # 사용자가 클리핑 작업을 완료할 수 있도록 60초 대기
    print("Obsidian Web Clipper가 실행되었습니다. 60초 후에 브라우저가 닫힙니다.")
    time.sleep(60)  # 대기 시간 조정 가능
except Exception as e:
    print("클립 버튼 어디 있어?:", e)
finally:
    driver.quit()  # 드라이버 종료

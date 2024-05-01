from selenium.webdriver.common.by import By

BASE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

amount_value = 0
class home:
    TRANSACTIONS = By.XPATH, "//button[normalize-space()='Transactions']"
    WITHDRAW = By.XPATH, "//button[normalize-space()='Withdrawl']"
    DEPOSIT = By.XPATH, "//button[normalize-space()='Deposit']"
    WELCOME_NAME = By.XPATH, "//span[@class='fontBig ng-binding']"
class transaction:
    RESET = By.XPATH, "//button[normalize-space()='Reset']"
    BACK = By.XPATH, "//button[normalize-space()='Back']"
class deposit:
    DEPOSIT_BTN = By.XPATH, "//button[@type='submit']"
    AMOUNT = By.XPATH, "//input[@placeholder='amount']"
    MESSAGE = By.XPATH, "//span[@class='error ng-binding']"
    BALANCE = By.XPATH, "//div[@ng-hide='noAccount']/strong[2]"

class withdraw:
    WITH_DRAW_BTN = By.XPATH, "(//button[normalize-space()='Withdraw'])[1]"
    AMOUNT = By.XPATH, "//input[@placeholder='amount']"
    MESSAGE = By.XPATH, "//span[@class='error ng-binding']"
class login:
    CUSTOMER_LOGIN = By.XPATH, "//button[normalize-space()='Customer Login']"
    USER_SELECT = By.XPATH, "//select[@name='userSelect']"
    LOGIN_BTN = By.XPATH, "//button[@type='submit']"
    HOME = By.XPATH, "//button[@class='btn home']"
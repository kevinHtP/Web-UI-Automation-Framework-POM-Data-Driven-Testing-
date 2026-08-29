class LoginPage:
    def __init__(self, page):
        self.page = page
        # Locator elemen halaman login saucedemo
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"

    def buka_halaman(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def ambil_pesan_error(self):
        return self.page.locator(self.error_message).inner_text()
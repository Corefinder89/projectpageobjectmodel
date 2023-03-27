from seleniumpagefactory.Pagefactory import PageFactory

class Homepage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        "sign_in": ("ID", "signin"),
        "user_name": ("CSS", ".username")
    }

    def click_sign_in(self):
        self.sign_in.click()

    def get_username(self):
        retrieved_username = self.user_name.get_text()
        assert retrieved_username == "demouser"
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FillOutForm:
    def __init__(self):
        google_form_link = ('https://docs.google.com/forms/d/e'
                            '/1FAIpQLSc3RZWHduZwzp3nX21KLlo23_Ii6GAkuWQiCQ1huOn9PZJJrg/viewform?usp=sf_link')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.get(google_form_link)

    def fill_out(self, addresses_list, prices_list, links_list):
        for number in range(len(addresses_list)):
            input_fields = self.driver.find_elements(By.CSS_SELECTOR, 'div[role="listitem"] input')
            # address
            input_fields[0].click()
            input_fields[0].send_keys(addresses_list[number])

            # price
            input_fields[1].click()
            input_fields[1].send_keys(prices_list[number])

            # link
            input_fields[2].click()
            input_fields[2].send_keys(links_list[number])

            send_button = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Senden')]")
            send_button.click()

            time.sleep(1)

            send_more = self.driver.find_element(By.LINK_TEXT, 'Weitere Antwort senden')
            send_more.click()

            time.sleep(1)

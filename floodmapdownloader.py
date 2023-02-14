from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import pandas as pd


df = pd.read_excel(r'C:\Users\pari1218\Downloads\Flood Maps\Try\Cordinates.xlsx')

# for index in range(len(df)):
#     structureName = df['Structure Name'].loc[index]
#     path_and_filename = r'C:\Users\pari1218\Downloads\Flood Maps\Try\%s.pdf' % (str(structureName))
#     # print(path_and_filename)



if __name__ == '__main__':
    for index in range(len(df)):
        locationCords = df['Location Coords'].loc[index]
        structureName = df['Structure Name'].loc[index]
        edgeBrowser = webdriver.Edge(r"msedgedriver.exe")
        edgeBrowser.get(
            'https://maps.cyfoethnaturiolcymru.gov.uk/Html5Viewer/Index.html?configBase=https://maps.cyfoethnaturiolcymru.gov.uk/Geocortex/Essentials/REST/sites/Flood_Risk/viewers/Flood_Risk/virtualdirectory/Resources/Config/Default&layerTheme=0')
        edgeBrowser.maximize_window()
        time.sleep(10)
        edgeBrowser.find_element(By.XPATH, "//button[contains(text(), 'Options')]").click()
        edgeBrowser.implicitly_wait(20)
        findAddress = edgeBrowser.find_element(By.XPATH, "//span[contains(text(), 'Find an address')]")
        findAddress.click()
        edgeBrowser.implicitly_wait(10)
        addressBox = edgeBrowser.find_element(By.XPATH, "//input[contains(@title, 'Type in an address or post code')]")
        addressBox.click()
        addressBox.send_keys(str(locationCords))
        findButton = edgeBrowser.find_element(By.XPATH, "//div[@class='form-btns']//button[./text()='Find']")
        # findButton = finds[1].find_element(By.XPATH, "//button[text(), 'Find')]")
        findButton.click()
        time.sleep(3)
        edgeBrowser.find_element(By.XPATH, "//button[contains(text(), 'Options')]").click()
        printButton = edgeBrowser.find_element(By.XPATH,
                                               "//span[contains(text(), 'Create a printable version of the map')]")
        printButton.click()
        edgeBrowser.find_element(By.XPATH, "//div[@class='form-btns']//button[./text()='Print']").click()

        edgeBrowser.implicitly_wait(500)
        edgeBrowser.find_element(By.XPATH, "//div[@class='form-btns']//button[./text()='Open File']").click()
        edgeBrowser.implicitly_wait(500)
        originalWindow = edgeBrowser.current_window_handle
        for window_handle in edgeBrowser.window_handles:
            if window_handle != originalWindow:
                edgeBrowser.switch_to.window(window_handle)
                break
        time.sleep(1)
        pyautogui.hotkey('ctrl', 's')
        time.sleep(2)
        path_and_filename = r'C:\Users\pari1218\Downloads\Flood Maps\ABD SF\%s.pdf' % (str(structureName))
        pyautogui.typewrite(path_and_filename)
        pyautogui.press('enter')
        time.sleep(3)
        edgeBrowser.quit()








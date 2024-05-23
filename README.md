## python-deepl-translator-selenium
API-less somewhat fast DeepL translation using Selenium.     
⚠️ Because no account is used you can only translate up to 1500 characters     
### Usage
1. Download translator.py and add it to your project
2. Install selenium `pip install selenium` and webdriver-manager `pip install webdriver-manager`
3. Call `await get_translation(text, langFrom, langTo)` in your code. You can find the language codes [here](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)
4. If you get an error that says chromium command not found, install Chromium from your Linux package manager. For Windows read selenium's documentation.
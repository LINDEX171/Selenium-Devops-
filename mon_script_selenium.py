from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Options pour le WebDriver 
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')

# Création d'une instance de navigateur Chrome avec options
driver = webdriver.Chrome(options=options)

# Ouvrir votre site
driver.get("https://ibrahimaportofolio.netlify.app")

# Attendre quelques secondes pour le chargement complet de la page (ajustez si nécessaire)
driver.implicitly_wait(5)

# Capture d'écran du site
driver.save_screenshot("ibrahimaportofolio.png")

# Fermer le navigateur
driver.quit()

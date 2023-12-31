
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options


# URL of the webpage to scrape
def fetch_poster(name,id):
    name=name.replace(' ','_')
    url = f"https://myanimelist.net/anime/{id}/{name}/pics"
    # Set up the Selenium WebDriver (make sure you have the appropriate WebDriver installed)
    edge_options = Options()
    edge_options.add_argument('--headless')
    edge_options.add_argument('--disable-gpu')
    edge_options.add_argument('--no-sandbox')
    edge_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Edge(options=edge_options)  # You can use other browsers by changing this line

    # Open the webpage
    driver.get(url)

    # Find all image elements using Selenium
    img_elements = driver.find_elements(By.TAG_NAME, 'img')

    # Extract and print the src attribute for each image
    k=0
    l=[]
    for img_element in img_elements:
        k+=1
        src_value = img_element.get_attribute('src')
        
        if k==2:
           return src_value
    
       
    # Close the WebDriver
    driver.quit()
  
        


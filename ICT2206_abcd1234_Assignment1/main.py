import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

def ChromeTest():
    options = webdriver.ChromeOptions()
    options.add_argument("--enable-precise-memory-info")
    options.add_argument('--js-flags="--expose-gc"')
    driver = webdriver.Chrome(options = options)

    driver.get("http://127.0.0.1:5500/index.html")
    driver.maximize_window()
    print("===========================================")
    print("         Google Chrome Heap Analysis       ")
    print("===========================================")

    print("Before inserting nodes: " + str(round(driver.execute_script("return window.performance.memory.usedJSHeapSize/1024/1024"),2)) + "Mb")
    print("Number of Image Objects in Browser: " + str(driver.execute_script("return CheckForGC()")))

    for i in range(0,10):
        buttonCreate = driver.find_element(By.ID, "CreateLeak")
        buttonCreate.click()
        buttonRemove = driver.find_element(By.ID, 'RemoveDOMElems')
        buttonRemove.click()

    print("After inserting nodes: " + str(round(driver.execute_script("return window.performance.memory.usedJSHeapSize/1024/1024"),2)) + "Mb")
    print("Number of Image Objects in Browser: " + str(driver.execute_script("return CheckForGC()")))

    #To wait and see if garbage collection successful or not
    time.sleep(30)
    print("Maybe after garbage collection: " + str(round(driver.execute_script("return window.performance.memory.usedJSHeapSize/1024/1024"),2)) + "Mb")
    print("Number of Image Objects in Browser: " + str(driver.execute_script("return CheckForGC()")))



def AnalyzeFirefox():
    print("===========================================")
    print("           FireFox Heap Analysis           ")
    print("===========================================")
    options =  webdriver.FirefoxOptions()
    options.add_argument('--js-flags="--expose-gc"')
    driver = webdriver.Firefox(options=options)
    driver.get("http://127.0.0.1:5500/index.html")
    driver.maximize_window()

    # Switch to the new window and open new URL
    driver.execute_script("""window.open('');""")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("about:performance")

    #save the dynamic table file
    time.sleep(3)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(2)
    pyautogui.typewrite("Performance" + '.html')
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(2)
    # My path is C:\Users\Alaric Tang\Documents\Downloads
    path = input("Where is the path to your downloads?: ")
    performancePath = path + "\\Performance.html"
    with open(performancePath, "r") as f:
        lines = f.readlines()

    for i in range(0,len(lines)):
        if "Leaky Browser" in lines[i]:
            codeLine = lines[i]

    lineArray = codeLine.split('>')
    finalSizeArray = lineArray[8].split("</")
    print("Before inserting nodes: " + str(finalSizeArray[0]))

    driver.switch_to.window(driver.window_handles[0])

    for i in range(0,10):
        buttonCreate = driver.find_element(By.ID, "CreateLeak")
        buttonCreate.click()
        buttonRemove = driver.find_element(By.ID, 'RemoveDOMElems')
        buttonRemove.click()

    driver.switch_to.window(driver.window_handles[1])

    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.typewrite("PerformancePost" + '.html')
    time.sleep(1)
    pyautogui.hotkey('enter')

    time.sleep(2)
    performancPostPath = path + "\\PerformancePost.html"
    with open(performancPostPath, "r") as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        if "Leaky Browser" in lines[i]:
            codeLine = lines[i]

    lineArray = codeLine.split('>')
    finalSizeArray = lineArray[8].split("</")
    time.sleep(1)
    print("After inserting nodes: " + str(finalSizeArray[0]))
    # print("Number of Image Objects in Browser: " + str(driver.execute_script("return CheckForGC()")))

    time.sleep(30)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(3)
    pyautogui.typewrite("PerformancePostGC" + '.html')
    time.sleep(2)
    pyautogui.hotkey('enter')

    time.sleep(2)
    performancPostPathGC = path + "\\PerformancePostGC.html"
    with open(performancPostPathGC, "r") as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        if "Leaky Browser" in lines[i]:
            codeLine = lines[i]

    lineArray = codeLine.split('>')
    finalSizeArray = lineArray[8].split("</")
    print("Maybe after GC: " + str(finalSizeArray[0]))
    # print("Number of Image Objects in Browser: " + str(driver.execute_script("return CheckForGC()")))

    #print(str(driver.execute_script("return findNumberOfDetachedNodes()")) + " Nodes in DOM")

def AnalyzeEdge():
    print("===========================================")
    print("       Microsoft Edge Heap Analysis        ")
    print("===========================================")

    options = webdriver.EdgeOptions()
    options.add_argument("--enable-precise-memory-info")
    driver = webdriver.Edge(options = options)

    driver.get("http://127.0.0.1:5500/index.html")
    driver.maximize_window()

    print("Before inserting nodes: " + str(round(driver.execute_script("return window.performance.memory.usedJSHeapSize/1024/1024"),2)) + "Mb")
    print("Number of Image Objects in Browser: " + str(driver.execute_script("return CheckForGC()")))

    for i in range(0, 10):
        buttonCreate = driver.find_element(By.ID, "CreateLeak")
        buttonCreate.click()
        buttonRemove = buttonCreate = driver.find_element(By.ID, 'RemoveDOMElems')
        buttonRemove.click()

    print("After inserting nodes: " + str(round(driver.execute_script("return window.performance.memory.usedJSHeapSize/1024/1024"),2)) + "Mb")
    print("Number of Image Objects in Browser: " + str(driver.execute_script("return CheckForGC()")))

    time.sleep(30)
    print("Maybe after GC: " + str(round(driver.execute_script("return window.performance.memory.usedJSHeapSize/1024/1024"),2)) + "Mb")
    print("Number of Image Objects in Browser: " + str(driver.execute_script("return CheckForGC()")))

print("====================================================")
print("               Leaky Browser Analysis               ")
print("====================================================")

while(1):
    choice = input("\nWhich browser do you wish to analyze? Google Chrome (1), Mozilla Firefox(2), or Microsoft Edge(3)? If not press 4 to quit: ")

    if choice == "1":
        ChromeTest()
    elif choice == "2":
        AnalyzeFirefox()
    elif choice == "3":
        AnalyzeEdge()
    elif choice == "4":
        print("See you!")
        break
    else:
        print("Choice not accepted try again")
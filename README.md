# ICT2206_abcd1234_Assignment1 Leaky Browser Analyzer

This project was to test the performance of the 3 commonly used web browsers: Google Chrome, Mozilla Firefox and Microsoft Edge
The python script written is able to get the heap size used by the testing website and also find if the image nodes created by the javascript code in the testing website
is collected by JavaScript's Garbage Collector

![image](https://user-images.githubusercontent.com/73848081/161975035-4bcccec1-a653-4b48-9070-b712b3bec1bc.png)


By viewing the heapsize used by the website at 3 given times, before testing, after testing and 30 seconds after testing, the heap size on each browser between the 3 timings can be compared.

<h1>Steps to get the project running</h1>

1. To get the python script running make sure you install the correct version of web drivers. The web drivers that are used are chromedriver, geckodriver, and        msedgedriver. For chromedriver, make sure the version is compatible with your Google Chrome version. In order to find the compatible version of the drivers, go to:
  </br>https://chromedriver.chromium.org/downloads </br>
  https://github.com/mozilla/geckodriver/releases </br>
  https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ </br>
2. Unzip the web drivers
3. Copy the exe web driver files into ICT2206_abcd1234_Assignment1
4. Open up visual studio code with the file MemLeakPage
5. Install the extension Live Server

![image](https://user-images.githubusercontent.com/73848081/161980643-d23b789b-6939-45f4-9a26-d043a1c6e7ef.png)

6. Open the file ICT2206_abcd1234_Assignment1 with PyCharm
7. Install all the modules, in this code selenium, pyautogui and time are used
8. Finally run the code

<h2>Note</h2>

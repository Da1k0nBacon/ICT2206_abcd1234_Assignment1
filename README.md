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
8. Finally run the Python code on PyCharm

![image](https://user-images.githubusercontent.com/73848081/161986741-99e1d950-37d0-41f9-8bf4-0a3902d63f89.png)

<h2>Notes</h2>
- <p>Mozilla Firefox analyzer will only show the Heap size used by the testing website and not the number of image nodes to see if they were garbage collected</p>
- <p>In order to see number of nodes in Firefox, call the function CheckForGC() in the console</p>

![image](https://user-images.githubusercontent.com/73848081/161986532-4691b0d4-10af-4d86-a056-cdd2bf6ed590.png)

- <p>When the Mozilla Firefox analysis is happening, it will download 3 HTML files just press enter when the name of the file is changed these HTML file are used to        get the current Heap size used by the testing website</p>

![image](https://user-images.githubusercontent.com/73848081/161987165-21281a67-98f2-41ef-9b09-898b9c8d0380.png)







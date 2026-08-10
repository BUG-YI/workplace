驱动

不安装驱动selenium会自动下载安装

[edge驱动](https://msedgedriver.microsoft.com/catalog/index.html?form=MA13LH)

[chrome驱动151及以上](https://googlechromelabs.github.io/chrome-for-testing/)



### 安装selenium

```cmd
pip install selenium
```



### 使用

自行下载驱动,以edge为例,其余浏览器类似

```python
from selenium import webdriver
from selenium.webdriver.edge.service import Service

url = 'https://www.baidu.com'
edge_driver_path = '下载驱动的路径'
service = Service(edge_driver_path)
driver = webdriver.Edge(service=service)

#打开网址
driver.get(url)

#结束后关闭浏览器
driver.close()
```



selenium自动检测安装

```python
from selenium import webdriver

url = 'https://www.baidu.com'
#首次运行可能会很缓慢，selenium在下载驱动
driver = webdriver.Edge()

#其他相同
driver.get(url)

driver.close()
```



### 获取网页源码

```python
from selenium import webdriver

url = 'https://www.baidu.com'

driver = webdriver.Edge()
driver.get(url)

source = driver.page_source
print(source)

driver.close()
```



### 元素定位

find_element: 第一个匹配的元素
find_elements: 多个匹配的元素

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.baidu.com'

driver = webdriver.Edge()
driver.get(url)

#通过id定位元素
el = driver.find_element(By.ID,'id')

#class定位
el1 = driver.find_element(By.CLASS_NAME,'class')

#通过xpath定位
el2 = driver.find_element(By.XPATH,'xpath')

#通过css选择器定位
el3 = driver.find_element(By.CSS_SELECTOR,'[#id="id"]')

#通过部分文本内容定位
el4 = driver.find_element(By.PARTIAL_LINK_TEXT,'context')

driver.close()
```



### 元素信息



### selenium交互

```python
from selenium import webdriver

driver = webdriver.Edge()

#支持执行js代码
driver.execute_script('js代码')
```



### selenium option

依旧edge为例

```python
from selenium import webdriver
from selenium.webdriver.edge.options import Options

options = Options()

#启动时最大化窗口
options.add_argument("--start-maximized")

#无头模式（不显示界面）
options.add_argument("--headless")

#禁用 GPU 加速
options.add_argument("--disable-gpu")

driver = webdriver.Edge(options=options)
```



|参数                                            | 说明                 
|-----------------------------------------------|------------------------------|
|--start-maximized                              | 启动时最大化窗口            
|--headless	                                    | 无头模式（不显示界面）        
|--disable-gpu	                                | 禁用 GPU 加速             
|--no-sandbox	                                | 禁用沙盒模式（Linux 需要）   
|--disable-dev-shm-usage	                    | 解决共享内存问题（Linux）    
|--disable-blink-features=AutomationControlled  | 隐藏自动化特征             
|--user-agent="..."	                            | 设置 User-Agent          
|--window-size=1920,1080	                    | 设置窗口大小              
|--disable-extensions	                        | 禁用扩展                 
|--disable-popup-blocking	                    | 禁用弹窗拦截              
|--ignore-certificate-errors	                | 忽略证书错误              
|--incognito	                                | 隐私模式（Chrome）        
|--inprivate	                                | 隐私模式（Edge）          
|--lang=zh-CN	                                | 设置语言                 
|--remote-debugging-port=9222	                | 远程调试端口
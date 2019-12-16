**本项目为移动端（Android、iOS）自动化测试项目**


> 依托APPIUM和PYTHON，基于PageObject模式，进行底层方法的封装。

**目录结构为：**

> |-- BasePage　　　　　　　　　　　　　　# BasePage目录，里面包含AppiumDriver、AppiumSever、BasePage，等底层的封装  
> |....| AppiumDriver.py  
> |....| AppiumSever.py  
> |....| BasePage.py  
> |-- Login　　　　　　　　　　　　　　　　# 登录模块  
> |....|-- LoginPage  
> |........|-- LoginPage.py　　　　　　　　# 登录模块 Page 上的方法封装  
> |....|-- TestCases　　　　　　　　　　　　# 登录模块的测试用例  
> |........|-- TestLogin.py  
> |........|-- TestSignOut.py  
> |-- OtherModel　　　　　　　　　　　　　　# 其他模块  
> |....|-- OtherModelPage  
> |........|-- OtherModelPage.py　　　　　　# 其他模块 Page 上的方法封装  
> |....|-- TestCases　　　　　　　　　　　　# 其他模块的测试用例  
> |........|-- TestOtherModel.py  
> .  
> .  
> .  
> .  
> |-- venv　　　　　　　　　　　　　　　　# Mac环境，运行此项目所需的Python库  
> |-- .gitignore　　　　　　　　　　　　　# git 推送忽略文件  
> |-- pytest.ini　　　　　　　　　　　　　# pytest 设置文件，例如：设置filterwarnings参数后，调试执行测试用例时可以忽略warning消息  
> |-- README.md　　　　　　　　　　　　　#　项目说明文件  
> |-- RunCase.py　　　　　　　　　　　　　# 如何执行测试用例，用此种方式，才能生成allure原生报告 
 


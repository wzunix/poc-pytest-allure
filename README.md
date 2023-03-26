# POC-Pytest-Allure
This is a POC project of integration of API test by Pytest with Allure report.
- Example target is [UK Parliament Members API](https://members-api.parliament.uk/index.html).

**Note** - Next project `PIC-Pytest-Core` include this project, plus how to run pytest tests

## Scope:
    1. Able to request (with Pytest) UK Parliament Members API (2 apis), and generate Allure test report.
    2. Capture both http request & Response details in Allure test report.

## 1. Project Setup
**1.1 requirements.txt:**
     
      brew install allure  -> install Allure v2.21.0 in order to generate Allure report
      
      Python 3.8
      requests==2.28.2
      pytest==7.2.1
      pytest-html==3.2.0 -> a plugin for pytest that generates a HTML report for test results.
      allure-pytest==2.12.0 -> a plugin for 'Allure pytest integration' that generates a Allure report for test results.
              

**1.2 Setup local project environment:**

    Step 1: Clone pic-core Repo from github
            $ git clone https://github.com/wzunix/poc-pytest-allure.git
 
    Step 2: Create Anaconda Virtural environment
            $ conda create --name poc-pytest-allure python=3.8
             
    Step 3: activate virtual environment 
            $ conda activate poc-pytest-allure           
    
    Step 4: Run pip install on requirements.txt
            $ pip install -r requirements.txt        
    
    Note    If see setuptools related errors, try run:            
        (pic-core)$ python -m pip install -U pip setuptools     

## Packages used in this poc-pytest-allure 
### 1. [requests](https://requests.readthedocs.io/en/latest/)  
Requests allows you to send **HTTP/1.1** requests extremely easily.

**Brief history of HTTP module used inside Python3**

1.1 **urllib2** and **urllib** contains a high-level HTTP interface that didn't require you to mess around with the details of **http.client** (formerly httplib). But they were missing a long list of critical features. 

1.2 **urllib3** can do nearly everything the above 2 do and has some extra features, and **the vast majority of programmers use urllib3 and requests**.

1.3 **requests** uses **urllib3** under the hood and makes it even simpler to make requests and retrieve data. For one thing, keep-alive is 100% automatic, compared to urllib3 where it's not.

**Note: on some site warning msg shows** 

Issue: 
		
	InsecureRequestWarning: Unverified HTTPS request is being made to host 'abc..d.com'. Adding certificate verification is strongly advised.

Solution: 

	import urllib3
	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

### 2. [Generate Pytest Report](https://docs.pytest.org/en/stable/)
#### Test File Naming Convention ####
-   By default pytest only identifies the **file names** starting with `test_` or ending with `_test` as the **test files**.
#### Test Method Naming Convention ####
-   Pytest requires the **test method names** to **start** with `test`. All other method names will be ignored even if we explicitly ask to run those methods.                
#### Test Report Generation ####
-   If tests are inside a folder 'Tests', then run the following command : `pytest Tests`.

**To generate Pytest html report**
    
    run the following command : `python -m pytest Tests --html=report/pytest-report.html`

**To generate Pytest xml report**

    run the following command : `pytest Tests --junitxml="result.xml"`

### 3. [Generate Allure Report](https://docs.qameta.io/allure-report/#_installing_a_commandline)
#### 3.1 Install Allure ####
- For MAC OS, run command - `brew install allure`
#### 3.2 Check Allure Version ####
- Run command - `allure --version`
#### 3.3 Execute pytest and save results to 'report/result' folder ####
    run the following command : `python -m pytest uk_parliament_test --alluredir=report/result`
#### 3.4 Generate Allure report ####
    run the following command : `allure generate report/result -c -o report/html`

### 4. pathlib2
    pip install pathlib2==2.3.7.post1
All utilities are listed in `pic_core/utils/fileUtils.py`	
	
	
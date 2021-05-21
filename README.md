# CrossLog: Intelligent-Log-Analyzer
*CrossLog: Intelligent Log Analyzer is a Machine Learning based real-time Intrusion detection system and Web Application security scanner, powered using python3 and flask. It wields defense against Cross-Site Scripting (XSS), Path Traversal attacks, Server Side Includes (SSI), OS Command Injections, XPath Injections, LDAP Injections, CRLF Injections, and other Anomalous categories.*
1. ***Download Crosslog files***<br />
```
    i.   Open terminal
    ii.  Run command: svn checkout https://github.com/Narendran36/CrossLog-Intelligent-Log-Analyzer/trunk/CrossLog
    iii. Extract requirments.rar in CrossLog directory
    iv. Replace <sender email id>, <sender password>, and <receiver email id> with proper values to receive email alerts.
    iv.  Run command: apt-get install python3-pip -y
```

2. ***Install necessary libraries***<br />
```
    pip install flask
    pip install scikit-learn==0.22.2.post1
    pip install scrapy
    
```
3. ***Run app.py***<br />
```
    python3 app.py
    Navigate to http://127.0.0.1:5000/
    
```
4. ***Scan log***<br />
``` 
    Browse the log file and submit
    Displays different types of attacks present in the log file
   
```
5. ***Realtime IDS***<br />
```
    Insert webserver log location and submit
    Realtime scan results are displayed
    
```
6. ***Web app scanner***<br />
```
    Enter web application url and submit
    Scanned result will displays the vulnerability of that web application
    
```
7. ***Test query***<br />
```
    Enter query to test
    Displays attack type of query
    
```
***Reasearch Dataset Files:***<br /> https://drive.google.com/drive/folders/1jzb8YOe021eZm2SS9na-agPaI5dYZGKr?usp=sharing

Read out all the csv files from the csic and ecml folder into pandas dataframe, and merge them together for further processing.

Note: Go through the Research Files on our repository for more details.



***demo link:*** <br />
https://youtu.be/_W9BoO_F2Bk

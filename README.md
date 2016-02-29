How to run the Server
--------------------------
````
git clone https://github.com/sarathsp06/exomlgen.git
sudo pip install -r exomlgen/requirements.txt
python -m exomlgen
````
**NOTE** : python2.6 + is required
###Following code snipets shows how to create and retrieve static xmls

####Sample Create Request [PUT]
------------------------------
without digits
```
curl -XPUT http://127.0.0.1:8080/echo/SASASA/2121 \
-d '<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>Hello</Say>
</Response>' \
-H "Content-Type: text/plain"
```
with digits
```
curl -XPUT http://127.0.0.1:8080/echo/SASASA/2121?digits=12 \
-d '<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>Hello after dtmf 12</Say>
</Response>' \
-H "Content-Type: text/plain"
```

####Sample Read Request [POST and GET]
-----------------------
Without digits
```
curl  http://127.0.0.1:8080/echo/SASASA/2121
```

With digits
```
curl  http://127.0.0.1:8080/echo/SASASA/2121?digits=12
```



###Following code snipets shows how to use exomlgen server to get exoml verbs dynamically generated
---------------


Using dial verb
The following will return a dial verb with +919742033616 as the number to dial
````
 curl -XGET  "http://127.0.0.1:8080/verb/dial?number=%2B919742033616
````



**Configuration**
1. Datastore contains the xmls
2. There are two ways to put exoml and use it
    1. make a put request in the following ormat
    ```
    curl -XPUT http://127.0.0.1:8080/echo/SASASA/2121 \
    -d '<?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Say>Hello</Say>
    </Response>' \
    -H "Content-Type: text/plain"
    ```

    2. Put the exoml inside folder datastore/[scenario_name]/[xml_name]
3. For IVR/Menu driven flows put xml for curresponding digits pressed in the same folder as parent with and same file name and the digits seperated by a underscore
   For example
       exoml for url /SASASA/2121 would be stored in datastore//SASASA/2121.xml and
       exoml for menu 3 for url /SASASA/2121 would be stored in datastore//SASASA/2121_3.xml

**NOTE**
 1. If there is no curresponding file for the test/id?digits= combination Hangup will be returned
 2. For DTMF If digits is wrong parent menu will be responded

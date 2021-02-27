# ipgeolocation
API - Check geolocation based on provided IP or URL adress. You can add, delete records to database. Based on ipstack.com

Requeres authorisation via JWT

endpoints:
0. GET TOKEN  ```/api/token```
1. REFRESH EXPIRED TOKEN: ```/api/token/refresh```
2. ```/api/ip-geolocation?ip={IP_OR_URL}``` - get geolocation for provided IP or URL
3. ```/api/ip-geolocation``` - List all ip geolocation data, or create a new one.
4. ```/api/ip-geolocation/<ip>``` - retrieve or delete geolocation data.

### Development
Install requirements:
```bash
pip install -r requirements.txt
```

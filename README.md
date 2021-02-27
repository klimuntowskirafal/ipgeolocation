# ipgeolocation
API - Check geolocation based on provided IP or URL adress. You can add, delete records to database. Based on ipstack.com

Requeres authorisation via JWT

endpoints:

0. Contact me for username and password at klimuntowski.rafal@gmail.com
1. ```/api/token``` - use login credentials to get ACCESS TOKEN
2. ```/api/token/refresh``` - refresh expired token
3. ```/api/ip-geolocation ? ip = IP_OR_URL``` - get geolocation for provided IP or URL
4. ```/api/ip-geolocation``` - List all ip geolocation data, or create a new one.
5. ```/api/ip-geolocation/<ip>``` - retrieve or delete geolocation data for the specified ip

### Development
Install requirements:
```bash
pip install -r requirements.txt
```

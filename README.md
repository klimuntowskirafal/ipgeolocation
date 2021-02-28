# ip geolocation api
Check geolocation based on provided IP or URL adress. You can add, delete records to database. Provided data is based on ipstack.com API

Requeres authorisation via JWT

You can interract with the API only programmatically. On each request you need to explicitly provide the authentication credentials as well as Access Token.
If we try to access API  without authenticating, an error will show up:
```
{
    "detail": "Authentication credentials were not provided."
}
```

credentials:
```
username: test_user
password: Ipgeolocation_Zadanie
```

Endpoints:

1. ```/api/token/``` - send POST request with login credentials to get ACCESS TOKEN
2. ```/api/token/refresh/``` - send POST request with refresh token to refresh your access token
3. ```/api/ip-geolocation ? ip = IP_OR_URL``` - get geolocation for provided IP or URL - Token required
4. ```/api/ip-geolocation/``` - List all ip geolocation data, or create a new one - Token required
5. ```/api/ip-geolocation/<ip or id>/``` - retrieve or delete geolocation data for the specified ip - Token required

### Testing
1. use POSTMAN to send request to the endpoints provided above

### Development
Install requirements:
```bash
pip install -r requirements.txt
```

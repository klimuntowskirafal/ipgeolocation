some change
# free ip geolocation api - https://geolocate-ip.herokuapp.com/
Check geolocation based on provided IP or URL adress. You can add, delete records to database. Provided data is based on ipstack.com API

Requires authorisation via JWT

You can interract with the API only programmatically. This means you have to use tools like POSTMAN, or send requests programmatically to the relative endpoints.
On each request you need to explicitly provide Token authorisation (that you can acccess from one of the endpoints provided below).
If you try to access API  without authenticating, an error will show up:
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

1. ```/api/token``` - send POST request with login credentials to get ACCESS TOKEN
2. ```/api/token/refresh``` - send POST request with refresh token to refresh your access token
3. ```/api/ip-geolocation ? ip = IP_OR_URL``` - get geolocation for provided IP or URL - Token required
4. ```/api/ip-geolocation``` - List all ip geolocation data, or create a new one - Token required
5. ```/api/ip-geolocation/<ip>``` - retrieve or delete geolocation data for the specified ip - Token required

### Development
Install requirements:
```bash
pip install -r requirements.txt
```

To run the project locally:
* using local settings - for full api functionality, get new api key from ipstack.com and override variable API_IPSTACK_KEY with new value
    ```bash
    py manage.py runserver --settings ipgeolocation.settings_local
    ```

To load dummy-data:

    py manage.py loaddata ipdata.json

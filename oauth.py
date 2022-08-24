import requests
class Oauth(object):
    API_ENDPOINT = 'https://discord.com/api/v8'
    CLIENT_ID = '1011832765932650576'
    CLIENT_SECRET = 'lOLq2s3r9VHGX59wUJw0AhQbbcUe1UeF'
    REDIRECT_URI = 'https://nearnear.tk/login'
    @staticmethod
    def exchange_code(code):
        data = {
            'client_id': Oauth.CLIENT_ID,
            'client_secret': Oauth.CLIENT_SECRET,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': Oauth.REDIRECT_URI
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        } 
        r = requests.post('%s/oauth2/token' % Oauth.API_ENDPOINT, data=data, headers=headers)
        r.raise_for_status()
        return r.json()
    @staticmethod
    def add_to_guild(access_token, userID,server_id):
        url = f"{Oauth.API_ENDPOINT}/guilds/{server_id}/members/{userID}"

        botToken = "MTAxMTgzMjc2NTkzMjY1MDU3Ng.Gn3mPj.zLu_CMVlthK-3nSQ_5b9Qwyu-J8Xj7vVOBcNYg"
        data = {
            "access_token" : access_token,
        }
        headers = {
            "Authorization" : f"Bot {botToken}",
            'Content-Type': 'application/json'

        }
        response = requests.put(url=url, headers=headers, json=data)
        print(response.text)
    @staticmethod
    def get_user_json(token):
        url = Oauth.API_ENDPOINT + "/users/@me"
        headers = {
            "Authorization": "Bearer {}".format(token)
        }

        user_object = requests.get(url=url,headers=headers)
        user_json = user_object.json()
        return user_json
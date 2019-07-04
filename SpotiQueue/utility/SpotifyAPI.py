from urllib.parse import quote
import requests


class SpotifyAPI:
    def __init__(self):
        self.authorization_url = 'https://accounts.spotify.com/authorize'
        self.client_id = 'ce14133db3fd476680ab0859e62e4791'
        self.scopes = 'user-read-private user-read-email'
        self.redirect_url = 'http://127.0.0.1:8000/'

    def authorization_request(self):
        r = requests.get(url=self.build_authorization_url())
        print(r)

    def build_authorization_url(self):
        url = self.authorization_url + '?response_type=code' + '&client_id=' + self.client_id + \
              '&scope=' + quote(self.scopes.encode('utf-8')) + \
              '&redirect_uri=' + quote(self.redirect_url.encode('utf-8'))
        return url


if __name__ == "__main__":
    api = SpotifyAPI()
    print(api.authorization_request())

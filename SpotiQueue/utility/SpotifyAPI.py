from urllib.parse import quote


def authorization_request():
    authorization_url = 'https://accounts.spotify.com/authorize'
    client_id = 'ce14133db3fd476680ab0859e62e4791'
    scopes = 'user-read-email playlist-read-collaborative playlist-modify-private'
    redirect_url = 'http://127.0.0.1:8000/'

    url = authorization_url + '?response_type=code' + '&client_id=' + client_id + '&scope=' + \
          quote(scopes.encode('utf-8')) + '&redirect_uri=' + quote(redirect_url.encode('utf-8'))

    return url


if __name__ == "__main__":
    print(authorization_request())

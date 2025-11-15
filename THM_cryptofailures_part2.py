import requests
import urllib.parse
from passlib.hash import des_crypt
from string import printable


URL = "http://cryptofailures.thm" #update your /etc/hosts with the room's given IP
USER = "guest"
SEPARATOR = ":"


def get_secure_cookie(user_agent):
    session = requests.Session()
    response = session.get(URL, headers={"user":USER, "User-Agent":user_agent})
    cookie = session.cookies.get("secure_cookie")
    #avoids interpreted characters
    cookie = urllib.parse.unquote(cookie)
    return cookie

def build_bloc(secret, char, user_agent):
    bloc = USER + SEPARATOR + user_agent + SEPARATOR + secret + char
    return bloc[-8:]


secret = ""

progress = True
while progress:

    base = len(USER + SEPARATOR + SEPARATOR + secret)
    user_agent_length = (7 - base) % 8
    user_agent = "X" * user_agent_length

    progress = False
    # The program runs until there is no character found
    cookie = get_secure_cookie(user_agent)
    salt = cookie[:2]
    for char in printable:

        bloc = build_bloc(secret, char, user_agent)
        compared = des_crypt.hash(bloc, salt=salt)

        # I could check the exact part of the cookie but this check is sufficient
        if compared in cookie:
            secret += char
            # Print the result char by char because it's beautiful this way !
            print(char, end="", flush=True)
            progress = True
            break

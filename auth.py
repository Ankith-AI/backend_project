from keycloak import KeycloakOpenID
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

# Keycloak configuration
keycloak_openid = KeycloakOpenID(
    server_url="http://localhost:8080/auth",
    # server_url="http://localhost:8080",
    client_id="myclient",
    realm_name="myrealm"
)

# Define OAuth2 flow for FastAPI
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Function to get the current user (authenticated via Keycloak)
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        # Verify the token with Keycloak
        user_info = keycloak_openid.userinfo(token)
        if not user_info:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_info
    except Exception:
        raise HTTPException(status_code=401, detail="Could not validate credentials")


# Function to handle login and return access token
def login_user(username: str, password: str):
    try:
        # Get the token from Keycloak using the user's credentials
        token = keycloak_openid.token(username, password)
        return {
            "access_token": token['access_token'],
            "refresh_token": token['refresh_token']
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid credentials")

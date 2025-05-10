import requests
from time import sleep

BASE_URL: str = "https://popstool.io/api"

class CarParkTool:
    def __init__(self, access_key) -> None:
        self.auth_token = None
        self.access_key = access_key
    
    def login(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/account_login", params=params, data=payload)
        response_decoded = response.json()
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")
    
    def register(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/account_register", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("error")
    
    def delete(self):
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        requests.post(f"{BASE_URL}/account_delete", params=params, data=payload)

    def get_player_data(self) -> any:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/get_data", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded

    def hack_car_speed(self, car_id, new_hp, new_inner_hp, new_nm, new_torque):
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "new_hp": new_hp,
            "new_inner_hp": new_inner_hp,
            "new_nm": new_nm,
            "new_torque": new_torque,
        }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/hack_car_speed", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def max_max1(self, car_id, custom):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id,
        "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{BASE_URL}/max_max1", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def max_max2(self, car_id, custom):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id,
        "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{BASE_URL}/max_max2", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def millage_car(self, car_id, custom):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id,
        "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{BASE_URL}/millage_car", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def brake_car(self, car_id, custom):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id,
        "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{BASE_URL}/brake_car", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

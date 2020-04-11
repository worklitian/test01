import requests
import json

from dna_request_token import get_token

def get_device_list():
    token = get_token()
    api_path = "https://sandboxdnac.cisco.com/dna"
    headers = {"Content-type": "application/json", "X-Auth-Token": token}
    auth_resp = requests.get(
        f"https://sandboxdnac.cisco.com/api/v1/network-device", headers=headers
    )

    auth_resp.raise_for_status()

    device_list = auth_resp.json()
    return device_list

def main():
    device_list = get_device_list()
    print(device_list)

if __name__ == "__main__":
    main()
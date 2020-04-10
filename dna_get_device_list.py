import requests
from dna_requests_token import get_token

def get_device_list():
    token = get_token()
    api_path = "https://sandboxdnac.cisco.com/dna"
    headers = {"Content-type": "application/json", "X-Auth-Token": token}
    auth_resp = requests.get(
        f"{api_path}/intent/api/v1/network-device/", headers=headers
    )

    auth_resp.raise_for_status()
    device_list = {}
    for device in auth_resp.json()['response']:
        device_list[device["managementIpAddress"]] = device["id"]
    return device_list

def main():
    device_list = get_device_list()
    print(device_list)

if __name__ == "__main__":
    main()
# -------------------------------
# Performing Normal GET Request
# -------------------------------
import aiohttp
import asyncio
import requests
import certifi

# url: str = "https://jsonplaceholder.typicode.com/posts/1"

# try:
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         print("API Response: ")
#         print(data)
#     else:
#         print(f"Error: {response.status_code} - {response.text}")
# except requests.exceptions.RequestException as e:
#     print(f"An unuconditional Error Occured: {e}")

#
#
# --------------------------------------
#   Performing Weather API GET Request
# --------------------------------------
#
#

url: str = (
    "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,relative_humidity_2m,precipitation,wind_speed_120m"
)


try:
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        data = response.json()
        times = data["hourly"]["time"]
        temps = data["hourly"]["temperature_2m"]
        humidity = data["hourly"]["relative_humidity_2m"]

        print("Next 5 hours forecast:")
        for i in range(5):
            print(f"{times[i]}")
except requests.exceptions.RequestException as e:
    print(f"An unuconditional Error Occured: {e}")


# using async requests

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = response.json()
            print("from async: ",data)

asyncio.run(main())
print("Before async")

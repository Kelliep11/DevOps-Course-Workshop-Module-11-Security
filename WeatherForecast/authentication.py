import requests

reqUrl = "https://login.microsoftonline.com/7d6f97d6-d755-4c10-b763-409cc4b6638f/oauth2/v2.0/token"

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "Content-Type": "multipart/form-data; boundary=kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A" 
}

payload = "--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name=\"client_id\"\r\n\r\n650059b1-b991-42ed-a4be-c85d13f9de83\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name=\"client_secret\"\r\n\r\ndrv8Q~P6J_deYuf2L1ITkRQBqql.pmlgueraEb8m\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name=\"scope\"\r\n\r\napi://3d81ee40-6843-4e92-bf3f-a79a31a65618/.default\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name=\"grant_type\"\r\n\r\nclient_credentials\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A--\r\n"

response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

print(response.text)
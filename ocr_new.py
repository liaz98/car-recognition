import requests

url = "https://text-in-images-recognition.p.rapidapi.com/prod"

payload = {"objectUrl": "C:/Users/Mukhammad/Desktop/projects/car-predict/tex_data_front.jpg"}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "ae7678d039msh05134fa843e30a4p1b65bdjsn0ad0f398101a",
	"X-RapidAPI-Host": "text-in-images-recognition.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
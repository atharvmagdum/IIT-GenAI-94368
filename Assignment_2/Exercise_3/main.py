import requests
response = requests.get("https://jsonplaceholder.typicode.com/albums")
status_code = response.status_code
print("Status Code :", {status_code})

#print(response.text)
try:
    data=response.json()
    with open("json_data.txt",'w')as file:
        print(data)
        json.dump(data,file)
except:
    print("Errorrr!!")
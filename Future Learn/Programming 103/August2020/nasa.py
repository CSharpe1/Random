import requests
r = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
NASA = r.json()
print(NASA)
#with open("Future Learn\Programming 103\August2020\\nasa.json", "w") as f:
#    json.dump(data, f)


f = open("Future Learn\Programming 103\August2020\\NASA.txt", "a") #a appends to file, w makes new file     #"w")
f.write(str(NASA))
f.close()
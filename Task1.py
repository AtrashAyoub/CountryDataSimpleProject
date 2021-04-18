
import requests
from flask import Flask

app = Flask(__name__)
@app.route('/<country>')
def Task(country):
    url = "https://restcountries.eu/rest/v2/name/"+country+"?fullText=true"
    response = requests.get(url)
    if response.status_code != 200:
        return("Country not found!")
    else:
        res = '<h1>Welcome to Ayoub app</h1>'
        data = (response.json())
        Data_dic = data[0]
        res+="<b>Country’s Full Name: "+Data_dic['name']+'<br/>'
        res+="Country’s Capital: "+Data_dic['capital']+'<br/>'
        res+="Country’s Common Language: "+Data_dic["languages"][0]["name"]+'<br/>'
        res+="Country’s Currency Name: "+Data_dic['currencies'][0]["name"]+'<br/>'
        Curr_code= Data_dic['currencies'][0]["code"]
        curr_url = "http://data.fixer.io/api/latest?access_key=0f74f9e3e64cb0c2ce6ec5230dc7592d&format=1&symbols="+Curr_code
        curr_response = requests.get(curr_url)
        curr_data = (curr_response.json())
        res+="Country’s Currency rate: "+ str(curr_data["rates"][Curr_code])
        return(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0' , debug=True)
    
## Run the script, then open the webpage: "http://127.0.0.1:5000/<country>"
## and replace <country> with the relevant country
## for example: http://127.0.0.1:5000/aruba



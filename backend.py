import requests 

api_key = "bb8c487ce98c5273bfb29176ee18a6a9"

def get_data(place, forecast_days=None, kind=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response =  requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    
    if kind == "Temperature":
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    if kind == 'Sky':
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]   
    return data

if __name__ == '__main__':
    print(get_data(place='Tokyo'))
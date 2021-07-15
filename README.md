# Weather application

🌱🥬🌱🥬🌱🥬🌱🥬🌱🥬🌱🥬🌱🥬

### `Description`

A CLI weather information from [weatherapi.com](https://weatherapi.com) API and present it in a terminal. We will add some options that can be passed as arguments to the application, such as:

- The name of a city where you can get the weather information

### `Example`

```bash
$ python app -l <city_name>
$ python app -l rufisque
```

### Config file

- `config.json` :In this file you can set your API key provided by the weatherapi.com and the desired language. e.g LANG=fr or Lang=en or Lang=ar

```json
{
  "API_KEY": "<your_api_key>",
  "LANG": "<language_code>",
  "BASE_URL": "http://api.weatherapi.com/v1/current.json"
}
```

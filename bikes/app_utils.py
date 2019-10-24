from bikes import api_utils
from flask import Flask


app = Flask(__name__)
fun = api_utils.get_data_WB


@app.route("/<year>/<month>/<day>/<hour>/<minute>/<second>")
def weather(year, month, day, hour, minute, second):
    year, month, day = int(year), int(month), int(day)
    hour, minute, second = int(hour), int(minute), int(second)
    
    return fun(year, month, day, hour, minute, second)


@app.route("/<dep>/<year>/<month>/<day>/<hour>/<minute>/<second>/<arr>")
def station(dep, arr, year, month, day, hour, minute, second):
    request = {
        "departure_station": dep,
        "Year": int(year),
        "Month": int(month),
        "Day": int(day),
        "Hour": int(hour),
        "Minute": int(minute),
        "Second": int(second),
        "arrival_station": arr
    }
    
    return api_utils.get_all_infos(request)

    
@app.route("/<dep>/<year>/<month>/<day>/<hour>/<minute>/<second>/<arr>/<predict>")
def silly_predict(dep, arr, year, month, day, hour, minute, second, predict):
    request = {
        "departure_station": dep,
        "Year": int(year),
        "Month": int(month),
        "Day": int(day),
        "Hour": int(hour),
        "Minute": int(minute),
        "Second": int(second),
        "arrival_station": arr
    }
    print(request)
    return api_utils.get_silly_estimates(request)


if __name__ == "__main__":
    app.run()

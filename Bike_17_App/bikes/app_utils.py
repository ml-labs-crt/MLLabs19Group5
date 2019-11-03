import api_utils
from flask import Flask


app = Flask(__name__)
fun = api_utils.get_data_WB
# model = api_utils.load_yasser_model()


@app.route("/<year>/<month>/<day>/<hour>/<minute>/<second>")
def weather(year, month, day, hour, minute, second):
    year, month, day = int(year), int(month), int(day)
    hour, minute, second = int(hour), int(minute), int(second)
    
    return fun(year, month, day, hour, minute, second)


@app.route("/<dep>/<year>/<month>/<day>/<hour>/<minute>/<second>/<arr>")
def station(dep, arr, year, month, day, hour, minute, second):
    year, month, day = int(year), int(month), int(day)
    hour, minute, second = int(hour), int(minute), int(second)

    request = {
        "departure_station": dep,
        "Year": year,
        "Month": month,
        "Day": day,
        "Hour": hour,
        "Minute": minute,
        "Second": second,
        "arrival_station": arr
    }
    
    return api_utils.get_all_infos(request)

    
@app.route("/predict/<dep>/<year>/<month>/<day>/<hour>/<minute>/<second>/<arr>/")
def silly_predict(dep, arr, year, month, day, hour, minute, second):

    request = {
        "departure_station": dep,
        "Year": year,
        "Month": month,
        "Day": day,
        "Hour": hour,
        "Minute": minute,
        "Second": second,
        "arrival_station": arr
    }

    print("Attempting to load the Keras model! :O")
    model = api_utils.load_yasser_model()
    print("Model loaded successfully! :D")
    package = api_utils.get_all_infos(request)
    return api_utils.predict_packages(package, api_utils.get_average_behaviour)
    # return api_utils.predict_packages(package, model.predict)


@app.route("/data/<dep>/<year>/<month>/<day>/<hour>/<minute>/<second>/<arr>/")
def get_all_data(dep, arr, year, month, day, hour, minute, second):

    request = {
        "departure_station": dep,
        "Year": year,
        "Month": month,
        "Day": day,
        "Hour": hour,
        "Minute": minute,
        "Second": second,
        "arrival_station": arr
    }

    stations = api_utils.get_all_infos(request)
    conditions = weather(year, month, day, hour, minute, second)
    for key in stations.keys():
        stations[key].update(conditions)

    return stations
    


if __name__ == "__main__":
    app.run()

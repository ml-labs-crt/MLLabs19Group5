from bikes import api_utils
from flask import Flask


app = Flask(__name__)
fun = api_utils.get_data_WB


@app.route("/<year>/<month>/<day>/<hour>/<minute>/<second>")
def main(year, month, day, hour, minute, second):
    year, month, day = int(year), int(month), int(day)
    hour, minute, second = int(hour), int(minute), int(second)
    
    return fun(year, month, day, hour, minute, second)


if __name__ == "_main__":
    app.run()

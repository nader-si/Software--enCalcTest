from flask import Flask, request

app = Flask(__name__)

def sum_numbers(num1, num2):
    return num1 + num2

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            result = sum_numbers(num1, num2)
            return f"result: {result}"
        except ValueError:
            return "you are intered invalid value"
    else:
        return '''
            <form method="post">
                inputN1: <input type="text" name="num1"><br>
                inputN2: <input type="text" name="num2"><br>
                <input type="submit" value="SUM">
            </form>
        '''

if __name__ == "__main__":
    app.run("0.0.0.0",4444)

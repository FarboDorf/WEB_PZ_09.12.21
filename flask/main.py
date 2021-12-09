from flask import Flask, render_template, request, make_response
import datetime
import postgre

app = Flask(__name__)
users = [{"title": "Graph", "userName": "Persik"},
         {"title": "Lord", "userName": "Abrikos"}]


@app.route("/", methods=["GET", "POST"])
def index():
    if(request.method == "POST"):
        res = postgre.select()
        print(res)
        for user in res:
            title = user[10]
            userName = user[12]
            users.append({"title": title, "userName": userName})

        # title = request.form.get('title')
        # userName = request.form.get('userName')
        # users.append({"title": title, "userName": userName})
        # return f"{title} {userName}"
    return render_template("index.html",
                           time=datetime.datetime.now().replace(microsecond=False),
                           users=users)


if __name__ == '__main__':
    app.run(debug=True)

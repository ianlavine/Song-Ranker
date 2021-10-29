from flask import Flask, request, render_template
import user_data
import PythonRanker

app = Flask(__name__)

artists = user_data.return_artists(None)
artist_data = [{'name': artists[x].name} for x in range(len(artists))]

@app.route("/")
def index():
    # celsius = request.args.get("celsius", "")
    # if celsius:
    #     fahrenheit = fahrenheit_from(celsius)
    # else:
    #     fahrenheit = ""
    # return (
    #     """<form action="" method="get">
    #             <input type="text" name="celsius">
    #             <input type="submit" value="Convert">
    #           </form>"""
    #           + "Fahrenheit: " + fahrenheit
    # )

    choice = request.args.get("chosen_artist", "")
    if choice:
        album_data = get_albums(choice)
    else:
        album_data = []

    return render_template('index.html', artist_data=artist_data, album_data=album_data)


# def fahrenheit_from(celsius):
#     """Convert Celsius to Fahrenheit degrees."""
#     try:
#         fahrenheit = float(celsius) * 9 / 5 + 32
#         fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
#         return str(fahrenheit)
#     except ValueError:
#         return "invalid input"


def get_albums(artist):
    for art in artists:
        if artist == art.name:
            albums = [{'name': alb.name, 'on': str(art.Album_dict[alb])} for alb in art.Album_dict]
            return albums
    new_artist(artist)
    return get_albums(artist)

def new_artist(artist):
    artists.extend(user_data.return_artists([artist]))
    artist_data.append({'name': artists[-1].name})

def play(artist):
    game = PythonRanker.Play(artist)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
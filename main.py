from app import create_app, db
from app.models import User, Artist, Album, Song

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Artist': Artist, 'Album': Album, 'Song': Song}
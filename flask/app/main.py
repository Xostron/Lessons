from app import app
from app import db
from blueprint import posts
import view




app.register_blueprint(posts, url_prefix='/blog')
print(f"1 @@@@@@@@@@@@ {posts}")
if __name__ == "__main__":
    app.run()
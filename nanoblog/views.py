from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from nanoblog.models import Post

posts = Blueprint('posts', __name__, template_folder='templates')


class ListView(MethodView):

    def get(self):
        posts = Post.objects.all()
        return render_template('posts/list.html', posts=posts)

class JsonView(MethodView):
    def get(self):
        posts = Post.objects.all()
        return render_template('posts/list.json', posts=posts)

def register_blueprints(app):
    # Prevents circular imports
    app.register_blueprint(posts)

# Register the urls
posts.add_url_rule('/', view_func=ListView.as_view('list'))
posts.add_url_rule('/json', view_func=JsonView.as_view('json'))

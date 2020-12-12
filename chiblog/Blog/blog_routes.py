from flask import render_template, url_for, request, flash, Blueprint, redirect
from chiblog import db
from chiblog.Blog.blog_model import Blog, Category
from flask_login import login_required

blog = Blueprint('blog', __name__)

@blog.route('/blogs/new', methods=['GET', 'POST'])
@login_required
def new_blog():
    if request.method == 'POST':
        blog = Blog(title=request.form["title"], content=request.form["content"])
        category = Category.query.filter_by(name= request.form["category"]).first()
        if category:
            blog.category = category
        else:
            category = Category(name = request.form["category"])
            blog.category = category
        db.session.add(blog)
        db.session.commit()
        flash('Your post has been created!', 'dark')
        return redirect(url_for('blog.blogs'))
    return render_template('create_post.html', title='New Blog', legend="Create a Post")

@blog.route('/blogs')
@blog.route('/blogs/')
def blogs():
    page = request.args.get('page', 1, type=int)
    blogs = Blog.query.order_by(Blog.created_at.desc()).paginate(page=page, per_page=5)
    return render_template('blogs.html', posts=blogs)

@blog.route("/blogs/<int:blog_id>")
def one_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    return render_template('oneblog.html', title=blog.title, blog=blog)

@blog.route("/blogs/<int:blog_id>/update", methods=['GET', 'POST'])
@login_required
def update_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    if request.method == "POST":
        blog.title = request.form["title"]
        blog.content = request.form["content"]
        category = Category.query.filter_by(name= request.form["category"]).first()
        if category:
            blog.category = category
        else:
            category = Category(name = request.form["category"])
            blog.category = category
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('blog.one_blog', blog_id=blog.id))
    return render_template('create_post.html', title="Update Blog", legend='Update Post', blog=blog)

@blog.route("/blogs/<int:blog_id>/delete", methods=['POST'])
@login_required
def delete_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    db.session.delete(blog)
    db.session.commit()
    flash('Your post has been deleted!', 'dark')
    return redirect(url_for('blog.blogs'))

@blog.route("/category/<string:category>", methods=['GET'])
@blog.route("/category/<string:category>/", methods=['GET'])
def category_blog(category):
    cat = Category.query.filter_by(name= category).first()
    page = request.args.get('page', 1, type=int)
    blogs = Blog.query.filter_by(category = cat).order_by(Blog.created_at.desc()).paginate(page=page, per_page=5)
    return render_template('category.html', blogs = blogs, legend = category)

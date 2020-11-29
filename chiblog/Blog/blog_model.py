from datetime import datetime
from chiblog import db

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String, nullable=True, default = 'default.jpg')
    created_at = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref= db.backref('blogs', lazy=True))
    #lazy is how the database is loaded

    def __repr__(self):
        return f"Blog('{self.title}', '{self.created_at}')"

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), default = 'story')

    def __repr__(self):
        return f"Category('{self.name}')"


""" from chiblog import db
from datetime import datetime

class Blog():
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f"Blog('{self.title}', '{self.created_at}')" """



""" tag_blog = db.Table('tag_blog',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('blog_id', db.Integer, db.ForeignKey('blog.id'), primary_key=True)
)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(50), nullable=False)
    content=db.Column(db.Text, nullable=False)
    feature_image=db.Column(db.String, nullable=True)
    create_at=db.Column(db.DateTime, default=datetime.utcnow)
    tags=db.relationship('Tag', secondary = tag_blog, backref = db.backref('blogs_associated', lazy='dynamic'))

    @property
    def serialize(self): #return data in JSON format
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'feature_image': self.feature_image,
            'created_at': self.create_at
        }

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        } """


from datetime import datetime
from chiblog import db

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20), nullable=True, default = 'default.jpg')
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



from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField
from wtforms.validators import Required

class NewBlogpost(FlaskForm):
    title = StringField("Post Title", validators=[Required()])
    # image = FileField("Post image", validators=[Required()])
    author = StringField("Author's name", validators=[Required()])
    post_content= TextAreaField("Post content")
    submit = SubmitField("Create Post")
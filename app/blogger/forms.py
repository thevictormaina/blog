from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField
from wtforms.validators import Required, Email

class NewBlogpost(FlaskForm):
    title = StringField("Post Title", validators=[Required()])
    # image = FileField("Post image", validators=[Required()])
    author = StringField("Author's name", validators=[Required()])
    post_content= TextAreaField("Post content")
    submit = SubmitField("Create Post")

class CommentForm(FlaskForm):
    name = StringField("Full name", validators=[Required()])
    email = StringField("Email address", validators=[Required(), Email()])
    comment = TextAreaField("Comment", validators=[Required()])
    submit = SubmitField("Submit")
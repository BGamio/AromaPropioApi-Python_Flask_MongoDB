from djongo import models

class User(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=255)
    birth_date = models.DateField()

    class Meta:
        abstract = True

class Comment(models.Model):
    user_name = models.EmbeddedField(model_container=User)
    comment = models.TextField()
    published_at = models.DateTimeField()

    class Meta:
        abstract = True

class Post(models.Model):
    post_photo_url = models.CharField(max_length=255)
    published_at = models.DateTimeField()
    content = models.TextField()
    users = models.EmbeddedField(model_container=User)
    comments = models.ArrayField(model_container=Comment)

class Resennia(models.Model):
    published_at = models.DateTimeField()
    content = models.TextField()
    users = models.ArrayField(model_container=User)

class IdType(models.Model):
    id = models.IntegerField()
    description = models.CharField(max_length=250)

    class Meta:
        abstract = True

class LibroDeReclamaciones(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_type = models.EmbeddedField(model_container=IdType)
    department = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    mail = models.EmailField()
    message = models.TextField()
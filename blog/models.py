"""Import relevant modules for the application"""

from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, 'Draft'), (1, 'Published'))


class Category(models.Model):
    """
    This class creates the Category model.
    """

    name = models.CharField(max_length=255, unique=True)

    class Meta:
        """
        This meta class orders the model by name.
        """

        ordering = ['name']

    def __str__(self):
        """
        This function returns the name of the category
        to add user readability.
        """

        return str(self.name)


CATEGORY_CHOICES = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in CATEGORY_CHOICES:
    choice_list.append(item)


class Post(models.Model):
    """
    This class creates the blog post model.
    """

    title = models.CharField(max_length=255, unique=True)
    blog_headline = models.CharField(max_length=255, null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts")
    body = models.TextField()
    category = models.CharField(max_length=255, default='Uncategorized',
                                choices=choice_list)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        This meta class orders the model by date.
        """

        ordering = ['-date_created_on']

    def __str__(self):
        """
        This function returns the title
        to add better user readability.
        """

        return self.title

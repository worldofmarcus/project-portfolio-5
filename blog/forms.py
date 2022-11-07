class CreateBlogPostForm(forms.ModelForm):
    """
    This class creates the blog form.
    """

    class Meta:
        """
        This meta class adds the fields to the form
        based on the post model. It also adds a number
        of widgets to customize and add functionality
        to the form.
        """

        model = Post
        fields = ('title', '', 'featured_image', 'body',
                  'category', 'status',)

        widgets = {
                        'category': forms.Select(
                            attrs={'class': 'form-select'}),
                        'status': forms.Select(attrs={'class': 'form-select'}),
                        }

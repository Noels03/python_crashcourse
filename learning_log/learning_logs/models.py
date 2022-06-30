from django.db import models


#####Topic class defines model's basic funcionality#####
class Topic(models.Model):
    """A topic that a use is learning about."""
    #####Reserves space for Topic name#####
    text = models.CharField(max_length=200)
    #####automatically sets records dat and time when user creates new Topic#####
    date_added = models.DateTimeField(auto_now_add=True)

    #####displays a simple representation of a model####
    def __str__(self):
        """Return a string representation of the model."""
        return self.text
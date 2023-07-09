from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

""" class Question(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions_to_review', blank=True, null=True)

    def __str__(self):
        return self.text

class QuestionForm(formset_factory.ModelForm):
    teacher = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Teacher'))

    class Meta:
        model = Question
        fields = ('text',)


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

   """


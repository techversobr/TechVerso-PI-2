from django.db import models

class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Novo campo
    contract_type = models.CharField(
        max_length=50,
        choices=[
            ('CLT', 'CLT'),
            ('PJ', 'PJ'),
            ('Estágio', 'Estágio'),
            ('Freelancer', 'Freelancer'),
        ],
        null=True,
        blank=True
    )  # Novo campo
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
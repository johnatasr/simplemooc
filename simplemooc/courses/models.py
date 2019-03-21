from django.urls import reverse
from django.db import models

class CourseManager(models.Model):
    def search(self, query):
        return self.get_queryset().filter(
           models.Q(name__icontains=query) | \
           models.Q(descripition__icontains=query)
    )

class Course(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho', blank=True, unique=True)
    text = models.TextField('Descrição simples', blank=True)
    about = models.TextField('Sobre o curso', blank=True)
    start_date = models.DateField('Data de  Início',
                null=True, blank=True
        )
    image = models.ImageField(
        upload_to='courses/images', verbose_name='image')

    created_at = models.DateTimeField(

        'Criado em ', auto_now_add=True
    )
    edited_at = models.DateTimeField(
        'Editado em ', auto_now=True
    )


    objects = CourseManager()

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('courses:details', args=[self.slug])

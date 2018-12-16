from django.db import models

# Create your models here.


class Author(models.Model):

    name = models.CharField(max_length=20)

    email = models.EmailField()

    descript = models.TextField()

    def __unicode__(self):

        return u'%s' %(self.name)



class Tag(models.Model):

    tag_name = models.CharField(max_length=20)

    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):

        return u'%s' %(self.tag_name)




class Blog(models.Model):

    title = models.CharField(max_length=45)

    body = models.TextField()

    tags = models.ManyToManyField(Tag,blank=True)

    author = models.ForeignKey(Author,on_delete=models.SET('huanzai'))

    publish_time = models.DateTimeField(auto_now_add=True)

    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):

        return u'%s %s %s' %(self.title,self.author,self.publish_time)

    class Meta:

        ordering = ['-publish_time']







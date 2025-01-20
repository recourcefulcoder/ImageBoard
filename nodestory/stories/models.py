from django.contrib.auth import get_user_model
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)


class ClosureTable(models.Model):
    ancestor_id = models.IntegerField()
    descendant_id = models.IntegerField()
    depth = models.SmallIntegerField()


class StoryManager(models.Manager):
    def create(self, ancestor_id: int = None, **kwargs):
        created_object = super(StoryManager, self).create(**kwargs)
        if ancestor_id:
            records = ClosureTable.objects.filter(descendant_id=ancestor_id)
            for record in records:
                ClosureTable.objects.create(
                    ancestor_id=record.ancestor_id,
                    descendant_id=created_object.pk,
                    depth=1 + record.depth,
                )
        else:
            ClosureTable.objects.create(
                ancestor_id=created_object.pk,
                descendant_id=created_object.pk,
                depth=0,
            )


class StoryNode(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        null=True,
        on_delete=models.SET_NULL,
    )
    # NULL will mean that post's author account is deleted
    text = models.TextField()
    tags = models.ManyToManyField(Tag)
    objects = StoryManager()

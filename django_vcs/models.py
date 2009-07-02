from itertools import count

from django.db import models

from pyvcs.backends import AVAILABLE_BACKENDS, get_backend

REPOSITORY_TYPES = zip(count(), AVAILABLE_BACKENDS.keys())

class CodeRepository(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    repository_type = models.IntegerField(choices=REPOSITORY_TYPES)

    location = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s: %s" % (self.get_repository_type_display(), self.name)

    @property
    def repo(self):
        if hasattr(self, '_repo'):
            return self._repo
        self._repo = get_backend(self.get_repository_type_display())(self.location)
        return self._repo

    def get_recent_commits(self, since=None):
        return self.repo.get_recent_commits(since=since)

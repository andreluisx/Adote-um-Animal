"""
Database models
"""

from django.utils import timezone
from django.db import models
import uuid
from ourAnimal import settings


class BaseModelManager(models.Manager):
    """Manager for timestamps and soft delete"""
    
    def get_by_natural_key(self, natural_key):
        return self.get(id=natural_key)

    def active(self):
        """Retrieve non-deleted records."""
        return self.filter(deleted_at__isnull=True)

    def soft_deleted(self):
        """Retrieve soft-deleted records."""
        return self.filter(deleted_at__isnull=False)

    def by_created_at(self, start=None, end=None):
        """Filter records by created_at timestamp range."""
        queryset = self.get_queryset()
        if start:
            queryset = queryset.filter(created_at__gte=start)
        if end:
            queryset = queryset.filter(created_at__lte=end)
        return queryset

    def by_updated_at(self, start=None, end=None):
        """Filter records by updated_at timestamp range."""
        queryset = self.get_queryset()
        if start:
            queryset = queryset.filter(updated_at__gte=start)
        if end:
            queryset = queryset.filter(updated_at__lte=end)
        return queryset


class BaseModel(models.Model):
    """Model for adding timestamps and soft delete"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = BaseModelManager()

    class Meta:
        abstract = True  # Set this to True to create an abstract base model

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

class UserIndexedModel(BaseModel):
    """Model for adding the responsible user"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True  # Set this to True to create an abstract base model
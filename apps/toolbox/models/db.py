"""Models for `toolbox` app."""

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.utils.html import format_html
from django_extensions.db import fields
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager

from apps.images.handlers import UUIDFilename

upload_dir = UUIDFilename("upload/")


class Category(MPTTModel):
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")

    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "category"

    def __str__(self):
        return f"{self.title}"


class ToolBox(models.Model):
    slug = fields.RandomCharField(
        length=12,
        unique=True,
        include_alpha=False,
        db_index=True,
        editable=False,
    )
    icon = models.ImageField(upload_to=upload_dir)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    url = models.URLField(max_length=255)
    is_published = models.BooleanField(default=True)

    tags = TaggableManager(blank=True)

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = "toolbox"
        verbose_name_plural = "tool box"

    def __str__(self):
        return f"{self.title}"

    @admin.display(description="icon")
    def logo_thumb(self) -> str:
        if self.icon.url:
            return format_html(
                f'<img src="{self.icon.url}" "width="64" height="64" />'
            )
        else:
            return format_html(
                '<img src="https://via.placeholder.com/128/?text=cypherhunter" width="64" height="64" />'
            )

from django.db import models

#adding task list model
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class TaskList(models.Model):
    name = models.CharField(_("Tasklist Name"), max_length=255)
    slug = models.CharField(_("Tasklist Slug"), max_length=255)

    tasks: QuerySet["Task"]
    
    class Meta:
        verbose_name = "Task List"
        verbose_name_plural = "Task Lists"
        
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self) -> str:
        return reverse("tasklist-detail", kwargs={"slug": self.slug})

    @property
    def is_complete(self) -> bool:
        return not self.tasks.filter(is_done=False).exists()

    @property
    def complete_tasks(self) -> models.QuerySet["Task"]:
        return self.tasks.filter(is_done=True)

    @property
    def incomplete_tasks(self) -> models.QuerySet["Task"]:
        return self.tasks.filter(is_done=False)
# Create your models here.

class Task(models.Model):
    task_list = models.ForeignKey(
        TaskList,
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    name = models.CharField(_("Task Name"),max_length=255)
    completed = models.BooleanField(_("Task Is Done"), default=False)
    deleted = models.BooleanField(default=False)
    dueDate = models.DateTimeField()
    startDate = models.DateTimeField()
    
    class Meta:
        verbose_name = "Task Item"
        verbose_name_plural = "Task Items"

    def __str__(self):
        return self.name
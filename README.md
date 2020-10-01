# django_view_models

## Installation/Usage
- `pip install django_view_models`
- add `django_view_models` to `INSTALLED_APPS`
- define view models
- `python manage.py sync_view_models`

## Defining View Models

```python
from django.db import models
from django_view_models.models import ViewModel, MaterializedViewModel

class GoodBook(ViewModel):
    VIEW_DEF...
```
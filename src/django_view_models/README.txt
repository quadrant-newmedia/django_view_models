This is a simple module to make it easier to create django models backed by
views (or materialzed views) instead of regular tables.

Designed for Postgres, but should work with other DBs.

You need to subclass ViewModel (or MaterializedViewModel), declare your fields
as usual, and then provide the view definition in the model's VIEW_DEFINITION
property (only the select statement - no "create view" part).

This module provides management commands for creating the views from your models,
and for refreshing your materialized views. Views are never created automatically.

IMPORTANT - creating the views will first DROP ... CASCADE them.
So if view B depends on view A, creating view A will drop view B,
and you'll need to create view B again.

You may also call the create_view and/or refresh_view class methods on your model.

When using this module, it is recommended to call sync_view_models as part of your
deployment strategy, or to write data migrations that call these methods
whenever you change your views.
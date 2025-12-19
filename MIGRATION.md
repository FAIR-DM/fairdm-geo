# FairDM Geo Migration Guide

## Overview

FairDM Geo has been completely modernized to align with the current FairDM framework API. This guide explains what changed and how to migrate existing code.

## Breaking Changes

### 1. Plugin System Rewrite

**Old API (❌ Broken):**
```python
# Old - DOES NOT WORK
from fairdm import plugins
from fairdm.layouts import ApplicationLayout

class Map(plugins.Explore, ApplicationLayout, TemplateView):
    menu_item = {
        "name": _("Map"),
        "icon": "map",
    }

@plugins.project.register()
class ProjectMap(Map):
    pass
```

**New API (✅ Current):**
```python
# New - Modern FairDM API
from fairdm import plugins
from django.views.generic import TemplateView

@plugins.register(Project, Dataset)
class Map(plugins.FairDMPlugin, TemplateView):
    title = _("Map")
    menu_item = plugins.PluginMenuItem(
        name=_("Map"),
        category=plugins.EXPLORE,
        icon="map",
    )
    template_name = "fairdm_geo/plugins/map.html"
```

**Key Changes:**
- ❌ Removed: `plugins.Explore` base class
- ❌ Removed: `ApplicationLayout` mixin
- ❌ Removed: `@plugins.project.register()` decorator
- ✅ Added: `@plugins.register(Model1, Model2)` decorator
- ✅ Added: `plugins.FairDMPlugin` base class
- ✅ Changed: `menu_item` is now `PluginMenuItem` object, not dict
- ✅ Changed: Access model instance via `self.base_object`

### 2. Model Registration System

**Old API (❌ Broken):**
```python
# Old - DOES NOT WORK
import fairdm
from fairdm.metadata import ModelConfig
from fairdm_geo.metadata import FairDMGeoMeta

@fairdm.register(GenericSite)
class GenericSiteConfig(FairDMGeoMeta, ModelConfig):
    description = "..."
    fields = [...]
```

**New API (✅ Current):**
```python
# New - Modern FairDM API
from fairdm import register
from fairdm.registry import ModelConfiguration, ModelMetadata, Authority

@register
class GenericSiteConfig(ModelConfiguration):
    model = GenericSite
    
    metadata = ModelMetadata(
        description="...",
        authority=Authority(
            name="Your Team",
            website="https://example.com"
        ),
        keywords=["geology", "site"],
    )
    
    fields = [...]
```

**Key Changes:**
- ❌ Removed: `@fairdm.register(Model)` - model as decorator argument
- ❌ Removed: `ModelConfig` import from `fairdm.metadata`
- ❌ Removed: `FairDMGeoMeta` mixin
- ✅ Changed: Use `@register` decorator (no arguments)
- ✅ Changed: Specify model with `model = YourModel` attribute
- ✅ Changed: Inherit from `ModelConfiguration`
- ✅ Changed: Use `ModelMetadata`, `Authority`, `Citation` objects

### 3. Template Structure

**Old (❌ Broken):**
```django
{% extends "base.html" %}
{% block content %}
  <c-layouts.standard>
    {{ plot|safe }}
  </c-layouts.standard>
{% endblock %}
```

**New (✅ Current):**
```django
{% extends "fairdm/plugin.html" %}

{% block plugin %}
  <div class="map-container">
    {{ plot|safe }}
  </div>
{% endblock %}
```

**Key Changes:**
- ❌ Removed: Extending `base.html` directly
- ❌ Removed: `<c-layouts.standard>` wrapper
- ✅ Changed: Extend `fairdm/plugin.html`
- ✅ Changed: Use `{% block plugin %}` instead of `{% block content %}`

### 4. Addon Setup

**Old (❌ Missing):**
```python
# No setup infrastructure
```

**New (✅ Current):**
```python
# fairdm_geo/__init__.py
__fdm_setup_module__ = "fairdm_geo.settings"

# fairdm_geo/apps.py
class EarthScienceConfig(AppConfig):
    def ready(self):
        import fairdm_geo.config   # Register models
        import fairdm_geo.plugins  # Register plugins
```

**Key Changes:**
- ✅ Added: `__fdm_setup_module__` in `__init__.py`
- ✅ Added: `ready()` method in `AppConfig` to import config/plugins
- ✅ Added: `settings.py` module for addon configuration

### 5. Admin Registration

**Old (❌ Removed):**
```python
# fairdm_geo/admin.py
class RockSampleAdmin(admin.ModelAdmin):
    pass

for model in EARTH_SAMPLES:
    m = apps.get_model("fairdm_geo", model)
    admin.site.register(m, RockSampleAdmin)
```

**New (✅ Auto-generated):**
```python
# No admin.py needed!
# FairDM auto-generates admin from ModelConfiguration
```

**Key Changes:**
- ❌ Removed: Custom `admin.py` file
- ✅ Changed: Admin is auto-generated from `ModelConfiguration`

## Migration Steps

### Step 1: Update Plugin Classes

1. Open `fairdm_geo/plugins.py`
2. Replace all plugin classes using the new API pattern
3. Remove inheritance from `plugins.Explore` and `ApplicationLayout`
4. Change to `@plugins.register(Model1, Model2)` decorator
5. Inherit from `plugins.FairDMPlugin` + Django view class
6. Convert `menu_item` dict to `PluginMenuItem` object

### Step 2: Update Model Configurations

1. Create `fairdm_geo/config.py` if it doesn't exist
2. Import from `fairdm.registry`, not `fairdm.metadata`
3. Use `@register` decorator without arguments
4. Set `model = YourModel` as class attribute
5. Create `ModelMetadata` with `Authority` and description
6. Remove any `FairDMGeoMeta` mixin usage

### Step 3: Update App Configuration

1. Add `__fdm_setup_module__ = "fairdm_geo.settings"` to `__init__.py`
2. Create `settings.py` with `EARTH_SAMPLES` list
3. Add `ready()` method to `AppConfig` that imports `config` and `plugins`

### Step 4: Update Templates

1. Change `{% extends "base.html" %}` to `{% extends "fairdm/plugin.html" %}`
2. Change `{% block content %}` to `{% block plugin %}`
3. Remove any `<c-layouts.standard>` wrappers
4. Access model via `{{ base_object }}` in templates

### Step 5: Remove Legacy Files

1. Delete `admin.py` - no longer needed
2. Delete or update old `conf.py` files
3. Update `metadata.py` or remove if no longer needed

### Step 6: Test Everything

1. Run migrations: `python manage.py migrate`
2. Check model registration: `python manage.py show_models`
3. Check plugin registration: Access a Project/Dataset detail page
4. Verify map plugin appears and works
5. Check admin interface for registered models

## Troubleshooting

### Plugin Not Appearing

**Problem:** Map plugin doesn't show in menu

**Solutions:**
- Verify `fairdm_geo` is in `INSTALLED_APPS`
- Check `apps.py` has `ready()` method that imports `plugins`
- Ensure `@plugins.register()` decorator is present
- Verify models are imported correctly (Project, Dataset)

### Model Not Registered

**Problem:** Model doesn't appear in admin or can't be used

**Solutions:**
- Check `EARTH_SAMPLES` setting includes the model name
- Verify `@register` decorator is on the config class
- Ensure `ready()` method imports `config` module
- Run `python manage.py migrate` to create tables

### Template Not Found

**Problem:** `TemplateDoesNotExist` error

**Solutions:**
- Verify template path matches `template_name` attribute
- Check template is in `fairdm_geo/templates/fairdm_geo/plugins/`
- Ensure template extends `fairdm/plugin.html`

### Import Errors

**Problem:** `ImportError: cannot import name 'X'`

**Solutions:**
- Update import paths:
  - `fairdm.metadata.ModelConfig` → `fairdm.registry.ModelConfiguration`
  - `fairdm.metadata.Authority` → `fairdm.registry.Authority`
- Remove imports of removed classes:
  - `plugins.Explore`
  - `ApplicationLayout`
  - `FairDMGeoMeta`

## Reference Implementation

The fairdm-discussions addon demonstrates all modern patterns:
- https://github.com/FAIR-DM/fairdm-discussions

Use it as a reference for:
- Plugin registration
- Model configuration
- Template structure
- Addon setup

## Questions?

If you encounter issues not covered in this guide:
1. Check the FairDM documentation: https://fairdm.org
2. Review the fairdm-discussions reference implementation
3. Open an issue: https://github.com/FAIR-DM/fairdm-geo/issues

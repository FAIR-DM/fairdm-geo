# FairDM Geo - Changelog

## Version 0.3.0 - Multi-App Architecture (December 19, 2025)

### 🏗️ Breaking Changes - Complete Restructuring

Restructured from a single Django app to a multi-app architecture following Django best practices.

#### New Structure

**Apps:**
- `fairdm_geo.core` - Abstract base models (GenericEarthSample, GenericHole, intervals)
- `fairdm_geo.rocks` - Concrete rock sample models (RockSample, DrillCore, etc.)
- `fairdm_geo.sites` - Concrete sampling location models (SamplingLocation, Borehole)

**Installation:**
```python
INSTALLED_APPS = [
    ...
    "fairdm_geo.core",
    "fairdm_geo.rocks", 
    "fairdm_geo.sites",
]
```

### ❌ Removed (Breaking)

- **EARTH_SAMPLES setting**: No longer needed - models are always concrete
- **utils.is_abstract()**: Removed anti-pattern of dynamic `abstract` status
- **Single config.py**: Split into separate config modules per app
- **Single settings.py**: Each app now has its own settings (currently minimal)
- **models/ directory**: Models moved to app-specific locations

### ✨ Added

- **Core app** (`fairdm_geo.core`):
  - Abstract base models in `core/models/base.py`
  - All interval classes (Interval, VerticalInterval, GeoDepthInterval)
  - GenericEarthSample and GenericHole base classes

- **Rocks app** (`fairdm_geo.rocks`):
  - BaseRock abstract model
  - 5 concrete models: RockSample, DrillCore, DrillCuttings, ThinSection, RockPowder
  - Dedicated config.py with model registrations
  - App dependency checking (requires core)

- **Sites app** (`fairdm_geo.sites`):
  - 2 concrete models: SamplingLocation, Borehole
  - Dedicated config.py with model registrations
  - App dependency checking (requires core)

- **MIGRATION_GUIDE.md**: Complete migration guide from v0.2.0 to v0.3.0

### 🔧 Modified

- **Static abstract flags**: All models now have `abstract = False` (concrete) or `abstract = True` (base classes)
  - No more dynamic abstract status based on settings
  - Stable migrations that don't break when configuration changes

- **Backward compatibility**:
  - `fairdm_geo/__init__.py` exports models for old import paths
  - `fairdm_geo/apps.py` shows deprecation warning but still works
  - Old imports like `from fairdm_geo.models import RockSample` still work

- **App dependencies**: Each app checks for required dependencies in `ready()` method
  - Rocks and Sites require Core to be installed first
  - Clear error messages if dependencies missing

### 📚 Benefits

1. **Stable Migrations**: Models always have same abstract status, no migration chaos
2. **Selective Installation**: Install only apps you need (e.g., just rocks)
3. **Clear Dependencies**: Explicit app installation in INSTALLED_APPS
4. **Django Best Practices**: Standard patterns, better IDE support
5. **Domain-Driven**: Separate apps for rocks vs sites makes sense conceptually

### 📋 Migration Steps

See MIGRATION_GUIDE.md for complete instructions. Summary:

1. Replace `"fairdm_geo"` in INSTALLED_APPS with three apps
2. Remove EARTH_SAMPLES setting
3. Run new migrations for each app
4. Optionally update imports to use new paths

## Version 0.2.0 - Streamlined Focus (December 19, 2025)

### 🎯 Focus Change

Refocused fairdm-geo to be a **models and vocabularies addon** rather than a full-featured plugin collection. Visualization and analysis features will be developed as separate dedicated addons.

### ❌ Removed

- **Map Plugin**: Removed Plotly-based map visualization plugin
  - Will be recreated as a separate dedicated addon with better features
  - Deleted `plugins.py` implementation (replaced with placeholder)
  - Deleted plugin templates directory
  - Removed `plotly` dependency

- **Geospatial Settings**: Removed unused coordinate configuration
  - `CRS` setting (not used by models - FairDM core handles geospatial)
  - `X_COORD` and `Y_COORD` precision settings (not used)
  - Icon aliases (not used)

- **Documentation**: Removed MIGRATION.md
  - No longer highlighting legacy patterns
  - Focus on current, clean API only

### 🔧 Modified

- **`plugins.py`**: Now a placeholder for future plugins
- **`settings.py`**: Simplified to only `EARTH_SAMPLES` configuration
- **`apps.py`**: Removed plugins import from `ready()` method
- **README.md**: Complete rewrite focusing on:
  - Models and vocabularies as core features
  - Clear, concise usage examples
  - No mention of legacy APIs or migration paths
  - Project structure and contribution guidelines

### 📋 Current Focus

FairDM Geo now provides:
- ✅ Ready-to-use geoscience sample models (RockSample, DrillCore, etc.)
- ✅ Sampling feature models (SamplingLocation, Borehole)
- ✅ ODM2 controlled vocabulary integration
- ✅ Well-documented model hierarchy
- ✅ Simple configuration via `EARTH_SAMPLES` setting

Visualization plugins will be developed separately as dedicated addons.

## Version 0.1.0 - API Modernization (December 19, 2025)

### 🔄 Major Changes - Complete API Rewrite

This release completely modernizes fairdm-geo to align with the current FairDM framework API. The addon was lagging behind the framework's evolution and required a comprehensive update.

### ✅ Added

#### Addon Infrastructure
- **`__init__.py`**: Added `__fdm_setup_module__ = "fairdm_geo.settings"` for FairDM addon integration
- **`settings.py`**: New addon settings module defining:
  - `EARTH_SAMPLES` list for model registration control
  - Geospatial configuration (`CRS`, `X_COORD`, `Y_COORD`)
  - Icon aliases for geoscience UI elements
  
#### Model Configuration System
- **`config.py`**: New model registration system using modern FairDM API
  - 7 model configurations with `@register` decorator
  - `ModelConfiguration` base class with `ModelMetadata`
  - Comprehensive metadata for each model (description, authority, keywords)
  - Model configs for: `RockSample`, `DrillCore`, `DrillCuttings`, `ThinSection`, `RockPowder`, `SamplingLocation`, `Borehole`

#### Plugin System
- **`plugins.py`**: Complete rewrite using modern plugin API
  - Single `Map` plugin registered to `Project` and `Dataset`
  - Uses `@plugins.register(Model1, Model2)` decorator
  - Inherits from `plugins.FairDMPlugin` + `TemplateView`
  - `PluginMenuItem` with `category=plugins.EXPLORE`
  - Improved map generation with better error handling
  - Context includes sample count and null checks

#### App Configuration
- **`apps.py`**: Added `ready()` method to import config and plugins modules
  - Enables auto-discovery of model registrations
  - Enables auto-discovery of plugin registrations

#### Documentation
- **`README.md`**: Complete rewrite with modern usage examples
- **`MIGRATION.md`**: Comprehensive migration guide for upgrading from old API
- Both documents include:
  - Installation instructions
  - Configuration examples
  - Usage patterns
  - Troubleshooting guides

#### Template Updates
- **`templates/fairdm_geo/plugins/map.html`**: Updated to modern plugin template structure
  - Extends `fairdm/plugin.html` (not `base.html`)
  - Uses `{% block plugin %}` (not `{% block content %}`)
  - Improved user feedback for empty states
  - Better Bootstrap 5 styling

### ❌ Removed

#### Deprecated Files
- **`admin.py`**: Deleted custom admin registration (now auto-generated by FairDM)
- **`conf.py`**: Deleted old AppConf-based settings (replaced by `settings.py`)
- **`example/config.py`**: Deleted example using old API
- **Duplicate template**: Removed `map copy.html`

#### Deprecated Classes & Patterns
- `plugins.Explore` base class (never existed in current FairDM)
- `ApplicationLayout` mixin (never existed in current FairDM)
- `@plugins.project.register()` decorator syntax
- `@plugins.dataset.register()` decorator syntax
- Dict-based `menu_item` configuration
- `FairDMGeoMeta` mixin class (deprecated but file retained for reference)
- Old `@fairdm.register(Model)` pattern (model as decorator argument)
- Import from `fairdm.metadata.ModelConfig`

### 🔧 Modified

#### Core Files
- **`utils.py`**: 
  - Converted lambda functions to proper documented functions
  - Updated to import from `fairdm_geo.settings` instead of Django settings
  - Added type hints and docstrings

- **`metadata.py`**: 
  - Marked as deprecated with clear migration instructions
  - Retained for backwards compatibility reference
  - Points to `config.py` for current metadata definitions

### 📋 Technical Details

#### Plugin System Changes

**Old (Broken):**
```python
class Map(plugins.Explore, ApplicationLayout, TemplateView):
    menu_item = {"name": _("Map"), "icon": "map"}

@plugins.project.register()
class ProjectMap(Map):
    pass
```

**New (Current):**
```python
@plugins.register(Project, Dataset)
class Map(plugins.FairDMPlugin, TemplateView):
    title = _("Map")
    menu_item = plugins.PluginMenuItem(
        name=_("Map"),
        category=plugins.EXPLORE,
        icon="map",
    )
```

#### Model Registration Changes

**Old (Broken):**
```python
@fairdm.register(GenericSite)
class GenericSiteConfig(FairDMGeoMeta, ModelConfig):
    description = "..."
```

**New (Current):**
```python
@register
class GenericSiteConfig(ModelConfiguration):
    model = GenericSite
    metadata = ModelMetadata(
        description="...",
        authority=Authority(...)
    )
```

### 🎯 Impact

#### Breaking Changes
This is a **complete breaking change** from any previous version. The addon was non-functional with current FairDM and required full modernization.

**Projects using the old API will need to:**
1. Update all plugin registrations
2. Update all model configurations
3. Update template inheritance
4. Update import statements
5. Follow the `MIGRATION.md` guide

#### Benefits
- ✅ Full compatibility with current FairDM framework
- ✅ Auto-generated admin interfaces
- ✅ Proper plugin system integration
- ✅ FAIR-compliant metadata for all models
- ✅ Improved code organization and documentation
- ✅ Type hints and better error handling
- ✅ Reference implementation for other FairDM addons

### 🔍 Validation

All critical components verified:
- ✅ `__fdm_setup_module__` present in `__init__.py`
- ✅ `EARTH_SAMPLES` defined in `settings.py`
- ✅ 7 `@register` decorators in `config.py`
- ✅ `ready()` method in `apps.py`
- ✅ `@plugins.register()` in `plugins.py`
- ✅ Template extends `fairdm/plugin.html`
- ✅ Template uses `{% block plugin %}`

### 📚 Reference Implementation

This modernization follows the pattern established by `fairdm-discussions`, which serves as the canonical reference for FairDM addon architecture.

### 🚀 Migration Path

Users should follow these steps:
1. Read `MIGRATION.md` for complete migration guide
2. Update to latest FairDM framework version
3. Update all plugin and model registration code
4. Update templates to new structure
5. Test all functionality
6. Remove deprecated code

### 👥 Credits

Modernization completed on December 19, 2025, following FairDM framework API evolution.

### 🔗 Resources

- **FairDM Documentation**: https://fairdm.org
- **Reference Addon**: https://github.com/FAIR-DM/fairdm-discussions
- **Repository**: https://github.com/FAIR-DM/fairdm-geo
- **Issues**: https://github.com/FAIR-DM/fairdm-geo/issues

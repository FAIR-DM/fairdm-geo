# Add fairdm-geo to a portal

Add the geoscience models to a FairDM portal and create their tables. Do this once for each
portal that should hold geoscience samples.

## Before you start

You need a FairDM 0.3 portal on Python 3.13 and Django 6.0. FairDM needs PostgreSQL with PostGIS.

## Steps

1. Install the package. `fairdm-geo` does not install FairDM, because your portal pins its own
   version.

   ```bash
   pip install fairdm-geo
   ```

2. List `fairdm_geo` as an add-on in your portal's `fairdm.setup()` call, and name the apps whose
   models you want in `apps`:

   ```python
   fairdm.setup(
       apps=[
           "fairdm_geo.sites",
           "fairdm_geo.rocks",
       ],
       addons=["fairdm_geo"],
   )
   ```

   Leave out an app you do not need. `fairdm_geo.sites` holds the [sampling location and
   borehole models](../reference/models.md), and `fairdm_geo.rocks` holds the rock sample models.

3. Create the tables:

   ```bash
   python manage.py migrate
   ```

4. [Load the vocabularies](load-the-vocabularies.md), so the fields have terms to offer.

## The result

The models you named are registered with FairDM, so your portal can list and edit them like any
other sample type. Listing the add-on also installed `fairdm_geo.core` and
`fairdm_geo.geology.stratigraphy`, which the other apps build on.

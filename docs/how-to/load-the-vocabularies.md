# Load the vocabularies

Load the controlled vocabularies the models use into the database. Do this after
[adding fairdm-geo to a portal](add-fairdm-geo-to-a-portal.md), and again after upgrading the
package, because a new release can ship updated vocabulary files.

## Steps

1. Run the command:

   ```bash
   python manage.py sync_vocabularies
   ```

   The command loads every vocabulary that a concept field on an installed model names. It reads
   the files the package ships, so it needs no network access.

2. Check the output. It reports each vocabulary it loaded and any it could not.

## The result

Each field that takes a term now offers the concepts of its vocabulary. [The
vocabularies](../reference/vocabularies.md) page lists each vocabulary and the field that uses
it. To see why the files ship with the package, read [Why vocabularies ship as
files](../explanation/why-vocabularies-ship-as-files.md).

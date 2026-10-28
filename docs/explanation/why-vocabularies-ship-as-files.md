# Why vocabularies ship as files

Why `fairdm-geo` carries copies of published vocabularies inside the package, and what that costs.
It does not cover how to load them, which [Load the vocabularies](../how-to/load-the-vocabularies.md)
does.

## Terms come from publishers

A lithology, a geological age or a type of specimen is only useful for comparing datasets if
everyone means the same thing by it. The package therefore offers the concepts of vocabularies that
others publish and maintain, and defines none of its own. A field names a vocabulary and accepts the
concepts in it.

## The files are copies, so loading needs no network

Each vocabulary is a file kept unmodified in the package, and `django-controlled-vocabularies` loads
it into the database. A portal can load its vocabularies when it deploys or tests, on a machine with
no internet access, and gets the same terms every time. A publisher's server being slow or down
cannot break a deployment.

## What it costs

The copies are a snapshot. The package records when each file was retrieved, and a publisher's later
changes reach your portal only when a new release of `fairdm-geo` ships updated files. A term a
publisher adds tomorrow is not available until then.

Because the files are unmodified, the package never edits a term. To change one, change it with its
publisher.

## Licences travel with the files

Redistributing a file means carrying its publisher's licence. The [vocabularies
reference](../reference/vocabularies.md) points to where each licence is recorded.

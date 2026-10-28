# Changelog

All notable changes to this project are recorded here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses
[semantic versioning](https://semver.org/).

## [Unreleased]

The first release. fairdm-geo has not been published before.

### Added

- `fairdm_geo.core`: abstract base models for earth samples, holes and vertical depth
  intervals, with a check constraint that keeps an interval's bottom below its top.
- `fairdm_geo.rocks`: rock sample, drill core, drill cuttings, thin section and rock powder
  models.
- `fairdm_geo.sites`: sampling location and borehole models.
- `fairdm_geo.geology.stratigraphy`: stratigraphic units with a rank and a genesis.
- Controlled vocabularies from ODM2, the CGI and the International Commission on
  Stratigraphy, shipped with the package and loaded with `sync_vocabularies` from
  django-controlled-vocabularies, so loading them never needs the network.
- Registration of every concrete model with FairDM.

### Requirements

- Python 3.13, Django 6.0 and FairDM 0.3.

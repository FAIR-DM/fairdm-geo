from research_vocabs.vocabularies import RemoteVocabulary


class GeologicalTimescale(RemoteVocabulary):
    class Meta:
        source = "https://vocabs.ardc.edu.au/registry/api/resource/downloads/1211/isc2020.ttl"
        prefix = "isc"
        namespace = "http://resource.geosciml.org/classifier/ics/ischart/"
        rdf_type = "gts:GeochronologicEra"


class GeochronologicBoundary(RemoteVocabulary):
    class Meta:
        source = "https://vocabs.ardc.edu.au/registry/api/resource/downloads/1211/isc2020.ttl"
        prefix = "isc"
        namespace = "http://resource.geosciml.org/classifier/ics/ischart/"
        rdf_type = "gts:GeochronologicBoundary"


class EraBoundary(RemoteVocabulary):
    class Meta:
        source = "https://vocabs.ardc.edu.au/registry/api/resource/downloads/1211/isc2020.ttl"
        prefix = "isc"
        namespace = "http://resource.geosciml.org/classifier/ics/ischart/"
        rdf_type = "gts:GeochronologicEraBoundary"

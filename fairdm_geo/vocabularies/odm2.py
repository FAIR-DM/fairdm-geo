from research_vocabs import RemoteVocabulary


class ActionType(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/actiontype/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/actiontype/"


class AggregationStatistic(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/aggregationstatistic/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/aggregationstatistic/"


class AnnotationType(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/annotationtype/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/annotationtype/"


class CensorCode(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/censorcode/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/censorcode/"


class DataQualityType(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/dataqualitytype/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/dataqualitytype/"


class DatasetType(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/datasettype/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/datasettype/"


class DirectivesType(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/directivestype/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/directivestype/"


class ElevationDatum(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/elevationdatum/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/elevationdatum/"


class EquipmentType(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/equipmenttype/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/equipmenttype/"


class Medium(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/medium/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/medium/"


class MethodType(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/methodtype/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/methodtype/"


class OrganizationType(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/organizationtype/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/organizationtype/"


class PropertyDataType(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/propertydatatype/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/propertydatatype/"


class QualityCode(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/qualitycode/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/qualitycode/"


class RelationshipType(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/relationshiptype/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/relationshiptype/"


class ResultType(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/resulttype/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/resulttype/"


class SamplingFeatureGeoType(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/samplingfeaturegeotype/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/samplingfeaturegeotype/"


class SamplingFeatureType(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/samplingfeaturetype/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/samplingfeaturetype/"


class SiteType(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/sitetype/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/sitetype/"


class SpatialOffsetType(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/spatialoffsettype/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/spatialoffsettype/"


class Speciation(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/speciation/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/speciation/"


class SpecimenType(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/specimentype/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/specimentype/"


class Status(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/status/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/status/"


class TaxonomicClassifierType(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/taxonomicclassifiertype/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/taxonomicclassifiertype/"


class UnitsType(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/unittype/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/unittype/"


class VariableName(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/variablename/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/variablename/"


class VariableType(RemoteVocabulary):
    class Meta:
        source = {
            "source": "http://vocabulary.odm2.org/api/v1/variabletype/?format=skos",
            "format": "xml",
        }
        prefix = "odm2b"
        namespace = "http://vocabulary.odm2.org/variabletype/"


# class ODM2Units(RemoteVocabulary):
#     class Meta:
#         source = "http://vocabulary.odm2.org/api/v1/unitstype/?format=skos"
#         prefix = "odm2b"
#         namespace = "http://vocabulary.odm2.org/unitstype/"

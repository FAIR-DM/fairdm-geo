"""Collection of vocabularies from the CGI GeoSciML RemoteTTLVocabulary.

<https://cgi.vocabs.ga.gov.au/vocab/>

note::

It doesn't seem possible to download full vocabularies direct from the CGI website or from Research Vocabs Australia.
Therefore, the vocabularies are linked direct to the .ttl representations stored in the official CGI-IUGS GitHub repository.

https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs

"""

from research_vocabs.vocabularies import RemoteVocabulary


class RemoteTTLVocabulary(RemoteVocabulary):
    def _source(self):
        return {
            "source": self._meta.source,
            "format": "turtle",
        }


class AlterationType(RemoteTTLVocabulary):
    class Meta:
        source = "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/alterationtype.ttl"


class BoreholeDrillingMethod(RemoteTTLVocabulary):
    class Meta:
        source = "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/boreholedrillingmethod.ttl"


class CompositionCategory(RemoteTTLVocabulary):
    class Meta:
        source = (
            "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/compositioncategory.ttl"
        )


class CompoundMaterialConstituentPart(RemoteTTLVocabulary):
    class Meta:
        source = "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/compoundmaterialconstituentpartrole.ttl"


class ConsolidationDegree(RemoteTTLVocabulary):
    class Meta:
        source = (
            "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/consolidationdegree.ttl"
        )


class ContactType(RemoteTTLVocabulary):
    class Meta:
        source = "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/contacttype.ttl"


class ConventionCodeForStrikeAndDipMeasurements(RemoteTTLVocabulary):
    class Meta:
        source = "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/conventioncode.ttl"


class DeformationStyle(RemoteTTLVocabulary):
    class Meta:
        source = (
            "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/deformationstyle.ttl"
        )


class DescriptionPurpose(RemoteTTLVocabulary):
    class Meta:
        source = (
            "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/descriptionpurpose.ttl"
        )


class DeterminationMethodOrientation(RemoteTTLVocabulary):
    class Meta:
        source = "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/determinationmethodorientation.ttl"


class EventEnvironment(RemoteTTLVocabulary):
    class Meta:
        source = (
            "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/eventenvironment.ttl"
        )


class EventProcess(RemoteTTLVocabulary):
    class Meta:
        source = "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/eventprocess.ttl"


class FaultMovementSense(RemoteTTLVocabulary):
    class Meta:
        source = (
            "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/faultmovementsense.ttl"
        )


class FaultMovementType(RemoteTTLVocabulary):
    class Meta:
        source = (
            "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/faultmovementtype.ttl"
        )


class FaultType(RemoteTTLVocabulary):
    class Meta:
        source = "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/faulttype.ttl"


class FoliationType(RemoteTTLVocabulary):
    class Meta:
        source = "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/foliationtype.ttl"


class GeneticCategory(RemoteTTLVocabulary):
    class Meta:
        source = (
            "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/geneticcategory.ttl"
        )


class GeologicUnitMorphology(RemoteTTLVocabulary):
    class Meta:
        source = "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/geologicunitmorphology.ttl"


class GeologicUnitPartRole(RemoteTTLVocabulary):
    class Meta:
        source = "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/geologicunitpartrole.ttl"


class GeologicUnitType(RemoteTTLVocabulary):
    class Meta:
        source = (
            "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/geologicunittype.ttl"
        )


class LineationType(RemoteTTLVocabulary):
    class Meta:
        source = "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/lineationtype.ttl"


class MappingFrame(RemoteTTLVocabulary):
    class Meta:
        source = "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/mappedfeatureobservationmethod.ttl"


class MetamorphicFacies(RemoteTTLVocabulary):
    class Meta:
        source = (
            "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/metamorphicfacies.ttl"
        )


class MetamorphicGrade(RemoteTTLVocabulary):
    class Meta:
        source = (
            "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/metamorphicgrade.ttl"
        )


class ObservationMethodGeologicFeature(RemoteTTLVocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifierscheme/cgi/2016.01/featureobservationmethod"


class ObservationMethodMappedFeature(RemoteTTLVocabulary):
    class Meta:
        source = "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/mappedfeatureobservationmethod.ttl"


class OrientationDeterminationMethod(RemoteTTLVocabulary):
    class Meta:
        source = "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/determinationmethodorientation.ttl"


class ParticleAspectRatio(RemoteTTLVocabulary):
    class Meta:
        source = (
            "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/particleaspectratio.ttl"
        )


class ParticleShape(RemoteTTLVocabulary):
    class Meta:
        source = "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/particleshape.ttl"


class ParticleType(RemoteTTLVocabulary):
    class Meta:
        source = "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/particletype.ttl"


class PlanarPolarityCode(RemoteTTLVocabulary):
    class Meta:
        source = (
            "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/planarpolaritycode.ttl"
        )


class ProportionTerm(RemoteTTLVocabulary):
    class Meta:
        source = "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/proportionterm.ttl"


class SimpleLithology(RemoteTTLVocabulary):
    # This vocabulary is available from the Aus Research Vocabs website, however, we are using the CGI-IUGS GitHub repository
    # for consistency with the other vocabs. (and assuming the repository is the most up-to-date source for the vocabularies?)

    class Meta:
        source = (
            "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/simplelithology.ttl"
        )
        namespace = "http://resource.geosciml.org/classifier/cgi/lithology/"
        # source = "https://vocabs.ardc.edu.au/registry/api/resource/downloads/214/ga_simple-lithology_v0-1.ttl"


class StratigraphicRank(RemoteTTLVocabulary):
    class Meta:
        source = (
            "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/stratigraphicrank.ttl"
        )


class ValueQualifier(RemoteTTLVocabulary):
    class Meta:
        source = "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/valuequalifier.ttl"


class RemoteTTLVocabularyRelation(RemoteTTLVocabulary):
    class Meta:
        source = (
            "https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/vocabularyrelation.ttl"
        )

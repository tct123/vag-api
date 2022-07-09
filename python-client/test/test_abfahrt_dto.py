"""
    VAG API

    OpenAPI-Dokumentation der API zu start.vag - dem Verkehrs-Aktiengesellschaft (VAG) Abfahrsmonitor mit Echtzeitprognose. Die API gibt Zugriff auf alle Haltestellen, Fahrten und Abfahrten im Gebiet des Verkehrsbund Großraum Nürnberg (VGN). Eine Schnittstellenbeschreibung durch die VAG findet sich auf https://opendata.vag.de/dataset/api-echtzeitauskunft unter Creative CommonsAttribution 4.0 Int veröffentlicht.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.vag.model.abfahrt_dto import AbfahrtDto

from deutschland import vag


class TestAbfahrtDto(unittest.TestCase):
    """AbfahrtDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAbfahrtDto(self):
        """Test AbfahrtDto"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AbfahrtDto()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

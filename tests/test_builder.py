from lib.ogame.constants import Buildings, Research
from ogame_bot.builder import Builder


def test_building_prerequisites():
    test_building = Buildings.FusionReactor
    planet_buildings = {Buildings.DeuteriumSynthesizer: 5,
                        Research.EnergyTechnology: 3}

    assert Builder.building_prerequisites(test_building, planet_buildings)

    planet_buildings = {Buildings.MetalMine: 3,
                        Buildings.DeuteriumSynthesizer: 5,
                        Research.CombustionDrive: 1,
                        Research.ArmourTechnology: 10,
                        Research.EnergyTechnology: 3}

    assert Builder.building_prerequisites(test_building, planet_buildings)

    planet_buildings = {Buildings.MetalMine: 3,
                        Buildings.DeuteriumSynthesizer: 5,
                        Research.CombustionDrive: 1,
                        Research.ArmourTechnology: 10,
                        Research.EnergyTechnology: 2}

    assert not Builder.building_prerequisites(test_building, planet_buildings)

    planet_buildings = {Buildings.MetalMine: 3,
                        Buildings.DeuteriumSynthesizer: 5,
                        Research.CombustionDrive: 1,
                        Research.ArmourTechnology: 10,
                        Research.EnergyTechnology: 4}

    assert Builder.building_prerequisites(test_building, planet_buildings)

    planet_buildings = {Buildings.MetalMine: 3,
                        Buildings.DeuteriumSynthesizer: 15,
                        Research.CombustionDrive: 1,
                        Research.ArmourTechnology: 10,
                        Research.EnergyTechnology: 6}

    assert Builder.building_prerequisites(test_building, planet_buildings)

    planet_buildings = {Buildings.MetalMine: 3,
                        Buildings.DeuteriumSynthesizer: 1,
                        Research.CombustionDrive: 1,
                        Research.ArmourTechnology: 10,
                        Research.EnergyTechnology: 2}

    assert not Builder.building_prerequisites(test_building, planet_buildings)

    planet_buildings = {Buildings.MetalMine: 3,
                        Research.CombustionDrive: 1,
                        Research.ArmourTechnology: 10}

    assert not Builder.building_prerequisites(test_building, planet_buildings)

    planet_buildings = {}

    assert not Builder.building_prerequisites(test_building, planet_buildings)

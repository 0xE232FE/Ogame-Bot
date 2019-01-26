from lib.ogame.constants import Buildings, Research, Resources, Ships
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


def test_check_cost():
    test_building = Buildings.MetalMine
    test_level = 1
    planet_resources = {Resources.Metal: 100,
                        Resources.Crystal: 100,
                        Resources.Deuterium: 100,
                        Resources.Energy: 10}

    assert Builder.check_cost(test_building, test_level, planet_resources)

    test_level = 3
    assert not Builder.check_cost(test_building, test_level, planet_resources)

    test_building = Research.ComputerTechnology
    test_level = 1
    planet_resources = {Resources.Metal: 100,
                        Resources.Crystal: 1000,
                        Resources.Deuterium: 600,
                        Resources.Energy: 10}
    assert Builder.check_cost(test_building, test_level, planet_resources)

    test_level = 5
    assert not Builder.check_cost(test_building, test_level, planet_resources)

    test_building = Research.ComputerTechnology
    test_level = 1
    planet_resources = {Resources.Metal: 100,
                        Resources.Crystal: 1000,
                        Resources.Deuterium: 100,
                        Resources.Energy: 10}
    assert not Builder.check_cost(test_building, test_level, planet_resources)

    test_building = Research.GravitonTechnology
    test_level = 1

    planet_resources = {Resources.Metal: 100,
                        Resources.Crystal: 1000,
                        Resources.Deuterium: 600,
                        Resources.Energy: 10}
    assert not Builder.check_cost(test_building, test_level, planet_resources)

    planet_resources = {Resources.Metal: 100,
                        Resources.Crystal: 1000,
                        Resources.Deuterium: 100,
                        Resources.Energy: 300000}
    assert Builder.check_cost(test_building, test_level, planet_resources)

    test_building = Ships.Cruiser
    test_level = 1
    test_nbr = 1

    planet_resources = {Resources.Metal: 100,
                        Resources.Crystal: 1000,
                        Resources.Deuterium: 600,
                        Resources.Energy: 10}
    assert not Builder.check_cost(test_building, test_level, planet_resources, nbr=test_nbr)

    planet_resources = {Resources.Metal: 30000,
                        Resources.Crystal: 10000,
                        Resources.Deuterium: 2000,
                        Resources.Energy: 10}
    assert Builder.check_cost(test_building, test_level, planet_resources, nbr=test_nbr)

    test_nbr = 5
    assert not Builder.check_cost(test_building, test_level, planet_resources, nbr=test_nbr)

    planet_resources = {Resources.Metal: 300000,
                        Resources.Crystal: 100000,
                        Resources.Deuterium: 20000,
                        Resources.Energy: 10}
    assert Builder.check_cost(test_building, test_level, planet_resources, nbr=test_nbr)

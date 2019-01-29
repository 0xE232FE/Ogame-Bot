package main

import (
	"github.com/alaingilbert/ogame"
	"log"
)

type planetInfo struct {
	planet ogame.Planet
	planetResources ogame.Resources
	planetResourcesBuildings ogame.ResourcesBuildings
	planetFacilitiesBuildings ogame.Facilities
}

type userInfo struct {
	userResearches ogame.Researches
}

func getUserData(bot *ogame.OGame) userInfo {
	return userInfo{
		bot.GetResearch(),
	}
}

func getPlanetData(bot *ogame.OGame, planet ogame.Planet) planetInfo {
	resources, err := planet.GetResources()
	if err != nil {
		log.Fatal(err)
	}

	resourcesBuildings, err := planet.GetResourcesBuildings()
	if err != nil {
		log.Fatal(err)
	}
	facilitiesBuildings, err := planet.GetFacilities()

	if err != nil {
		log.Fatal(err)
	}

	return planetInfo{
		planet,
		resources,
		resourcesBuildings,
		facilitiesBuildings,
	}
}

func canAffordWrapper(userData userInfo, planetData planetInfo, price ogame.Resources, toBuild ogame.BaseOgameObj) bool {
	return planetData.planetResources.CanAfford(price) && toBuild.IsAvailable(	planetData.planet.GetType(),
																				planetData.planetResourcesBuildings,
																				planetData.planetFacilitiesBuildings,
																				userData.userResearches,
																				planetData.planetResources.Energy)
}

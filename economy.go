package main

import (
	"github.com/alaingilbert/ogame"
	"log"
	"time"
)s

func economyBot(bot *ogame.OGame) {
	logPrefix := "[ECONOMY] "
	priorityBuildings := [8]ogame.ID{
		ogame.MetalMineID, ogame.CrystalMineID, ogame.DeuteriumSynthesizerID,
		ogame.SolarPlantID, ogame.FusionReactorID, ogame.RoboticsFactoryID, ogame.ShipyardID,
		ogame.ResearchLabID,
	}
	for {
		researches := bot.GetResearch()
		for _, planet := range bot.GetPlanets() {
			log.Println(logPrefix, "Check buildings on ", planet.ID, " ...")

			resources, _ := planet.GetResources()
			resourcesBuildings, _ := planet.GetResourcesBuildings()
			facilitiesBuildings, _ := planet.GetFacilities()

			for _, buildingID := range priorityBuildings {
				currentLevel := 0
				building := ogame.Objs.ByID(buildingID)

				if ogame.IsResourceBuildingID(buildingID.Int()) {
					currentLevel = resourcesBuildings.ByID(buildingID)
				} else if ogame.IsFacilityID(buildingID.Int()) {
					currentLevel = facilitiesBuildings.ByID(buildingID)
				}

				log.Println(logPrefix, "try to build new level of ", building)

				price := building.GetPrice(currentLevel + 1)
				if resources.CanAfford(price) && building.IsAvailable(planet.GetType(), resourcesBuildings, facilitiesBuildings, researches, resources.Energy){
					log.Println(logPrefix, "Building new level of ", building)
					_ := planet.Build(buildingID, 1)
				}
			}
		}

		time.Sleep(5 * time.Minute)
	}
}



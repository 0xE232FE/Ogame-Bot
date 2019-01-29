package main

import (
	"github.com/alaingilbert/ogame"
	"log"
	"math/rand"
	"time"
)

func attackerBot(bot *ogame.OGame) {
	logPrefix := "[ATTACKER] "
	priorityShips := []ogame.ID{
		ogame.ColonyShipID, ogame.HeavyFighterID, ogame.LightFighterID, ogame.SmallCargoID,
		ogame.EspionageProbeID, ogame.RecyclerID,
	}
	for {
		researches := bot.GetResearch()

		performPriorityShipsBuilding(bot, logPrefix, priorityShips, researches)

		time.Sleep(time.Duration(rand.Intn(100)) * time.Minute)
	}
}

func performPriorityShipsBuilding(bot *ogame.OGame, logPrefix string, priorityShips []ogame.ID, researches ogame.Researches){
	for _, planet := range bot.GetPlanets() {
		log.Println(logPrefix, "Check ships on ", planet.ID, " ...")

		resources, _ := planet.GetResources()
		resourcesBuildings, _ := planet.GetResourcesBuildings()
		facilitiesBuildings, _ := planet.GetFacilities()
		//ships, _ := planet.GetShips()

		for _, shipID := range priorityShips {
			ship := ogame.Objs.ByID(shipID)
			//currentNbr := ships.ByID(shipID)
			buildNbr := 1

			price := ship.GetPrice(buildNbr)
			if resources.CanAfford(price) && ship.IsAvailable(planet.GetType(), resourcesBuildings, facilitiesBuildings, researches, resources.Energy){
				log.Println(logPrefix, "try to build some ", ship)
				err := planet.Build(shipID, buildNbr)
				if err != nil {
					log.Fatal(logPrefix, err)
				}else{
					log.Println(logPrefix, "building a new ", ship)
					resources = resources.Sub(price)
				}
			}
			time.Sleep(time.Duration(rand.Intn(100)) * time.Second)
		}
		time.Sleep(time.Duration(rand.Intn(200)) * time.Second)
	}
}

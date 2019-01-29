package main

import (
	"github.com/alaingilbert/ogame"
	"log"
	"math/rand"
	"time"
)

type attack struct {
	logPrefix string
	priorityShips []ogame.ID
}

type civilian struct {
	logPrefix string
	priorityShips []ogame.ID
}

type explore struct {
	logPrefix string
}

func initializeAttackBots() (attack, civilian, explore){
	return attack{
		"[ATTACKER] ",
		[]ogame.ID{
				ogame.HeavyFighterID, ogame.LightFighterID, ogame.SmallCargoID,
			},
		},
		civilian{
			"[CIVILIAN] ",
			[]ogame.ID{
				ogame.RecyclerID,
			},
		},
		explore{
			"[EXPLORER] ",
		}
}

func attackerBot(bot *ogame.OGame) {
	attackerBot, civilianBot, _ := initializeAttackBots()

	for {
		userData := getUserData(bot)

		for _, planet := range bot.GetPlanets() {
			planetData := getPlanetData(bot, planet)

			log.Println(attackerBot.logPrefix, "Check attack ship to build on ", planet.ID, " ...")
			performAttackPriorityShipsBuilding(attackerBot, userData, planetData)
			time.Sleep(time.Duration(rand.Intn(5)) * time.Minute)

			log.Println(attackerBot.logPrefix, "Check civilian ship to build on ", planet.ID, " ...")
			performCivilianPriorityShipsBuilding(civilianBot, userData, planetData)
			time.Sleep(time.Duration(rand.Intn(5)) * time.Minute)
		}

		time.Sleep(time.Duration(rand.Intn(40)) * time.Minute)
	}
}

func performAttackPriorityShipsBuilding(attackerBot attack, userData userInfo, planetData planetInfo){
	for _, shipID := range attackerBot.priorityShips {
		ship := ogame.Objs.ByID(shipID)
		//currentNbr := ships.ByID(shipID)
		buildNbr := rand.Intn(10)

		fleetBuild(userData, planetData, attackerBot.logPrefix, ship, buildNbr)
		time.Sleep(time.Duration(rand.Intn(100)) * time.Second)
	}
}

func performCivilianPriorityShipsBuilding(attackerBot attack, userData userInfo, planetData planetInfo){
	for _, shipID := range attackerBot.priorityShips {
		ship := ogame.Objs.ByID(shipID)
		//currentNbr := ships.ByID(shipID)
		buildNbr := rand.Intn(10)

		fleetBuild(userData, planetData, attackerBot.logPrefix, ship, buildNbr)
		time.Sleep(time.Duration(rand.Intn(100)) * time.Second)
	}
}

func fleetBuild(userData userInfo, planetData planetInfo, logPrefix string, ship ogame.BaseOgameObj, nbr int){
	price := ship.GetPrice(nbr)
	if canAffordWrapper(userData, planetData, price, ship){
		log.Println(logPrefix, "try to build ", nbr, " of ", ship)

		err := planetData.planet.Build(ship.GetID(), nbr)
		if err != nil {
			log.Fatal(logPrefix, err)
		}else{
			planetData.planetResources = planetData.planetResources.Sub(price)
			log.Println(logPrefix, "building ", nbr, " of ", ship)
		}
	}
}

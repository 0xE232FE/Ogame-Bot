package main

import (
	"github.com/alaingilbert/ogame"
	"log"
	"time"
)

func attackerBot(bot *ogame.OGame) {
	logPrefix := "[ATTACKER]"
	for {
		log.Print(logPrefix, "Searching someone to attack... ")
		time.Sleep(5 * time.Minute)
	}
}

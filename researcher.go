package main

import (
	"github.com/alaingilbert/ogame"
	"log"
	"time"
)

func researcherBot(bot *ogame.OGame) {
	logPrefix := "[RESEARCHER]"
	for {
		log.Print(logPrefix, "Search for a research to do... ")
		time.Sleep(5 * time.Minute)
	}
}

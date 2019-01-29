package main

import (
	"github.com/alaingilbert/ogame"
	"log"
	"time"
)

func defenderBot(bot *ogame.OGame) {
	logPrefix := "[DEFENDER] "
	for {
		attacked := bot.IsUnderAttack()
		log.Print(logPrefix, attacked) // False
		time.Sleep(10 * time.Second)
	}
}

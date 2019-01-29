package main

import (
	"github.com/alaingilbert/ogame"
	"log"
	"math/rand"
	"time"
)

func defenderBot(bot *ogame.OGame) {
	logPrefix := "[DEFENDER] "
	for {
		attacked := bot.IsUnderAttack()
		log.Print(logPrefix, attacked) // False
		time.Sleep(time.Duration(rand.Intn(5)) * time.Minute)
	}
}

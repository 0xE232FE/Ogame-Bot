package main

import (
	"github.com/alaingilbert/ogame"
	"math/rand"
	"os"
	"time"
)

func main() {
	universe := os.Getenv("UNIVERSE")
	username := os.Getenv("USERNAME")
	password := os.Getenv("PASSWORD")
	language := os.Getenv("LANGUAGE")
	bot, err := ogame.New(universe, username, password, language)
	if err != nil {
		panic(err)
	}

	go defenderBot(bot)
	time.Sleep(time.Duration(rand.Intn(2)) * time.Minute)
	go economyBot(bot)
	time.Sleep(time.Duration(rand.Intn(3)) * time.Minute)
	go attackerBot(bot)
	time.Sleep(time.Duration(rand.Intn(4)) * time.Minute)
	go researcherBot(bot)

	select{ }
}

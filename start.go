package main

import (
	"fmt"
	"os"
)

import "github.com/alaingilbert/ogame"

func main() {
	universe := os.Getenv("UNIVERSE")
	username := os.Getenv("USERNAME")
	password := os.Getenv("PASSWORD")
	language := os.Getenv("LANGUAGE")
	bot, err := ogame.New(universe, username, password, language)
	if err != nil {
		panic(err)
	}
	attacked := bot.IsUnderAttack()
	fmt.Println(attacked) // False

	for _, planet := range bot.GetPlanets() {
		planet.Build(210, 1)
	}
}

package routes

/*
file: routes/forms.go

this file is going to be for parsing forms and creating errors based off of the form data.
as well as creating relavant information from the form data
*/

import (
	"log"
	"strconv"

	"golang.org/x/crypto/bcrypt"
)

func ConvertStrToInt(f string) (int, error) {
	conversion, err := strconv.Atoi(f)
	if err != nil {
		log.Printf("Error converting %s to int.", f)
		return 0, err
	}
	return conversion, nil
}

func ConvertStrToFloat64(f string) (float64, error) {
	conversion, err := strconv.ParseFloat(f, 64)
	if err != nil {
		log.Printf("Error converting %s to float64.", f)
		return 0.0, err
	}
	return conversion, nil
}

func HashString(s string, cost int) (string, error) {
	salt, err := bcrypt.GenerateFromPassword([]byte(s), cost)
	if err != nil {
		return "", err
	}
	return string(salt), nil
}

func GetFormError() string { return "" }

func ProcessCreateProjectForm(status, lead, client, codename, description, hourly, wholesale, totalTime, subscription string) error {
	// decide if client or lead

	// if lead
	// create client from lead

	// convert hourly, wholesale, totaltime, subscription to float64

	// create project with this information

	return nil
}

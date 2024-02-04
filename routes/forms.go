package routes

/*
file: routes/forms.go

this file is going to be for parsing forms and creating errors based off of the form data.
as well as creating relavant information from the form data
*/

import (
	"log"
	"strconv"

	"github.com/SmokierLemur51/lo-go/models"

	"golang.org/x/crypto/bcrypt"
	"gorm.io/gorm"
)

func ConvertStrToInt(f string) (int, error) {
	if f == "" {
		return 0, nil
	}
	conversion, err := strconv.Atoi(f)
	if err != nil {
		log.Printf("Error converting %s to int.", f)
		return 0, err
	}
	return conversion, nil
}

func ConvertStrTo_Uint(f string) (uint, error) {
	if f == "" {
		return 0, nil
	}
	conversion, err := strconv.ParseUint(f, 10, 32)
	if err != nil {
		return 0, err
	}
	return uint(conversion), nil
}

func ConvertStrToFloat64(f string) (float64, error) {
	if f == "" {
		return 0.0, nil
	}
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

func ProcessCreateProjectForm(
	db *gorm.DB,
	status, lead, client, codename, description,
	hourly, wholesale, totalTime, subscription string) error {

	hourlyRate, _ := ConvertStrToFloat64(hourly)
	wholesalePrice, _ := ConvertStrToFloat64(wholesale)
	timeSpent, _ := ConvertStrToFloat64(totalTime)
	subs, _ := ConvertStrToFloat64(subscription)
	stat, _ := ConvertStrTo_Uint(status)
	if len(lead) > 0 && len(client) == 0 {
		// convert lead to client
		var convertedLead models.Lead
		if result := db.Where("id = ?", lead).First(&convertedLead); result.Error != nil {
			return result.Error
		}
		newClient, _ := convertedLead.ConvertLeadIntoClient(db)
		if err := newClient.Insert(db); err != nil {
			return err
		}
		var personal bool
		if newClient.ID == 1 {
			personal = true
		} else {
			personal = false
		}
		newProject := models.Project{
			StatusCodeID:      stat,
			Personal:          personal,
			ClientID:          newClient.ID,
			Codename:          codename,
			Description:       description,
			HourlyRate:        hourlyRate,
			WholesalePrice:    wholesalePrice,
			SubscriptionPrice: subs,
			TotalTime:         timeSpent,
		}
		if err := newProject.Insert(db); err != nil {
			return err
		}
	} else if len(client) > 0 && len(lead) == 0 {
		clientID, _ := ConvertStrTo_Uint(client)
		var personal bool
		if clientID == 1 {
			personal = true
		} else {
			personal = false
		}
		newProject := models.Project{
			StatusCodeID:      stat,
			Personal:          personal,
			ClientID:          clientID,
			Codename:          codename,
			Description:       description,
			HourlyRate:        hourlyRate,
			WholesalePrice:    wholesalePrice,
			SubscriptionPrice: subs,
			TotalTime:         timeSpent,
		}
		if err := newProject.Insert(db); err != nil {
			return err
		}
	}

	return nil
}

package models

import (
	"log"

	"gorm.io/gorm"
)

func CreateProject(status, client uint, personal bool, codename, description string, hourlyRate, wholesale, subscription float64) Project {
	return Project{
		StatusCodeID:      status,
		ClientID:          client,
		Personal:          personal,
		Codename:          codename,
		Description:       description,
		HourlyRate:        hourlyRate,
		WholesalePrice:    wholesale,
		SubscriptionPrice: subscription,
	}
}

func (p *Project) Insert(db *gorm.DB) error {
	if result := db.FirstOrCreate(p, p); result.Error != nil {
		return result.Error
	}
	return nil
}

func (p *Project) Update(db *gorm.DB) error { return nil }

func (p *Project) Delete(db *gorm.DB) error { return nil }

func QueryProjects(db *gorm.DB, status string) ([]Project, error) {
	// "all" as the status loads all
	if status == "all" {
		var projects []Project
		if result := db.Find(&projects); result.Error != nil {
			log.Println(result.Error)
			return []Project{}, result.Error
		}
		return projects, nil
	} else {
		var stat StatusCode
		// query status first
		if result := db.Where("stat_code = ?", status).First(&stat); result.Error != nil {
			return nil, result.Error
		}
		// using status, find the projects associated
		var projects []Project
		if result := db.Where("status_code_id = ?", stat.ID).Find(&projects); result.Error != nil {
			return nil, result.Error
		}
		// query projects by status id
		return []Project{}, nil
	}
}

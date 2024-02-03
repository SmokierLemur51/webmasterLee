package tests

import (
	"github.com/SmokierLemur51/lo-go/models"
	"gorm.io/gorm"
)

func CreateModels(db *gorm.DB) {
	db.AutoMigrate(&models.Lead{}, &models.Client{}, &models.StatusCode{}, &models.TimeClock{}, &models.Project{})
}

func PopulateLeads(db *gorm.DB) error {
	leads := []*models.Lead{
		{Company: "Thrasher Improvements", Phone: "502-802-1437", Contacted: false, Converted: false},
		{Company: "A Cut Above Rennovations", Phone: "502-759-5335", Contacted: false, Converted: false},
		{Company: "Heaton Rennovations", Phone: "502-640-3214", Contacted: false, Converted: false},
		{Company: "Baird Property", Phone: "812-283-3345", Contacted: false, Converted: false},
		{Company: "Kentuckiana Siding", Phone: "502-222-1953", Contacted: false, Converted: false},
		{Company: "JP One LLC", Phone: "502-380-7470", Contacted: false, Converted: false},
		{Company: "Cracker Jack Construction", Phone: "270-945-7859", Contacted: false, Converted: false},
		{Company: "Traditional Heating & Cooling", Phone: "502-643-9126", Contacted: false, Converted: false},
		{Company: "Defining Edge", Name: "Charlie", Phone: "502-821-4299"},
		{Company: "502 Gutter Crew (Also does leaf removal)", Name: "Pat", Phone: "502-226-0536"},
		{Company: "SC General Contracting", Phone: "502-386-9386"},
		{Company: "Handyman Services LLC", Phone: "502-657-8450"},
		{Company: "Ixma Roofing", Name: "Henry / Geraldine", Phone: "270-231-5651"},
		{Company: "Diaz Gutter Works", Name: "Alfredo", Phone: "502-220-6091"},
		{Company: "Precision Contracting", Name: "Ben Glass", Phone: "502-338-3365"},
		{Company: "Bourbon Country Roofing", Phone: "502-769-8560"},
		{Company: "Hamilton Vinyl Siding", Phone: "502-249-0218"},
		{Company: "Mattingly Seamless", Phone: "270-699-1712"},
		{Company: "Froggies Bar & Grill", Phone: "502-252-4004"},
		{Company: "Seryel LLC", Phone: "502-807-7469"},
	}
	for _, l := range leads {
		if result := db.FirstOrCreate(&l, l); result.Error != nil {
			return result.Error
		}
	}
	return nil
}

func PopulateClients(db *gorm.DB) error {
	clients := []*models.Client{
		{Company: "Personal", Name: "Logan Lee", Phone: "812-679-6147", Email: "ldl6147@gmail.com"},
		{Company: "Greenleaf Cleaning", Name: "Logan Lee", Phone: "812-679-6147"},
		{Company: "Higginbotham Paint", Name: "Kevin Higginbotham", Phone: "812-572-5856"},
	}
	for _, c := range clients {
		if result := db.FirstOrCreate(&c, c); result.Error != nil {
			return result.Error
		}
	}
	return nil
}

// this func is useless,
func PopulateProjects(db *gorm.DB) error {
	var personal models.Client
	if result := db.Where("company = ?", "Personal").First(&personal); result.Error != nil {
		return result.Error
	}
	projects := []*models.Project{
		{},
	}
	for _, p := range projects {
		if result := db.FirstOrCreate(&p, p); result.Error != nil {
			return result.Error
		}
	}
	return nil
}

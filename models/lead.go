package models

import (
	"gorm.io/gorm"
)

func (l *Lead) Insert(db *gorm.DB) error {
	if result := db.FirstOrCreate(l, l); result.Error != nil {
		return result.Error
	}
	return nil
}

func (l *Lead) Update(db *gorm.DB) error { return nil }

func (l *Lead) Delete(db *gorm.DB) error { return nil }

func QueryLeads(db *gorm.DB, status string) ([]Lead, error) {
	// passing "all" will load all leads in db
	if status == "all" {
		var leads []Lead
		if result := db.Find(&leads); result.Error != nil {
			return nil, result.Error
		}
		return leads, nil
	} else {
		var stat StatusCode
		// query status first
		if result := db.Where("stat_code = ?", status).First(&stat); result.Error != nil {
			return nil, result.Error
		}
		var leads []Lead
		if result := db.Where("status = ?", stat.ID).Find(&leads); result.Error != nil {
			return nil, result.Error
		}
		return leads, nil
	}
}

func (l *Lead) ConvertLeadIntoClient(db *gorm.DB) (*Client, error) {
	// first update converted bool to true
	l.Converted = true
	if result := db.Save(l); result.Error != nil {
		return nil, result.Error
	}
	// return new client
	return (&Client{
		Company: l.Company, Name: l.Name, Phone: l.Phone, Email: l.Email,
	}), nil
}

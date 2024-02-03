package models

import (
	"gorm.io/gorm"
)

func (c *Client) Insert(db *gorm.DB) error {
	if result := db.FirstOrCreate(c, c); result.Error != nil {
		return result.Error
	}
	return nil
}

func (c *Client) Update(db *gorm.DB) error { return nil }

func (c *Client) Delete(db *gorm.DB) error { return nil }

func QueryClients(db *gorm.DB, status string) ([]Client, error) {
	// passing "all" will load all leads in db
	if status == "all" {
		var clients []Client
		if result := db.Find(&clients); result.Error != nil {
			return nil, result.Error
		}
		return clients, nil
	} else {
		var stat StatusCode
		// query status first
		if result := db.Where("stat_code = ?", status).First(&stat); result.Error != nil {
			return nil, result.Error
		}
		var clients []Client
		if result := db.Where("status = ?", stat.ID).Find(&clients); result.Error != nil {
			return nil, result.Error
		}
		return clients, nil
	}
}

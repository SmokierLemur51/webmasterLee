package models

import (
	"gorm.io/gorm"
)

type StatusCode struct {
	gorm.Model
	StatCode        string
	StatDescription string
}

type Lead struct {
	gorm.Model
	Company   string
	Name      string `gorm:"default:uknown"`
	Phone     string
	Email     string `gorm:"default:john.doe@uknown.com"`
	Converted bool   `gorm:"default:false"`
	Contacted bool   `gorm:"default:false"`
}

type Client struct {
	gorm.Model
	Company  string
	Name     string
	Phone    string
	Email    string
	Projects []Project `gorm:"foreignKey:ClientID"`
}

type TimeClock struct {
	gorm.Model
	ProjectID uint    `gorm:"not null"`
	Project   Project `gorm:"foreignKey:ProjectID"`
}

// thinking about removing personal bool here and just having a client that is named Personal
type Project struct {
	gorm.Model
	StatusCodeID      uint       `gorm:"not null"`
	StatusCode        StatusCode `gorm:"foreignKey:StatusCodeID"`
	Personal          bool       // might be best to remove and make a client named Personal
	ClientID          uint       `gorm:"not null"`
	Client            Client     `gorm:"constraint:OnUpdate:CASCADE,OnDelete:SET NULL;"`
	Codename          string
	Description       string
	TotalTime         float64
	HourlyRate        float64 `gorm:"default:0.0"`
	WholesalePrice    float64 `gorm:"default:0.0"`
	SubscriptionPrice float64 `gorm:"default:0.0"`
}

// none of the below have been created yet, they need fine tuning

type Employer struct {
	// who currently employs me, paychecks come from here
	gorm.Model
	Employer string
}

type Paycheck struct {
	// paychecks are from my dayjob
	gorm.Model
	EmployerID uint     `gorm:"not null"`
	Employer   Employer `gorm:"foreignKey:EmployerID"`
	Total      float64
	FourOneK   float64
	Taxes      float64
	NetCheck   float64
}

type ExpenseCategory struct {
	gorm.Model
	Category    string `gorm:"not null"`
	Description string `gorm:"not null"`
}

type ExpenseLocation struct {
	gorm.Model
	ExpenseCategoryId uint
	ExpenseCategory   ExpenseCategory `gorm:"foreignKey:ExpenseCategoryId"`
	Location          string          `gorm:"not null"`
}

type Expense struct {
	gorm.Model
	ExpenseLocationId uint
	ExpenseLocation   ExpenseLocation
	Amount            float64
}

type BillType struct {
	gorm.Model
	BillType string `gorm:"not null"`
}

type Bill struct {
	gorm.Model
	BillTypeID uint
	BillType   BillType
	BilledTo   string
	Amount     float64
}

type InvoiceCategory struct{}

type Invoice struct {
	gorm.Model
	ClientID    uint
	Client      Client `gorm:"foreignKey:ClientID"`
	InvoicedFor InvoiceCategory
	Total       float64
	Taxes       float64
	Net         float64
} // this will be for lee development

type Finances struct {
	gorm.Model
}

func QueryStatCodes(db *gorm.DB) ([]StatusCode, error) {
	var stats []StatusCode
	if result := db.Find(&stats); result.Error != nil {
		return nil, result.Error
	}
	return stats, nil
}

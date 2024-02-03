package models

/*
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
*/

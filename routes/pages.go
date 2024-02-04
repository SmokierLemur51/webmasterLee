package routes

import (
	"html/template"
	"net/http"

	"github.com/SmokierLemur51/lo-go/models"
)

type Calculation struct {
}

type PublicPageData struct {
	Page    string
	Title   string
	Content string
	Math    Calculation
	CSS     string
}

var PUBLIC_CSS string = "/static/css/main.css"
var PORTAL_CSS string = "/static/css/portal.css"

func (p PublicPageData) RenderHTMLTemplate(w http.ResponseWriter) {
	tmpl, err := template.ParseFiles("templates/" + p.Page)
	if err != nil {
		return
	}
	err = tmpl.Execute(w, p)
	if err != nil {
		return
	}
	// this prevents the superflous hanlder err
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
}

type PortalPageData struct {
	Page      string
	Title     string
	Content   string
	CSS       string
	StatCodes []models.StatusCode
	Lead      models.Lead
	Leads     []models.Lead
	Client    models.Client
	Clients   []models.Client
	Project   models.Project
	Projects  []models.Project
}

func (p PortalPageData) RenderHTMLTemplate(w http.ResponseWriter) {
	tmpl, err := template.ParseFiles("templates/portal/" + p.Page)
	if err != nil {
		return
	}
	err = tmpl.Execute(w, p)
	if err != nil {
		return
	}
	// this prevents the superflous hanlder err
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
}

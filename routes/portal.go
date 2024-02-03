package routes

import (
	"fmt"
	"log"
	"net/http"

	"github.com/SmokierLemur51/lo-go/models"

	"github.com/go-chi/chi/v5"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

type PortalHandler struct {
	DB *gorm.DB
}

func (h *PortalHandler) ConnectDatabase(databaseFile string) {
	var err error
	if h.DB, err = gorm.Open(sqlite.Open(fmt.Sprintf("data/instance/%s", databaseFile)), &gorm.Config{}); err != nil {
		panic(err)
	}
}

func (h PortalHandler) ConfigureRoutes(r chi.Router) {
	r.Method(http.MethodGet, "/portal/", h.PortalRoute())
	r.Method(http.MethodGet, "/portal/projects/", h.ProjectsRoute())
	r.Method(http.MethodGet, "/portal/finances/", h.FinancesRoute())
	// post methods
	r.Method(http.MethodPost, "/portal/projects/create-project/", h.CreateProjectHandler())
	// r.Method(http.MethodPost, "/contact-request", h.ContactRequestPublicHandler())
}

func (h PortalHandler) PortalRoute() http.HandlerFunc {
	// test authentication here
	return func(w http.ResponseWriter, r *http.Request) {
		codes, _ := models.QueryStatusCodes(h.DB)
		leads, _ := models.QueryLeads(h.DB, "all")
		clients, _ := models.QueryClients(h.DB, "all")
		p := PortalPageData{Page: "portal/portal.html", Title: "Success", StatCodes: codes, Leads: leads, Clients: clients}
		p.RenderHTMLTemplate(w)
	}
}

func (h PortalHandler) ProjectsRoute() http.HandlerFunc {

	return func(w http.ResponseWriter, r *http.Request) {
		clients, err := models.QueryClients(h.DB, "all")
		if err != nil {
			panic(err)
		}
		leads, err := models.QueryLeads(h.DB, "all")
		if err != nil {
			panic(err)
		}
		p := PortalPageData{Page: "portal/projects.html", Title: "Projects", Clients: clients, Leads: leads}
		p.RenderHTMLTemplate(w)
	}
}

// incomplete, needs input validation
func (h PortalHandler) CreateProjectHandler() http.HandlerFunc {

	return func(w http.ResponseWriter, r *http.Request) {
		if err := r.ParseForm(); err != nil {
			log.Println(err)
			// add better error handling
			http.Error(w, err.Error(), http.StatusBadRequest)
		}
		c := r.FormValue("codename")
		s := r.FormValue("leadSelect")
		err := ProcessCreateProjectForm(
			r.FormValue("status"), r.FormValue("lead"), r.FormValue("client"),
			r.FormValue("codename"), r.FormValue("description"), r.FormValue("hourly"),
			r.FormValue("wholesale"), r.FormValue("totalTime"), r.FormValue("subscription"),
		)
		if err != nil {
			log.Println(err)
		}
		fmt.Printf("\nCodename: %s Lead: %v\n\n", c, s)
		http.Redirect(w, r, "/portal/projects/", http.StatusSeeOther)
	}
}

/*
Financial Section
*/
func (h PortalHandler) FinancesRoute() http.HandlerFunc {

	return func(w http.ResponseWriter, r *http.Request) {
		// need to define models for finances
		p := PortalPageData{Page: "portal/finances.html", Title: "Finances"}
		p.RenderHTMLTemplate(w)
	}
}

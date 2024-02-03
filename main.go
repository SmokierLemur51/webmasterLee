package main

import (
	"log"

	"github.com/SmokierLemur51/lo-go/routes"

	"net/http"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"

	// "github.com/go-chi/jwtauth/v5"
	_ "github.com/mattn/go-sqlite3"
)

func main() {
	var PORT string = ":5000"
	var DATABASE_FILE = "testing_gorm_v1.db"

	r := chi.NewRouter()
	r.Use(middleware.RequestID)
	r.Use(middleware.RealIP)
	r.Use(middleware.Logger)
	r.Use(middleware.Recoverer)

	r.Handle("/static/*", http.StripPrefix("/static/", http.FileServer(http.Dir("./static"))))

	h := routes.PublicHandler{}
	h.ConnectDatabase(DATABASE_FILE)
	h.ConfigureRoutes(r)

	portal := &routes.PortalHandler{}
	portal.ConnectDatabase(DATABASE_FILE)
	portal.ConfigureRoutes(r)

	// tests.CreateModels(portal.DB)
	// tests.PopulateLeads(portal.DB)
	// tests.PopulateClients(portal.DB)

	log.Println("Starting server on port ", PORT)
	http.ListenAndServe(PORT, r)
}

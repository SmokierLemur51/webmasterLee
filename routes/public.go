package routes

import (
	"fmt"
	"log"

	// "github.com/SmokierLemur51/lo-go/models"
	"net/http"

	"github.com/go-chi/chi/v5"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

type PublicHandler struct {
	DB *gorm.DB
}

func (h *PublicHandler) ConnectDatabase(databaseFile string) {
	var err error
	if h.DB, err = gorm.Open(sqlite.Open(fmt.Sprintf("data/instance/%s", databaseFile)), &gorm.Config{}); err != nil {
		panic(err)
	}
}

func (h PublicHandler) ConfigureRoutes(r chi.Router) {
	r.Method(http.MethodGet, "/", h.IndexPublicHandler())
	r.Method(http.MethodGet, "/about", h.AboutPublicHandler())
	r.Method(http.MethodGet, "/blog", h.BlogPublicHandler())
	r.Method(http.MethodGet, "/blog/{article}", h.ArticlePublicHandler())
	r.Method(http.MethodGet, "/calculator", h.CalculatorPublicHandler())

	// post methods
	r.Method(http.MethodPost, "/contact-request", h.ContactRequestPublicHandler())
}

func (h PublicHandler) IndexPublicHandler() http.HandlerFunc {
	// test authentication here
	return func(w http.ResponseWriter, r *http.Request) {
		p := PublicPageData{Page: "index.html", Title: "Success"}
		p.RenderHTMLTemplate(w)
	}
}

func (h PublicHandler) AboutPublicHandler() http.HandlerFunc {
	// test authentication here
	return func(w http.ResponseWriter, r *http.Request) {
		p := PublicPageData{Page: "about.html", Title: "Success"}
		p.RenderHTMLTemplate(w)
	}
}

func (h PublicHandler) BlogPublicHandler() http.HandlerFunc {
	// test authentication here
	return func(w http.ResponseWriter, r *http.Request) {
		// load all articles

		p := PublicPageData{Page: "blog.html", Title: "Success"}
		p.RenderHTMLTemplate(w)
	}
}

func (h PublicHandler) LoginPublicHandler() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		p := PublicPageData{Page: "login.html", Title: "Success"}
		p.RenderHTMLTemplate(w)
	}
}

func (h PublicHandler) ArticlePublicHandler() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		article := chi.URLParam(r, "article") // https://go-chi.io/#/pages/routing
		log.Printf("Article %s", article)
		p := PublicPageData{Page: "article.html", Title: "Success"}
		p.RenderHTMLTemplate(w)
	}
}

func (h PublicHandler) CalculatorPublicHandler() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {

		p := PublicPageData{Page: "calculator.html", Title: "Calculator"}
		p.RenderHTMLTemplate(w)
	}
}

// Post
func (h PublicHandler) ContactRequestPublicHandler() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		err := r.ParseForm()
		if err != nil {
			// redirect to error page
			http.Error(w, "Error processing contact request.", http.StatusBadRequest)
		}
		// parse form

		// add to database

		// send email/text confirmation
	}
}

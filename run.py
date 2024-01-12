from web import create_app

app = create_app("testing.db")

if __name__ == "__main__":
	app.run(debug=True)
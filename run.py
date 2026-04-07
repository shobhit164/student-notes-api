from app import create_app

app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) #check the port connection -> Thanks for the heads up charan! I checked eveything it is working fine! The problem with port number is resolved now!


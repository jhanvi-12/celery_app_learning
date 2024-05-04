"""This module is the server side of the application to run the application."""
import uvicorn

from app.__init__ import app

if __name__ == '__main__':
    uvicorn.run("run:app",
                host="localhost",
                port=8006,
                reload=True)

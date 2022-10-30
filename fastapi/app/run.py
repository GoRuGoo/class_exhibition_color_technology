import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="100.64.1.47", reload=True, access_log=True)

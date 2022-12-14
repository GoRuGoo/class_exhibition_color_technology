import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8000,
        host="192.168.10.3",
        reload=True,
        access_log=True,
        ssl_keyfile="./server.key",
        ssl_certfile="./server.crt",
    )

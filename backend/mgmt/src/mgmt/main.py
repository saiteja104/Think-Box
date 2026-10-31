from fastapi import FastAPI


app = FastAPI(title = "ThinkBox API")



@app.get("/health")
def health_check():
    return {"status":"ok"}
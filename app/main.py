from fastapi import FastAPI, Body
import uvicorn
import run_agent


app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Hello World"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/send_message")
def send_message(message: str = Body(..., embed=True)):
    print("message: ", message)
    if not message:
        return {"error": "No message provided"}
    
    return {"response": run_agent.send_message_to_agent(message)}


@app.get("/get_agent_intro")
def get_agent_intro():
    return {"response": run_agent.get_agent_intro()}


if __name__ == "__main__":    
    uvicorn.run(app, host="127.0.0.1", port=8000)

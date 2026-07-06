from fastapi import FastAPI
from pydantic import BaseModel
from src.inference import analyze_ticket

app = FastAPI(title="Hybrid-Local AI IT Service Desk Copilot")


class TicketRequest(BaseModel):
    ticket_text: str


@app.post("/analyze-ticket")
def analyze_ticket_api(request: TicketRequest):
    result = analyze_ticket(request.ticket_text)
    return result
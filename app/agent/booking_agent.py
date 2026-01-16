from strands import Agent
from app.mcp.tools.availability import check_room_availability
from app.mcp.tools.book_room import make_room_reservation

booking_agent = Agent(
    name="Booking Agent",
    model="anthropic.claude-3-5-sonnet-20240620-v1:0",
    tools=[check_room_availability, make_room_reservation],
    system_prompt="Você é responsável apenas por consultas e reservas."
)
from strands import Agent
from app.agent.util.invoke_model import bedrockModel
from app.mcp.mcp_client import mcp_client
from app.mcp.tools.availability import check_room_availability
from app.mcp.tools.book_room import make_room_reservation

booking_agent = Agent(
    name="Booking Agent",
    model=bedrockModel,
    tools=[check_room_availability, make_room_reservation],
    system_prompt="Você é responsável apenas por consultas e reservas. Estamos no ano de 2026, entao se o usuario fornecer somente o dia da data, considere o ano atual e o mes atual"
)
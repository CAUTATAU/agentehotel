from strands.tools import tool
from app.aws.adapters.booking_adapter import BookingAdapter

booking_adapter = BookingAdapter()

@tool(
    name="check_room_availability",
    description="Verifica a disponibilidade de quartos para uma data específica. Use este ferramenta para verificar se há quartos disponíveis antes de fazer uma reserva.",
)
def check_room_availability(date: str) -> dict:
    return booking_adapter.check_availability(date)
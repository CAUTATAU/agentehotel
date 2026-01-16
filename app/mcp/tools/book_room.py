from strands.tools import tool
from app.aws.adapters.booking_adapter import BookingAdapter

booking_adapter = BookingAdapter()

@tool(
    name="make_room_reservation",
    description="Faz uma reserva de quarto para um cliente. Use esta ferramenta para reservar um quarto após verificar a disponibilidade.",
)
def make_room_reservation(date: str, name: str, room_type: str, number_of_nights: int) -> dict:
    return booking_adapter.create_booking(date, name, room_type, number_of_nights)
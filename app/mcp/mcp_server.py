from mcp.server.fastmcp import FastMCP
mcp_server = FastMCP("hotel-mcp")

@mcp_server.tool()
def knowledge_base_query(query: str) -> str:
    from tools.knowledge_tool import knowledge_base_query
    return knowledge_base_query(query)

@mcp_server.tool()
def check_room_availability(date: str) -> dict:
    from app.mcp.tools.availability import check_room_availability
    return check_room_availability(date)

@mcp_server.tool()
def make_room_reservation(date: str, room_type: str, guest_name: str) -> dict:
    from app.mcp.tools.book_room import make_room_reservation
    return make_room_reservation(date, room_type, guest_name)

if __name__ == "__main__":
    mcp_server.run()
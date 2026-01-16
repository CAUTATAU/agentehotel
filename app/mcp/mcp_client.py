from strands.tools.mcp import MCPClient
from mcp import stdio_client, StdioServerParameters
def hotel_mcp_transport():
    return stdio_client(
        StdioServerParameters(
            command="python",
            args=["-m", "app.mcp.mcp_server"]
        )
    )

mcp_client = MCPClient(hotel_mcp_transport)
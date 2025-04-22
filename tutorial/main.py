# server.py
from mcp.server.fastmcp import FastMCP
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Create an MCP server
mcp = FastMCP("DemoServer")
print(f"Created MCP server: {mcp.name}")

# Simple tool
@mcp.tool()
def say_hello(name: str) -> str:
    """Say hello to someone

    Args:
        name: The person's name to greet
    """
    message = f"Hello, {name}! Nice to meet you."
    print(f"Tool executed: say_hello({name}) -> \"{message}\"")
    return message

# Run the server
if __name__ == "__main__":
    print("Starting MCP server...")
    try:
        mcp.run()
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"Error running server: {e}")
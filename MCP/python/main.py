"""
MCP Server - Python Implementation
"""

import os
import json
import requests
from pathlib import Path
from typing import Annotated
from pydantic import Field
from mcp.server.fastmcp import FastMCP

# Create MCP server instance
mcp = FastMCP("MCP Server")

def get_config():
    """Get configuration from environment or config file."""
    class Config:
        def __init__(self):
            self.base_url = os.getenv("API_BASE_URL")
            self.bearer_token = os.getenv("API_BEARER_TOKEN")
            
            # Try to load from config file if env vars not set
            if not self.base_url or not self.bearer_token:
                config_path = Path.home() / ".api" / "config.json"
                if config_path.exists():
                    with open(config_path, 'r') as f:
                        config_data = json.load(f)
                        self.base_url = self.base_url or config_data.get("baseURL")
                        self.bearer_token = self.bearer_token or config_data.get("bearerToken")
    
    return Config()

# Add configuration resource
@mcp.resource("config://settings")
def get_config_resource() -> str:
    """Get current configuration settings."""
    config = get_config()
    return json.dumps({
        "base_url": config.base_url,
        "bearer_token": "***" if config.bearer_token else None
    }, indent=2)

# Tool functions
@mcp.tool()
def get_get_settings() -> str:
    """get notification settings"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        
        # Make API call
        url = f"{config.base_url}/get_settings"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_record_action_trails() -> str:
    """analytics"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/record_action_trails"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_get_suggested_follows_all(page_size: Annotated[str, Field(description="")], page: Annotated[str, Field(description="")], in_onboarding: Annotated[str, Field(description="")]) -> str:
    """gets suggested follows during signup"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if page_size: params["page_size"] = page_size
        if page: params["page"] = page
        if in_onboarding: params["in_onboarding"] = in_onboarding
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_check_for_update(is_testflight: Annotated[str, Field(description="")]) -> str:
    """Clubhouse uses this to check for updates when app is not installed from App Store (eg TestFlight)"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if is_testflight: params["is_testflight"] = is_testflight
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_create_channel() -> str:
    """creates a channel"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/create_channel"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_update_username() -> str:
    """edits username."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/update_username"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_get_suggested_club_invites() -> str:
    """find users to invite to clubs based on phone number"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/get_suggested_club_invites"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_get_club() -> str:
    """gets club by id"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/get_club"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_complete_phone_number_auth() -> str:
    """Call phone number auth."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/complete_phone_number_auth"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_get_online_friends() -> str:
    """gets online friends on the app homepage."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/get_online_friends"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_update_notifications() -> str:
    """updates notification during signup."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/update_notifications"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_get_release_notes() -> str:
    """gets release notes."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/get_release_notes"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_get_topic() -> str:
    """looks up topic by ID."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/get_topic"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_join_channel() -> str:
    """join a channel."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/join_channel"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_get_welcome_channel() -> str:
    """called during signup"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        
        # Make API call
        url = f"{config.base_url}/get_welcome_channel"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_get_users_for_topic(topic_id: Annotated[str, Field(description="")], page_size: Annotated[str, Field(description="")], page: Annotated[str, Field(description="")]) -> str:
    """looks up users by topic."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if topic_id: params["topic_id"] = topic_id
        if page_size: params["page_size"] = page_size
        if page: params["page"] = page
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_invite_to_app() -> str:
    """invite a user to the app, using one of your invites"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/invite_to_app"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_get_clubs_for_topic() -> str:
    """looks up clubs by topic."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/get_clubs_for_topic"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_get_profile() -> str:
    """looks up user profile by ID."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/get_profile"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_me() -> str:
    """gets user"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/me"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_get_channels() -> str:
    """get all channels"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        
        # Make API call
        url = f"{config.base_url}/get_channels"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_follow() -> str:
    """follows a user"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/follow"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_resend_phone_number_auth() -> str:
    """Resend phone number auth."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/resend_phone_number_auth"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_get_actionable_notifications() -> str:
    """get actionable notifications (the bell again)"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        
        # Make API call
        url = f"{config.base_url}/get_actionable_notifications"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_invite_from_waitlist() -> str:
    """wave to another user on the waitlist to give them access"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/invite_from_waitlist"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_refresh_token() -> str:
    """gets an access_token from a refresh_token."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/refresh_token"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_get_create_channel_targets() -> str:
    """is fetched when you tap Create Room"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/get_create_channel_targets"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_get_all_topics() -> str:
    """gets all topics."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        
        # Make API call
        url = f"{config.base_url}/get_all_topics"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_get_events(page_size: Annotated[str, Field(description="")], page: Annotated[str, Field(description="")], is_filtered: Annotated[str, Field(description="")]) -> str:
    """the Upcoming for You page"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if page_size: params["page_size"] = page_size
        if page: params["page"] = page
        if is_filtered: params["is_filtered"] = is_filtered
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_leave_channel() -> str:
    """leave a channel."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/leave_channel"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_get_suggested_follows_similar() -> str:
    """find similar users. (The Sparkles button on Clubhouse's profile page)"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/get_suggested_follows_similar"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_get_suggested_follows_friends_only() -> str:
    """find people to follow by uploading contacts during signup"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/get_suggested_follows_friends_only"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_get_suggested_invites() -> str:
    """find users to invite based on phone number."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/get_suggested_invites"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_get_notifications(page_size: Annotated[str, Field(description="")], page: Annotated[str, Field(description="")]) -> str:
    """get notifications (the bell icon)"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if page_size: params["page_size"] = page_size
        if page: params["page"] = page
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_get_following() -> str:
    """get a list of the users and clubs that this user is following. Returned users have bios truncated to ~80 characters."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/get_following"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_get_suggested_speakers() -> str:
    """gets suggested users when you start a private room"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/get_suggested_speakers"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_call_phone_number_auth() -> str:
    """Call phone number auth."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/call_phone_number_auth"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_start_phone_number_auth() -> str:
    """Starts phone number auth."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/start_phone_number_auth"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_search_clubs() -> str:
    """search clubs."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/search_clubs"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_check_waitlist_status() -> str:
    """checks waitlist status."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/check_waitlist_status"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_search_users() -> str:
    """search for users"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body (customize based on your API requirements)
        request_data = {}
        
        # Make API call
        url = f"{config.base_url}/search_users"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


if __name__ == "__main__":
    mcp.run()

from pydantic import BaseModel
from app.config import DeploymentType


class UIConfig(BaseModel):
    """Parameters for frontend access to Keycloak"""

    clientId: str
    realm: str
    url: str
    deployment: DeploymentType

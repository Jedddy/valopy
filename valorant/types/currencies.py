from typing import TypedDict


class CurrencyPayload(TypedDict):
    uuid: str
    displayName: str
    displayNameSingular: str
    displayIcon: str
    largeIcon: str
    assetPath: str

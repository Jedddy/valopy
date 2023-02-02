from typing import TypedDict, Union


class BundlePayload(TypedDict):
    uuid: str
    displayName: str
    displayNameSubText: Union[str, None]
    description: str
    extraDescription: Union[str, None]
    promoDescription: Union[str, None]
    useAdditionalContext: bool
    displayIcon: str
    displayIcon2: str
    verticalPromoImage: str
    assetPath: str

"""Bundles"""

from typing import Union

from .assets import Media
from .types.bundles import BundlePayload


class Bundle:
    """Represents a valorant bundle.

    Attributes
    ----------
    uuid: :class:`str`
        The bundle's UUID.
    name: :class:`str`
        The bundle's name.
    name_subtext: Optional[:class:`str`]
        The name subtext.
    description: :class:`str`
        The bundle's description.
    extra_description: Optional[:class:`str`]
        The extra description.
    promo_description: Optional[:class:`str`]
        The promo description
    use_additional_context: :class:`bool`
        Indicates if the bundle uses additional context.
    display_icon: :class:`valorant.Media`
        The display icon.
    display_icon2: :class:`valorant.Media`
        Another version of the display icon.
    vertical_promo_image: :class:`valorant.Media`
        The vertical promo image.
    asset_path: :class:`str`
        The asset path on the API.
    """

    __slots__ = (
        "uuid",
        "name",
        "name_subtext",
        "description",
        "extra_description",
        "promo_description",
        "use_additional_context",
        "display_icon",
        "display_icon2",
        "vertical_promo_image",
        "asset_path",
    )

    uuid: str
    name: str
    name_subtext: Union[str, None]
    description: str
    extra_description: Union[str, None]
    promo_description: Union[str, None]
    use_additional_context: bool
    display_icon: Media
    display_icon2: Media
    vertical_promo_image: Media
    asset_path: str

    def __init__(self, data: BundlePayload) -> None:
        self.uuid: str = data["uuid"]
        self.name: str = data["displayName"]
        self.name_subtext: Union[str, None] = data["displayNameSubText"]
        self.description: str = data["description"]
        self.extra_description: Union[str, None] = data["extraDescription"]
        self.promo_description: Union[str, None] = data["promoDescription"]
        self.use_additional_context: bool = data["useAdditionalContext"]
        self.display_icon: Media = Media(data["displayIcon"])
        self.display_icon2: Media = Media(data["displayIcon2"])
        self.vertical_promo_image: Media = Media(data["verticalPromoImage"])
        self.asset_path: str = data["assetPath"]

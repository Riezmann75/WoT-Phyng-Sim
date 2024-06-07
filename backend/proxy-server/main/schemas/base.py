from typing import TYPE_CHECKING
from typing_extensions import Annotated

import annotated_types
from pydantic import AnyUrl, BaseModel, UrlConstraints, HttpUrl, ConfigDict


class BaseSchema(BaseModel):
    def json_serializable_dict(self):
        return self.model_dump(mode="json")


class BaseResponseSchema(BaseSchema):
    model_config = ConfigDict(from_attributes=True)


class BaseValidationSchema(BaseSchema):
    model_config = ConfigDict(extra="ignore", str_strip_whitespace=True, frozen=False)


class MutableBaseValidationSchema(BaseValidationSchema):
    model_config = ConfigDict(frozen=True)


if TYPE_CHECKING:
    NonEmptyString = str
    ShortString = str
    NonEmptyList = list
    LongString = str
    StrictUrl = str
    Url = str
    Slug = str
    MaskedStr = str
else:
    NonEmptyString = Annotated[str, annotated_types.MinLen(1)]

    ShortString = Annotated[NonEmptyString, annotated_types.MaxLen(256)]

    LongString = Annotated[NonEmptyString, annotated_types.MaxLen(5000)]

    Slug = Annotated[NonEmptyString, annotated_types.MaxLen(1024)]

    NonEmptyList = Annotated[list, annotated_types.MinLen(1)]

    Url = Annotated[AnyUrl, UrlConstraints(max_length=2048)]

    StrictUrl = Annotated[HttpUrl, UrlConstraints()]

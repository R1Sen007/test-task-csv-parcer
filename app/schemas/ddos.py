from pydantic import BaseModel, ConfigDict, field_validator
from pydantic.networks import IPvAnyAddress


class DdosSchema(BaseModel):
    '''
    Ddos info schema.
    '''

    saddr: IPvAnyAddress
    avgDur: float

    model_config = ConfigDict(
        extra='forbid',
    )

    @field_validator('saddr')
    def validate_uuids(cls, value):
        if value:
            return str(value)
        return value

from .base import BaseValidationSchema

class RunCaseSchema(BaseValidationSchema):
    ac_temperature: float
    ac_velocity: float
    ac_angle:float

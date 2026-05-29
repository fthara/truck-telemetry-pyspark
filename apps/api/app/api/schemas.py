from pydantic import BaseModel

#### Client Schemas ####
class CreateClientSchema(BaseModel):
    name: str
    cnpj: str

class UpdateClientSchema(BaseModel):
    name: str
    cnpj: str

class ListClientSchema(BaseModel):
    id: int
    name: str
    cnpj: str

#### Truck Schemas ####
class CreateTruckSchema(BaseModel):
    license_plate: str
    client_id: int

#### Driver Schemas ####
class CreateDriverSchema(BaseModel):
    name: str
    document: str
    client_id: int

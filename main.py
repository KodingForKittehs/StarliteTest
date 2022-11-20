
import logging
import pydantic
import starlite
from typing import Literal, List
from starlite import Controller, get

logging.basicConfig(level=logging.INFO)


class Cat(pydantic.BaseModel):
    name: str
    color: Literal['orange', 'brown']
    age: int


class CatController(Controller):
    path = "/cats"

    @get()
    async def list_cats(self) -> List[Cat]:
        return [Cat(name='talon', color='brown', age='18')]


if __name__ == '__main__':
    logging.info('Starting')

    talon = Cat(name='talon', color='brown', age='18')
    print(talon)

    app = starlite.Starlite(route_handlers=[CatController])
    pass

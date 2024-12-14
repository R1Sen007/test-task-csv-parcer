import pandas as pd
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.ddos import Ddos
from app.schemas.ddos import DdosSchema


class DdosCrud(CRUDBase):
    '''
    Create, read, update, delete obj from database.
    '''

    async def get(
        self,
        obj_saddr: int,
        session: AsyncSession,
    ):
        db_obj = await session.execute(
            select(self.model).where(
                self.model.saddr == obj_saddr
            )
        )
        return db_obj.scalars().first()

    async def get_all_existing_saddr(self, session: AsyncSession):
        '''Get all existing saddr in database.'''
        ddos_objects = await self.get_multi(session)
        return [obj.saddr for obj in ddos_objects]

    async def create_update_from_csv(self, file, session: AsyncSession):
        '''Creating or updating if exists data from csv.'''
        data_frame = pd.read_csv(file.file, usecols=['saddr', 'dur'])
        results = (
            data_frame
            .groupby('saddr', as_index=False)
            .mean()
            .rename(columns={'dur': 'avgDur'})
            .to_dict(orient='records')
        )
        results = [DdosSchema(**row) for row in results]
        existing_saddr = await self.get_all_existing_saddr(session)
        for row in results:
            if row.saddr in existing_saddr:
                db_obj = await self.get(row.saddr, session)
                await self.update(db_obj, row, session)
            else:
                await self.create(row, session)
        return results


ddos_crud = DdosCrud(Ddos)

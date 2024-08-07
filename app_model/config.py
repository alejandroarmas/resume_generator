from motorhead import AgnosticDatabase


async def create_indexes(database: AgnosticDatabase) -> None:
    from .job_application.service import DeviceService

    await DeviceService(database).create_indexes()

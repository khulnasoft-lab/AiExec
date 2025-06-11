from typing_extensions import override

from aiexec.services.factory import ServiceFactory
from aiexec.services.settings.service import SettingsService
from aiexec.services.state.service import InMemoryStateService


class StateServiceFactory(ServiceFactory):
    def __init__(self) -> None:
        super().__init__(InMemoryStateService)

    @override
    def create(self, settings_service: SettingsService):
        return InMemoryStateService(
            settings_service,
        )

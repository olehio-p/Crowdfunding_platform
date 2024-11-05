from abc import ABC, abstractmethod
from typing import Any, Optional, List, Dict


class BaseRepository(ABC):
    @abstractmethod
    def get(self, instance_id: Any) -> Optional[Any]:
        pass

    @abstractmethod
    def get_all(self) -> List[Any]:
        pass

    @abstractmethod
    def create(self, **kwargs: Any) -> Any:
        pass

    @abstractmethod
    def update(self, instance_id: Any, **kwargs: Any) -> Optional[Any]:
        pass

    @abstractmethod
    def delete(self, instance_id: Any) -> bool:
        pass

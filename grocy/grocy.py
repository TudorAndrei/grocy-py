import logging
import os
from functools import cached_property

from .grocy_api_client import DEFAULT_PORT_NUMBER, GrocyApiClient
from .managers.batteries import BatteryManager
from .managers.calendar import CalendarManager
from .managers.chores import ChoreManager
from .managers.equipment import EquipmentManager
from .managers.files import FileManager
from .managers.generic import GenericEntityManager
from .managers.meal_plan import MealPlanManager
from .managers.recipes import RecipeManager
from .managers.shopping_list import ShoppingListManager
from .managers.stock import StockManager
from .managers.system import SystemManager
from .managers.tasks import TaskManager
from .managers.users import UserManager

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class Grocy:
    """Main client for the Grocy ERP API.

    Provides access to domain-specific managers as cached properties.
    Each manager handles a subset of the Grocy API.

    Args:
        base_url: Grocy server URL (e.g. ``"https://grocy.example.com"``).
            If not provided, reads from ``GROCY_BASE_URL``.
        api_key: API key for authentication. Use ``"demo_mode"`` for the demo server.
            If not provided, reads from ``GROCY_API_KEY``.
        port: Server port number.
        path: Optional URL path prefix (e.g. ``"grocy"`` for ``/grocy/api/``).
        verify_ssl: Whether to verify SSL certificates.
        debug: Enable debug logging.
    """

    def __init__(
        self,
        base_url: str | None = None,
        api_key: str | None = None,
        port: int = DEFAULT_PORT_NUMBER,
        path: str | None = None,
        verify_ssl=True,
        debug=False,
    ):
        resolved_base_url = base_url or os.getenv("GROCY_BASE_URL")
        resolved_api_key = api_key or os.getenv("GROCY_API_KEY")

        if not resolved_base_url:
            raise ValueError(
                "Grocy base URL is required. Pass base_url or set GROCY_BASE_URL."
            )

        if not resolved_api_key:
            raise ValueError(
                "Grocy API key is required. Pass api_key or set GROCY_API_KEY."
            )

        self._api_client = GrocyApiClient(
            resolved_base_url, resolved_api_key, port, path, verify_ssl, debug
        )

        if debug:
            _LOGGER.setLevel(logging.DEBUG)

    @cached_property
    def stock(self) -> StockManager:
        """Access stock management operations."""
        return StockManager(self._api_client)

    @cached_property
    def shopping_list(self) -> ShoppingListManager:
        """Access shopping list operations."""
        return ShoppingListManager(self._api_client)

    @cached_property
    def recipes(self) -> RecipeManager:
        """Access recipe operations."""
        return RecipeManager(self._api_client)

    @cached_property
    def chores(self) -> ChoreManager:
        """Access chore management operations."""
        return ChoreManager(self._api_client)

    @cached_property
    def tasks(self) -> TaskManager:
        """Access task management operations."""
        return TaskManager(self._api_client)

    @cached_property
    def batteries(self) -> BatteryManager:
        """Access battery tracking operations."""
        return BatteryManager(self._api_client)

    @cached_property
    def equipment(self) -> EquipmentManager:
        """Access equipment management operations."""
        return EquipmentManager(self._api_client)

    @cached_property
    def meal_plan(self) -> MealPlanManager:
        """Access meal planning operations."""
        return MealPlanManager(self._api_client)

    @cached_property
    def users(self) -> UserManager:
        """Access user management operations."""
        return UserManager(self._api_client)

    @cached_property
    def system(self) -> SystemManager:
        """Access system information and configuration."""
        return SystemManager(self._api_client)

    @cached_property
    def generic(self) -> GenericEntityManager:
        """Access generic entity CRUD operations."""
        return GenericEntityManager(self._api_client)

    @cached_property
    def calendar(self) -> CalendarManager:
        """Access calendar operations."""
        return CalendarManager(self._api_client)

    @cached_property
    def files(self) -> FileManager:
        """Access file management operations."""
        return FileManager(self._api_client)

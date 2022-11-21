import logging
from flet import flet, AppBar, View, colors, Page, Text, ElevatedButton, Image, PopupMenuButton, PopupMenuItem
from config.config import Settings
from services.helper_service import HelperService
from services.license_service import LicenseService
from services.logging_service import LoggingService
from pages.greet import PageGreet
from pages.main import PageMain

logger = logging.getLogger(__name__)


def main(page: Page):

    settings = Settings()
    helper = HelperService(settings)
    license = LicenseService(settings, helper)
    LoggingService(settings)

    page_greet = PageGreet(page, settings,  helper, license)
    page_main = PageMain(page, settings, helper, license)

    # Base Page Settings
    page.title = settings.SOFTWARE_TITLE
    page.window_width = settings.APP_WINDOW_WIDTH
    page.window_height = settings.APP_WINDOW_HEIGHT

    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    page_greet.build()
                ]
            )
        )
        if page.route == "/main":
            page.views.append(
                View(
                    "/main",
                    [
                        page_main.build()
                    ]
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


flet.app(target=main, assets_dir="assets")  # , view=flet.WEB_BROWSER)

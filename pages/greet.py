from flet import Image, Icon, Text, ElevatedButton, icons, Row, colors, Column, TextButton, AlertDialog
from pathlib import Path
import os


class PageGreet():

    def __init__(self, page, settings, helper, license):

        self.page = page
        self.settings = settings
        self.helper = helper
        self.license = license

    def on_click_btn_reload_license(self, e):

        self.check_license()

        self.icn_wifi.update()
        self.txt_license_details.update()
        self.btn_open_app.update()

    def on_click_btn_open_app(self, e):

        self.dlg_modal = AlertDialog(
            modal=True,
            title=Text("Confirm Acceptance"),
            content=Text(self.settings.TDI_ITAR_PROP_STATEMENT),
            actions=[
                TextButton("Accept", on_click=self.on_click_open_main),
                TextButton("Cancel", on_click=self.on_click_close_dlg),
            ],
            actions_alignment="end",
        )
        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()

    def on_click_close_dlg(self, e):
        self.dlg_modal.open = False
        self.page.update()

    def on_click_open_main(self, e):
        self.dlg_modal.open = False
        self.page.route = "/main"
        self.page.update()

    def check_license(self):

        cur_internet_status = self.helper.is_internet_active(
            self.settings.CHECK_INTERNET_TIMEOUT)
        if cur_internet_status:
            self.icn_wifi.color = colors.GREEN
        else:
            self.icn_wifi.color = colors.RED

        # Check For Authentication
        if not self.license.is_auth:
            self.txt_license_details.value = "No Valid License File"
            self.txt_license_details.color = colors.RED_600
        else:
            self.txt_license_details.value = "Valid License File"
            self.txt_license_details.color = colors.GREEN_600

        # Check For Enable Application
        if not cur_internet_status or not self.license.is_auth:
            self.btn_open_app.disabled = True
        else:
            self.btn_open_app.disabled = False

    def build(self):

        # Controls
        self.logo = Image(
            src=f"images/TDI-logo.png",
            width=500,
            height=500,
            fit="contain",
        )

        self.icn_wifi = Icon(name=icons.WIFI)
        self.txt_license_details = Text(size=20)
        self.btn_reload_license = ElevatedButton(
            "Reread License File", on_click=self.on_click_btn_reload_license)
        self.btn_open_app = ElevatedButton(
            "Open " + self.settings.SOFTWARE_NAME, on_click=self.on_click_btn_open_app)

        # Containers
        self.row_logo = Row(
            controls=[self.logo], alignment="center")
        self.row_user = Row(controls=[self.icn_wifi, self.txt_license_details,
                                      self.btn_reload_license, self.btn_open_app], alignment="center")
        # Check For Internet
        self.check_license()

        return Column(controls=[self.row_logo, self.row_user], alignment="spaceEvenly", height=self.settings.APP_WINDOW_HEIGHT)

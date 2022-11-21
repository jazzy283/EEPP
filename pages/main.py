from flet import flet, Text, Tabs, Tab, Dropdown, dropdown, PopupMenuButton, IconButton, PopupMenuItem, Icon, icons, Row, AppBar, TextField, Switch, Container, Divider, Column, ElevatedButton, Checkbox, FilePicker, Image
from datetime import datetime, timezone


class PageMain():

    def __init__(self, page, settings, helper, license) -> None:
        self.page = page
        self.settings = settings
        self.helper = helper
        self.license = license

    def show_license_info(e):
        pass

    def update_engine(self, e):

        # Update Power Extraction
        cur_eng_index = self.settings.ENGINE_FAMILIES.index(
            self.dd_eng_type.value)
        cur_power_extraction = self.settings.PAGE_MAIN_ENGINE_POWER_EXTRACTION[cur_eng_index]

        self.dd_power_extraction.options.clear()
        self.dd_power_extraction.value = ""

        for item in cur_power_extraction:
            self.dd_power_extraction.options.append(dropdown.Option(item))

        self.dd_power_extraction.update()

        # Update Engine Image
        self.col_eng_image.controls.clear()
        self.col_eng_image.controls.append(
            Image(
                src=f"images/{self.dd_eng_type.value}.png",
                width=500,
                height=500,
                fit="contain",
            )
        )
        self.col_eng_image.update()

    def reset_main_tab(self, e):

        self.dd_eng_type.value = ""
        self.dd_altitude_min.value = int(
            self.settings.PAGE_MAIN_ALTITUDE_LINSPACE[0])
        self.dd_altitude_max.value = int(
            self.settings.PAGE_MAIN_ALTITUDE_LINSPACE[-1])
        self.dd_mach_number_min.value = f"{self.settings.PAGE_MAIN_MACH_NUMBER_LINSPACE[0]:.2f}"
        self.dd_mach_number_max.value = f"{self.settings.PAGE_MAIN_MACH_NUMBER_LINSPACE[-1]:.2f}"
        self.dd_atmosphere.value = ""
        self.dd_power_extraction.options.clear()
        self.dd_power_extraction.value = ""
        self.dd_fuel_type.value = ""
        self.dd_inlet_pressure_recovery.value = ""

        # Update Engine Image
        self.col_eng_image.controls.clear()
        self.col_eng_image.controls.append(
            Image(
                src=f"images/TDI-logo.png",
                width=500,
                height=500,
                fit="contain",
            )
        )
        self.col_eng_image.update()

        self.page.update()

    def build_main_tab(self):

        dd_width = 400

        # Engine Type Dropdown
        self.dd_eng_type = Dropdown(
            width=dd_width,
            label="Choose Engine Type:",
            on_change=self.update_engine)

        for item in self.license.auth_engine_access:
            self.dd_eng_type.options.append(dropdown.Option(item))

        # Altitude Dropdown/s
        self.dd_altitude_min = Dropdown(
            width=dd_width,
            label="Choose Minimum Altitude [ft]:"
        )
        self.dd_altitude_max = Dropdown(
            width=dd_width,
            label="Choose Maximum Altitude [ft]:"
        )
        for item in self.settings.PAGE_MAIN_ALTITUDE_LINSPACE:
            self.dd_altitude_min.options.append(dropdown.Option(int(item)))
            self.dd_altitude_max.options.append(dropdown.Option(int(item)))
        self.dd_altitude_min.value = int(
            self.settings.PAGE_MAIN_ALTITUDE_LINSPACE[0])
        self.dd_altitude_max.value = int(
            self.settings.PAGE_MAIN_ALTITUDE_LINSPACE[-1])

        # Mach Number Dropdown/s
        self.dd_mach_number_min = Dropdown(
            width=dd_width,
            label="Choose Minimum Mach Number:"
        )
        self.dd_mach_number_max = Dropdown(
            width=dd_width,
            label="Choose Maximum Mach Number:"
        )
        for item in self.settings.PAGE_MAIN_MACH_NUMBER_LINSPACE:
            self.dd_mach_number_min.options.append(
                dropdown.Option(f"{item:.2f}"))
            self.dd_mach_number_max.options.append(
                dropdown.Option(f"{item:.2f}"))
        self.dd_mach_number_min.value = f"{self.settings.PAGE_MAIN_MACH_NUMBER_LINSPACE[0]:.2f}"
        self.dd_mach_number_max.value = f"{self.settings.PAGE_MAIN_MACH_NUMBER_LINSPACE[-1]:.2f}"

        # Atmoshpere Drowndown
        self.dd_atmosphere = Dropdown(
            width=dd_width,
            label="Choose Atmoshphere:"
        )
        for item in self.settings.PAGE_MAIN_ATMOSPHERE:
            self.dd_atmosphere.options.append(dropdown.Option(item))

        # Power Extraction
        self.dd_power_extraction = Dropdown(
            width=dd_width,
            label="Choose Power Extraction:"
        )

        # Fuel Type Drowndown
        self.dd_fuel_type = Dropdown(
            width=dd_width,
            label="Choose Fuel Type:"
        )
        for item in self.settings.PAGE_MAIN_FUEL_TYPES:
            self.dd_fuel_type.options.append(dropdown.Option(item))

        # Inlet Pressure Recovery
        self.dd_inlet_pressure_recovery = Dropdown(
            width=dd_width,
            label="Choose Inlet Pressure Recovery:"
        )
        for item in self.settings.PAGE_MAIN_INLET_PRESSURE_RECOVERY:
            self.dd_inlet_pressure_recovery.options.append(
                dropdown.Option(item))

        # Throttle Details
        self.txt_throttle = Text(
            f"Throttle will be swept from {self.settings.PAGE_MAIN_THROTTLE[0]}-{self.settings.PAGE_MAIN_THROTTLE[1]}% in increments of 5%.")

        # Buttons
        self.btn_reset = ElevatedButton("Reset", on_click=self.reset_main_tab)
        self.btn_export_data = ElevatedButton("Export Data")

        # Layout
        self.col_eng_image = Column(alignment="center", controls=[
            Image(
                src=f"images/TDI-logo.png",
                width=500,
                height=500,
                fit="contain",
            )]

        )
        self.col_user = Column(alignment="center", controls=[
            self.dd_eng_type,
            Row(controls=[self.dd_altitude_min,
                          self.dd_altitude_max]),
            Row(controls=[self.dd_mach_number_min,
                          self.dd_mach_number_max]),
            self.dd_atmosphere,
            self.dd_power_extraction,
            self.dd_fuel_type,
            self.dd_inlet_pressure_recovery,
            self.txt_throttle,
            Row(controls=[self.btn_reset,
                          self.btn_export_data])
        ]
        )

        self.row_main = Row(alignment="spaceEvenly", controls=[
                            self.col_eng_image, self.col_user])

        return self.row_main

    def build_admin_tab(self):
        pass
    #     # Admin Create License
    #     self.get_directory_dialog = FilePicker()
    #     self.page.overlay.extend([self.get_directory_dialog])

    #     self.txtfld_company_name = TextField(
    #         label="Company Name"
    #     )
    #     self.swtch_is_admin = Switch(
    #         label="Is Admin?"
    #     )
    #     self.txtfld_expire_days = TextField(
    #         label="License Duration (days)"
    #     )
    #     self.btn_license_save_location = ElevatedButton(
    #         "Save License",
    #         icon=icons.FOLDER_OPEN,
    #         on_click=lambda _: self.get_directory_dialog.get_directory_path(),
    #         # disabled=self.page.web,
    #     )
    #     self.clmn_eng_families = Column()
    #     for item in self.license.auth_engine_access:
    #         self.clmn_eng_families.controls.append(Checkbox(label=item))

    #     # Open directory dialog

    #     self.row_admin_create_license = Row(
    #         vertical_alignment="center",
    #         controls=[
    #             self.txtfld_company_name,
    #             self.swtch_is_admin,
    #             self.txtfld_expire_days,
    #             self.clmn_eng_families,
    #             self.btn_license_save_location

    #         ]
    #     )

    #     self.row_admin_manage_library = Row()
        # Column(controls=[
        #                 self.row_header,
        #                 self.row_admin_create_license,
        #                 self.row_admin_manage_library

    # def appbar(self):

    #     return AppBar(
    #         actions=[
    #             IconButton(icons.INFO_OUTLINED,
    #                        on_click=self.show_license_info),
    #             PopupMenuButton(

    #                 items=[
    #                     PopupMenuItem(text="License Details"),
    #                     PopupMenuItem(),
    #                     PopupMenuItem(text="Company Name: " +
    #                                   self.license.auth_company),
    #                     PopupMenuItem(text="License Expires: " +
    #                                   str(datetime.fromtimestamp(float(self.license.auth_expire_date), timezone.utc))),
    #                     PopupMenuItem(text="Engine Familly Access:" +
    #                                   (", ").join(self.license.auth_engine_access))
    #                 ]
    #             ),
    #         ],
    #     )

    def build(self):

        # Header Row
        self.row_header = Row(
            controls=[IconButton(icon=icons.INFO_OUTLINED)],
            alignment="end"
        )

        self.tab_main = Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                Tab(
                    text="Data Analysis",
                    content=self.build_main_tab(),
                )
            ],
            expand=1,
        )
        if self.license.auth_is_admin:
            self.tab_main.tabs.append(
                Tab(
                    text="Admin",
                    content=self.build_admin_tab()
                )
            ),

        # return self.row_header
        return Column(controls=[self.row_header, self.tab_main])

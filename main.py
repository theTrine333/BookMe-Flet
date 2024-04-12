import flet as f
from flet import *
from api.__api__ import *
import time
def main(page:Page)->None:
    page.title = "BookMe"
    page.horizontal_alignment = "center",
    page.vertical_alignment = "center",
    page.theme_mode = ThemeMode.DARK,
    page.fonts = {
        "MPS": "fonts/Poppins-Medium.ttf",
        "BPS":"fonts/Poppins-SemiBold.ttf",
        "LCD":"fonts/Lcd.ttf"
    }
    
    search_field = TextField(
        height=30,
        filled=True,
        text_size =13,
        cursor_height= 28,
        multiline = False,
        border_color="transparent",
        hint_text="Search a book",
        hint_style=TextStyle(
            size=12,
            color="GREY"
        )
    )
    
    spinner = ProgressRing(
        height=20,
        width=20,
        color="orange",
        visible=False
    )
    
    def show_loading():
        spinner.visible = True
        page.update()
    
    def hide_loading():
        print("Called")
        spinner.visible = False
        page.update()
    
    search_field.on_submit = lambda _ : (
        print("Searching..."),
        show_loading(),
        searchBooks(str(search_field.value))    
    )
    
    def get_to_search():
        print("Triggered!!!")
        print(search_field.value)
    
    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    Row(
                        alignment = MainAxisAlignment.CENTER,
                        controls = [
                            Text(
                                "BookME",
                                size = 18,
                                weight="bold",
                                color = "orange",
                                font_family = "BPS"
                            )
                        ]
                    ),
                    Column(
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        controls = [
                            Image(
                                src="icons/0.png",
                                fit=ImageFit.CONTAIN, 
                            ),
                            Divider(
                                height = 5    
                            ),
                            Text(
                                "Looking for that book on the web is not easy,\nHere you just tell us the name or the topic and we organise the results for you.",
                                size = 12,
                                weight = "bold",
                                color = "orange",
                                font_family = "MPS"
                            ),
                            Divider(
                                height = 5    
                            ),
                            IconButton(
                                content = Text(
                                    "Get Started",
                                    color = "white",
                                    weight = "bold"               
                                ),
                                width=180,
                                height=44,
                                style=ButtonStyle(
                                    bgcolor={"": "orange"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=8)
                                    },
                                ),
                                on_click=lambda _ : page.go('/search')
                            ),
                            Text(
                                "POWEREDBY:",
                                size = 10,
                                font_family = "MPS"
                            ),
                            Text(
                                "TRINETECHNOLOGIES",
                                size = 10,
                                color = "blue",
                                font_family = "BPS"
                                )
                        ]
                    )
                ]
            )  
        )
        page.update()
        
        if page.route == "/search":
            page.views.append(
                View(
                    route="/search",
                    controls=[
                        Row(
                            alignment=MainAxisAlignment.START,
                            controls=[
                                IconButton(
                                    icon=icons.ARROW_BACK,
                                    icon_size = 20,
                                    icon_color="orange",
                                    on_click=lambda _ : page.go('/')
                                ),
                                search_field,
                            ],
                        ),
                        Column(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                spinner,
                            ]
                        )
                    ],
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
            page.update()
    
    def view_pop(e:ViewPopEvent) -> None:
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route) 
    
    page.on_view_pop = view_pop                   
    page.on_route_change = route_change
    page.go(page.route)

if __name__ == '__main__':
    f.app(target=main)
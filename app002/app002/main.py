from pydoc import pager
import flet as ft

def main(page: ft.Page):
    page.title="¿me perdonas?"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.bgcolor="blue"
    
    lbl1=ft.text("¿me perdnas?",
                style=ft.TextStyle(size=40,weight="bold"))
                                    
    img1=ft.image(src="triste.png",width=200,height=200)
    
    btnSi=ft.Elevatedbutton("si",
    color="green",
    width=100,
    height=50)
    
    btnNo=ft.Elevatedbutton("No",
 color="red",
    width=100,
    height=50)
    
    page.add(
        ft.Column(
            [
                lbl1,
                img1,
                ft.row([btnSi,btnNo])
            ]
        )
    )


ft.app(main)

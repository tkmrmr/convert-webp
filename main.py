import flet as ft
import os
from convert_to_webp import convert_to_webp

def main(page: ft.Page):
    page.title = "WebP変換ツール"
    page.window.width = 800
    page.window.height = 600
    page.theme = ft.Theme(color_scheme_seed="white")

    filepath_display = ft.Text("", visible=False)
    selected_image = ft.Image(
        src="", height=300, fit=ft.ImageFit.SCALE_DOWN, visible=False
    )
    compression_message = ft.Text("", visible=False)

    def pick_files_result(e: ft.FilePickerResultEvent):
        if e.files:
            filepath_display.value = e.files[0].path
            filepath_display.visible = True
            selected_image.src = e.files[0].path
            selected_image.visible = True
            convert_button.visible = True
            page.update()
        else:
            pass

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)

    file_select_button = ft.ElevatedButton(
        "ファイルを選択",
        icon=ft.icons.FILE_OPEN,
        on_click=lambda _: pick_files_dialog.pick_files(allowed_extensions=["png", "jpg", "jpeg"], allow_multiple=False),
    )

    def convert_button_clicked(e):
        convert_to_webp(selected_image.src)
        selected_image_size = os.path.getsize(selected_image.src)
        compression_message.value = f"{selected_image_size}％削減されました"
        compression_message.visible = True
        page.update()

    convert_button = ft.ElevatedButton(
        "WebPに変換",
        icon=ft.icons.FILE_DOWNLOAD,
        on_click=convert_button_clicked,
        visible=False,
    )

    page.add(
        ft.Column(
            [
                ft.Text("WebPに変換する画像を選択"),
                ft.Row([file_select_button, filepath_display]),
                selected_image,
                convert_button,
                compression_message,
            ],
        )
    )

ft.app(target=main)

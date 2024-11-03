import flet as ft
import os
from convert_to_webp import convert_to_webp

def main(page: ft.Page):
    page.title = "WebP変換ツール"
    page.window.width = 600
    page.window.height = 450
    page.theme = ft.Theme(color_scheme_seed="white")

    filepath_display = ft.Text("", visible=False)
    selected_image = ft.Image(
        src="", fit=ft.ImageFit.SCALE_DOWN, visible=False
    )
    compression_message = ft.Text("", visible=False)

    def pick_files_result(e: ft.FilePickerResultEvent):
        if e.files:
            filepath = e.files[0].path
            parts = filepath.split(os.sep)
            filepath_display.value = f"{parts[0]+os.sep+parts[1]+os.sep}...{os.sep+parts[-1]}" if len(parts) > 2 else filepath
            filepath_display.visible = True
            selected_image.src = filepath
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
        converted_image = convert_to_webp(selected_image.src)
        selected_image_size = os.path.getsize(selected_image.src)
        convered_image_size = os.path.getsize(converted_image)
        compression_rate = round((1 - convered_image_size / selected_image_size) * 100)
        compression_message.value = f"{compression_rate}％削減されました"
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
                # ft.Text("WebPに変換する画像を選択"),
                ft.Row(
                    [file_select_button, filepath_display],

                ),
                ft.Container(
                    content=selected_image,
                    height=280,
                    width=580,
                    padding=10,
                    border=ft.border.all(1),
                ),
                convert_button,
                compression_message,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)

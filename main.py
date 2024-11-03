import flet as ft
import os
from convert_to_webp import convert_to_webp

def main(page: ft.Page):
    # ウィンドウ全体の設定
    page.title = "WebP変換ツール"
    page.window.width = 600
    page.window.height = 450
    page.theme = ft.Theme()

    def pick_files_result(e: ft.FilePickerResultEvent):
        if e.files:
            filepath = e.files[0].path
            parts = filepath.split(os.sep)
            filepath_display.value = f"{parts[0]+os.sep+parts[1]+os.sep}...{os.sep+parts[-1]}" if len(parts) > 2 else filepath
            filepath_display.visible = True
            selected_image.src = filepath
            selected_image.visible = True
            convert_button.disabled = False
            page.update()
        else:
            pass

    def convert_button_clicked(e):
        file_select_button.disabled = True
        convert_button.disabled = True
        progress_ring.visible = True
        page.update()
        converted_image = convert_to_webp(selected_image.src)
        selected_image_size = os.path.getsize(selected_image.src)
        converted_image_size = os.path.getsize(converted_image)
        compression_rate = round((1 - converted_image_size / selected_image_size) * 100)
        compression_message.value = f"{compression_rate}％削減されました！"
        compression_message.visible = True
        file_select_button.disabled = False
        convert_button.disabled = False
        progress_ring.visible = False
        page.update()

    # 各コントロール
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)
    compression_message = ft.Text("", visible=False)

    file_select_button = ft.ElevatedButton(
        "ファイルを選択",
        icon=ft.icons.FILE_OPEN,
        on_click=lambda _: pick_files_dialog.pick_files(allowed_extensions=["png", "jpg", "jpeg"], allow_multiple=False),
        disabled=False,
    )
    filepath_display = ft.Text("", visible=False)

    selected_image = ft.Image(
        src="", fit=ft.ImageFit.SCALE_DOWN, visible=False,
    )
    progress_ring = ft.ProgressRing(visible=False)

    convert_button = ft.ElevatedButton(
        "WebPに変換",
        icon=ft.icons.FILE_DOWNLOAD,
        on_click=convert_button_clicked,
        disabled=True,
    )

    page.add(
        ft.Column(
            [
                ft.Row([
                    ft.Row(
                        [file_select_button, filepath_display],
                    ),
                    compression_message,
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Container(
                    content=ft.Stack(
                        [selected_image, progress_ring], 
                        alignment=ft.alignment.center,
                    ), 
                    height=280,
                    width=580,
                    padding=10,
                    border=ft.border.all(1),
                    margin=ft.margin.only(bottom=5),
                ),
                convert_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)

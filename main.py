import flet as ft


def main(page: ft.Page):
    page.title = "WebP変換ツール"
    page.window.width = 600
    page.window.height = 400
    page.theme = ft.Theme(color_scheme_seed="white")

    filepath = ""

    def pick_files_result(e: ft.FilePickerResultEvent):
        if e.files:
            filepath = e.files[0].path
        else:
            pass

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)

    file_select_button = ft.ElevatedButton(
        "ファイルを選択",
        icon=ft.icons.FILE_OPEN,
        on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=False),
    )

    page.add(
        ft.Column(
            [
                ft.Text("WebPに変換する画像を選択"),
                file_select_button,
            ],
        )
    )


ft.app(target=main)

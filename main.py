from ui.MainWindow import MainWindow
from models.update_checker import check_update

if __name__ == "__main__":
    check_update()
    MainWindow().run()
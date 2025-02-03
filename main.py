import webview
import os
import configparser

current_dir = os.path.dirname(os.path.realpath(__file__))
Assets = os.path.join(current_dir, 'Assets')

class API:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('Assets/Config.ini')
        self.directory = self.config.get('Settings', 'directory', fallback='')

    def select_directory(self):
        # 使用 pywebview 的文件选择对话框
        directory = webview.windows[0].create_file_dialog(webview.FOLDER_DIALOG)
        if directory:
            self.directory = directory[0]
            self.config.set('Settings', 'directory', self.directory)
            with open('Assets/Config.ini', 'w') as configfile:
                self.config.write(configfile)
        return self.directory

    def OpenGames(self):
        program_path = os.path.join(self.directory, "LaunchGTAIV.exe")
        if not os.path.exists(program_path):
            return "未找到LaunchGTAIV.exe程序，请检查目录是否正确。"
        os.startfile(program_path)
        return "Ciallo～(∠・ω< )⌒☆"


api = API()

webview.create_window(
    '罪恶都市次世代版启动器丨Powered by 鼠子Tomoriゞ', 
    'Assets/UI/index.html', 
    js_api=api,
    width=900,
    height=530
)
webview.start()
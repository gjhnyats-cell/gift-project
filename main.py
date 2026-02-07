from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label  # 必须导入一个插件
from kivy.utils import platform
import time

class OPaoApp(App):
    def build(self):
        # 1. 必须返回一个界面，否则会闪退
        # 这里我们显示一个全黑的背景，上面写一句话（或者留白）
        layout = Label(text="Loading your gift...", font_size='20sp')

        # 2. 延迟执行音量和播放逻辑，防止启动太快卡死
        if platform == 'android':
            try:
                from jnius import autoclass
                Context = autoclass('android.content.Context')
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                activity = PythonActivity.mActivity
                AudioManager = autoclass('android.media.AudioManager')
                audio_manager = activity.getSystemService(Context.AUDIO_SERVICE)

                # 尝试强制最大音量
                max_volume = audio_manager.getStreamMaxVolume(AudioManager.STREAM_MUSIC)
                audio_manager.setStreamVolume(AudioManager.STREAM_MUSIC, max_volume, 0)
            except Exception as e:
                print(f"Volume control failed: {e}")

        # 3. 播放音乐逻辑
        try:
            self.sound = SoundLoader.load('opao.mp3')
            if self.sound:
                self.sound.loop = True
                self.sound.play()
        except Exception as e:
            print(f"Audio play failed: {e}")

        return layout

if __name__ == '__main__':
    OPaoApp().run()
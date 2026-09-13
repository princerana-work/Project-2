import os
import urllib.parse
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.network.urlrequest import UrlRequest

# Set mobile preview window size ONLY when running on desktop
if 'ANDROID_ARGUMENT' not in os.environ:
    Window.size = (360, 640)


class MusicPlayer(BoxLayout):
    def __init__(self, **kwargs):
        super(MusicPlayer, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 15
        self.spacing = 10

        # Header Title
        self.add_widget(
            Label(
                text='[b]My Music Streamer[/b]',
                markup=True,
                font_size='22sp',
                size_hint_y=0.1
            )
        )

        # Search Bar Section
        search_box = BoxLayout(orientation='horizontal', size_hint_y=0.1, spacing=5)
        self.search_input = TextInput(
            hint_text='Enter song name...',
            multiline=False
        )
        search_btn = Button(
            text='Search',
            size_hint_x=0.3,
            background_color=(0.2, 0.6, 1, 1)
        )
        search_btn.bind(on_press=self.search_song)
        search_box.add_widget(self.search_input)
        search_box.add_widget(search_btn)
        self.add_widget(search_box)

        # Status & Track Information Label
        self.status = Label(
            text='Search for a song or play demo stream',
            size_hint_y=0.1,
            font_size='14sp'
        )
        self.add_widget(self.status)

        # Audio Playback Controls
        controls = BoxLayout(orientation='horizontal', size_hint_y=0.15, spacing=10)
        self.play_btn = Button(
            text='PLAY DEMO',
            background_color=(0.2, 0.8, 0.4, 1)
        )
        self.play_btn.bind(on_press=self.play_demo)

        self.stop_btn = Button(
            text='STOP',
            background_color=(0.9, 0.2, 0.2, 1)
        )
        self.stop_btn.bind(on_press=self.stop_audio)

        controls.add_widget(self.play_btn)
        controls.add_widget(self.stop_btn)
        self.add_widget(controls)

        self.sound = None
        # Educational MP3 Stream URL
        self.current_stream_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"

    def search_song(self, instance):
        query = self.search_input.text.strip()
        if not query:
            self.status.text = "Please enter a song name!"
            return

        self.status.text = f"Searching for: {query}..."

        # JioSaavn API query URL encoding
        encoded_query = urllib.parse.quote(query)
        api_url = f"https://saavn.dev/api/search/songs?query={encoded_query}&limit=1"

        UrlRequest(
            api_url,
            on_success=self.on_search_success,
            on_failure=self.on_search_error,
            on_error=self.on_search_error
        )

    def on_search_success(self, request, result):
        try:
            songs = result.get('data', {}).get('results', [])
            if songs:
                song = songs[0]
                song_name = song.get('name', 'Unknown Song')
                download_urls = song.get('downloadUrl', [])
                if download_urls:
                    # Select the highest quality audio stream available
                    self.current_stream_url = download_urls[-1].get('url')
                    self.status.text = f"Found: {song_name}\nReady to play!"
                else:
                    self.status.text = "Stream URL not found."
            else:
                self.status.text = "No song found."
        except Exception:
            self.status.text = "Error parsing response."

    def on_search_error(self, request, error):
        self.status.text = "Network Error! Please check your internet connection."

    def play_demo(self, instance):
        if self.sound:
            try:
                self.sound.stop()
            except Exception:
                pass

        if not self.current_stream_url:
            self.status.text = "No audio URL available to play."
            return

        self.status.text = "Buffering audio stream..."

        try:
            self.sound = SoundLoader.load(self.current_stream_url)
            if self.sound:
                self.sound.play()
                self.status.text = "Now Playing..."
            else:
                self.status.text = "Failed to load audio stream."
        except Exception as e:
            self.status.text = f"Playback Error: {str(e)}"

    def stop_audio(self, instance):
        if self.sound:
            try:
                self.sound.stop()
                self.status.text = "Audio Stopped."
            except Exception:
                pass


class MainApp(App):
    def build(self):
        return MusicPlayer()


if __name__ == '__main__':
    MainApp().run()

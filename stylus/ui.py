

class Window:
	def __init__(self, content: str, width: int=0, height: int=0):
		self.content = content
		self.width = width
		self.height = height

	def print_window(self) -> None:
		if self.width == 0 and self.height == 0:
			lines = []

			for line in self.content.split('\n'):
				lines.append(line)

			window_ui = f'┌─{"─" * max([len(line) for line in lines])}─┐\n'

			for line in lines:
				spaces = " " * (len(f'┌─{"─" * max([len(line) for line in lines])}─┐\n') - len(f'│ {line} │\n'))
				window_ui += f'│ {line} {spaces}│\n'
			
			window_ui += f'└─{"─" * max([len(line) for line in lines])}─┘'
		elif self.width > 0 and self.height > 0:
			lines = []
			window_ui = f'┌─{"─" * (self.height - 4)}─┐\n'

			for line in self.content.split('\n'):
				lines.append(line)

			for line in lines:
				spaces = " " * (len(f'┌─{"─" * (self.height - 4)}─┐\n') - len(f'│ {line} │\n'))
				window_ui += f'│ {line} {spaces}│\n'

			window_ui += f'└─{"─" * (self.height - 4)}─┘\n'

		print(window_ui)

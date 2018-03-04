from state import  Level1State, MenuState, OptionState

class Manager():

	def __init__(self):
		self.currentState = 0
		
		self.states = [
			MenuState(self),
			OptionState(self),
			Level1State(self)
		]

	def setState(self, state):
		self.currentState = state

	def update(self):
		self.states[self.currentState].update()

	def draw(self, display):
		self.states[self.currentState].draw(display)

	def keyPressed(self, key):
		self.states[self.currentState].keyPressed(key)

	def keyReleased(self, key):
		self.states[self.currentState].keyReleased(key)

import flet as ft

# Adding second card. Now one of the cards will not be on top of stack when being dragged
# move_on_top function to move the card on top on_pan_start event

SLOT_WIDTH = 70
SLOT_HEIGHT = 100


class Slot(ft.Container):
    def __init__(self, top, left):
        super().__init__()
        self.pile = []
        self.width = SLOT_WIDTH
        self.height = SLOT_HEIGHT
        self.left = left
        self.top = top
        self.border = ft.Border.all(1)


CARD_WIDTH = 70
CARD_HEIGHT = 100
DROP_PROXIMITY = 20


class Card(ft.GestureDetector):
    def __init__(self, solitaire, color):
        super().__init__()

        self.slot = None
        self.solitaire = solitaire
        self.color = color

        self.mouse_cursor = ft.MouseCursor.MOVE
        self.drag_interval = 5

        self.on_pan_start = self.start_drag
        self.on_pan_update = self.drag
        self.on_pan_end = self.drop

        self.left = None
        self.top = None

        self.content = ft.Container(
            bgcolor=self.color,
            width=CARD_WIDTH,
            height=CARD_HEIGHT,
        )

    def move_on_top(self):
        """Moves draggable card to the top of the stack"""
        self.solitaire.controls.remove(self)
        self.solitaire.controls.append(self)
        self.solitaire.update()

    def bounce_back(self):
        """Returns card to its original position"""
        self.top = self.slot.top
        self.left = self.slot.left
        self.update()

    def place(self, slot):
        """Place card to the slot"""
        self.top = slot.top
        self.left = slot.left
        self.slot = slot

    def start_drag(self, e: ft.DragStartEvent):
        self.move_on_top()
        self.update()

    def drag(self, e: ft.DragUpdateEvent):
        self.top = max(0, self.top + e.local_delta.y)
        self.left = max(0, self.left + e.local_delta.x)
        self.update()

    def drop(self, e: ft.DragEndEvent):
        for slot in self.solitaire.slots:
            if (
                abs(self.top - slot.top) < DROP_PROXIMITY
                and abs(self.left - slot.left) < DROP_PROXIMITY
            ):
                self.place(slot)
                self.update()
                return

        self.bounce_back()
        self.update()


SOLITAIRE_WIDTH = 1000
SOLITAIRE_HEIGHT = 500


class Solitaire(ft.Stack):
    def __init__(self):
        super().__init__()

        self.controls = []
        self.slots = []
        self.cards = []

        self.width = SOLITAIRE_WIDTH
        self.height = SOLITAIRE_HEIGHT

    def did_mount(self):
        self.create_card_deck()
        self.create_slots()
        self.deal_cards()

    def create_card_deck(self):
        card1 = Card(self, color=ft.Colors.GREEN)
        card2 = Card(self, color=ft.Colors.YELLOW)
        self.cards = [card1, card2]

    def create_slots(self):
        self.slots.append(Slot(top=0, left=0))
        self.slots.append(Slot(top=0, left=200))
        self.slots.append(Slot(top=0, left=300))

        self.controls.extend(self.slots)
        self.update()

    def deal_cards(self):
        self.controls.extend(self.cards)

        for card in self.cards:
            card.place(self.slots[0])

        self.update()


def main(page: ft.Page):
    solitaire = Solitaire()
    page.add(solitaire)


ft.run(main)
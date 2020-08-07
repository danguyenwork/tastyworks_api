from tastyworks.dxfeed.mapped_item import MappedItem


class Candle(MappedItem):
    DXFEED_TEXT = 'Candle'

    def __init__(self, data=None):
        super().__init__(data=data)

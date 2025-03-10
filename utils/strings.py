
class ExpressionHandler:

    MAPPING = {
        "bình_thường": "Ngồi yên",
        "cảm_ơn": "Cảm ơn",
        "xin_chào": "Xin chào",
        "yêu": "Yêu",
        "không": "Không"
    }

    def __init__(self):
        # Save the current message and the time received the current message
        self.current_message = ""

    def receive(self, message):
        self.current_message = message

    def get_message(self):
        return ExpressionHandler.MAPPING[self.current_message]

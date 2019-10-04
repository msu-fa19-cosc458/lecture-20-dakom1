import unittest
import functions

class ChatBotResponseTest(unittest.TestCase):
    def test_not_command(self):
        response = functions.get_chatbot_response("!! divide 12 4")
        print(response)
        self.assertEquals(response, 3)

if __name__ == '__main__':
    unittest.main()
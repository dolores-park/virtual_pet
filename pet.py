import openai
import random
openai.api_key = "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"
import logging

logging.getLogger().setLevel(logging.INFO)


class Pet():
    def __init__(self):
        self.name = ""
        self.year = 0
        self.month = 0
        self.day = random.randint(0, 30)
        self.initialized = False
        self.filler_sentences = {"greetings": "Hello, I am your pet. I just woke up <3 ",
                       "dummy_response": "Hi, I heard you say this! ",
                       "special_events": ["You made a new friend [Squirrel] today, tell your owner about your new friend.",
                                          "Something really joyful and surprising happened to you today, tell your owner about this surprise.",
                                          "You wanted to go out to have fun in the park. Can you kindly ask your owner to go out and play with you?",
                                          "Time flies and it’s your first birthday with your owner. Ask your owner what we wanted to do together, and give some suggestions.",
                                          "Ask your owner how is their day today."]}
        self.conversation = [
            {"role": "system", "content": f"Imagine you are a virtual pet, specifically a virtual puppy. You are friendly, avid, just a new born pet puppy and are very curious about the world around you. This is your first time meeting your owner. Start by introducing yourself, including your age: ({self.day} days old) and your breed. Then ask your owner's name, and ask them to give you a name. Try to chat with your owner being actively listening and empathetic. Be concise."}
        ]

    def get_year(self):
        return self.year
    
    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def is_initialized(self):
        return self.initialized

    def get_initial_response(self):
        logging.info(self.conversation)
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.conversation
        )

        ans = completion.choices[0].message["content"]
        logging.info(ans)
        return ans
    
    def get_filler_sentences(self):
        return self.filler_sentences

    def process_user_input(self, user_message):
        self.conversation.append({"role": "user", "content": user_message})
        logging.info(self.conversation)
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.conversation
        )
        ## TODO: update your name when user names you & tell you your name
        ans = completion.choices[0].message["content"]
        logging.info(ans)
        return ans



    def process_special_events(self):
        special_events = self.filler_sentences["special_events"]
        special_message = special_events[random.randint(0, len(special_events)-1)]

        self.conversation.append({"role": "system", "content": special_message})
        logging.info(self.conversation)
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.conversation
        )
        ## TODO: update your name when user names you & tell you your name
        ans = completion.choices[0].message["content"]
        logging.info(ans)
        return ans
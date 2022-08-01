# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import actions.modules.WeatherSiteCrawler.sitecrawler as sc


class ActionGetWeather(Action):

    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        for blob in tracker.latest_message['entities']:
            if blob['entity'] == 'city':
                city_name = blob['value']
                city_id = sc.choose_city(city_name, sc.city_dict)
                dispatcher.utter_message(sc.produce_output(sc.return_weather(city_id)))
            else:
                dispatcher.utter_message("Sorry. I don't recognize that city. Can you try again? ")
                
        
        return []


#    # data to be sent to the weather crawl api
#         
#         data = {'name' : city_name}
#         post_r = requests.post(url = url, data = data)

#         #exracting response text
#         result = post_r.text
#         dispatcher.utter_message(result)
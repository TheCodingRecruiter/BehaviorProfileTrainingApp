import json
from pprint import pprint
from random import choice

with open("data.json") as f:
    content = json.loads(f.read())
    winner = choice(content)

# pprint(winner)


name = winner["Name"]
amplifying_gestures = winner["Amplifying Gestures"]
body_region = winner["Body Region"]
confirming_gestures = winner["Confirming Gestures"]
conflicting_behaviors = winner["Conflicting Behaviors"]
cultural_prevalence = winner["Cultural Prevalence"]
deception_rating = winner["Deception Rating"]
deception_timeframe = winner["Deception Timeframe"]
gesture_type = winner["Gesture Type"]
microphysiological = winner["Microphysiological "]
reference = winner["Reference"]
sexual_propensity = winner["Sexual Propensity"]
gesture_symbol = winner["Symbol"]
variable_factors = winner["Variable Factors"]


todays_training = (
    f"Today the random gesture we will cover is '{name}'."
    f" The symbol we use to notate {name} is {gesture_symbol}."
    f" {name} can be identified by observing the/an {body_region}."
    f" {sexual_propensity} are more prone to this gesture."
    f" {confirming_gestures} are common gestures that we see in association with {name} and indicate low deception or concealment of emotions."
    f" If you see {conflicting_behaviors}, then it is likely that deception is present and the deception rating of {deception_rating} should be added to any other conflicting behavior observed.  If the total of all these conflicting behaviors equates to 11 or more there is high likelihood that decpeption is present. "
)

print(todays_training)





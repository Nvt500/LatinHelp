from dataclasses import dataclass
from typing import Union
import json
import random

@dataclass
class Verb:
    
    conj: str
    first: str
    second: str
    third: str
    fourth: str
    
    def get_form(self, person: Union[str, int], number: Union[str, int], tense: Union[str, int], voice: Union[str, int]) -> [str, list]:
        
        try:
            if isinstance(person, int):
                person = VerbHelper.PERSON[person]
            if isinstance(number, int):
                number = VerbHelper.NUMBER[number]
            if isinstance(tense, int):
                tense = VerbHelper.TENSE[tense]
            if isinstance(voice, int):
                voice = VerbHelper.VOICE[voice]
            
        except ValueError:
            raise Exception(NotImplemented)
        
        comp = [person, number, tense, voice]

        word = VerbHelper.COMP.get(str(self.conj)).get(voice).get(tense).get(number).get(person)
        
        new_word = ""
        skip = False
        for i, char in enumerate(word):
            if char == "/":
                skip = False
                continue
            if skip:
                continue
            if char == "1":
                new_word += self.first
                continue
            if char == "2":
                new_word += self.second
                continue
            if char == "3":
                new_word += self.third
                continue
            if char == "4":
                new_word += self.fourth
                continue
            if char == "-":
                new_word = new_word[:0 - len(word[i+1:word.find("/")])]
                skip = True
                continue
            new_word += char
        
        word = new_word   

        return word, comp
        
        
    def get_random_form(self) -> str:
        
        return self.get_form(
            random.choice(VerbHelper.PERSON),
            random.choice(VerbHelper.NUMBER),
            random.choice(VerbHelper.TENSE),
            random.choice(VerbHelper.VOICE)
            )
    
    
    def __repr__(self) -> str:
        
        return f"conjugation: {self.conj} - {self.first}, {self.second}, {self.third}, {self.fourth}"
    
    
    def __iter__(self) -> iter:
        
        return iter([self.first, self.second, self.third, self.fourth])
    
    
    def prints(self) -> None:
        
        print(self)
        
    
    
class VerbHelper:
    
    COMP = json.loads(open("_code/verb.json", "r").read())
    
    FIRST_PERSON = "first"
    SECOND_PERSON = "second"
    THIRD_PERSON = "third"
    
    PERSON = ("first", "second", "third")
    
    SINGULAR = "singular"
    PLURAL = "plural"
    
    NUMBER = ("singular", "plural")
    
    PRESENT = "present"
    IMPERFECT = "imperfect"
    FUTURE = "future"
    PERFECT = "perfect"
    PLU_PERFECT = "plu perfect"
    FUTURE_PERFECT = "future perfect"
    
    TENSE = ("present", "imperfect", "future", "perfect", "plu perfect", "future perfect")
    
    ACTIVE = "active"
    PASSIVE = "passive"
    
    VOICE = ("active", "passive")
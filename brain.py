import random
list1 = []
list2 = []


class MatchBrain:

    def __init__(self,name_list,match_list) -> None:
        self.name_dict: dict = name_list
        self.match_list: list = match_list
        self.exceptions_dict = {key:value for (key,value) in self.name_dict.items() if value is not None}
        self.all_matches = []

    
    def match_names(self):
        for name in self.name_dict.items():
            _match = random.choice(self.match_list)
            if self.check_exception(name,_match): #returns true if the names can be matched
                self.match_list.remove(_match)
                self.all_matches.append((name,_match))

    def check_exception(self,name,match):
        pass


from itertools import count
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer, TagIdNameSerializer, InterestTagIdNameSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Tag, InterestTag


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class TagList(ListCreateAPIView):
    # Retrieve, update, or delete a tag suggestion
    queryset = Tag.objects.all().order_by('id')
    serializer_class = TagIdNameSerializer

    def get_queryset(self):
        queryset = Tag.objects.all().order_by('id')
        answerNames = []
        for e in queryset:
            answerNames.append(e.name)
        topTwoAttrb = personalityQuizAlgorithm(answerNames)
        val = 1000 #temporary
        for let in topTwoAttrb:
            if (not queryset.filter(name = let)):
                Tag.objects.create(id = val, name = let)
                val += 1
        return queryset

class InterestTagList(ListCreateAPIView):
    # Retrieve, update, or delete a tag suggestion
    queryset = InterestTag.objects.all().order_by('id')
    serializer_class = InterestTagIdNameSerializer

    def get_queryset(self):
        queryset = InterestTag.objects.all().order_by('id')
        answerNames = []
        for e in queryset:
            answerNames.append(e.name)
        topThreeAttrb = interestQuizAlgorithm(answerNames)
        val = queryset.count() + 1000 #temporary
        for let in topThreeAttrb:
            if (not queryset.filter(name = let)):
                InterestTag.objects.create(id = val, name = let)
                val += 1
        return queryset


def personalityQuizAlgorithm(personality_arr):
    """
    Stability: S
    Conscientious: C
    Openness: O
    Extraversion: E
    Agreeableness: A
    """
    person_dict = {'S': 0, 'C': 0, 'O': 0, 'E': 0, 'A': 0}
    Item_txt_dict = {"Prepared": "C", "Controlled": "S", "Reflective": "O", "Talkative": "E", "Tranquil": "S", "Artistic": "O",
                     "Smart": "O", "Loving": "A", "Organized": "C", "Kindhearted": "A", "Gifted": "O", "Sensitive": "A", "Comfortable": "S",
                     "Responsible": "C", "Orderly": "C", "Complex": "O", "Laid-back": "S", "Caring": "A", "Tidy": "C", "Dutiful": "C",
                     "Excitable": "E", "Harmonious": "A", "Assertive": "E", "Pleased": "S", "Sympathetic": "A",
                     "Passionate": "O", "Cautious": "C", "Gregarious": "E", "Helpful": "A", "Happy": "E", "Focused": "C", "Softhearted": "A",
                     "Competent": "C", "Resilient": "S", "Captivating": "E", "Funny": "E", "Unconventional": "O", "Successful": "C", "Calm": "S",
                     "Thick-skinned": "S", "Adventurous": "O", "Even-keeled": "S", "Trusting": "A", "Cheerful": "E",
                     "Friendly": "E", "Charitable": "A", "Deliberate": "C", "Unorthodox": "O", "Communal": "A", "Fun": "E", "Intellectual": "O",
                     "Relaxed": "S", "Dominant": "E", "Conscientious": "C", "Imaginative": "O", "Approachable": "E", "Quick-witted": "O"
                     }
    """
    Agreeableness: compassionate
    Conscientiousness: Conscientious
    Emotion Stability: Composed
    Openness: Adventurous
    Extraversion: Enthusiastic
    """
    counter = 0
    for i in personality_arr:
        try:
            if counter == 0 and i == "Controlled":
                person_dict[Item_txt_dict[i]] += 0
            elif counter == 1 and i == "Reflective":
                person_dict[Item_txt_dict[i]] += 0
            elif counter == 1 and i == "Talkative":
                person_dict[Item_txt_dict[i]] += 2
            elif counter == 3 and i == "Smart":
                person_dict[Item_txt_dict[i]] += 2
            elif counter == 4 and i == "Loving":
                person_dict[Item_txt_dict[i]] += 0
            elif counter == 6 and i == "Sensitive":
                person_dict[Item_txt_dict[i]] += 0
            elif counter == 7 and i == "Comfortable":
                person_dict[Item_txt_dict[i]] += 0
            elif counter == 9 and i == "Reflective":
                person_dict[Item_txt_dict[i]] += 2
            elif counter == 11 and i == "Excitable":
                person_dict[Item_txt_dict[i]] += 3
            elif counter == 16 and i == "Happy":
                person_dict[Item_txt_dict[i]] += 3
            elif counter == 17 and i == "Laid-back":
                person_dict[Item_txt_dict[i]] += 2
            elif counter == 22 and i == "Unconventional":
                person_dict[Item_txt_dict[i]] += 0
            elif counter == 23 and i == "Successful":
                person_dict[Item_txt_dict[i]] += 0
            elif counter == 23 and i == "Resilient":
                person_dict[Item_txt_dict[i]] += 2
            elif counter == 24 and i == "Softhearted":
                person_dict[Item_txt_dict[i]] += 0
            elif counter == 25 and i == "Adventurous":
                person_dict[Item_txt_dict[i]] += 2
            elif counter == 27 and i == "Even-keeled":
                person_dict[Item_txt_dict[i]] += 0
            elif counter == 30 and i == "Deliberate":
                person_dict[Item_txt_dict[i]] += 0
            elif counter == 31 and i == "Unorthodox":
                person_dict[Item_txt_dict[i]] += 0
            elif counter == 34 and i == "Charitable":
                person_dict[Item_txt_dict[i]] += 2
            elif counter == 35 and i == "Gifted":
                person_dict[Item_txt_dict[i]] += 0
            elif counter == 35 and i == "Relaxed":
                person_dict[Item_txt_dict[i]] += 2.5
            elif counter == 38 and i == "Imaginative":
                person_dict[Item_txt_dict[i]] += 0
            elif counter == 7 and i == "Quick-witted":
                person_dict[Item_txt_dict[i]] += 2
            else:
                person_dict[Item_txt_dict[i]] += 1
            counter += 1
        except Exception as e:
            print(e)

    person_dict = dict(sorted(person_dict.items(), key=lambda item: item[1], reverse = True))
    return list(person_dict.keys())[0:3]

def interestQuizAlgorithm(interest_arr):
    interest_dict = {'R':0, 'S':0, 'I':0, 'E':0, 'C':0, 'A':0}
    Interest_item_txt_dict = {"Persuading others": "E", "Writing stories": "I", 
                        "Preparing legal documents":"C", "Building appliances":"R",
                        "Providing diet advice":"S", "Fitting pipes":"R",
                        "Negotiating contacts":"E", "Assisting the elderly":"S",
                        "Analyzing people":"I", "Creating graphs":"C",
                        "Decorating houses":"A",
                        "Preparing data":"C", "Judging legal cases":"I",
                        "Programming code":"F", "Playing an instrument":"A",
                        "Performing plays":"A", "Installing equipment":"R",
                        "Putting up drywall":"R", "Appointing department heads":"E",
                        "Providing career guidance":"S", "Programming code":"C",
                        "Treating diseases":"I", "Operating heavy machinery":"R",
                        "Starting a business":"E",
                        "Serving customers":"S",
                        "Buying stocks":"E",
                        "Writing show scripts":"A", "Organizing shelves":"R",
                        "Selling stocks":"E", "Creating music":"A",
                        "Solving problems":"I",
                        "Rehabilitating others":"S", "Managing a store":"E",
                        "Managing a financial portfolio":"E", "Babysitting children":"S",
                        "Investigating stories":"C", "Maintaining shipping records":"I",
                        "Organizing inventory":"F", "Creating art":"A",
                        "Inventing products":"I", "Singing":"A",
                        "Overseeing budget":"E", "Researching animals":"I",
                        "Dancing":"A", "Teaching students":"I",
                        "Driving trucks":"R",
                        "Teaching fitness classes":"S",
                        "Volunteering at a shelter":"S", "Filming movies":"A",
                        "Assembling machinery":"R",
                        "Studying planets":"I", 
                        "Teaching high-schoolers":"S",
                        "Teaching children":"S",
                        "Investigating problems":"I", "Flying planes":"R",
                        "Treating psychological problems":"S",
                        "Repairing equipment":"R", "Managing a large department":"E",
                        "Maintaining office supplies":"C",
                        "Accounting":"C", 
                        "Calculating employee wages":"C",
                        "Welding":"R", "Scheduling appointments":"C",
                        "Operating a shop":"E", "Developing a spreadsheet":"C",
                        "Proofreading documents":"F",
                        "Composing music":"A",
                        "Maintaining shipping records":"C",
                        "Discovering medical solutions":"I", "Filming movies":"A"}
    counter = 0
    try:
        for j in interest_arr: 
            if counter == 0 and j == "Writing stories":
                interest_dict[Interest_item_txt_dict[j]] += 2
            elif counter == 1 and j == "Preparing legal documents":
                interest_dict[Interest_item_txt_dict[j]] += 2
            elif counter == 4 and j == "Analyzing people":
                interest_dict[Interest_item_txt_dict[j]] += 2
            elif counter == 6 and j == "Judging legal cases":
                interest_dict[Interest_item_txt_dict[j]] += 3
            elif counter == 6 and j == "Preparing data":
                interest_dict[Interest_item_txt_dict[j]] += 0
            elif counter == 12 and j == "Starting a business":
                interest_dict[Interest_item_txt_dict[j]] += 2
            elif counter == 14 and j == "Treating diseases":
                interest_dict[Interest_item_txt_dict[j]] += 2
            elif counter == 20 and j == "Investigating stories":
                interest_dict[Interest_item_txt_dict[j]] += 2
            elif counter == 21 and j == "Organizing inventory":
                interest_dict[Interest_item_txt_dict[j]] += 2
            elif counter == 23 and j == "Overseeing budgets":
                interest_dict[Interest_item_txt_dict[j]] += 2
            elif counter == 26 and j == "Preparing legal documents":
                interest_dict[Interest_item_txt_dict[j]] += 2
            elif counter == 29 and j == "Studying planets":
                interest_dict[Interest_item_txt_dict[j]] += 0
            elif counter == 34 and j == "Managing a large department":
                interest_dict[Interest_item_txt_dict[j]] += 2
            elif counter == 35 and j == "Maintaining office supplies":
                interest_dict[Interest_item_txt_dict[j]] += 3
            elif counter == 39 and j == "Developing a spreadsheet":
                interest_dict[Interest_item_txt_dict[j]] += 2
            elif counter == 40 and j == "Analyzing people":
                interest_dict[Interest_item_txt_dict[j]] += 0
            elif counter == 41 and j == "Proofreading documents":
                interest_dict[Interest_item_txt_dict[j]] += 2
            elif counter == 42 and j == "Buying stocks":
                interest_dict[Interest_item_txt_dict[j]] += 2
            elif counter == 43 and j == "Appointing department heads":
                interest_dict[Interest_item_txt_dict[j]] += 2
            elif counter == 44 and j == "Discovering medical solutions":
                interest_dict[Interest_item_txt_dict[j]] += 3    
            else:
                interest_dict[Interest_item_txt_dict[j]] += 1
            counter = counter + 1
    except Exception as e:
        print(e)

    interest_dict = dict(sorted(interest_dict.items(), key=lambda item: item[1], reverse = True))
    print(interest_dict)
    return list(interest_dict.keys())[0:3]
RELATIONS = {
    '/r/RelatedTo': {
        'Description': 'The most general relation. There is some positive relationship between A and B, but ConceptNet can\'t determine what that relationship is based on the data. This was called "ConceptuallyRelatedTo" in ConceptNet 2 through 4. Symmetric.',
        'Examples': 'learn -> erudition'
    },
    '/r/FormOf': {
        'Description': 'A is an inflected form of B; B is the root word of A.',
        'Examples': 'slept -> sleep'
    },
    '/r/IsA': {
        'Description': 'A is a subtype or a specific instance of B; every A is a B. This can include specific instances; the distinction between subtypes and instances is often blurry in language. This is the *hyponym* relation in WordNet.',
        'Examples': 'car -> vehicle; Chicago -> city'
    },
    '/r/PartOf': {
        'Description': 'A is a part of B. This is the *part meronym* relation in WordNet.',
        'Examples': 'gearshift -> car'
    },
    '/r/HasA': {
        'Description': 'B belongs to A, either as an inherent part or due to a social construct of possession. HasA is often the reverse of PartOf.',
        'Examples': 'bird -> wing; pen -> ink'
    },
    '/r/UsedFor': {
        'Description': 'A is used for B; the purpose of A is B.',
        'Examples': 'bridge -> cross water'
    },
    '/r/CapableOf': {
        'Description': 'Something that A can typically do is B.',
        'Examples': 'knife -> cut'
    },
    '/r/AtLocation': {
        'Description': 'A is a typical location for B, or A is the inherent location of B. Some instances of this would be considered meronyms in WordNet.',
        'Examples': 'butter -> refrigerator; Boston -> Massachusetts'
    },
    '/r/Causes': {
        'Description': 'A and B are events, and it is typical for A to cause B.',
        'Examples': 'exercise -> sweat'
    },
    '/r/HasSubevent': {
        'Description': 'A and B are events, and B happens as a subevent of A.',
        'Examples': 'eating -> chewing'
    },
    '/r/HasFirstSubevent': {
        'Description': 'A is an event that begins with subevent B.',
        'Examples': 'sleep -> close eyes'
    },
    '/r/HasLastSubevent': {
        'Description': 'A is an event that concludes with subevent B.',
        'Examples': 'cook -> clean up kitchen'
    },
    '/r/HasPrerequisite': {
        'Description': 'In order for A to happen, B needs to happen; B is a dependency of A.',
        'Examples': 'dream -> sleep'
    },
    '/r/HasProperty': {
        'Description': 'A has B as a property; A can be described as B.',
        'Examples': 'ice -> cold'
    },
    '/r/MotivatedByGoal': {
        'Description': 'Someone does A because they want result B; A is a step toward accomplishing the goal B.',
        'Examples': 'compete -> win'
    },
    '/r/Desires': {
        'Description': 'A is a conscious entity that typically wants B. Many assertions of this type use the appropriate language\'s word for "person" as A.',
        'Examples': 'person -> love'
    },
    '/r/CreatedBy': {
        'Description': 'B is a process or agent that creates A.',
        'Examples': 'cake -> bake'
    },
    '/r/Synonym': {
        'Description': 'A and B have very similar meanings. They may be translations of each other in different languages. This is the *synonym* relation in WordNet as well. Symmetric.',
        'Examples': 'sunlight -> sunshine'
    },
    '/r/Antonym': {
        'Description': 'A and B are opposites in some relevant way, such as being opposite ends of a scale, or fundamentally similar things with a key difference between them. This is the *antonym* relation in WordNet as well. Symmetric.',
        'Examples': 'black -> white; hot -> cold'
    },
    '/r/DistinctFrom': {
        'Description': 'A and B are distinct member of a set; something that is A is not B. Symmetric.',
        'Examples': 'red -> blue; August -> September'
    },
    '/r/DerivedFrom': {
        'Description': 'A is a word or phrase that appears within B and contributes to B\'s meaning.',
        'Examples': 'pocketbook -> book'
    },
    '/r/DefinedAs': {
        'Description': 'A and B overlap considerably in meaning, and B is a more explanatory version of A.',
        'Examples': 'peace -> absence of war'
    },
    '/r/HasContext': {
        'Description': 'A is a word used in the context of B, which could be a topic area, technical field, or regional dialect.',
        'Examples': 'astern -> ship; arvo -> Australia'
    },
    '/r/SimilarTo': {
        'Description': 'A is similar to B. Symmetric.',
        'Examples': 'mixer -> food processor'
    },
    '/r/EtymologicallyRelatedTo': {
        'Description': 'A and B have a common origin. Symmetric.',
        'Examples': 'folkmusiikki -> folk music'
    },
    '/r/CausesDesire': {
        'Description': 'A makes someone want B.',
        'Examples': 'having no food -> go to a store'
    },
    '/r/MadeOf': {
        'Description': 'A is made of B.',
        'Examples': 'bottle -> plastic'
    },
    '/r/ReceivesAction': {
        'Description': 'B can be done to A.',
        'Examples': 'button -> push'
    }
}

RELATIONS_TABLE = """\
| Relation URI                 | Description                                                                                                                                                                                                                               | Examples                                                                           |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| /r/RelatedTo                 | The most general relation. There is some positive relationship between A and B, but ConceptNet can't determine what that relationship is based on the data. This was called "ConceptuallyRelatedTo" in ConceptNet 2 through 4. Symmetric. | learn ↔ erudition                                                                  |
| /r/FormOf                    | A is an inflected form of B; B is the root word of A.                                                                                                                                                                                     | slept → sleep                                                                      |
| /r/IsA                       | A is a subtype or a specific instance of B; every A is a B. This can include specific instances; the distinction between subtypes and instances is often blurry in language. This is the *hyponym* relation in WordNet.                   | car → vehicle; Chicago → city                                                      |
| /r/PartOf                    | A is a part of B. This is the *part meronym* relation in WordNet.                                                                                                                                                                         | gearshift → car                                                                    |
| /r/HasA                      | B belongs to A, either as an inherent part or due to a social construct of possession. HasA is often the reverse of PartOf.                                                                                                               | bird → wing; pen → ink                                                             |
| /r/UsedFor                   | A is used for B; the purpose of A is B.                                                                                                                                                                                                   | bridge → cross water                                                               |
| /r/CapableOf                 | Something that A can typically do is B.                                                                                                                                                                                                   | knife → cut                                                                        |
| /r/AtLocation                | A is a typical location for B, or A is the inherent location of B. Some instances of this would be considered meronyms in WordNet.                                                                                                        | butter → refrigerator; Boston → Massachusetts                                      |
| /r/Causes                    | A and B are events, and it is typical for A to cause B.                                                                                                                                                                                   | exercise → sweat                                                                   |
| /r/HasSubevent               | A and B are events, and B happens as a subevent of A.                                                                                                                                                                                     | eating → chewing                                                                   |
| /r/HasFirstSubevent          | A is an event that begins with subevent B.                                                                                                                                                                                                | sleep → close eyes                                                                 |
| /r/HasLastSubevent           | A is an event that concludes with subevent B.                                                                                                                                                                                             | cook → clean up kitchen                                                            |
| /r/HasPrerequisite           | In order for A to happen, B needs to happen; B is a dependency of A.                                                                                                                                                                      | dream → sleep                                                                      |
| /r/HasProperty               | A has B as a property; A can be described as B.                                                                                                                                                                                           | ice → cold                                                                         |
| /r/MotivatedByGoal           | Someone does A because they want result B; A is a step toward accomplishing the goal B.                                                                                                                                                   | compete → win                                                                      |
| /r/Desires                   | A is a conscious entity that typically wants B. Many assertions of this type use the appropriate language's word for "person" as A.                                                                                                       | person → love                                                                      |
| /r/CreatedBy                 | B is a process or agent that creates A.                                                                                                                                                                                                   | cake → bake                                                                        |
| /r/Synonym                   | A and B have very similar meanings. They may be translations of each other in different languages. This is the *synonym* relation in WordNet as well. Symmetric.                                                                          | sunlight ↔ sunshine                                                                |
| /r/Antonym                   | A and B are opposites in some relevant way, such as being opposite ends of a scale, or fundamentally similar things with a key difference between them. This is the *antonym* relation in WordNet as well. Symmetric.                     | black ↔ white; hot ↔ cold                                                          |
| /r/DistinctFrom              | A and B are distinct member of a set; something that is A is not B. Symmetric.                                                                                                                                                            | red ↔ blue; August ↔ September                                                     |
| /r/DerivedFrom               | A is a word or phrase that appears within B and contributes to B's meaning.                                                                                                                                                               | pocketbook → book                                                                  |
| /r/DefinedAs                 | A and B overlap considerably in meaning, and B is a more explanatory version of A.                                                                                                                                                        | peace → absence of war                                                             |
| /r/HasContext                | A is a word used in the context of B, which could be a topic area, technical field, or regional dialect.                                                                                                                                  | astern → ship; arvo → Australia                                                    |
| /r/SimilarTo                 | A is similar to B. Symmetric.                                                                                                                                                                                                             | mixer ↔ food processor                                                             |
| /r/EtymologicallyRelatedTo   | A and B have a common origin. Symmetric.                                                                                                                                                                                                  | folkmusiikki ↔ folk music                                                          |
| /r/CausesDesire              | A makes someone want B.                                                                                                                                                                                                                   | having no food → go to a store                                                     |
| /r/MadeOf                    | A is made of B.                                                                                                                                                                                                                           | bottle → plastic                                                                   |
| /r/ReceivesAction            | B can be done to A.                                                                                                                                                                                                                       | button → push                                                                      |
"""

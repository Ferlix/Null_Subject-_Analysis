from textpipeliner import NamedEntityFilterPipe
from textpipeliner import NamedEntityExtractorPipe
from textpipeliner import FindTokensPipe
from textpipeliner import SequencePipe
from textpipeliner import AggregatePipe
from textpipeliner import AnyPipe
from textpipeliner import *


def find_subjects(sen, list_verbs, Verbose = True):
    #print('list')
    #print(list_verbs)
    results = []

    pipes_structure = [  
                SequencePipe([
            #FindTokensPipe("VERB/nsubj/*"),
            FindTokensPipe("VERB/advcl/VERB/nsubj"),
            #FindTokensPipe("VERB/nsubj/*"),
            #NamedEntityFilterPipe(),
            #NamedEntityExtractorPipe()
            ]),
           # FindTokensPipe("VERB/aux"),
            FindTokensPipe("VERB/advcl/VERB"),
          #  FindTokensPipe("*/*/*/*/*/conj") ])

                     ]

    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        #print(str(i[1]))
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 1')
                    print(i)
                results.append(i)

    pipes_structure = [  
                    AggregatePipe([
                        FindTokensPipe("VERB/nsubj:pass/*"),
                        FindTokensPipe("VERB/nsubj/*"),
                        FindTokensPipe("VERB/advcl/NOUN/nsubj/*"),
                        
                        ]),
                FindTokensPipe("VERB/aux"),
                FindTokensPipe("VERB")
                         ]
    
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 2')
                    print(i)
                results.append(i)

    pipes_structure = [  
                SequencePipe([
            FindTokensPipe("VERB/nsubj/*"),
            NamedEntityFilterPipe(),
            NamedEntityExtractorPipe()
            ]),
            FindTokensPipe("*/*/*/*/*/conj"),
                     ]

    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 3')
                    print(i)
                results.append(i)

    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("VERB/nsubj:pass/*"),
            FindTokensPipe("VERB/nsubj/*"),
            FindTokensPipe("VERB/subj"),
            FindTokensPipe("VERB/advmod/NOUN")

            ]),
            FindTokensPipe("VERB"),
                     ]
    


    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 4')
                    print(i)
                results.append(i)
    

    pipes_structure_comp = [  
        AggregatePipe([
            FindTokensPipe("ADV/advcl/VERB/nsubj") ]),

            FindTokensPipe("ADV/advcl"),
                     ]

    engine = PipelineEngine(pipes_structure_comp, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 5')
                    print(i)
                results.append(i)

    pipes_structure = [  
                        AggregatePipe([
                    FindTokensPipe("AUX/nsubj/*"),
                    FindTokensPipe("AUX/nsubj:pass/*"),
                    ]),
                    FindTokensPipe("AUX/aux"),
                             ]



    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 6')
                    print(i)
                results.append(i)
   
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("NOUN"),
                    FindTokensPipe("AUX/nsubj/*"),
                    FindTokensPipe("AUX/advcl/VERB/nsubj")
            ]),
            FindTokensPipe("AUX"),
                     ]

    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 7')
                    print(i)
                results.append(i)
                

    
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("AUX"),
             FindTokensPipe("AUX/*/VERB/nsubj"),
            ]),
            FindTokensPipe("AUX/cop/VERB")
                     ]

    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 8')
                    print(i)
                results.append(i)
                
    pipes_structure = [  
                SequencePipe([
            FindTokensPipe("AUX/*/VERB/*/NOUN/*/NOUN/nsubj"),
            ]),
            FindTokensPipe("AUX/*/VERB/*/NOUN/*/NOUN/aux/AUX"),
             ]

    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 9')
                    print(i)
                results.append(i)
                
    pipes_structure = [  
        SequencePipe([
    FindTokensPipe("VERB/advcl/AUX/nsubj"),
    NamedEntityFilterPipe(),
    NamedEntityExtractorPipe()
    ]),
    FindTokensPipe("VERB/advcl/AUX/aux/AUX"),
    ]
        
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 10')
                    print(i)
                results.append(i)
                
    pipes_structure = [  
            FindTokensPipe("NOUN/nsubj/*"),
            FindTokensPipe("NOUN/aux"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 11')
                    print(i)
                results.append(i)
                
                
    pipes_structure = [  
            FindTokensPipe("*/**/AUX/nsubj/NOUN"),
            FindTokensPipe("VERB/advcl/AUX/conj/AUX/aux/AUX"),
                     ]

    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 12')
                    print(i)
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("PRON/nsubj/*"),
            FindTokensPipe("PRON/csubj:pass/*"),
            ]),
            FindTokensPipe("PRON/cop/*")
                     ]


    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 13')
                    print(i)
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("VERB/nsubj:pass/*"),

            ]),
            FindTokensPipe("VERB/aux:pass/AUX"),
                     ]

    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 14')
                    print(i)
                results.append(i)
               
            


    
    pipes_structure = [  
                        AggregatePipe([
                            FindTokensPipe("X/nsubj/*"),
                            FindTokensPipe("X/nsubj:pass/*"),
                            FindTokensPipe("NOUN/nsubj:pass/*"),
                            FindTokensPipe("NOUN/nsubj/*"),
                            FindTokensPipe("NOUN/csubj/*"),
                            FindTokensPipe("X/csubj/*"),
                            FindTokensPipe("NOUN/cop/VERB/nsubj"),
                            
                    ]),
                    AggregatePipe([
                    FindTokensPipe("X/cop/AUX"),
                     FindTokensPipe("X/cop/VERB"),
                    FindTokensPipe("NOUN/cop/*"),
                        
                             ])
        ]
    
    
        
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 15')
                    print(i)
                results.append(i)
                
    
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADJ/nsubj:pass/*"),
            FindTokensPipe("ADJ/nsubj/*"),
            FindTokensPipe("ADJ/conj/ADJ/csubj/*"),
            ]),
            FindTokensPipe("ADJ/cop/VERB"),
        
    ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 16')
                    print(i)
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADJ/advcl/VERB/nsubj"),
           # FindTokensPipe("VERB/nsubj"),
            #NamedEntityFilterPipe(),
            #NamedEntityExtractorPipe()
            ]),
            FindTokensPipe("ADJ/advcl/VERB")]
        
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 17')
                    print(i)
                results.append(i)
        
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("PROPN/**/PROPN"),

            ]),
            FindTokensPipe("PROPN/conj/VERB"),
    ]
    
            

    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 18')
                    print(i)
                results.append(i)
            
            
    pipes_structure = [  
                SequencePipe([
            FindTokensPipe("ADJ/nsubj/*"),
           # FindTokensPipe("VERB/nsubj"),
            #NamedEntityFilterPipe(),
            #NamedEntityExtractorPipe()
            ]),
            FindTokensPipe("ADJ/cop/AUX"),
                     ]

    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 19')
                    print(i)
                results.append(i)
                
    pipes_structure = [  
                SequencePipe([
            FindTokensPipe("*/**/*/conj/VERB/nsubj"),
           # FindTokensPipe("VERB/nsubj"),
            #NamedEntityFilterPipe(),
            #NamedEntityExtractorPipe()
            ]),
            FindTokensPipe("*/**/*/conj/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 20')
                    print(i)
                results.append(i)
                
    pipes_structure = [  
                SequencePipe([
            FindTokensPipe("PRON"),
           # FindTokensPipe("VERB/nsubj"),
            #NamedEntityFilterPipe(),
            #NamedEntityExtractorPipe()
            ]),
            FindTokensPipe("PRON/acl:relcl/VERB"),
        
                     ]

    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 21')
                    print(i)
                results.append(i)
                
    pipes_structure = [  
                SequencePipe([
            FindTokensPipe("DET"),
           # FindTokensPipe("VERB/nsubj"),
            #NamedEntityFilterPipe(),
            #NamedEntityExtractorPipe()
            ]),
            FindTokensPipe("DET/cop/AUX"),
        
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 22')
                    print(i)
                results.append(i)
                



    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("PRON/nsubj/*"),
                            ]),
            FindTokensPipe("PRON/aux/AUX"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 24')
                    print(i)
                results.append(i)
                

                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("VERB/obj/NOUN/conj/NOUN/acl:relcl/VERB/nsubj/*")

            ]),
            FindTokensPipe("VERB/obj/NOUN/conj/NOUN/acl:relcl/VERB"),
    ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 25')
                    print(i)
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("AUX/nsubj:pass/*"),


            ]),
            FindTokensPipe("AUX/aux:pass/AUX"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 26')
                    print(i)
                results.append(i)
                
    pipes_structure = [  
            AggregatePipe([
        FindTokensPipe("ADJ/nsubj/*"),
        FindTokensPipe("ADJ/csubj/*"),
        FindTokensPipe("ADJ/nsubj:pass/*"),
        ]),
        FindTokensPipe("ADJ/aux/AUX"),
                 ]
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 27')
                    print(i)
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("VERB/nsubj/*"),
            FindTokensPipe("VERB/nsubj:pass/*"),
            ]),
            FindTokensPipe("VERB/cop/AUX"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 28')
                    print(i)
                results.append(i)
                


                
    pipes_structure = [  
                        AggregatePipe([
                    FindTokensPipe("VERB/ccomp/AUX/nsubj/*"),
                    FindTokensPipe("VERB/ccomp/AUX/nsubj:pass/*"),
                    ]),
                    FindTokensPipe("VERB/ccomp/AUX/aux/*"),
                             ]

    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 29')
                    print(i)   
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN"),
            ]),
            FindTokensPipe("NOUN/amod/ADJ/cop/*")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 30')
                    print(i)   
                results.append(i)
                
    pipes_structure = [  
            AggregatePipe([
        FindTokensPipe("ADV/nsubj/*"),
        FindTokensPipe("ADV/nsubj:pass/*"),

        ]),
        FindTokensPipe("ADV/cop/VERB"),
                 ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 31')
                    print(i)   
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADJ/nsubj/*"),
            FindTokensPipe("ADJ/nsubj:pass/*"),

            ]),
            FindTokensPipe("ADJ/aux:pass/*"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 32')
                    print(i)   
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("PROPN"),
            FindTokensPipe("PROPN/nsubj/*"),

            ]),
        AggregatePipe([
            FindTokensPipe("PROPN/cop/VERB"),
            FindTokensPipe("PROPN/cop/AUX"),
            FindTokensPipe("PROPN/aux/*"),
        ])
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 33')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                SequencePipe([
            FindTokensPipe("VERB/nsubj/*"),

            ]),
            FindTokensPipe("AUX/conj/VERB/ccomp/VERB/aux:pass/AUX"),

                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 34')
                    print(i)  
                results.append(i)

    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NUM"),
            ]),
            FindTokensPipe("NUM/cop/*")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 35')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADV/conj/PRON/nsubj/*"),
            ]),
            FindTokensPipe("ADV/conj/PRON/cop/*")
                     ]
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 36')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
            AggregatePipe([
        FindTokensPipe("NOUN/nmod/NOUN/acl:relcl/NOUN/nsubj"),

        ]),
        FindTokensPipe("NOUN/nmod/NOUN/acl:relcl/NOUN/cop"),
                 ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 37')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/nmod/NOUN/acl/VERB/nsubj"),

            ]),
            FindTokensPipe("NOUN/nmod/NOUN/acl/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 38')
                    print(i)  
                results.append(i)


                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NUM/acl:relcl/VERB/nsubj"),
            ]),
            FindTokensPipe("NUM/acl:relcl/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 40')
                    print(i)  
                results.append(i)
              
                    
    # relative che
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/acl:relcl/VERB/nsubj"),
            ]),
            FindTokensPipe("NOUN/acl:relcl/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 42')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("SCONJ/conj/VERB/nsubj"),
            ]),
            FindTokensPipe("SCONJ/conj/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 43')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("VERB/nsubj:pass"),
            ]),
            FindTokensPipe("VERB/aux:pass/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 44')
                    print(i)  
                results.append(i)
                
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/advcl/VERB/nsubj"),
            ]),
            FindTokensPipe("NOUN/advcl/VERB")
                     ]
    
    
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 46')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NUM/advcl/AUX/nsubj"),
            ]),
            FindTokensPipe("NUM/advcl/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 47')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("VERB/case/VERB/nsubj"),
            ]),
            FindTokensPipe("VERB/case/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 48')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("PROPN/obl/NOUN/acl:relcl/AUX/nsubj")
            ]),
            FindTokensPipe("PROPN/obl/NOUN/acl:relcl/AUX")
                     ]
                
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 49')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("X/nsubj")
            ]),
            FindTokensPipe("X/aux/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 50')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/parataxis/VERB/nsubj")
            ]),
            FindTokensPipe("NOUN/parataxis/VERB")
                     ]
    
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 51')
                    print(i)  
                results.append(i)
                
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("AUX/nsubj")
            ]),
        AnyPipe([
            FindTokensPipe("AUX/conj/VERB")
        ])
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 53')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADV/ccomp/X/csubj/AUX")
            ]),
            FindTokensPipe("ADV/ccomp/X/cop/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 54')
                    print(i)  
                results.append(i)

    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("PROPN")
            ]),
            FindTokensPipe("PROPN/amod/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 55')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("VERB/parataxis/VERB/nsubj")
            ]),
            FindTokensPipe("VERB/parataxis")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 56')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/acl:relcl/VERB/nsubj")
            ]),
            FindTokensPipe("NOUN/acl:relcl/VERB/aux/AUX")
                     ]

    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 57')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/acl:relcl/VERB/nsubj:pass/NOUN")
            ]),
            FindTokensPipe("NOUN/acl:relcl/VERB/aux:pass/AUX")
                     ]

    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 58')
                    print(i)  
                results.append(i)
        
        # che
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/acl:relcl/AUX/nsubj")
            ]),
            FindTokensPipe("NOUN/acl:relcl/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 59')
                    print(i)  
                results.append(i)
                
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("AUX/nsubj")
            ]),
            FindTokensPipe("AUX/cop/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 60')
                    print(i)  
                results.append(i)
                

    
    pipes_structure = [  
                    AggregatePipe([

                        FindTokensPipe("VERB/conj/X/nsubj"),
                        ]),
                FindTokensPipe("VERB/conj/X/cop/VERB"),
                         ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 62')
                    print(i)  
                results.append(i)
                
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("VERB/csubj/VERB")
            ]),
            FindTokensPipe("VERB/cop/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 64')
                    print(i)  
                results.append(i)
                
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/acl:relcl/NOUN/nsubj")
            ]),
            FindTokensPipe("NOUN/acl:relcl/NOUN/aux")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 65')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/nsubj")
            ]),
            FindTokensPipe("NOUN/det:predet/VERB")
                     ]

    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 66')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/appos/NOUN/nmod/NOUN/acl:relcl/AUX/nsubj")
            ]),
            FindTokensPipe("NOUN/appos/NOUN/nmod/NOUN/acl:relcl/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 67')
                    print(i)  
                results.append(i)
        pipes_structure = [  
                AnyPipe([
            FindTokensPipe("VERB/conj/AUX/nsubj"),
                    FindTokensPipe("VERB/nsubj"),
            
            ]),
            FindTokensPipe("VERB/conj/AUX")
                     ]
        
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 68')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADV/conj/NOUN/nsubj")
            ]),
            FindTokensPipe("ADV/conj/NOUN/aux/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 69')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/ccomp/VERB/nsubj")
            ]),
            FindTokensPipe("NOUN/ccomp/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 70')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/conj/NOUN")
            ]),
            FindTokensPipe("NOUN/conj/NOUN/aux/*")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 71')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADV/nsubj")
            ]),
            FindTokensPipe("ADV/cop/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 72')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/conj/PROPN/acl:relcl/VERB/nsubj")
            ]),
            FindTokensPipe("NOUN/conj/PROPN/acl:relcl/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 73')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADJ/obj/NOUN/ccomp/VERB/nsubj:pass")
            ]),
            FindTokensPipe("ADJ/obj/NOUN/ccomp/VERB/aux:pass/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 74')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("PROPN/nsubj/NOUN")
            ]),
            FindTokensPipe("PROPN/nsubj/NOUN/cop/VERB")
                     ]
    

    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 75')
                    print(i)  
                results.append(i)
                

                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN")
            ]),
            FindTokensPipe("NOUN/acl/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 77')
                    print(i)  
                results.append(i)

    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/appos/NOUN/acl:relcl/VERB/nsubj")
            ]),
            FindTokensPipe("NOUN/appos/NOUN/acl:relcl/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 78')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/acl:relcl/AUX/aux/AUX/nsubj"),
                    FindTokensPipe("NOUN/acl:relcl/AUX/nsubj")
            
            ]),
            FindTokensPipe("NOUN/acl:relcl/AUX/aux/AUX")
                     ]

    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 79')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/conj/VERB/aux/AUX")
            ]),
            FindTokensPipe("NOUN/obl/PRON")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 80')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NUM/acl:relcl/AUX/nsubj/NOUN")
            ]),
            FindTokensPipe("NUM/acl:relcl/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 81')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("AUX/obj/NOUN/acl:relcl/VERB/nsubj:pass")
            ]),
            FindTokensPipe("AUX/obj/NOUN/acl:relcl/VERB/aux")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 82')
                    print(i)  
                results.append(i)
                
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("DET/nsubj")
            ]),
            FindTokensPipe("DET/cop/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 83')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("PRON/nmod/NOUN/nmod/NOUN/acl:relcl/VERB/nsubj")
            ]),
            FindTokensPipe("PRON/nmod/NOUN/nmod/NOUN/acl:relcl/VERB/aux")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 84')
                    print(i)  
                results.append(i)
                
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADJ/parataxis/VERB/nsubj")
            ]),
            FindTokensPipe("ADJ/parataxis/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 85')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADV/nsubj")
            ]),
            FindTokensPipe("ADV/aux/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 86')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADV/ccomp/VERB/aux/nsubj")
            ]),
            FindTokensPipe("ADV/ccomp/VERB/aux")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 87')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADJ/conj/NOUN/nsubj")
            ]),
            FindTokensPipe("ADJ/conj/NOUN/aux/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 88')
                    print(i)  
                results.append(i)
    
    
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/nmod/NOUN/nmod/NOUN/nmod/PRON")
            ]),
            FindTokensPipe("NOUN/nmod/NOUN/nmod/NOUN/acl:relcl/VERB/aux")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 89')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("PRON/nmod/NOUN/nsubj")
            ]),
            FindTokensPipe("PRON/nmod/NOUN/cop/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 90')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADV/punct/ADV/conj/VERB/nsubj")
            ]),
            FindTokensPipe("ADV/punct/ADV/conj/VERB/aux")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 91')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/nsubj")
            ]),
            FindTokensPipe("NOUN/nsubj/NOUN/amod/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 92')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADJ/nsubj")
            ]),
            FindTokensPipe("ADJ/nsubj/NOUN/cop/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 93')
                    print(i)  
                results.append(i)
                
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("PRON/acl:relcl/NOUN/mark/PRON")
            ]),
            FindTokensPipe("PRON/acl:relcl/NOUN/cop/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 94')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("PROPN/nsubj")
            ]),
            FindTokensPipe("PROPN/cop/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 95')
                    print(i)  
                results.append(i)

    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADP/nsubj")
            ]),
            FindTokensPipe("ADP")
                     ]

    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 96')
                    print(i)  
                results.append(i)
    
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/conj/ADJ/nsubj")
            ]),
            FindTokensPipe("NOUN/conj/ADJ/cop/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 97')
                    print(i)  
                results.append(i)
    
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("AUX/obl/NOUN/acl:relcl/VERB/nsubj")
            ]),
            FindTokensPipe("AUX/obl/NOUN/acl:relcl/VERB/aux")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 98')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                    AggregatePipe([

                        FindTokensPipe("NOUN/nsubj"),
                        ]),
                FindTokensPipe("NOUN"),
                         ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 99')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("AUX/obj/NOUN/nsubj")
            ]),
            FindTokensPipe("AUX/obj/NOUN/cop/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 100')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("AUX/nsubj")
            ]),
            FindTokensPipe("AUX/nsubj/ADJ/punct/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 101')
                    print(i)  
                results.append(i)
    
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN")
            ]),
            FindTokensPipe("NOUN/acl/VERB/aux:pass/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 102')
                    print(i)  
                results.append(i)
    
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADV/obj/NOUN/acl:relcl/VERB/nsubj")
            ]),
            FindTokensPipe("ADV/obj/NOUN/acl:relcl/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 103')
                    print(i)  
                results.append(i)
    
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("PRON/nsubj")
            ]),
            FindTokensPipe("PRON/cop/VERB/aux/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 104')
                    print(i)  
                results.append(i)

    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("SCONJ/punct/VERB/nsubj")
            ]),
            FindTokensPipe("SCONJ/punct/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 105')
                    print(i)  
                results.append(i)
    
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN")
            ]),
            FindTokensPipe("NOUN/nmod/NOUN/cop/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 106')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADJ/nsubj")
            ]),
            FindTokensPipe("ADJ")
                     ]
    
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 107')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN")
            ]),
            FindTokensPipe("NOUN/punct/VERB")
                     ]

    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 108')
                    print(i)  
                results.append(i)
    
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/acl:relcl/NOUN/case/PRON")
            ]),
            FindTokensPipe("NOUN/acl:relcl/NOUN/amod/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 109')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/appos/NOUN/acl/VERB/nsubj")
            ]),
            FindTokensPipe("NOUN/appos/NOUN/acl/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 110')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("X/csubj/AUX/ccomp/VERB/nsubj")
            ]),
            FindTokensPipe("X/csubj/AUX/ccomp/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 111')
                    print(i)  
                results.append(i)
    

           
    
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADV/nsubj")
            ]),
            FindTokensPipe("ADV/conj/VERB/aux/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 114')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADV/nsubj")
            ]),
            FindTokensPipe("ADV/aux/*")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 115')
                    print(i)  
                results.append(i)
    
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("PROPN/acl:relcl/AUX/nsubj")
            ]),
            FindTokensPipe("PROPN/acl:relcl/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 116')
                    print(i)  
                results.append(i)
    
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("X/amod/ADJ/nsubj")
            ]),
            FindTokensPipe("X/amod/ADJ/aux")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 117')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/appos/PRON/acl:relcl/AUX/nsubj")
            ]),
            FindTokensPipe("NOUN/appos/PRON/acl:relcl/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 118')
                    print(i)  
                results.append(i)
    
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("PRON")
            ]),
            FindTokensPipe("PRON/acl:relcl/AUX/aux/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 119')
                    print(i)  
                results.append(i)
    
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/advmod/ADV/case/VERB/nsunj")
            ]),
            FindTokensPipe("NOUN/advmod/ADV/case/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 120')
                    print(i)  
                results.append(i)
    
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADV/ccomp/VERB/nsubj:pass")
            ]),
            FindTokensPipe("ADV/ccomp/VERB/aux:pass")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 121')
                    print(i)  
                results.append(i)
                


    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("PROPN/nmod/NOUN/ccomp/VERB/nsubj")
            ]),
            FindTokensPipe("PROPN/nmod/NOUN/ccomp/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 124')
                    print(i)  
                results.append(i)

    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("ADV/ccomp/ADJ/nsubj")
            ]),
            FindTokensPipe("ADV/ccomp/ADJ/cop/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 125')
                    print(i)  
                results.append(i)

    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("DET/xcomp/AUX/obj/NOUN")
            ]),
            FindTokensPipe("DET/xcomp/AUX/obj/NOUN/acl/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 126')
                    print(i)  
                results.append(i)

    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN")
            ]),
            FindTokensPipe("NOUN/nsubj/NOUN/cop/AUX")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 127')
                    print(i)  
                results.append(i)

    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("AUX/xcomp/AUX/obj/NOUN/acl:relcl/VERB/nsubj")
            ]),
            FindTokensPipe("AUX/xcomp/AUX/obj/NOUN/acl:relcl/VERB")
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 128')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("PROPN/nsubj")
            ]),
            FindTokensPipe("PROPN/aux")
                     ]
    
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 129')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
           FindTokensPipe("AUX/nsubj"),
            ]),
            FindTokensPipe("AUX/nsubj/NOUN/aux"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 130')
                    print(i)  
                results.append(i)
    
    pipes_structure = [  
                AggregatePipe([
           FindTokensPipe("NOUN/advcl/AUX/aux/AUX/nsubj"),
            ]),
            FindTokensPipe("NOUN/advcl/AUX/aux"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 131')
                    print(i)  
                results.append(i)
    
 
    
    pipes_structure = [  
                AggregatePipe([
           FindTokensPipe("NOUN/case/ADP/nsubj"),
            ]),
            FindTokensPipe("NOUN/case/ADP"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 133')
                    print(i)  
                results.append(i)
    
    pipes_structure = [  
                AggregatePipe([
           FindTokensPipe("NOUN/conj/VERB/nsubj"),
            ]),
            FindTokensPipe("NOUN/conj/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 134')
                    print(i)  
                results.append(i)
                
    ##############################################################
    

                

                

    

    
    
                
   
                
 ########################################################

    pipes_structure = [  
                    AggregatePipe([

                        FindTokensPipe("AUX/obj/NOUN/acl:relcl/AUX/nsubj"),
                        ]),
                FindTokensPipe("AUX/obj/NOUN/acl:relcl/AUX"),
                         ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 140')
                    print(i)  
                results.append(i)  
                

                
                
                
    pipes_structure = [  
                    AggregatePipe([

                        FindTokensPipe("VERB/ccomp/NOUN/nsubj"),
                        ]),
                FindTokensPipe("VERB/ccomp/NOUN/nsubj/NOUN/conj/NOUN/amod/ADJ"),
                         ]
    
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 143')
                    print(i)  
                results.append(i) 
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("X/csubj/AUX/ccomp/NOUN/nsubj"),
            ]),
            FindTokensPipe("X/csubj/AUX/ccomp/NOUN/cop/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 144')
                    print(i)  
                results.append(i) 
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("ADV/ccomp/AUX/nsubj"),
            ]),
            FindTokensPipe("ADV/ccomp/AUX/aux"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 145')
                    print(i)  
                results.append(i) 
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("INTJ/nsubj")

            ]),
            FindTokensPipe("INTJ/cop/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 146')
                    print(i)  
                results.append(i) 
                

                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("AUX/obj/PRON/acl:relcl/VERB/nsubj")

            ]),
            FindTokensPipe("AUX/obj/PRON/acl:relcl/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 148')
                    print(i)  
                results.append(i) 
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("AUX/obl/NOUN/cop/VERB/nsubj")

            ]),
            FindTokensPipe("AUX/obl/NOUN/cop/VERB"),
                     ]
    
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 149')
                    print(i)  
                results.append(i) 
                
             
            
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/conj/VERB/nsubj")

            ]),
            FindTokensPipe("NOUN/conj/VERB/aux"),
                     ]
    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 150')
                    print(i)  
                results.append(i) 
                
                
    pipes_structure = [  
            AggregatePipe([
        FindTokensPipe("PROPN/nsubj"),
        ]),
        FindTokensPipe("PROPN/aux"),
                 ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 151')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
            AggregatePipe([
        FindTokensPipe("ADV/ccomp/AUX/nsubj"),
        ]),
        FindTokensPipe("ADV/ccomp/AUX"),
                 ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 152')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
            AggregatePipe([
        FindTokensPipe("ADV/advmod/ADV/cop/VERB/nsubj"),
        ]),
        FindTokensPipe("ADV/advmod/ADV/cop/VERB"),
                 ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 153')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
            AggregatePipe([
        FindTokensPipe("NOUN/nmod/ADV/case/VERB/nsubj"),
        ]),
        FindTokensPipe("NOUN/nmod/ADV/case/VERB"),
                 ]
    
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 154')
                    print(i)  
                results.append(i)
                

                
    pipes_structure = [  
            AggregatePipe([
        FindTokensPipe("ADJ/xcomp/VERB/nsubj"),
        ]),
        FindTokensPipe("ADJ/xcomp/VERB"),
                 ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 156')
                    print(i)  
                results.append(i)
                
                
    pipes_structure = [  
            AggregatePipe([
        FindTokensPipe("ADV/conj/NOUN/nsubj"),
        ]),
        FindTokensPipe("ADV/conj/NOUN/cop/AUX"),
                 ]
    
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 157')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
            AggregatePipe([
        FindTokensPipe("NUM/advcl/VERB/nsubj"),
        ]),
        FindTokensPipe("NUM/advcl/VERB"),
                 ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 158')
                    print(i)  
                results.append(i)  
                
    pipes_structure = [  
            AggregatePipe([
        FindTokensPipe("ADV/conj/VERB/nsubj"),
        ]),
        FindTokensPipe("ADV/conj/VERB/aux"),
                 ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 159')
                    print(i)  
                results.append(i)  
                
 
                
    pipes_structure = [  
            AggregatePipe([
        FindTokensPipe("AUX/advcl/VERB/nsubj"),
        ]),
        FindTokensPipe("AUX/advcl/VERB/aux"),
                 ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 161')
                    print(i)  
                results.append(i) 
                


                
    pipes_structure = [  
                    SequencePipe([

                        FindTokensPipe("VERB/conj/X/advcl/VERB/nsubj/NOUN"),
                        ]),
        
                FindTokensPipe("VERB/conj/X/advcl/VERB/aux/AUX"),
                         ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 164')
                    print(i)  
                results.append(i) 
                
    pipes_structure = [  
                    AggregatePipe([

                        FindTokensPipe("VERB/ccomp/AUX/conj/VERB/ccomp/VERB/nsubj"),
                        
                        ]),
        
                FindTokensPipe("VERB/ccomp/AUX/conj/VERB/ccomp/VERB/aux"),
                         ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 165')
                    print(i)  
                results.append(i) 
                
    pipes_structure = [  
                    AggregatePipe([

                        FindTokensPipe("VERB/obj/NOUN/advcl/VERB/nsubj"),
                        ]),
                FindTokensPipe("VERB/obj/NOUN/advcl/VERB/aux"),
                         ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 166')
                    print(i)  
                results.append(i) 
                
    pipes_structure = [  
                    AggregatePipe([

                        FindTokensPipe("AUX/ccomp/AUX/nsubj:pass"),
                        ]),
                FindTokensPipe("AUX/ccomp/AUX/aux"),
                         ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 167')
                    print(i)  
                results.append(i) 
                

    
    
    pipes_structure = [  
                    AggregatePipe([

                        FindTokensPipe("VERB/nsubj"),
                        ]),
                FindTokensPipe("VERB/conj/AUX/aux"),
                         ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 169')
                    print(i)  
                results.append(i)
                

                

                
                
    pipes_structure = [  
                    AggregatePipe([

                        FindTokensPipe("VERB/obl/NOUN/acl/AUX/nsubj"),
                        ]),
                FindTokensPipe("VERB/obl/NOUN/acl/AUX")
                         ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 173')
                    print(i)  
                results.append(i)
                

                
    pipes_structure = [  
                    AggregatePipe([
                        FindTokensPipe("VERB/advcl/AUX/conj/AUX/obj/NOUN/nmod/NOUN/nmod/NOUN/conj/NOUN/nmod/NOUN/nmod/NOUN/acl:relcl/AUX/nsubj"),
                        
                        ]),
                FindTokensPipe("VERB/advcl/AUX/conj/AUX/obj/NOUN/nmod/NOUN/nmod/NOUN/conj/NOUN/nmod/NOUN/nmod/NOUN/acl:relcl/AUX")
                         ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 175')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                    AggregatePipe([
                        FindTokensPipe("AUX/nsubj"),
                        
                        ]),
                FindTokensPipe("AUX/conj/NOUN/cop/AUX")
                         ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 176')
                    print(i)  
                results.append(i)

                
        pipes_structure = [  
                AnyPipe([
            FindTokensPipe("AUX/advcl/AUX/obj/NOUN/nmod/NOUN/acl:relcl/AUX/nsubj"),
            
            ]),
            FindTokensPipe("AUX/advcl/AUX/obj/NOUN/nmod/NOUN/acl:relcl/AUX")
                     ]
        
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 177')
                    print(i)  
                results.append(i)
                
                
        pipes_structure = [  
                AnyPipe([
            FindTokensPipe("VERB/obl/NOUN/acl:relcl/VERB/nsubj"),
            
            ]),
            FindTokensPipe("VERB/obl/NOUN/acl:relcl/VERB/aux/AUX"),
            FindTokensPipe("VERB/obl/NOUN/acl:relcl/VERB")
                     ]

    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 178')
                    print(i)  
                results.append(i)
                
        pipes_structure = [  
                AnyPipe([
            FindTokensPipe("AUX/obj/PRON/acl:relcl/VERB/nsubj"),
            
            ]),
            FindTokensPipe("AUX/obj/PRON/acl:relcl/VERB/aux"),
            FindTokensPipe("AUX/obj/PRON/acl:relcl/VERB"),
                     ]
        
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 179')
                    print(i)  
                results.append(i)
                

                
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("NOUN/acl/AUX/ccomp/VERB/nsubj"),

            ]),
            FindTokensPipe("NOUN/acl/AUX/ccomp/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 182')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("VERB/nsubj/PRON/acl:relcl/VERB/nsubj/NOUN"),

            ]),
            FindTokensPipe("VERB/nsubj/PRON/acl:relcl/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 183')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("VERB/advcl/VERB/nsubj"),

            ]),
            FindTokensPipe("VERB/advcl/VERB/aux/AUX"),
            FindTokensPipe("VERB/advcl/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 184')
                    print(i)  
                results.append(i)
                

    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("VERB/conj/VERB/nsubj"),

            ]),
            FindTokensPipe("VERB/conj/VERB/aux/AUX"),
            FindTokensPipe("VERB/conj/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 186')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
            FindTokensPipe("VERB/obl/NOUN/acl:relcl/VERB/nsubj:pass"),

            ]),
            FindTokensPipe("VERB/obl/NOUN/acl:relcl/VERB/aux:pass/AUX"),
            FindTokensPipe("VERB/obl/NOUN/acl:relcl/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 187')
                    print(i)  
                results.append(i)
                
                
    
    
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("VERB/ccomp/VERB/nsubj:pass"),
                    FindTokensPipe("VERB/ccomp/AUX/ccomp/AUX/nsubj:pass"),
            ]),
        FindTokensPipe("VERB/ccomp/AUX/ccomp/AUX/aux:pass/AUX"),
        FindTokensPipe("VERB/ccomp/AUX/ccomp/AUX"),
            
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 191')
                    print(i)  
                results.append(i)
    
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("VERB/ccomp/ADJ/nsubj"),
            ]),
        FindTokensPipe("VERB/ccomp/ADJ/aux/AUX"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 191')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("AUX/advcl/AUX/nsubj"),
            ]),
        FindTokensPipe("AUX/advcl/AUX/aux/AUX"),
        FindTokensPipe("AUX/advcl/AUX"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 192')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("PRON"),
            ]),
        FindTokensPipe("PRON/conj/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 193')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("PRON/conj/VERB/obl/NOUN/amod/AUX/nsubj"),
            ]),
        FindTokensPipe("PRON/conj/VERB/obl/NOUN/amod/AUX"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 194')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("NOUN/nmod/NOUN/acl:relcl/AUX/nsubj:pass/NOUN"),
            ]),
        FindTokensPipe("NOUN/nmod/NOUN/acl:relcl/AUX/aux/AUX"),
        FindTokensPipe("NOUN/nmod/NOUN/acl:relcl/AUX"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 195')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("PRON/advcl/VERB/xcomp/AUX/ccomp/VERB/nsubj"),
            ]),
        FindTokensPipe("PRON/advcl/VERB/xcomp/AUX/ccomp/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 196')
                    print(i)  
                results.append(i)
                
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("PRON/acl/AUX/obj/NOUN/nmod/NOUN/acl:relcl/VERB/nsubj"),
            ]),
        FindTokensPipe("PRON/acl/AUX/obj/NOUN/nmod/NOUN/acl:relcl/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 197')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("VERB/obl/NOUN/nmod/NOUN/acl:relcl/VERB/nsubj"),
            ]),
        FindTokensPipe("VERB/obl/NOUN/nmod/NOUN/acl:relcl/VERB/aux/AUX"),
        FindTokensPipe("VERB/obl/NOUN/nmod/NOUN/acl:relcl/VERB"),
                     ]

    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 198')
                    print(i)  
                results.append(i)
                
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("VERB/xcomp/VERB/xcomp/ADJ/advcl/nsubj")
            ]),
        FindTokensPipe("VERB/xcomp/VERB/xcomp/ADJ/advcl/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 200')
                    print(i)  
                results.append(i)
                
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("VERB/obj/NOUN/acl/VERB/obj/NOUN/acl:relcl/VERB/nsubj"),
            ]),
        FindTokensPipe("VERB/obj/NOUN/acl/VERB/obj/NOUN/acl:relcl/VERB/aux/AUX"),
        FindTokensPipe("VERB/obj/NOUN/acl/VERB/obj/NOUN/acl:relcl/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 201')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("VERB/xcomp/AUX/ccomp/AUX/nsubj"),
            ]),
        FindTokensPipe("VERB/xcomp/AUX/ccomp/AUX/aux/AUX"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 202')
                    print(i)  
                results.append(i)
                
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("X/nsubj/NOUN/acl:relcl/VERB/nsubj:pass"),
            ]),
        FindTokensPipe("X/nsubj/NOUN/acl:relcl/VERB/aux"),
        FindTokensPipe("X/nsubj/NOUN/acl:relcl/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 203')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("VERB/xcomp/AUX/ccomp/VERB/nsubj"),
            ]),
        FindTokensPipe("VERB/xcomp/AUX/ccomp/VERB/aux"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 204')
                    print(i)  
                results.append(i)
                
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("ADJ/ccomp/VERB/nsubj:pass"),
            ]),
        AggregatePipe([
                            FindTokensPipe("ADJ/ccomp/VERB/aux/AUX"),
        FindTokensPipe("ADJ/ccomp/VERB/aux:pass/AUX"),
        FindTokensPipe("ADJ/ccomp/VERB"),
            ])
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 205')
                    print(i)  
                results.append(i)
                
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("VERB/csubj/AUX/obl/NOUN/acl:relcl/AUX/nsubj"),
            ]),
        FindTokensPipe("VERB/csubj/AUX/obl/NOUN/acl:relcl/AUX"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 206')
                    print(i)  
                results.append(i)
                
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("ADJ/obl/NOUN/acl:relcl/VERB/nsubj"),
            ]),
        FindTokensPipe("ADJ/obl/NOUN/acl:relcl/VERB"),
                     ]
    
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 207')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("X/ccomp/VERB/nsubj:pass"),
            ]),
        FindTokensPipe("X/ccomp/VERB/aux:pass/AUX"),
        FindTokensPipe("X/ccomp/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 208')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("ADJ/conj/AUX/nsubj"),
            ]),
        FindTokensPipe("ADJ/conj/AUX"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 209')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("AUX/advcl/VERB/nsubj"),
            ]),
        FindTokensPipe("AUX/advcl/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 210')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("AUX/advcl/ADJ/aux/AUX/nsubj"),
            ]),
        FindTokensPipe("AUX/advcl/ADJ/aux/AUX"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 211')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("VERB/obj/NOUN/acl:relcl/AUX/nsubj"),
            ]),
        FindTokensPipe("VERB/obj/NOUN/acl:relcl/AUX"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 212')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("ADJ/nsubj/NOUN/nmod/PRON/acl:relcl/VERB/nsubj"),
            ]),
        FindTokensPipe("ADJ/nsubj/NOUN/nmod/PRON/acl:relcl/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 213')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("AUX/xcomp/AUX/advcl/AUX/obj/NOUN/acl:relcl/AUX/nsubj"),
            ]),
        FindTokensPipe("AUX/xcomp/AUX/advcl/AUX/obj/NOUN/acl:relcl/AUX"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 214')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("NOUN/conj/NOUN/nsubj"),
            ]),
        FindTokensPipe("NOUN/conj/NOUN/cop/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 215')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("AUX/obj/ADV/amod/X/cop/VERB/nsubj"),
            ]),
        FindTokensPipe("AUX/obj/ADV/amod/X/cop/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 216')
                    print(i)  
                results.append(i)
                

                
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("VERB/obj/NOUN/nmod/NOUN/acl:relcl/AUX/nsubj"),
            ]),
        FindTokensPipe("VERB/obj/NOUN/nmod/NOUN/acl:relcl/AUX"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 219')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("PRON/acl:relcl/VERB/nsubj:pass")
            ]),
        FindTokensPipe("PRON/acl:relcl/VERB/aux:pass/AUX"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 220')
                    print(i)  
                results.append(i)
                
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("AUX/obj/NOUN/nmod/NOUN/acl:relcl/ADJ/csubj")
            ]),
        FindTokensPipe("AUX/obj/NOUN/nmod/NOUN/acl:relcl/ADJ/cop/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 222')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                    FindTokensPipe("VERB/xcomp/AUX/obj/NOUN/acl:relcl/VERB/nsubj"),
            ]),
        FindTokensPipe("VERB/xcomp/AUX/obj/NOUN/acl:relcl/VERB/aux/AUX"),
        FindTokensPipe("VERB/xcomp/AUX/obj/NOUN/acl:relcl/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 223')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                            FindTokensPipe("VERB/csubj/AUX/obj/NOUN/nmod/NOUN/nmod/NOUN/acl/ADJ/obl/PROPN/acl:relcl/VERB/nsubj"),
            ]),
        FindTokensPipe("VERB/csubj/AUX/obj/NOUN/nmod/NOUN/nmod/NOUN/acl/ADJ/obl/PROPN/acl:relcl/VERB/aux"),
        FindTokensPipe("VERB/csubj/AUX/obj/NOUN/nmod/NOUN/nmod/NOUN/acl/ADJ/obl/PROPN/acl:relcl/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 224')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                            FindTokensPipe("ADJ/conj/VERB/nsubj"),
            ]),
        FindTokensPipe("ADJ/conj/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 225')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                            FindTokensPipe("VERB/advmod/ADV/obl/PRON/acl:relcl/AUX/nsubj"),
            ]),
        FindTokensPipe("VERB/advmod/ADV/obl/PRON/acl:relcl/AUX/aux/AUX"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 226')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                            FindTokensPipe("ADJ/obl/NOUN/nmod/NOUN/acl:relcl/VERB/nsubj"),
            ]),
        FindTokensPipe("ADJ/obl/NOUN/nmod/NOUN/acl:relcl/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 227')
                    print(i)  
                results.append(i)
                
                
    pipes_structure = [  
                AggregatePipe([
                           FindTokensPipe("X/obl/PRON/acl:relcl/VERB/nsubj"),
            ]),
        FindTokensPipe("X/obl/PRON/acl:relcl/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 229')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                           FindTokensPipe("AUX/nsubj/NOUN/acl:relcl/AUX/nsubj"),
            ]),
        FindTokensPipe("AUX/nsubj/NOUN/acl:relcl/AUX"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 230')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                           FindTokensPipe("VERB/conj/VERB/nsubj:pass/NOUN"),
            ]),
        FindTokensPipe("VERB/conj/VERB/aux:pass/AUX"),
        FindTokensPipe("VERB/conj/VERB"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 231')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                           FindTokensPipe("VERB/obl/NOUN/acl/AUX/advcl/AUX/nsubj"),
            ]),
        FindTokensPipe("VERB/obl/NOUN/acl/AUX/advcl/AUX"),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 232')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                           FindTokensPipe("AUX/nsubj/NOUN/acl:relcl/VERB/nsubj"),
            ]),
        FindTokensPipe("AUX/nsubj/NOUN/acl:relcl/VERB/aux/AUX"),
        FindTokensPipe("AUX/nsubj/NOUN/acl:relcl/VERB"),
                     ]
    
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 233')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                           FindTokensPipe("PRON/nsubj/NOUN/acl:relcl/AUX/nsubj"),
            ]),
        FindTokensPipe('PRON/nsubj/NOUN/acl:relcl/AUX/aux/AUX'),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 234')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                           FindTokensPipe("VERB/nsubj/NOUN/nmod/NOUN/acl:relcl/VERB/nsubj"),
            ]),
        FindTokensPipe('VERB/nsubj/NOUN/nmod/NOUN/acl:relcl/VERB'),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 235')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                           FindTokensPipe("*/*/*/acl:relcl/VERB/nsubj"),
            ]),
        FindTokensPipe('*/*/*/acl:relcl/VERB'),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 236')
                    print(i)  
                results.append(i)
    
    pipes_structure = [  
                AggregatePipe([
                           FindTokensPipe("*/*/*/*/*/acl:relcl/AUX/nsubj"),
            ]),
        FindTokensPipe('*/*/*/*/*/acl:relcl/AUX'),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 237')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                           FindTokensPipe('*/csubj/VERB/nsubj:pass'),
            ]),
        FindTokensPipe('*/csubj/VERB/aux:pass/AUX'),
        FindTokensPipe('*/csubj/VERB'),
                     ]

    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 238')
                    print(i)  
                results.append(i)   
                
    pipes_structure = [  
                AggregatePipe([
                        FindTokensPipe('*/acl:relcl/NOUN/nsubj'),
            ]),
        FindTokensPipe('*/acl:relcl/NOUN/cop/VERB'),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 239')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                        FindTokensPipe('*/*/*/*/*/*/*/*/*/acl:relcl/AUX/nsubj'),
            ]),
        FindTokensPipe('*/*/*/*/*/*/*/*/*/acl:relcl/AUX/aux/AUX'),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 240')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                        FindTokensPipe('*/*/*/advcl/VERB/nsubj:pass'),
            ]),
        FindTokensPipe('*/*/*/*/*/aux:pass/AUX'),
        FindTokensPipe('*/*/*/advcl/VERB'),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 241')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                        FindTokensPipe('*/*/*/ccomp/VERB/nsubj'),
            ]),
        FindTokensPipe('*/*/*/ccomp/VERB'),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 242')
                    print(i)  
                results.append(i)
                
    pipes_structure = [  
                AggregatePipe([
                        FindTokensPipe('*/*/*/cop/VERB/nsubj'),
                        FindTokensPipe("*/ccomp/X/nsubj"),
                    FindTokensPipe("*/ccomp/NOUN/nsubj")
            ]),
        FindTokensPipe('*/*/*/cop/VERB'),
                     ]
    



    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 243')
                    print(i)  
                results.append(i)    
                
                
    pipes_structure = [  
                AggregatePipe([
                        FindTokensPipe('*/*/*/*/*/aux/AUX/nsubj'),
            ]),
        FindTokensPipe('*/*/*/*/*/aux/AUX'),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 244')
                    print(i)  
                results.append(i)    
                
    pipes_structure = [  
                AggregatePipe([
                        FindTokensPipe('*/advcl/AUX/nsubj'),
            ]),
        FindTokensPipe('*/advcl/AUX'),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 245')
                    print(i)  
                results.append(i) 
        if(len(i[1]) > 1 ):
            if i[1][1]:
                if str(i[1][1]) in list_verbs:
                    if Verbose:
                        print('Rule 245')
                        print(i)  
                    results.append(i) 
                    
    pipes_structure = [  
                AggregatePipe([
                        FindTokensPipe('*/*/*/*/*/*/AUX/nsubj'),
            ]),
        FindTokensPipe('*/*/*/*/*/*/AUX/aux/AUX'),
                     ]
    
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 245')
                    print(i)  
                results.append(i)   
                
    pipes_structure = [  
                AggregatePipe([
                        FindTokensPipe('*/*/*/*/*/*/*/*/VERB/nsubj'),
            ]),
        FindTokensPipe('*/*/*/*/*/*/*/*/*/aux/AUX'),
        FindTokensPipe('*/*/*/*/*/*/*/*/VERB'),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 246')
                    print(i)  
                results.append(i)   

    pipes_structure = [  
                AggregatePipe([
                        FindTokensPipe('*/*/*/*/*/*/VERB/nsubj'),
            ]),
        FindTokensPipe('*/*/*/*/*/*/VERB'),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 247')
                    print(i)  
                results.append(i)  
                
    pipes_structure = [  
                AggregatePipe([
                        FindTokensPipe('*/*/*/aux:pass/AUX/nusbj'),
            ]),
        FindTokensPipe('*/*/*/aux:pass/AUX'),
                     ]
                
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 250')
                    print(i)  
                results.append(i)  
                
    pipes_structure = [  
                AggregatePipe([
                        FindTokensPipe('*/*/*/*/*/*/*/*/*/acl:relcl/VERB/nsubj'),
            ]),
        FindTokensPipe('*/*/*/*/*/*/*/*/*/acl:relcl/VERB/aux/AUX'),
        FindTokensPipe('*/*/*/*/*/*/*/*/*/acl:relcl/VERB'),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 251')
                    print(i)  
                results.append(i) 
                
    pipes_structure = [  
                AggregatePipe([
                        FindTokensPipe('*/*/*/*/*/*/*/acl:relcl/VERB/nsubj'),
            ]),
        AggregatePipe([
        FindTokensPipe('*/*/*/*/*/*/*/acl:relcl/VERB/aux/AUX'),
        FindTokensPipe('*/*/*/*/*/*/*/acl:relcl/VERB'),
            ]),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 252')
                    print(i)  
                results.append(i) 
                
    pipes_structure = [  
                AggregatePipe([
                        FindTokensPipe('*/conj/AUX/nsubj'),
            ]),
        AggregatePipe([
        FindTokensPipe('*/conj/AUX'),
            ]),
                     ]
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 253')
                    print(i)  
                results.append(i) 
                
    pipes_structure = [  
                AggregatePipe([
                        FindTokensPipe('*/*/*/*/*/*/*/*/*/acl:relcl/VERB/nsubj'),
            ]),
        AggregatePipe([
        FindTokensPipe('*/*/*/*/*/*/*/*/*/acl:relcl/VERB'),
            ]),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 254')
                    print(i)  
                results.append(i) 
                
    pipes_structure = [  
                AggregatePipe([
                        FindTokensPipe('*/*/*/aux/AUX/nsubj'),
                    FindTokensPipe("*/*/VERB/nsubj:pass"),
                    FindTokensPipe("*/*/VERB/nsubj"),
            ]),
        AggregatePipe([
        FindTokensPipe('*/*/*/aux/AUX'),
        FindTokensPipe("*/*/VERB/aux:pass"),
        FindTokensPipe("*/ccomp/VERB"),
            ]),
                     ]
    
    
               
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 255')
                    print(i)  
                results.append(i) 
                
    pipes_structure = [  
                AggregatePipe([
                        FindTokensPipe('*/*/*/*/*/*/*/cop/AUX/nsubj'),
            ]),
        AggregatePipe([
        FindTokensPipe('*/*/*/*/*/*/*/cop/AUX'),
            ]),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 256')
                    print(i)  
                results.append(i) 
                
    pipes_structure = [  
                AggregatePipe([
                        FindTokensPipe('*/conj/VERB/nsubj'),
            ]),
        AggregatePipe([
        FindTokensPipe('*/conj/VERB'),
            ]),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 257')
                    print(i)  
                results.append(i) 
                
    pipes_structure = [  
                AggregatePipe([
                        FindTokensPipe('*/*/*/*/*/*/*/advcl/VERB/nsubj'),
            ]),
        AggregatePipe([
        FindTokensPipe('*/*/*/*/*/*/*/advcl/VERB'),
            ]),
                     ]
    
    engine = PipelineEngine(pipes_structure, Context(sen))
    res = engine.process()    
    for i in res:
        if i[1]:
            if str(i[1][0]) in list_verbs:
                if Verbose:
                    print('Rule 258')
                    print(i)  
                results.append(i) 
    return results
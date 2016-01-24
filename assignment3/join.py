import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()
    
# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    value = record
    #value.append(record[0])
    #words = value.split()
    #print record
    #print record
    mr.emit_intermediate(key, value)            
            
# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    doc_list = list()
    for v in list_of_values:
        if len(v) == 10:
            basic_list = v
    for v in list_of_values:
        if len(v) == 17:
            new_list = list(basic_list)
            for el in v:
                new_list.append(el)
            mr.emit((new_list))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)

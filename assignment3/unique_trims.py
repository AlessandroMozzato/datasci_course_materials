import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()
    
# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    mr.emit_intermediate(value[0:len(value)-10],key) 

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #print key,list_of_values
    #to_print = set(list_of_values)
    #for el in to_print:
    mr.emit(key)

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)

import MapReduce
import sys
# Part 1
mr = MapReduce.MapReduce()
    
# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = 1
    #value.append(record[0])
    #words = value.split()
    #print record
    #print record
    mr.emit_intermediate(key, value)            
            
# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    mr.emit((key, len(list_of_values)))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)

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
    print record
    mr.emit_intermediate(key,value) 
    mr.emit_intermediate(value,key) 
        
# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    dic = {}
    for el in list_of_values:
        if dic.has_key(el):
            dic.pop(el)
        else:
            dic[el] = key
    for el in dic:
        mr.emit((el,dic[el]))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)

register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
-- raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray);

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

-- ntriples_filt = filter ntriples by subject = '.*rdfabout\\.com.*';
ntriples_filt =	 filter ntriples by (subject matches '.*rdfabout.com.*') PARALLEL 50;
ntriples_filt2 = foreach ntriples_filt generate subject as subject2, predicate as predicate2, object as object2 PARALLEL 50;

-- describe ntriples_filt
-- describe ntriples_filt2

filt_join = join ntriples_filt BY object, ntriples_filt2 BY subject2 PARALLEL 50;

-- describe filt_join

-- store the results in the folder /user/hadoop/example-results
store filt_join into '/user/hadoop/problem3-results6' using PigStorage();






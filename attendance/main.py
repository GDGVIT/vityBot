import extractor
import makeQuery

id = raw_input('Enter ID: ').rstrip()

input_str = raw_input().lower().strip('?')

inp = input_str.split()

keywords = extractor.extractKeyWords(inp)

makeQuery.makeQuery(id, keywords)
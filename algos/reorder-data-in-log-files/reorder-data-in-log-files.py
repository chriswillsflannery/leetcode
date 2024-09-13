class Solution:
        # ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        #let1 art can, let3 art zero, let2 own kit dig, dig1 8 1 5 1, dig2 

        # all alphas get put in front
        # all numericals get put at end
        # alphas sorted by alphabetical sort of values
        # unless all values are same, where we sort by identifier
        # digit logs should retain existing order

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key = self.get_sort_key)
    def get_sort_key(self, logs):
        # 1 defines max amount of splits, i.e. here we break string in 2 parts
        # like a: dig1, b: 8 1 5 1
        identifier,content = logs.split(' ', 1)

        # content is letter
        # 0 denotes order of letter content going first
        # content: (favor sorting content values first)
        # identifier: then sort by identifier where content same
        if content[0].isalpha():
            return (0,content,identifier)
        else:
            # content is number
            # 1 places values after content-is-letter values
            # None None retains original order
            return (1,None,None)

# time complexity O(nLogN) due to sorting algo where n is number of logs
# space complexity O(n) due to storing sorted result

"""
example:
input:
["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

splits:
a: dig1, b: 8 1 5 1
a: let1, b: art can

sorts by 0 and 1 first, 
alphas like art can go at front
numers like 8 1 5 1 go at back

alphas get further sorted:
favoring content first:
art can
art zero

where content same, eg:
dig2 art can
dig1 art can

favor secondary by key
dig1 art can
dig2 art can

this results in priority:
first sorted alphas by content
where same by identifier
then numers, retaining OG order
"""

"""
Given a string print all subsets (not permutations)


Eg. String "abc" should output
empty string
a
b
c
ab
bc
ac
abc

"""

def printSubsets(string):
  def combine(substring, index, current, result):
    if index == len(substring):
      result.append(current)
      return
    
    # 2 choices for each character: include or skip

    #include
    combine(substring, index+1, current + string[index], result)

    #skip
    combine(substring, index+1, current, result)
  result = []
  combine(string, 0, "", result)
  return sorted(result)

# Test cases
def test_subsets():
    # Test case 1: "abc"
    print("Test case 1: 'abc'")
    subsets = printSubsets("abc")
    for subset in subsets:
        print(f"'{subset}'" if subset else "empty string")
    
    # Test case 2: empty string
    print("\nTest case 2: empty string")
    subsets = printSubsets("")
    for subset in subsets:
        print(f"'{subset}'" if subset else "empty string")
    
    # Test case 3: single character
    print("\nTest case 3: 'a'")
    subsets = printSubsets("a")
    for subset in subsets:
        print(f"'{subset}'" if subset else "empty string")

# Run the tests
test_subsets()
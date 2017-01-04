"""
STATEMENT
Given an absolute path for a file (Unix-style), simplify it.

CLARIFICATIONS
- Is it always given with respect to the root folder (/)? Not necessarily.
- I am assuming once in the root directory, doing "../" will still be in
  the root directory, so will return "/"? Yes.
- Should I ignore multiple consecutive "/" (except the one at the start, of course)? Yes.
- Should the trailing "/" remain? No.

EXAMPLES
"/home/" -> "/home"
"/a/./b/../../c/" -> "/c"
"/../" -> "/"
"/home//foo/" -> "/home/foo"

COMMENTS
- We will split the path by "/", ignore empty strings and consider spacial cases.
- When joining, we'd ensure we keep the first "/" if it starts the path.
"""

def simplifyPath(path):
        """
        :type path: str
        :rtype: str
        """
      path_split = path.split("/")
    	to_return_split = []
    	for chunk in path_split:
    		if chunk == "..":
    			try:
        			if to_return_split[-1] != "../":
        				temp = to_return_split.pop()
        			else:
        				to_return_split.append(chunk)
        		except IndexError:
        			continue
    		elif chunk == ".":
    			continue
    		elif chunk == "":
    			continue
    		else:
    			to_return_split.append(chunk)
    	if path[0] == "/":
    		return "/%s"%('/'.join(to_return_split))
    	else:
    		if to_return:
        		return ''.join(to_return_split)
        	else:
        		return './'

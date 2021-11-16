class Solution:
  def strstr(self, haystack, needle):
    if needle == "":
      
      return 0
    # To use KMP algorithm, you must first finish Longest Prefix Suffix part.
    # LPS
    lps = [0] * len(needle)
    
    prevLPS, i = 0, 1
    while i < len(needle):
      if needle[i] == needle[prevLPS]:
        lps[i] = prevLPS + 1
        prevLPS += 1
        i += 1
      elif prevLPS == 0:
        lps[i] = 0
        i += 1
      else:
        prevLPS = lps[prevLPS - 1]
  
    # KMP
    h = n = 0 # haystack = needle = 0
    while h < len(haystack):
      if haystack[h] == needle[n]:
        h, n = h + 1, n + 1
      
      else:
        if n == 0:
          h += 1
        else:
          n = lps[n - 1]
          
      if n == len(needle):
        
        return i - len(needle)
      
    return -1

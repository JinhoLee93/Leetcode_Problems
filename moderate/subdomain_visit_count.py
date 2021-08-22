class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cp = {}
        result = []
        
        for domain in cpdomains:
            dotNum = domain.count('.')
            num = ""
            dom1 = ""
            dom2 = ""
            dom3 = ""
            numPass = False
            for i in range(len(domain)):
                if domain[i] != " " and numPass == False:
                    num += domain[i]
                
                if domain[i] == " ":
                    numPass = True
                    continue
                    
                if domain[i] != "." and numPass:
                    if dotNum == 0:
                        dom3 += domain[i]
                    
                    elif dotNum == 1:
                        dom2 += domain[i]
                    
                    else: 
                        dom1 += domain[i]
                
                if domain[i] == ".":
                    dotNum -= 1
            
            if len(dom1) > 0:
                cp[dom1 + "." + dom2 + "." + dom3] = int(num) + cp.get(dom1 + "." + dom2 + "." + dom3, 0)
            cp[dom2 + "." + dom3] = int(num) + cp.get(dom2 + "." + dom3, 0)
            cp[dom3] = int(num) + cp.get(dom3, 0)
                    
        for key in cp.keys():
            result.append(f"{cp[key]} {key}")
        
        return result

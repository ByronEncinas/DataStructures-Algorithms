## My solution 37 ms
def numberOfRounds(loginTime: str, logoutTime: str) -> int:
    
    num = _number(loginTime, logoutTime)

    return "Number of playable rounds ( %s , %s ): %s" % (loginTime,logoutTime,num)

def _number(loginTime: str, logoutTime: str) -> int:
    inHH, inMM = loginTime.split(':')
    outHH, outMM = logoutTime.split(':')
    inHH, inMM = int(inHH), int(inMM)
    outHH, outMM = int(outHH), int(outMM)
    """
        inHH:inMM   = 00:01 
        outHH:outMM = 00:00
    """
    FullHR     = 0 
    startHR    = 0
    endHR      = 0
    if outHH == inHH and outMM > inMM: #inHH:inMM = 12:08 - outHH:outMM = 12:57
        if inMM%15 == 0:
            return outMM//15 - inMM//15
        if inMM < outMM:
            roundsLost = inMM//15 + 1
            if roundsLost <= outMM//15:
                return outMM//15 - roundsLost
        return 0
    if outHH > inHH:
        startHR = (60 - inMM)//15 # 60 - MM = 46 -> 46//15 = 3
        inHH += 1
        FullHR  = (outHH - inHH)*4 
        endHR   = outMM//15
        return startHR + FullHR + endHR
    else: # outHH < inHH
        startHR = (60-inMM)//15
        FullHR  = (23 - inHH)*4 + outHH*4
        endHR   = outMM//15
        return startHR + FullHR + endHR


print(numberOfRounds("09:31","10:14")) # 1
print(numberOfRounds("21:30","03:00")) # 22
print(numberOfRounds("23:30","03:00")) # 14
print(numberOfRounds("12:08","12:57")) # 2
print(numberOfRounds("06:13","06:19")) # 0
print(numberOfRounds("09:00","09:58")) # 3
print(numberOfRounds("19:15","19:46")) # 2
print(numberOfRounds("12:01","12:02")) # 0




from math import ceil, floor

def parse_time(time: str) -> int:
    hours, minutes = time.split(":")
    return int(hours) * 60 + int(minutes)
## Best Runtime 11 ms
class Solution:
    def _numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        # 21*60 + 30 -> 21*4+2 
        login_time = parse_time(loginTime)
        # 27*60 -> 27*4  6*4 - 2
        logout_time = parse_time(logoutTime)

        if logout_time < login_time:
            logout_time += 24 * 60
        
        # round login_time to next game
        login_time = ceil(login_time / 15)*15
        # previous game
        logout_time = floor(logout_time / 15)*15

        return max(int((logout_time - login_time)/15), 0)
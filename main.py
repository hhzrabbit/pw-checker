upper = "".join( [chr(x) for x in range(ord("A"), ord("Z")+1)] )
lower = "".join( [chr(x) for x in range(ord("a"), ord("z")+1)] )
numbers = "".join( [chr(x) for x in range(ord("0"), ord("9")+1)] )

def meetsReqs(pw):
    hasUpper = True in [x in upper for x in pw]
    hasLower = True in [x in lower for x in pw]
    hasNumber = True in [x in numbers for x in pw]
    return hasUpper and hasLower and hasNumber

print meetsReqs("abcd")
print meetsReqs("ABcd")
print meetsReqs("abcd4")
print meetsReqs("ABCD4")
print meetsReqs("AbCd4")

def strength(pw):
    convert = [0 if x in upper else 1 if x in lower else 2 if x in numbers else 3 for x in pw]

    rating = 0
    if 0 in convert and 1 in convert:
        rating += 1
    if 2 in convert:
        rating += 1
    if 3 in convert:
        rating += 1

    if rating == 3:
        rating += 1
        
    rating += (len(pw) - 5) / 2
        
    if rating < 0:
        rating = 0
    if rating > 9:
        rating = 9
            
    return rating + 1

print strength("1234")
print strength("password")
print strength("aprettydecentpassword")
print strength("ogjEDeDfu()$8fjk")


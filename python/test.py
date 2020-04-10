import re

td_text = "BannerCon GroupM_HR_PBU_Seat"
#td_text = "AdForm A/S"

ar_save_company = ["groupm"]

print(td_text.strip())

text_abc= re.sub(r"[^A-Za-z0-9 ]+","",td_text.strip()).lower()
print(text_abc)

text_abc = ' '.join( [w for w in text_abc.split() if len(w)>2] )
print(text_abc)

text_abc = re.sub(r"\s*ltd+\s*","",text_abc).strip()
text_abc = re.sub(r"\s*inc+\s*","",text_abc).strip()    

res = [ele for ele in ar_save_company if(text_abc.startswith(ele))] 
if len(res)>0:
    print("encontrado: " + res[0])
print(text_abc)


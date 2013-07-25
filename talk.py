import subprocess

# A requirement for this program is to have mpg123 installed, do this by calling
# sudo apt-get install mpg123 on a debian based system.

def talk(what, how):
   n = 0
   a = what.split();
   while ((len(a) - n) >= 10):
      string = '+'.join(a[n:n+10])  
      final_string = "http://translate.google.com/translate_tts?tl=" + how + "&q=" + string
      subprocess.call(["mpg123", final_string])
      print final_string
      string = "";
      n = n+10; 

   string = '+'.join(a[n:len(a)])
   final_string = "http://translate.google.com/translate_tts?tl=" + how + "&q=" + string
   subprocess.call(["mpg123", final_string])
   print final_string


#talk ("FOUR SCORE AND SEVEN YEARS AGO OUR FATHERS BROUGHT FORTH ON THIS CONTINENT A NEW NATION CONCEIVED IN LIBERTY AND DEDICATED TO THE PROPOSITION THAT ALL MEN ARE CREATED EQUAL NOW WE ARE ENGAGED IN A GREAT CIVIL WAR TESTING WHETHER THAT NATION OR ANY NATION SO CONCEIVED AND SO DEDICATED CAN LONG ENDURE WE ARE MET ON A GREAT BATTLEFIELD OF THAT WAR WE HAVE COME TO DEDICATE A PORTION OF THAT FIELD AS A FINAL RESTING PLACE FOR THOSE WHO HERE GAVE THEIR LIVES THAT THAT NATION MIGHT LIVE IT IS ALTOGETHER FITTING AND PROPER THAT WE SHOULD DO THIS BUT IN A LARGER SENSE WE CAN NOT DEDICATE WE CAN NOT CONSECRATE WE CAN NOT HALLOW THIS GROUND THE BRAVE MEN LIVING AND DEAD WHO STRUGGLED HERE HAVE CONSECRATED IT FAR ABOVE OUR POOR POWER TO ADD OR DETRACT THE WORLD WILL LITTLE NOTE NOR LONG REMEMBER WHAT WE SAY HERE BUT IT CAN NEVER FORGET WHAT THEY DID HERE IT IS FOR US THE LIVING RATHER TO BE DEDICATED HERE TO THE UNFINISHED WORK WHICH THEY WHO FOUGHT HERE HAVE THUS FAR SO NOBLY ADVANCED IT IS RATHER FOR US TO BE HERE DEDICATED TO THE GREAT TASK REMAINING BEFORE US THAT FROM THESE HONORED DEAD WE TAKE INCREASED DEVOTION TO THAT CAUSE FOR WHICH THEY GAVE THE LAST FULL MEASURE OF DEVOTION THAT WE HERE HIGHLY RESOLVE THAT THESE DEAD SHALL NOT HAVE DIED IN VAIN THAT THIS NATION UNDER GOD SHALL HAVE A NEW BIRTH OF FREEDOM AND THAT GOVERNMENT OF THE PEOPLE BY THE PEOPLE FOR THE PEOPLE SHALL NOT PERISH FROM THE EARTH","en")

#Supported Languages
# en    -- 
# af    -- afrikaans
# sq    -- albanian
# ar    -- arabic
# hy    -- Armenian
# bs    -- Bosnian
# ca    -- Catalan
# zh-cn -- Chinese (Simplified)
# zh-tw -- Chinese (Traditional)
# hr    -- Croatian
# cs    -- Czech
# da    -- Danish
# nl    -- Dutch
# eo    -- Esperanto
# fi    -- Finnish
# fr    -- French
# de    -- German
# el    -- Greek
# ht    -- Haitian Creole
# hi    --
# hu    --
# is    --
# id    --
# it    --
# ja    --
# ko    --
# la    --
# lv    --
# mk    --
# no    --
# pl    --
# pt-BR --
# ro    --
# ru    --
# sr    --
# sk    --
# es    --
# sw    --
# sv    --
# ta    --
# th    --
# tr    --
# vi    --
# cy    --
# yi    --

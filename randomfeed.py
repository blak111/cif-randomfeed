howmanyrecords=15000
recordtypes = ['ip','domain','url','md5','sha1']

import os
import random
import string
import hashlib
import time
import datetime

tlds = ['AC','AD','AE','AERO','AF','AG','AI','AL','AM','AN','AO',
        'AQ','AR','ARPA','AS','ASIA','AT','AU','AW','AX','AZ','BA',
        'BB','BD','BE','BF','BG','BH','BI','BIZ','BJ','BM','BN','BO',
        'BR','BS','BT','BV','BW','BY','BZ','CA','CAT','CC','CD','CF',
        'CG','CH','CI','CK','CL','CM','CN','CO','COM','COOP','CR','CU',
        'CV','CW','CX','CY','CZ','DE','DJ','DK','DM','DO','DZ','EC',
        'EDU','EE','EG','ER','ES','ET','EU','FI','FJ','FK','FM','FO',
        'FR','GA','GB','GD','GE','GF','GG','GH','GI','GL','GM','GN',
        'GOV','GP','GQ','GR','GS','GT','GU','GW','GY','HK','HM','HN',
        'HR','HT','HU','ID','IE','IL','IM','IN','INFO','INT','IO','IQ',
        'IR','IS','IT','JE','JM','JO','JOBS','JP','KE','KG','KH','KI',
        'KM','KN','KP','KR','KW','KY','KZ','LA','LB','LC','LI','LK',
        'LR','LS','LT','LU','LV','LY','MA','MC','MD','ME','MG','MH',
        'MIL','MK','ML','MM','MN','MO','MOBI','MP','MQ','MR','MS',
        'MT','MU','MUSEUM','MV','MW','MX','MY','MZ','NA','NAME',
        'NC','NE','NET','NF','NG','NI','NL','NO','NP','NR','NU','NZ'
        ,'OM','ORG','PA','PE','PF','PG','PH','PK','PL','PM','PN','POST','PR',
        'PRO','PS','PT','PW','PY','QA','RE','RO','RS','RU','RW','SA','SB','SC',
        'SD','SE','SG','SH','SI','SJ','SK','SL','SM','SN','SO','SR','ST','SU',
        'SV','SX','SY','SZ','TC','TD','TEL','TF','TG','TH','TJ','TK','TL','TM',
        'TN','TO','TP','TR','TRAVEL','TT','TV','TW','TZ','UA','UG','UK','US',
        'UY','UZ','VA','VC','VE','VG','VI','VN','VU','WF','WS','XXX','YE',
        'YT','ZA','ZM','ZW']

not_valid = [10,127,254,255,1,2,169,172,192]
for num in xrange(0,howmanyrecords):
    which = random.choice(recordtypes)
    random_string = ''
    desc = ''
    timestamp = int(time.time()) - random.randrange(0,86400)
    if (which == 'domain' or which == 'url'):
        N = random.randrange(1,70)
        random_string = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for x in range(N)) +'.'+ random.choice(tlds)
        if (which == 'domain'):
            random_string = random_string.lower() #cif only likes lower case domains
            desc = "this is a domain"
        else: 
            random_string="http://"+random_string+"/"
            desc = "this is a url"
    elif (which == 'md5'):
        random_string = hashlib.md5(str(random.random())+str(timestamp)).hexdigest()
        desc = "this is an md5 hash"
    elif (which == 'sha1'):
        random_string = hashlib.sha1(str(random.random())+str(timestamp)).hexdigest()
        desc = "this is a sha1 hash"
    elif (which == 'ip'):
        first = random.randrange(1,223)
        while first in not_valid:
            first = random.randrange(1,223)
        random_string = ".".join([str(first),str(random.randrange(1,256)),str(random.randrange(1,256)),str(random.randrange(1,256))])
        desc = "this is an IP"
    else:
        raise Exception('Unexpected data type specified '+which)
    
    print random_string+","+desc+","+datetime.datetime.fromtimestamp(timestamp).isoformat()


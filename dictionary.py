my_dict = {'first':'apple','second':'100','third':16,4:42,'six':(5,12,8),
           'ten':['aaa','ball',34,01],'seven':'555','100':{1:10,2:20,'pop':5},'float':10.5}

list=[my_dict['100']]

kl=my_dict.keys()

print int(my_dict['second']) + my_dict['float'] +my_dict['ten'][2]+my_dict['ten'][3] +my_dict[4] \
+kl[2]+list[0][1]+list[0][2]+list[0].keys()[0]+list[0].keys()[1] +list[0]['pop']+int(kl[5]) \
+int(my_dict['seven'])+ my_dict['third'] \
+my_dict['six'][0] +my_dict['six'][1] +my_dict['six'][2]